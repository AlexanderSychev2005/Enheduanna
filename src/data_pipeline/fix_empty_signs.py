"""Backfill the 'signs' column for existing hf_dataset_documents_with_cdli_bulk
rows where it is empty or carries no real glyphs (only "x"/"..." damage
markers) despite substantial real transliteration text.

Confirmed root causes (see session notes / commit messages for the
measurement): (1) prepare_oracc.py's extract_utf8() never resolved ORACC's
"v" (phonetic reading), "s" (logogram name), or "r" (numeral) GDL node
shapes -- only "utf8" nodes and ellipsis gaps -- so real word content was
silently dropped for any ORACC project using those shapes (confirmed:
most of them). (2) cuneiform_unicode.atf_to_lines() treated a literal "..."
token as an ordinary vocabulary miss instead of the "..." gap marker, so it
vanished from 'signs' instead of being recorded. Both are now fixed at the
source.

Rather than reprocessing raw sources and risking a different line/dedup
outcome that could shift the tablet-grouped 90/5/5 split (see
add_cdli_bulk_documents.py's docstring for why that split must never be
recomputed this late), this derives 'signs' directly from each affected
row's own existing, UNCHANGED 'text' field -- wrapping it as a synthetic
one-line ATF body ("1. " + text) and running it through the now-fixed
atf_to_lines(), the same tokenizer/vocabulary the rest of the corpus's
'signs' already comes from. text/tablet_id/labels/split are never touched,
and only rows that were already broken are modified.

Output: data/processed/hf_dataset_documents_with_cdli_bulk_fixed (a new
directory, left alongside the original for inspection -- swap it in by
hand once the printed stats look right).
"""
import os
import sys

from datasets import load_from_disk

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.data_pipeline.cuneiform_unicode import atf_to_lines

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS_DIR = os.path.join(BASE_DIR, "data", "processed", "hf_dataset_documents_with_cdli_bulk")
OUT_DIR = DOCS_DIR + "_fixed"

_DAMAGE_ONLY = {"x", "..."}


def needs_backfill(signs: list[str], text: str) -> bool:
    real = [s for s in signs if s not in _DAMAGE_ONLY]
    return not real and len((text or "").strip()) > 10


def derive_signs(text: str) -> list[str]:
    lines, _misses, _tok = atf_to_lines("1. " + text)
    return lines[0]["signs"] if lines else []


def main() -> None:
    ds = load_from_disk(DOCS_DIR)
    stats = {"checked": 0, "fixed": 0, "still_empty": 0, "untouched": 0}

    def fix(ex):
        stats["checked"] += 1
        if not needs_backfill(ex["signs"], ex["text"]):
            stats["untouched"] += 1
            return {"signs": ex["signs"]}
        new_signs = derive_signs(ex["text"])
        if new_signs:
            stats["fixed"] += 1
            return {"signs": new_signs}
        stats["still_empty"] += 1
        return {"signs": ex["signs"]}

    for split in ds:
        ds[split] = ds[split].map(fix, desc=f"backfilling signs ({split})")

    ds.save_to_disk(OUT_DIR)
    print(f"Saved to {OUT_DIR}")
    print(f"checked={stats['checked']} fixed={stats['fixed']} "
          f"still_empty_after_fix={stats['still_empty']} untouched={stats['untouched']}")


if __name__ == "__main__":
    main()
