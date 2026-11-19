"""Assemble the complete submission-ready manuscript."""
import os, sys, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

from docx_style import (para, rich, h1, h2, h3, set_run, shade, cell_borders,
                        table_rule, repeat_header, keep_row_together,
                        set_col_widths, add_page_number_footer, add_header)
from content_front import title_page, abstract_page, TITLE, SHORT_TITLE
from content_intro import introduction, methods
from content_results import results
from content_disc import discussion, declarations
from content_tables import TABLES
import content_intro, content_results, content_disc

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FIGDIR = os.path.join(ROOT, "figures")
OUTDIR = os.path.join(ROOT, "output")

FIG_FILES = {
    1: ("fig1_pathway.png", 16.0),
    2: ("fig2_prisma.png", 13.2),
    3: ("fig3_evidence.png", 16.0),
    4: ("fig4_occurrence_env.png", 16.0),
    5: ("fig5_occurrence.png", 16.0),
    6: ("fig6_workflow.png", 16.0),
    7: ("fig7_gap.png", 16.0),
    8: ("fig8_decision.png", 16.0),
}

CAPS = {
 1: ("Conceptual source-to-consumer exposure and effect pathway for engineered nanoparticles in seafood systems.",
     "Solid arrows indicate pathways supported by direct evidence; the highlighted terminal box marks the step at which the evidence chain currently becomes conditional rather than quantitative."),
 2: ("PRISMA 2020 flow diagram for the systematic review.",
     "Categories within each exclusion box sum to the stated total. n.r. = not separately recorded by the search platform."),
 3: ("Composition of the included corpus and confidence in the evidence chain.",
     "(a) Studies by thematic category. (b) Confidence assigned in this review to each link in the ENP\u2013seafood evidence chain, from none to strong. The dashed line marks the evidence level required for a quantitative risk conclusion."),
 4: ("Environmental occurrence and particle-size context.",
     "(a) Reported particle-number concentrations of metal-bearing nanoparticles in surface seawater from Laizhou Bay, China (mean of 24 stations). (b) Reported mean particle diameters across environmental and seafood matrices; the dashed line marks the 100 nm convention."),
 5: ("Occurrence and intake of metal-containing nanoparticles in canned seafood.",
     "(a) Mean TiO\u2082 nanoparticle concentrations (fraction <100 nm) in four canned products; error bars span reported minima and maxima. (b) Single-meal intake of particle-associated ZnO compared with dissolved Zn on a logarithmic scale. Adapted from data reported by Grasso et al. (2020, 2021, 2022)."),
 6: ("Analytical workflow for ENP determination in seafood.",
     "From sample collection through digestion, particle separation, spICP-MS determination and orthogonal confirmation; the footnote identifies the principal unresolved metrological constraint."),
 7: ("The laboratory-to-environment concentration gap.",
     "Indicative envelopes for measured environmental concentrations, reported effect concentrations and typical laboratory exposure concentrations, showing the 10\u2013100-fold separation that limits extrapolation from laboratory hazard to field risk."),
 8: ("Decision framework for interpreting a positive ENP detection in seafood.",
     "Each step is a precondition for the next; a negative answer changes the appropriate conclusion rather than merely reducing confidence."),
}


def page_setup(doc):
    s = doc.sections[0]
    s.page_width = Cm(21.0)
    s.page_height = Cm(29.7)
    s.top_margin = Cm(2.5)
    s.bottom_margin = Cm(2.5)
    s.left_margin = Cm(2.5)
    s.right_margin = Cm(2.5)
    s.header_distance = Cm(1.25)
    s.different_first_page_header_footer = True
    s.footer_distance = Cm(1.25)
    return s


def base_styles(doc):
    st = doc.styles["Normal"]
    st.font.name = "Times New Roman"
    st.font.size = Pt(12)
    st.paragraph_format.space_after = Pt(0)
    st.paragraph_format.line_spacing = 2.0
    rpr = st.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), "Times New Roman")


