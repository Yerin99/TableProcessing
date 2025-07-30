#!/usr/bin/env python
"""Minimal GMFT table extractor.

Usage:
  python gmft_extract.py --pdf path/to/file.pdf            # print markdown
  python gmft_extract.py --pdf docs/file.pdf --out file.md # save markdown

Example:
    python gmft_extract.py --pdf documents/"The Technology Bubble_ 25 Years On.pdf" --out results/bubble.md
    python gmft_extract.py --pdf documents/"Attention Is All You Need.pdf" --out results/attention.md

The first run downloads the 270 MB Table-Transformer weights.
All operations run on CPU so no GPU is required.
"""

import argparse
from pathlib import Path
import pandas as pd

from gmft.auto import AutoTableDetector, AutoTableFormatter
from gmft.pdf_bindings import PyPDFium2Document


def extract_tables(pdf_path: str):
    """Return list[pd.DataFrame] for every table in the PDF."""
    detector = AutoTableDetector()
    formatter = AutoTableFormatter()

    doc = PyPDFium2Document(pdf_path)
    dfs = []
    for page in doc:
        for cropped in detector.extract(page):
            dfs.append(formatter.extract(cropped).df())
    doc.close()
    return dfs


def main():
    p = argparse.ArgumentParser(description="GMFT PDF → Markdown extractor")
    p.add_argument("--pdf", required=True, help="Path to PDF file")
    p.add_argument("--out", help="Optional path to write markdown output")
    args = p.parse_args()

    pdf_path = Path(args.pdf).expanduser().resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    tables = extract_tables(str(pdf_path))
    if not tables:
        print("[warn] No tables detected.")
        return

    md_blocks = []
    for i, df in enumerate(tables, 1):
        md_blocks.append(f"\n### Table {i}\n\n{df.to_markdown(index=False)}")
    markdown = "\n\n---\n".join(md_blocks)

    if args.out:
        Path(args.out).write_text(markdown, encoding="utf-8")
        print(f"[info] Markdown saved to {args.out}")
    else:
        print(markdown)


if __name__ == "__main__":
    main() 