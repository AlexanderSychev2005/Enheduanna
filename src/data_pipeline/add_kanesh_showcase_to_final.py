"""Merge the Kanesh-article + Ea-nasir showcase rows (added to
CDLI_SPECIFIC_TIDS in add_showcase_texts.py) directly into the ALREADY
signs-fixed data/processed/hf_dataset_documents_with_cdli_bulk, instead of
re-running add_cdli_bulk_documents.py's own main().

Why not just re-run add_cdli_bulk_documents.py: it rebuilds
hf_dataset_documents_with_cdli_bulk from data/processed/hf_dataset_documents
(the BASE dataset) plus every interim patch file. That base dataset was
never itself patched by fix_empty_signs.py / the [#]->"..." rename (only
the derived _with_cdli_bulk directory was, in place) -- re-running the
normal pipeline would silently regress every one of today's signs fixes
for the ~57% of rows that needed them. This script instead appends only
the new showcase rows onto the current, already-fixed final dataset.

Run after add_showcase_texts.py has (re)written
data/interim/showcase_documents.jsonl with the new tablet_ids.
"""
import json
import os
import sys

from datasets import Dataset, concatenate_datasets, load_from_disk

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.data_pipeline.prepare_hf_dataset import (
    GENRE_LABELS, LANGUAGE_LABELS, PERIOD_LABELS, PROVENIENCE_LABELS, label_to_idx,
    map_genre, map_language, map_period, map_provenience,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SHOWCASE_PATH = os.path.join(BASE_DIR, "data", "interim", "showcase_documents.jsonl")
DOCS_DIR = os.path.join(BASE_DIR, "data", "processed", "hf_dataset_documents_with_cdli_bulk")
TRANSLATIONS_PATH = os.path.join(os.path.dirname(__file__), "kanesh_showcase_translations.json")

TARGET_IDS = {"P333901", "P357584", "P297482", "P358584", "P359100", "P368333", "P359402", "P414985"}


def main() -> None:
    ds = load_from_disk(DOCS_DIR)
    translations = json.load(open(TRANSLATIONS_PATH, encoding="utf-8"))

    new_rows = {"train": [], "validation": [], "test": []}
    with open(SHOWCASE_PATH, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            if r["tablet_id"] not in TARGET_IDS:
                continue
            new_rows[r["split"]].append({
                "signs": r.get("signs", []),
                "text": r["text"],
                "tablet_id": r["tablet_id"],
                "period_labels": label_to_idx(map_period(r["period"]), PERIOD_LABELS),
                "genre_labels": label_to_idx(map_genre(r["genre"]), GENRE_LABELS),
                "language_labels": label_to_idx(map_language(r["language"]), LANGUAGE_LABELS),
                "provenience_labels": label_to_idx(map_provenience(r["provenience"]), PROVENIENCE_LABELS),
                "translation": translations.get(r["tablet_id"]) or "",
            })

    n_added = sum(len(v) for v in new_rows.values())
    print(f"Found {n_added} target rows in showcase_documents.jsonl "
          f"({[(s, len(v)) for s, v in new_rows.items()]})")

    # Drop any existing row whose tablet_id we're about to (re-)introduce,
    # same rule add_cdli_bulk_documents.py uses -- none of these 8 are
    # expected to already be in the corpus (verified in
    # kanesh_article/showcase_tablets.md), but keep the guard anyway so a
    # second run of this script is idempotent instead of duplicating rows.
    n_dropped = 0
    for split in ("train", "validation", "test"):
        before = len(ds[split])
        ds[split] = ds[split].filter(lambda ex: ex["tablet_id"] not in TARGET_IDS)
        n_dropped += before - len(ds[split])
    if n_dropped:
        print(f"Dropped {n_dropped} pre-existing rows with a colliding tablet_id (new copy wins).")

    for split, rows in new_rows.items():
        if not rows:
            continue
        addition = Dataset.from_list(rows, features=ds[split].features)
        ds[split] = concatenate_datasets([ds[split], addition])

    ds.save_to_disk(DOCS_DIR + "_plus_kanesh")
    print(f"Saved to {DOCS_DIR}_plus_kanesh")
    for split in ds:
        print(f"  {split}: {len(ds[split])}")


if __name__ == "__main__":
    main()