def render_table(doc, label, caption, header, rows, widths, note):
    # caption above the table (journal style)
    rich(doc, [(label + ". ", {"bold": True, "size": 9.5}),
               (caption, {"size": 9.5})],
         align="left", line=1.15, space_before=10, space_after=4, keep_next=True)

    t = doc.add_table(rows=1, cols=len(header))
    t.alignment = 1  # center
    t.style = "Table Grid"
    t.autofit = False

    hdr = t.rows[0]
    repeat_header(hdr)
    keep_row_together(hdr)
    for i, h in enumerate(header):
        c = hdr.cells[i]
        c.text = ""
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.keep_with_next = True
        r = p.add_run(h)
        set_run(r, size=8.2, bold=True)
        shade(c, "E9EDF1")

    for r_i, row in enumerate(rows):
        tr = t.add_row()
        keep_row_together(tr)
        is_last = (r_i == len(rows) - 1)
        for i, val in enumerate(row):
            c = tr.cells[i]
            c.text = ""
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(2.5)
            p.paragraph_format.space_after = Pt(2.5)
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.keep_with_next = not is_last
            from italics import italianize
            for seg, lat in italianize(val):
                if not seg:
                    continue
                r = p.add_run(seg)
                set_run(r, size=8.2, bold=(i == 0 and len(header) > 2),
                        italic=lat)

    total = sum(widths)
    widths = [w * 16.0 / total for w in widths]
    set_col_widths(t, widths)
    for row in t.rows:
        for cell in row.cells:
            cell_borders(cell, color="C6C6C6", sz=4)
    table_rule(t.rows, color="1A1A1A", sz=10)

    if note:
        p = para(doc, note, size=7.8, align="left", line=1.1,
                 space_before=3, space_after=12, italic=True)
    else:
        para(doc, "", size=4, line=1.0, space_after=10)


def _embed(doc, key):
    """Render a table or figure inline at the point of first citation."""
    if key.startswith("T"):
        tbl = [t for t in TABLES if t[0] == "Table " + key[1:]][0]
        render_table(doc, *tbl)
    else:
        n = int(key[1:])
        place_figure(doc, n)


def _install_embed(doc):
    fn = lambda key: _embed(doc, key)
    for mod in (content_intro, content_results, content_disc):
        mod._EMBED = fn


def place_figure(doc, n):
    fn, width = FIG_FILES[n]
    path = os.path.join(FIGDIR, fn)
    if not os.path.exists(path):
        para(doc, f"[Figure {n} missing: {fn}]", size=9, align="center",
             italic=True, space_after=10, color="B03A2E")
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(path, width=Cm(width))
    # caption
    head, body = CAPS[n]
    rich(doc, [(f"Figure {n}. ", {"bold": True, "size": 9}),
               (head + " ", {"size": 9}),
               (body, {"size": 9})],
         align="justify", line=1.12, space_before=3, space_after=14)




def italicise_latin(doc):
    """Italicise Latin binomials inside body text, preserving existing run formats."""
    from italics import italianize

    for p in doc.paragraphs:
        runs = list(p.runs)
        if not runs:
            continue
        joined = "".join(r.text for r in runs)
        if "https://doi.org/" in joined:
            continue                      # reference entries: handled at build time
        if not any(f for _, f in italianize(joined)):
            continue

        # Walk each run; only non-italic runs are candidates for new italic spans.
        for run in runs:
            if run.italic:
                continue
            txt = run.text
            pieces = italianize(txt)
            if not any(flag for _, flag in pieces):
                continue
            size = run.font.size.pt if run.font.size else 10
            bold = bool(run.bold)
            font = run.font.name or "Times New Roman"
            anchor = run._element
            parent = anchor.getparent()
            idx = list(parent).index(anchor)
            run.text = pieces[0][0]
            run.italic = pieces[0][1] or None
            insert_at = idx + 1
            for chunk, lat in pieces[1:]:
                new_r = copy.deepcopy(anchor)
                parent.insert(insert_at, new_r)
                insert_at += 1
                from docx.text.run import Run
                r_obj = Run(new_r, run._parent)
                r_obj.text = chunk
                r_obj.italic = lat or None
                set_run(r_obj, size=size, bold=bold, italic=lat, font=font)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    doc = Document()
    sec = page_setup(doc)
    base_styles(doc)
    _install_embed(doc)

    # Title page gets no header; from abstract onward a running head appears.
    add_header(sec, "Engineered nanoparticles and seafood safety")
    add_page_number_footer(sec)

    title_page(doc)
    abstract_page(doc)

    # body starts on a new section so the header applies there
    introduction(doc)
    methods(doc)
    results(doc)
    discussion(doc)
    declarations(doc)

    # ---- end matter
    out = os.path.join(OUTDIR, "Engineered_nanoparticles_seafood_safety_Systematic_Review.docx")
    italicise_latin(doc)
    doc.save(out)
    print("saved", out, os.path.getsize(out) // 1024, "KB")


if __name__ == "__main__":
    main()
