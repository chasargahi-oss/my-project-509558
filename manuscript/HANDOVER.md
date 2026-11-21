# Revision package — notes for the authors

Manuscript JSSP-S-26-04304 · *Journal of Soil Science and Plant Nutrition*

## Files

| File | What it is |
|---|---|
| `Revised_Manuscript_JSSP.docx` | The revised manuscript, submission format: A4, Times New Roman 12 pt, double-spaced, continuous line numbers, page numbers, 8 tables, 5 numbered figures |
| `Response_to_Editor.docx` | Point-by-point response to the seven editorial comments, with the location of every change |
| `Cover_Letter.docx` | Cover letter for resubmission, including the disclosure of the previous decision |
| `figures/Figure1.png` … `Figure5.png` | New figures, 300 dpi, numbered in the filename and on the caption |
| `src/*.md` | Markdown sources; edit these and re-run `python3 src/build_docx.py` to rebuild all three .docx files |
| `src/make_figures.py` | Figure script; all values are transcribed from Tables 1, 4, 5 and 8 |

## Why it was rejected, in one sentence

The paper was a competent local survey presented as a general test: the question and hypothesis were never stated, the design's logic was buried, the results recited the tables, the discussion was a series of labels rather than an argument, and the conclusion summarised instead of concluding. The revision keeps the data and rebuilds the argument around it.

## What changed, in substance

1. **The claim is now defensible.** The submitted version compared a species R² of 0.46 (5 df) with a provenance R² of 0.12 (1 df) and called the first larger. On a per-df basis provenance is actually the *more* efficient predictor. The revision reports the per-df values, partitions the species sum of squares into provenance (1 df) and species-within-provenance (4 df), and restates the result correctly: among-species variation within a provenance (0.34) is about three times the variation between provenances (0.12). The headline survives; the reasoning behind it is now sound.
2. **Three hypotheses, and a results section organised around them.**
3. **Methods rebuilt** with the subheadings the Editor asked for, plus the site data that were missing entirely (coordinates, 157 mm rainfall, 29.9 °C, geology, irrigation context, February–March 2017 sampling).
4. **Bulk-density sensitivity** added: stocks at 1.2, 1.4 and 1.6 g cm⁻³ (Table 8, Fig. 4). Ranking invariant; range widens to 17.6–112.5 Mg C ha⁻¹. This converts the biggest weakness into a quantified uncertainty.
5. **Walkley–Black stated as uncorrected**, so concentrations and stocks are declared lower bounds. The submitted version was silent.
6. **A new observation used as evidence:** *P. dactylifera* is the second-sandiest stand (62.4% sand) and has the most carbon — direct evidence against textural control of the ranking.
7. **Discussion** is one continuous argument of eight paragraphs, no subheadings, each opening with its purpose and closing with a take-home point.
8. **Conclusions** answer the three hypotheses, state the mechanism, contain no citations, and end on the management implication.
9. **Figures** regenerated, numbered, separated into individual files, captions matched to panels.
10. **References** cut from 84 to 39, every one cited in the text; one entry completed (Lázaro-Lobo et al. 2025, *Biol Rev* 100:1105–1126).

## Two things you must resolve before upload

**1. The thesis and the manuscript disagree about depth.** The thesis states that soil depth had no significant effect on SOC concentration or on clay, and marks these terms as non-significant in its ANOVA table; the manuscript reports a paired depth effect (*t*₁₇ = 3.70, *p* = 0.002) and a clay increase with depth (*p* < 0.001). The manuscript's internal arithmetic is consistent (means 1.51 → 1.02%), and the most likely explanation is that the thesis table's superscripts are misaligned, but this must be settled from the raw 36-sample data before the paper is read alongside the thesis. If the raw data are sent to me I will re-run the paired tests, the factorial ANOVA and the PERMANOVA and reconcile the two documents.

**2. Metadata only you hold:** distance of the sampling point from the trunk and number of composited cores; planting year, spacing and irrigation regime per stand; S. Yousefi's affiliation; the corresponding e-mail. These are listed in the pre-submission checklist at the end of the manuscript.

## What I could not verify, and what would strengthen the paper further

The uploads did not include Table S1 (the 36-sample record), so every statistic in the revision is carried over from the submitted manuscript rather than recomputed. With the sample-level data I could, in one pass:

- run an ANCOVA of SOC on provenance with silt as a covariate, which would put a number on the confounding instead of an argument (the Editor's strongest implied question);
- compute within-depth partial correlations, which would settle whether the carbon–clay correlation is an artefact of the depth gradient;
- report the PERMANOVA pseudo-F for the species-within-provenance term, currently given descriptively in Table 7;
- redo the figures as box plots from the individual values, as the original submission had them.

Beyond that, the two changes that would most increase the chance of acceptance are measured bulk density on a subset of profiles (24 cores would do) and one deeper increment (30–60 cm) under the three native species. Neither is essential; both would move the paper from "indicative" to "quantified".

## If JSSP declines again

The paper as revised fits, in descending order of fit: *Plant and Soil* (structured abstract already matches its format), *Journal of Arid Environments*, *Arid Land Research and Management*, *Forests*, *Ecological Engineering* (if the dust-suppression service is foregrounded), or *Carbon Management*. The 45 km² industrial-zone framing plays well to *Environmental Science and Pollution Research* or *Environmental Monitoring and Assessment*, but the soil-science contribution would be less visible there.

## Pre-submission checklist

1. Distance of the sampling point from the trunk, and the number of cores composited per sample (Methods, Soil sampling).
2. Planting year, spacing and irrigation regime for each of the six stands (Methods, Experimental design and treatments).
3. S. Yousefi's affiliation, both ORCIDs, and the corresponding e-mail and telephone (Title page).
4. A final Crossref check of every DOI, and completion of the Lázaro-Lobo et al. (2025) entry if the proofs differ.
5. Table S1 (the 36-sample record) as Online Resource 1, together with the analysis scripts.
6. Confirm the artificial-intelligence declaration on the title page.

## A note on the numbers

Every figure in the manuscript traces to a cell in the submitted tables. Where a quantity was derived for this revision it is arithmetic on the published values and is labelled as such: the per-df R² values and the nested partition in Table 7, the 1.2 and 1.6 g cm⁻³ columns in Table 8, the 21.1 and 28.5 Mg C ha⁻¹ increment means, and the 10.2–14.3% clay range. No new measurements have been introduced.
