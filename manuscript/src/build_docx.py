"""Build submission-style .docx files from the markdown sources."""
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent          # .../manuscript
FIGDIR = ROOT / "figures"

BODY_FONT = "Times New Roman"
BODY_SIZE = Pt(12)


# ----------------------------------------------------------------- helpers
def set_cell_font(cell, size=8.5, bold=False):
    for p in cell.paragraphs:
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        for r in p.runs:
            r.font.name = BODY_FONT
            r.font.size = Pt(size)
            r.font.bold = bold


def add_line_numbers(section):
    sectPr = section._sectPr
    ln = OxmlElement("w:lnNumType")
    ln.set(qn("w:countBy"), "1")
    ln.set(qn("w:restart"), "continuous")
    sectPr.append(ln)


def add_page_number_footer(section, text=""):
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if text:
        run = p.add_run(text + "    ")
        run.font.size = Pt(9)
        run.font.name = BODY_FONT
    run = p.add_run()
    fld1 = OxmlElement("w:fldChar"); fld1.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld2 = OxmlElement("w:fldChar"); fld2.set(qn("w:fldCharType"), "end")
    run._r.append(fld1); run._r.append(instr); run._r.append(fld2)
    run.font.size = Pt(9)
    run.font.name = BODY_FONT


INLINE = re.compile(r"(\*\*.+?\*\*|\*[^*]+?\*|~[^~]+?~|\^[^\^]+?\^)")


def add_runs(par, text, size=None, base_bold=False, base_italic=False):
    text = text.replace("\\*", "\u0001")
    for tok in INLINE.split(text):
        if not tok:
            continue
        bold, italic, sub, sup = base_bold, base_italic, False, False
        if tok.startswith("**") and tok.endswith("**") and len(tok) > 4:
            add_runs(par, tok[2:-2], size=size, base_bold=True, base_italic=base_italic)
            continue
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            tok, italic = tok[1:-1], True
        elif tok.startswith("~") and tok.endswith("~") and len(tok) > 2:
            tok, sub = tok[1:-1], True
        elif tok.startswith("^") and tok.endswith("^") and len(tok) > 2:
            tok, sup = tok[1:-1], True
        r = par.add_run(tok.replace("\u0001", "*"))
        r.font.name = BODY_FONT
        r.font.size = size or BODY_SIZE
        r.bold = bold
        r.italic = italic
        if sub:
            r.font.subscript = True
        if sup:
            r.font.superscript = True


def is_table_sep(line):
    s = line.strip()
    if not s.startswith("|"):
        return False
    body = s.strip("|").replace(" ", "")
    return bool(body) and set(body) <= set("-:|")


