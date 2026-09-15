"""Figures for the diploma: bar charts for period/genre/language/provenience.
Recomputes document counts fresh from the live HF dataset rather than
trusting any cached stats file -- see docs/corpus_stats.md for the same
numbers in table form.

Colors match the project's own web tool (src/web/static/style.css): a
clay-tablet palette. Bars are a single flat color -- these are sorted,
labeled counts, so color doesn't need to also flag "the biggest one" the
way src/web's own charts use seal-red to flag a model's top prediction;
that's a different kind of information. A single color avoids a redundant
encoding (the same reason a sequential color ramp is skipped too).

Usage: uv run python src/analysis/plot_category_figures.py
"""
import json
from pathlib import Path

import matplotlib.pyplot as plt
from datasets import load_from_disk

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "diploma" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Same palette as src/web/static/style.css's :root variables.
INK = "#2B2420"
CLAY = "#DCCBA8"
STONE = "#8A8175"
PARCHMENT = "#FBF8F2"

plt.rcParams.update({
    "font.family": "sans-serif",
    "text.color": INK,
    "axes.edgecolor": STONE,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
})


def load_doc_counts() -> dict[str, dict[str, int]]:
    docs = load_from_disk(str(ROOT / "data/processed/hf_dataset_documents_with_cdli_bulk"))
    label_configs = json.load(open(ROOT / "data/processed/label_configs.json", encoding="utf-8"))
    counts = {}
    for head, cfg in label_configs.items():
        labels = cfg["labels"]
        head_counts = {label: 0 for label in labels}
        for split in docs:
            for idx in docs[split][f"{head}_labels"]:
                if idx != -100:
                    head_counts[labels[idx]] += 1
        counts[head] = head_counts
    return counts


def plot_bar_vertical(counts: dict[str, int], title: str, filename: str) -> None:
    """For small class counts (period/genre/language): vertical bars,
    category labels on the x-axis, rotated to avoid overlap."""
    items = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    labels = [k for k, _ in items]
    values = [v for _, v in items]

    fig, ax = plt.subplots(figsize=(0.9 * len(labels) + 2, 5))
    x_pos = range(len(labels))
    ax.bar(x_pos, values, color=CLAY, edgecolor=STONE, linewidth=0.8, width=0.65)
    ax.set_xticks(list(x_pos))
    ax.set_xticklabels(labels, rotation=35, ha="right")
    ax.set_ylabel("Documents")
    ax.set_title(title)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for x, v in zip(x_pos, values):
        ax.text(x, v + max(values) * 0.015, f"{v:,}", ha="center", va="bottom", fontsize=9)
    ax.set_ylim(0, max(values) * 1.12)
    fig.tight_layout()
    fig.savefig(OUT_DIR / filename, dpi=200, facecolor=PARCHMENT)
    plt.close(fig)
    print(f"wrote {filename}")


def plot_bar_horizontal(counts: dict[str, int], title: str, filename: str, top_n: int | None = None) -> None:
    """For provenience: horizontal bars, sorted descending -- long category
    names don't fit readably on a rotated x-axis. `top_n` caps the list."""
    items = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    if top_n:
        items = items[:top_n]
    labels = [k for k, _ in items]
    values = [v for _, v in items]

    fig, ax = plt.subplots(figsize=(7.5, 0.32 * len(labels) + 1))
    y_pos = range(len(labels))
    ax.barh(y_pos, values, color=CLAY, edgecolor=STONE, linewidth=0.8)
    ax.set_yticks(list(y_pos))
    ax.set_yticklabels(labels, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlabel("Documents")
    ax.set_title(title)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for y, v in zip(y_pos, values):
        ax.text(v + max(values) * 0.01, y, f"{v:,}", va="center", fontsize=8)
    ax.set_xlim(0, max(values) * 1.14)
    fig.tight_layout()
    fig.savefig(OUT_DIR / filename, dpi=200, facecolor=PARCHMENT)
    plt.close(fig)
    print(f"wrote {filename}")


def main() -> None:
    counts = load_doc_counts()
    plot_bar_vertical(counts["period"], "Period (9 classes)", "period_bar.png")
    plot_bar_vertical(counts["genre"], "Genre (6 classes)", "genre_bar.png")
    plot_bar_vertical(counts["language"], "Language (4 classes)", "language_bar.png")
    plot_bar_horizontal(counts["provenience"], "Provenience (36 classes)", "provenience_bar.png")
    plot_bar_horizontal(counts["provenience"], "Provenience (top 10)", "provenience_bar_top10.png", top_n=10)


if __name__ == "__main__":
    main()
