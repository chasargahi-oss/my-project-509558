# Manuscript revision package

See [HANDOVER.md](HANDOVER.md) for what changed and what remains.

- `Revised_Manuscript_JSSP.docx` — revised manuscript, submission format
- `Response_to_Editor.docx` — point-by-point response to the seven editorial comments
- `Cover_Letter.docx` — resubmission cover letter
- `figures/` — Figures 1–5 (300 dpi), plus the figures extracted from the original submission PDF
- `src/` — markdown sources, figure script and docx build script

Rebuild the documents after editing the markdown:

```
cd manuscript && python3 src/build_docx.py
```
