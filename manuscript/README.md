# Manuscript revision package

Everything needed for resubmission to the *Journal of Soil Science and Plant Nutrition*, in Word format.
Read [HANDOVER.md](HANDOVER.md) (also supplied as `05_Revision_Notes.docx`) for what changed and what remains.

| File | Purpose | Submit? |
|---|---|---|
| `00_Cover_Letter.docx` | Cover letter to the Editor-in-Chief, disclosing the previous decision and summarising the revision | yes |
| `01_Title_Page.docx` | Title page with authors, affiliations, corresponding author, manuscript metrics, declarations, suggested reviewers | yes |
| `02_Revised_Manuscript.docx` | The revised manuscript, anonymised for double-blind review: A4, Times New Roman 12 pt, double-spaced, continuous line numbers, 8 tables, 5 figures with captions | yes |
| `03_Response_to_Editor.docx` | Point-by-point response to the seven editorial comments, with the location of every change | yes |
| `04_Figures.docx` | Figures 1–5, one per page with its caption, for the production system | yes |
| `05_Revision_Notes.docx` | Internal notes: diagnosis, what changed, what remains, fallback journals | no |

Individual figure files for upload are in `figures/Figure1.png` … `Figure5.png` (300 dpi).

## Rebuilding

Edit the markdown in `src/` (plus `HANDOVER.md`), then:

```
cd manuscript && python3 src/build_docx.py
```

`src/make_figures.py` regenerates the figures. All plotted values are transcribed from Tables 1, 4, 5 and 8; no data are simulated.
