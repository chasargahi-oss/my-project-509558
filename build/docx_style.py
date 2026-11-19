"""Word styling primitives for the manuscript."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

BODY_FONT = "Times New Roman"
HEAD_FONT = "Times New Roman"


def set_run(run, size=12, bold=False, italic=False, font=BODY_FONT,
            color=None, superscript=False, subscript=False, smallcaps=False):
    run.font.name = font
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = RGBColor.from_string(color)
    run.font.superscript = superscript
    run.font.subscript = subscript
    run.font.small_caps = smallcaps
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), font)
    return run


def para(doc, text="", size=12, bold=False, italic=False, align="justify",
         space_before=0, space_after=0, line=2.0, first_indent=0.0,
         left_indent=0.0, font=BODY_FONT, keep_next=False, style=None,
         color=None, smallcaps=False):
    p = doc.add_paragraph(style=style) if style else doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line
    pf.first_line_indent = Cm(first_indent)
    pf.left_indent = Cm(left_indent)
    pf.alignment = {"justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
                    "left": WD_ALIGN_PARAGRAPH.LEFT,
                    "center": WD_ALIGN_PARAGRAPH.CENTER,
                    "right": WD_ALIGN_PARAGRAPH.RIGHT}[align]
    pf.keep_with_next = keep_next
    pf.widow_control = True
    if text:
        r = p.add_run(text)
        set_run(r, size=size, bold=bold, italic=italic, font=font, color=color,
                smallcaps=smallcaps)
    return p


def rich(doc, parts, size=12, align="justify", space_before=0, space_after=0,
         line=2.0, first_indent=0.0, left_indent=0.0, keep_next=False):
    """parts: list of (text, dict(bold=, italic=, sup=, sub=, small=))"""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line
    pf.first_line_indent = Cm(first_indent)
    pf.left_indent = Cm(left_indent)
    pf.alignment = {"justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
                    "left": WD_ALIGN_PARAGRAPH.LEFT,
                    "center": WD_ALIGN_PARAGRAPH.CENTER,
                    "right": WD_ALIGN_PARAGRAPH.RIGHT}[align]
    pf.keep_with_next = keep_next
    pf.widow_control = True
    for txt, fmt in parts:
        r = p.add_run(txt)
        set_run(r, size=fmt.get("size", size), bold=fmt.get("bold", False),
                italic=fmt.get("italic", False),
                superscript=fmt.get("sup", False),
                subscript=fmt.get("sub", False),
                color=fmt.get("color"))
    return p


def h1(doc, text, num=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(18)
    pf.space_after = Pt(6)
    pf.line_spacing = 1.5
    pf.keep_with_next = True
    label = f"{num}. {text}" if num else text
    r = p.add_run(label)
    set_run(r, size=14, bold=True, font=HEAD_FONT, color="1A1A1A")
    return p


def h2(doc, text, num=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(12)
    pf.space_after = Pt(4)
    pf.line_spacing = 1.5
    pf.keep_with_next = True
    label = f"{num} {text}" if num else text
    r = p.add_run(label)
    set_run(r, size=12, bold=True, font=HEAD_FONT, color="1A1A1A")
    return p


def h3(doc, text, num=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(9)
    pf.space_after = Pt(3)
    pf.line_spacing = 1.5
    pf.keep_with_next = True
    label = f"{num} {text}" if num else text
    r = p.add_run(label)
    set_run(r, size=12, bold=False, italic=True, font=HEAD_FONT, color="1A1A1A")
    return p


def add_field(paragraph, instr, size=9, font=BODY_FONT):
    run = paragraph.add_run()
    set_run(run, size=size, font=font)
    fld_begin = OxmlElement("w:fldChar"); fld_begin.set(qn("w:fldCharType"), "begin")
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = instr
    fld_sep = OxmlElement("w:fldChar"); fld_sep.set(qn("w:fldCharType"), "separate")
    t = OxmlElement("w:t"); t.text = "1"
    fld_end = OxmlElement("w:fldChar"); fld_end.set(qn("w:fldCharType"), "end")
    for el in (fld_begin, it, fld_sep, t, fld_end):
        run._r.append(el)


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:color"), "auto")
    sh.set(qn("w:fill"), hexcolor)
    tcPr.append(sh)


def cell_borders(cell, color="B0B0B0", sz=4, edges=("top", "bottom", "left", "right")):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for e in edges:
        el = OxmlElement(f"w:{e}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(sz))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tcPr.append(borders)


def table_rule(rows, color="1A1A1A", sz=8):
    """Add horizontal rules above the header and below the final row."""
    for r_i in (0, len(rows) - 1):
        for cell in rows[r_i].cells:
            tcPr = cell._tc.get_or_add_tcPr()
            borders = OxmlElement("w:tcBorders")
            edge = "top" if r_i == 0 else "bottom"
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), str(sz))
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), color)
            borders.append(el)
            tcPr.append(borders)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    trPr.append(el)


def keep_row_together(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:cantSplit")
    el.set(qn("w:val"), "true")
    trPr.append(el)


def set_col_widths(table, widths_cm):
    table.autofit = False
    for row in table.rows:
        for i, w in enumerate(widths_cm):
            row.cells[i].width = Cm(w)


def add_page_number_footer(section, style="i"):
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_field(p, " PAGE ", size=9)
    for r in p.runs:
        r.font.name = BODY_FONT


def add_header(section, text):
    header = section.header
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run(text)
    set_run(r, size=8.5, italic=True, color="6E6E6E")
    # bottom rule
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "4")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "C8C8C8")
    pbdr.append(bottom)
    pPr.append(pbdr)