# ----------------------------------------------------------------- builder
def build(md_path, docx_path, title_page=True, line_numbers=True,
          double_space=False, first_header=""):
    lines = Path(md_path).read_text(encoding="utf-8").splitlines()

    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    for m in ("left_margin", "right_margin"):
        setattr(sec, m, Cm(2.5))
    sec.top_margin, sec.bottom_margin = Cm(2.5), Cm(2.5)

    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = BODY_SIZE
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 2.0 if double_space else 1.35
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts"); rpr.append(rfonts)
    rfonts.set(qn("w:eastAsia"), BODY_FONT)

    if line_numbers:
        add_line_numbers(sec)
    add_page_number_footer(sec, first_header)

    # ---- collect figure captions for the figure section
    fig_caps = {}
    for ln in lines:
        m = re.match(r"\*\*Fig\.\s*(\d+)\*\*", ln.strip())
        if m:
            fig_caps[int(m.group(1))] = ln.strip()

    i = 0
    n = len(lines)
    in_captions = False
    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # headings
        if stripped.startswith("### "):
            h = doc.add_heading(level=3)
            h.paragraph_format.space_before = Pt(10)
            h.paragraph_format.space_after = Pt(4)
            add_runs(h, stripped[4:], size=Pt(12), base_bold=True)
            for r in h.runs:
                r.font.color.rgb = RGBColor(0, 0, 0)
                r.font.name = BODY_FONT
            i += 1
            continue

        if stripped.startswith("## "):
            txt = stripped[3:]
            if txt.lower().startswith("figure captions"):
                in_captions = True
            h = doc.add_heading(level=2)
            h.paragraph_format.space_before = Pt(16)
            h.paragraph_format.space_after = Pt(6)
            add_runs(h, txt, size=Pt(13), base_bold=True)
            for r in h.runs:
                r.font.color.rgb = RGBColor(0, 0, 0)
                r.font.name = BODY_FONT
            if first_header:
                h.paragraph_format.page_break_before = False
            i += 1
            continue

        if stripped.startswith("# "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(12)
            add_runs(p, stripped[2:], size=Pt(15), base_bold=True)
            i += 1
            continue

        # tables
        if stripped.startswith("|") and i + 1 < n and is_table_sep(lines[i + 1]):
            header = [c.strip() for c in stripped.strip("|").split("|")]
            rows = []
            j = i + 2
            while j < n and lines[j].strip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")])
                j += 1
            table = doc.add_table(rows=1, cols=len(header))
            table.style = "Table Grid"
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            table.autofit = True
            for k, htxt in enumerate(header):
                cell = table.rows[0].cells[k]
                cell.text = ""
                par = cell.paragraphs[0]
                add_runs(par, htxt, size=Pt(8.5), base_bold=True)
                set_cell_font(cell, 8.5, bold=True)
            for row in rows:
                cells = table.add_row().cells
                for k, cval in enumerate(row[: len(header)]):
                    cells[k].text = ""
                    par = cells[k].paragraphs[0]
                    add_runs(par, cval, size=Pt(8.5))
                    set_cell_font(cells[k], 8.5)
            # header row repeat
            trPr = table.rows[0]._tr.get_or_add_trPr()
            tblHeader = OxmlElement("w:tblHeader")
            tblHeader.set(qn("w:val"), "true")
            trPr.append(tblHeader)
            doc.add_paragraph().paragraph_format.space_after = Pt(2)
            i = j
            continue

        # caption paragraphs (Table N. / Fig. N / Note)
        if re.match(r"^Table \d+\.", stripped):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.0
            m = re.match(r"^(Table \d+\.)\s*(.*)$", stripped)
            r = p.add_run(m.group(1) + " ")
            r.bold = True
            r.font.size = Pt(10)
            r.font.name = BODY_FONT
            add_runs(p, m.group(2), size=Pt(10))
            i += 1
            continue

        if stripped.startswith("**Table") or stripped.startswith("*Note.*"):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.0
            add_runs(p, stripped, size=Pt(10))
            i += 1
            continue

        if stripped.startswith("**Fig."):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.line_spacing = 1.15
            add_runs(p, stripped, size=Pt(10))
            i += 1
            continue

        # plain paragraph
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_runs(p, stripped)
        i += 1

    # ---- figure section
    if fig_caps:
        doc.add_page_break()
        h = doc.add_heading(level=2)
        add_runs(h, "Figures", size=Pt(13), base_bold=True)
        for r in h.runs:
            r.font.color.rgb = RGBColor(0, 0, 0)
        for num in sorted(fig_caps):
            f = FIGDIR / f"Figure{num}.png"
            if not f.exists():
                continue
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            run = p.add_run()
            width = Cm(16.0) if num in (1, 2, 3, 4) else Cm(10.5)
            run.add_picture(str(f), width=width)
            cp = doc.add_paragraph()
            cp.paragraph_format.space_before = Pt(4)
            cp.paragraph_format.line_spacing = 1.1
            add_runs(cp, fig_caps[num], size=Pt(10))

    doc.save(docx_path)
    return docx_path


def build_figures_doc(out_path):
    """One figure per page, numbered, caption beneath."""
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, m, Cm(2.5))
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = BODY_SIZE
    add_page_number_footer(sec, "Figures")

    md = (ROOT / "src" / "Revised_Manuscript.md").read_text(encoding="utf-8")
    caps = {}
    for ln in md.splitlines():
        m = re.match(r"\*\*Fig\.\s*(\d+)\*\*\s*(.*)", ln.strip())
        if m:
            caps[int(m.group(1))] = m.group(2)

    h = doc.add_heading(level=2)
    add_runs(h, "Figures", size=Pt(13), base_bold=True)
    for r in h.runs:
        r.font.color.rgb = RGBColor(0, 0, 0)

    numbers = sorted(caps)
    for k, num in enumerate(numbers):
        f = FIGDIR / f"Figure{num}.png"
        if not f.exists():
            continue
        if k:
            doc.add_page_break()
        lab = doc.add_paragraph()
        lab.paragraph_format.space_after = Pt(6)
        r = lab.add_run(f"Figure {num}")
        r.bold = True
        r.font.size = Pt(11)
        r.font.name = BODY_FONT
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(f), width=Cm(15.5) if num != 5 else Cm(10.5))
        cp = doc.add_paragraph()
        cp.paragraph_format.space_before = Pt(8)
        cp.paragraph_format.line_spacing = 1.15
        rr = cp.add_run(f"Fig. {num} ")
        rr.bold = True
        rr.font.size = Pt(10)
        rr.font.name = BODY_FONT
        add_runs(cp, caps[num], size=Pt(10))
    doc.save(out_path)
    return out_path


if __name__ == "__main__":
    src = ROOT / "src"
    made = []
    made.append(build(src / "Cover_Letter.md", ROOT / "00_Cover_Letter.docx",
                      first_header="Cover letter — JSSP-S-26-04304",
                      line_numbers=False, double_space=False))
    made.append(build(src / "Title_Page.md", ROOT / "01_Title_Page.docx",
                      first_header="Title page — JSSP-S-26-04304",
                      line_numbers=False, double_space=False))
    made.append(build(src / "Revised_Manuscript.md", ROOT / "02_Revised_Manuscript.docx",
                      first_header="Species identity and soil organic carbon — revised manuscript",
                      line_numbers=True, double_space=True))
    made.append(build(src / "Response_to_Editor.md", ROOT / "03_Response_to_Editor.docx",
                      first_header="Response to the Editor — JSSP-S-26-04304",
                      line_numbers=False, double_space=False))
    made.append(build_figures_doc(ROOT / "04_Figures.docx"))
    made.append(build(ROOT / "HANDOVER.md", ROOT / "05_Revision_Notes.docx",
                      first_header="Revision notes (not for submission)",
                      line_numbers=False, double_space=False))
    for m in made:
        print("wrote", m)
