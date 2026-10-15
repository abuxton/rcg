# Building and checking the PDF

The PDF must be generated from the Markdown source so the two cannot drift.

## Build

```bash
pip install markdown-it-py weasyprint
python skills/vaesen-scenario-author/scripts/build_pdf.py \
  assets/scenarios/<slug>.md assets/scenarios/<slug>.pdf --site-root .
```

The script renders the Markdown (including the embedded `<style>` block and
`<div>` wrappers) with WeasyPrint, which honours CSS columns, `@page` margins
and the fixed footer. Root-relative image paths resolve against `--site-root`.

## Visual check

1. Count pages (`python -c "import pymupdf;print(len(pymupdf.open('x.pdf')))"`).
   Aim for the shortest layout that stays readable.
2. Render each page to an image and look at it:
   `pymupdf.open('x.pdf')[i].get_pixmap(dpi=80).save('page.png')`.
3. Check: banner not distorted; title, preamble and prelude full-width; body in
   two columns; Conflicts, Clues (and any revelation) boxed and not split across
   pages; footer links readable; "Page N" bottom-right; nothing overflows.
4. Fix the Markdown, never the PDF, and rebuild.

## Note

The reference PDF in the repository predates this script and was produced with a
different tool, so page breaks may differ slightly. The Markdown is the source of truth.
