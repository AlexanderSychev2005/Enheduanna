"""Offline: compute and save one document embedding (interpret.py's
document_embedding -- Aeneas-style 0.5*([CLS] + mean of the rest)) per
tablet, for the web demo's similar-document lookup (src/web/app.py). No
retraining -- reuses the already fine-tuned checkpoint. Uses
checkpoints_final_vision (not checkpoints_final_text) to match app.py's own
single-model-at-inference design: app.py always queries
checkpoints_final_vision, so a live query embedding and this precomputed
corpus must come from the same backbone weights, or their cosine
similarity would be comparing two different embedding spaces.
document_embedding() itself never touches the image branch (it only reads
model.backbone.bert's hidden states), so this works for every document
regardless of whether it has a photo -- use_image=True below is only there
because it's required to load the vision checkpoint's full state_dict.

Run once (re-run only if the corpus or checkpoints_final_vision changes):

    python src/analysis/compute_embeddings.py

Output: results_final/embeddings/doc_embeddings.npy ((N, hidden) float32)
+ doc_meta.json (one {tablet_id, split, period, genre, language,
provenience} per row, same order) -- src/web/app.py loads both at startup.
"""
import argparse
import json
import os
import sys
from typing import Optional

import numpy as np
import torch
from safetensors.torch import load_file
from transformers import AutoTokenizer
from datasets import load_dataset
from tqdm import tqdm

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.training.train_mbert import MBertMultiTask, mark_damage_signals

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def batched_document_embedding(model, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> np.ndarray:
    """Same 0.5*([CLS] + mean of the other real tokens) as interpret.py's
    document_embedding(), vectorized over the batch dimension instead of
    interpret.py's single-example version (which app.py's live query path
    keeps using as-is -- this batched variant is only for this script's own
    corpus-wide pass, where looping one example at a time left the GPU
    mostly idle between tiny forward passes)."""
    with torch.no_grad():
        seq = model.backbone.bert(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
        mask = attention_mask.bool()
        cls = seq[:, 0]
        rest_mask = mask.clone()
        rest_mask[:, 0] = False
        rest_mask_f = rest_mask.unsqueeze(-1).float()
        counts = rest_mask_f.sum(dim=1)
        mean = (seq * rest_mask_f).sum(dim=1) / counts.clamp(min=1)
        mean = torch.where(counts > 0, mean, cls)
        emb = 0.5 * (cls + mean)
    return emb.detach().cpu().numpy().astype(np.float32)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", default=os.path.join(BASE_DIR, "checkpoints_final_vision", "final_model"))
    parser.add_argument("--data_dir", default="AlexSychovUN/Enheduanna-Dataset")
    parser.add_argument("--hf_config", default="documents")
    parser.add_argument("--model_name", default="bert-base-multilingual-cased")
    parser.add_argument("--label_config", default=os.path.join(BASE_DIR, "data", "processed", "label_configs.json"))
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--context_char_max", type=int, default=768,
                         help="Matches the document-granularity training window (MBertCollator's own default)")
    parser.add_argument("--batch_size", type=int, default=16,
                         help="Kept modest on purpose: app.py's own server keeps its copy of this same "
                              "checkpoint resident on the GPU the whole time it runs, so this script only "
                              "ever has whatever VRAM that leaves free to work with.")
    parser.add_argument("--out_dir", default=os.path.join(BASE_DIR, "results_final", "embeddings"))
    parser.add_argument("--incremental", action="store_true",
                         help="Load existing doc_embeddings.npy/doc_meta.json from --out_dir (if present) and only "
                              "run inference for tablet_ids not already in there, appending the result -- for "
                              "adding a handful of new documents (e.g. a new showcase text) without a full ~2h "
                              "corpus-wide recompute. Do NOT use this after checkpoints_final_vision itself "
                              "changes (retraining) -- the kept embeddings would then be stale, mixed with fresh "
                              "ones from different weights; do a full recompute (no --incremental) instead.")
    args = parser.parse_args()

    existing_keys = set()  # {(tablet_id, split)}
    embeddings, meta = [], []
    if args.incremental:
        emb_path = os.path.join(args.out_dir, "doc_embeddings.npy")
        meta_path = os.path.join(args.out_dir, "doc_meta.json")
        if os.path.exists(emb_path) and os.path.exists(meta_path):
            old_embeddings = list(np.load(emb_path))
            with open(meta_path, encoding="utf-8") as f:
                old_meta = json.load(f)
            # Keyed on (tablet_id, split), not tablet_id alone: a tablet_id
            # can change split across a corpus rebuild (e.g. a showcase
            # addition displacing an existing base-corpus copy of the same
            # tablet_id into a different split, per add_cdli_bulk_documents.py's
            # own "backfill's own split wins" rule) -- keying on tablet_id
            # alone would silently keep that stale, now-wrong-split row
            # instead of recomputing it. Rows whose (tablet_id, split) no
            # longer matches anything in the current corpus are dropped
            # below rather than carried over.
            for m, e in zip(old_meta, old_embeddings):
                existing_keys.add((m["tablet_id"], m["split"]))
                meta.append(m)
                embeddings.append(e)
            print(f"Incremental: {len(existing_keys)} (tablet_id, split) rows loaded from the existing file.")
        else:
            print("Incremental requested but no existing doc_embeddings.npy/doc_meta.json found -- doing a full run.")

    with open(args.label_config, encoding="utf-8") as f:
        label_configs = json.load(f)
    tasks = ["period", "genre", "language", "provenience"]
    num_labels = {t: len(label_configs[t]["labels"]) for t in tasks}
    label_names = {t: label_configs[t]["labels"] for t in tasks}

    print(f"Loading tokenizer + model from {args.checkpoint}...")
    tokenizer = AutoTokenizer.from_pretrained(args.checkpoint, use_fast=False)
    model = MBertMultiTask(
        args.model_name, num_period=num_labels["period"], num_genre=num_labels["genre"],
        num_language=num_labels["language"], num_provenience=num_labels["provenience"],
        use_image=True, vision_init="finetune",
    )
    state_dict = load_file(os.path.join(args.checkpoint, "model.safetensors"))
    model.load_state_dict(state_dict)
    model.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    print(f"Loading dataset {args.data_dir} ({args.hf_config})...")
    ds = load_dataset(args.data_dir, args.hf_config)

    if existing_keys:
        current_keys = {(tid, split) for split in ds for tid in ds[split]["tablet_id"]}
        keep = [k in current_keys for k in zip((m["tablet_id"] for m in meta), (m["split"] for m in meta))]
        n_dropped = len(keep) - sum(keep)
        if n_dropped:
            meta = [m for m, k in zip(meta, keep) if k]
            embeddings = [e for e, k in zip(embeddings, keep) if k]
            existing_keys = {(m["tablet_id"], m["split"]) for m in meta}
            print(f"Incremental: dropped {n_dropped} stale rows no longer matching a (tablet_id, split) in the "
                  f"current corpus (moved to a different split, or removed) -- will recompute/skip fresh below.")

    def label_name(task: str, idx: Optional[int]) -> Optional[str]:
        return label_names[task][idx] if idx is not None and idx != -100 else None

    for split in ds:
        rows = ds[split]
        if existing_keys:
            rows = rows.filter(lambda ex: (ex["tablet_id"], split) not in existing_keys)
        if len(rows) == 0:
            print(f"{split}: nothing new, skipping.")
            continue
        for start in tqdm(range(0, len(rows), args.batch_size), desc=split):
            batch = rows[start:start + args.batch_size]
            texts = [mark_damage_signals((t or "")[:args.context_char_max]) for t in batch["text"]]
            enc = tokenizer(texts, truncation=True, max_length=args.max_length, padding=True, return_tensors="pt")
            input_ids = enc["input_ids"].to(device)
            attn = enc["attention_mask"].to(device)
            embs = batched_document_embedding(model, input_ids, attn)
            for i in range(len(texts)):
                embeddings.append(embs[i])
                meta.append({
                    "tablet_id": batch["tablet_id"][i], "split": split,
                    "period": label_name("period", batch["period_labels"][i]),
                    "genre": label_name("genre", batch["genre_labels"][i]),
                    "language": label_name("language", batch["language_labels"][i]),
                    "provenience": label_name("provenience", batch["provenience_labels"][i]),
                    "text": batch["text"][i],
                    "signs": " ".join(batch["signs"][i]) if batch["signs"][i] else "",
                    "translation": batch.get("translation", [None] * len(texts))[i] or "",
                })

    os.makedirs(args.out_dir, exist_ok=True)
    arr = np.stack(embeddings).astype(np.float32)
    np.save(os.path.join(args.out_dir, "doc_embeddings.npy"), arr)
    with open(os.path.join(args.out_dir, "doc_meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False)
    n_new = arr.shape[0] - len(existing_keys)
    print(f"Saved {arr.shape[0]} embeddings (dim={arr.shape[1]}) to {args.out_dir}"
          + (f" ({n_new} newly computed, {len(existing_keys)} kept from the existing file)" if existing_keys else ""))
