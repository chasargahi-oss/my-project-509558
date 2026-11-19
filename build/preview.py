"""Approximate page renderer for the generated .docx, used only for visual QA.

Reconstructs page layout from the document body (paragraphs + tables + images)
using PIL text metrics, then draws each page with matplotlib.
"""
import os, sys
from docx import Document
from docx.shared import Emu
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn
from PIL import ImageFont
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# A4 in points
PW, PH = 595.28, 841.89
MARGIN = 70.87  # 2.5 cm
CONTENT_W = PW - 2 * MARGIN
CONTENT_TOP = PH - MARGIN
CONTENT_BOT = MARGIN
CONTENT_H = CONTENT_TOP - CONTENT_BOT

FONT_PATHS = {
 ("serif", False, False): "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
 ("serif", True, False): "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
 ("serif", False, True): "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
 ("serif", True, True): "/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf",
}
_cache = {}


def get_font(size_pt, bold=False, italic=False):
    key = (round(size_pt * 4), bold, italic)
    if key not in _cache:
        path = FONT_PATHS[("serif", bold, italic)]
        if not os.path.exists(path):
            path = FONT_PATHS[("serif", False, False)]
        _cache[key] = ImageFont.truetype(path, max(1, int(round(size_pt * 4))))
    return _cache[key]


def tw(text, size_pt, bold=False, italic=False):
    """width in points"""
    f = get_font(size_pt, bold, italic)
    return f.getlength(text) / 4.0


# ---------------------------------------------------------------- extraction
def para_props(p):
    pf = p.paragraph_format
    size, bold, italic = 12.0, False, False
    txt = ""
    runs = []
    for r in p.runs:
        if r.font.size:
            size = r.font.size.pt
        bold = bold or bool(r.bold)
        italic = italic or bool(r.italic)
        txt += r.text
        runs.append((r.text, r.font.size.pt if r.font.size else 12.0,
                     bool(r.bold), bool(r.italic)))
    ls = pf.line_spacing if pf.line_spacing else 1.0
    if ls is None:
        ls = 1.0
    indent_l = (pf.left_indent.pt if pf.left_indent else 0.0)
    indent_f = (pf.first_line_indent.pt if pf.first_line_indent else 0.0)
    before = pf.space_before.pt if pf.space_before else 0.0
    after = pf.space_after.pt if pf.space_after else 0.0
    align = pf.alignment
    has_img = False
    img_w = None
    img_ar = 0.55
    for r in p.runs:
        if r._element.findall(qn("w:drawing")):
            has_img = True
            for d in r._element.findall(qn("w:drawing")):
                for ext in d.iter(qn("wp:extent")):
                    cx, cy = int(ext.get("cx")), int(ext.get("cy"))
                    img_w = Emu(cx).pt
                    if cx:
                        img_ar = cy / cx
    return dict(text=txt, size=size, bold=bold, italic=italic, ls=ls,
                indent_l=indent_l, indent_f=indent_f, before=before,
                after=after, align=str(align), has_img=has_img, img_w=img_w,
                img_ar=img_ar, runs=runs)


def wrap_lines(text, size, width, bold=False, italic=False):
    if not text.strip():
        return [""]
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w) if cur else w
        if tw(trial, size, bold, italic) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def height_of(pp, width):
    if pp["has_img"]:
        return (pp["img_w"] or CONTENT_W) * pp["img_ar"] + 4
    if not pp["text"].strip():
        return pp["size"] * 0.6 * pp["ls"] + pp["before"] + pp["after"]
    w = width - pp["indent_l"] - max(0, pp["indent_f"])
    lines = wrap_lines(pp["text"], pp["size"], w, pp["bold"], pp["italic"])
    return len(lines) * pp["size"] * 1.17 * pp["ls"] + pp["before"] + pp["after"]


# ---------------------------------------------------------------- build flow
def iter_block(doc):
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield ("p", Paragraph(child, doc))
        elif child.tag == qn("w:tbl"):
            yield ("t", Table(child, doc))


def extract():
    doc = Document(os.path.join(
        ROOT, "output",
        "Engineered_nanoparticles_seafood_safety_Systematic_Review.docx"))
    blocks = []
    for kind, obj in iter_block(doc):
        if kind == "p":
            pp = para_props(obj)
            kwn = bool(obj.paragraph_format.keep_with_next)
            # page break detection
            brk = bool(obj._p.findall(".//" + qn("w:br")))
            brk = brk and any(b.get(qn("w:type")) == "page"
                              for b in obj._p.iter(qn("w:br")))
            blocks.append(("p", pp, brk, kwn))
        else:
            blocks.append(("t", obj, False, False))
    return blocks


def table_dims(tbl):
    """returns (widths_pt, rows_of_list_of_(text,size,bold), height_pt)"""
    grid = tbl._tbl.find(qn("w:tblGrid"))
    widths = []
    if grid is not None:
        for gc in grid.findall(qn("w:gridCol")):
            widths.append(int(gc.get(qn("w:w"))) / 20.0)
    if not widths or sum(widths) < 10:
        widths = [CONTENT_W / len(tbl.columns)] * len(tbl.columns)
    rows = []
    total_h = 0.0
    for row in tbl.rows:
        cells = []
        maxh = 0.0
        for i, c in enumerate(row.cells):
            txt = c.text
            size, bold = 8.2, False
            for p in c.paragraphs:
                for r in p.runs:
                    if r.font.size:
                        size = r.font.size.pt
                    bold = bool(r.bold)
            cells.append((txt, size, bold))
            inner = widths[i] - 11.0
            n = max(1, len(wrap_lines(txt, size, inner, bold)))
            maxh = max(maxh, n * size * 1.15 + 5.0)
        rows.append(cells)
        total_h += maxh
    return widths, rows, total_h


def _block_h(item):
    if item[0] == "p":
        return height_of(item[1], CONTENT_W)
    return item[-1]   # table tuple carries its height


def _emit_table(obj, y, pages, cur):
    """Emit table rows starting at y, splitting across pages. Returns (cur, y)."""
    widths, rows, th = table_dims(obj)
    if y - th < CONTENT_BOT and cur:
        pages.append(cur); cur = []; y = CONTENT_TOP
    remaining = list(rows)
    while remaining:
        avail = y - CONTENT_BOT
        fit, used = [], 0.0
        for r in remaining:
            rh = max((len(wrap_lines(c[0], c[1], widths[i] - 11, c[2])) *
                      c[1] * 1.15 + 5.0) for i, c in enumerate(r))
            if used + rh > avail and fit:
                break
            fit.append(r); used += rh
        cur.append(("t", obj, y, CONTENT_TOP, fit, widths, used))
        y -= used
        remaining = remaining[len(fit):]
        if remaining:
            pages.append(cur); cur = []; y = CONTENT_TOP
    return cur, y


def paginate(blocks):
    # group keep-with-next chains into atomic units
    units, i = [], 0
    while i < len(blocks):
        grp = [blocks[i]]
        while grp[-1][0] == "p" and grp[-1][3] and i + 1 < len(blocks):
            i += 1
            grp.append(blocks[i])
        units.append(grp)
        i += 1

    pages, cur, y = [], [], CONTENT_TOP
    for grp in units:
        kind, obj, brk, kwn = grp[0]
        if brk and cur:
            pages.append(cur); cur = []; y = CONTENT_TOP

        if kind == "p":
            total = 0.0
            for g in grp:
                if g[0] == "p":
                    total += height_of(g[1], CONTENT_W)
                else:
                    total += table_dims(g[1])[2]
            if y - total < CONTENT_BOT and cur:
                pages.append(cur); cur = []; y = CONTENT_TOP
            for g in grp:
                if g[0] == "p":
                    cur.append(("p", g[1], y, CONTENT_TOP))
                    y -= height_of(g[1], CONTENT_W)
                else:
                    cur, y = _emit_table(g[1], y, pages, cur)
        else:
            cur, y = _emit_table(obj, y, pages, cur)

    if cur:
        pages.append(cur)
    return pages


def draw_page(page, idx, outdir):
    fig = plt.figure(figsize=(PW / 72, PH / 72), dpi=110)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, PW); ax.set_ylim(0, PH); ax.axis("off")
    ax.add_patch(Rectangle((0, 0), PW, PH, facecolor="white", edgecolor="none"))
    ax.add_patch(Rectangle((MARGIN, MARGIN), CONTENT_W, CONTENT_H,
                           facecolor="none", edgecolor="#E8E8E8", lw=0.4))

    for item in page:
        if item[0] == "p":
            _, pp, y, _ = item
            if pp["has_img"]:
                w = min(pp["img_w"] or CONTENT_W, CONTENT_W)
                h = w * pp.get("img_ar", 0.55)
                ax.add_patch(Rectangle((MARGIN + (CONTENT_W - w) / 2, y - h), w, h,
                                       facecolor="#EAF2F8", edgecolor="#4A7C9B",
                                       lw=0.5, ls="--"))
                ax.text(MARGIN + CONTENT_W / 2, y - h / 2, "[image]",
                        ha="center", va="center", fontsize=6, color="#4A7C9B")
                continue
            if not pp["text"].strip():
                continue
            w = CONTENT_W - pp["indent_l"] - max(0, pp["indent_f"])
            lh = pp["size"] * 1.17 * pp["ls"]
            yy = y - pp["before"] - pp["size"] * 0.95
            centered = pp["align"].strip().startswith("CENTER")
            # wrap across the full paragraph, then place run-by-run with italics
            lines = wrap_lines(pp["text"], pp["size"], w, pp["bold"], pp["italic"])
            char_spans = []
            pos = 0
            for rtxt, rsz, rb, ri in pp.get("runs", []):
                char_spans.append((pos, pos + len(rtxt), rb, ri))
                pos += len(rtxt)
            # map paragraph text offset -> (bold, italic)
            def fmt_at(k):
                for a, b, rb, ri in char_spans:
                    if a <= k < b:
                        return rb, ri
                return pp["bold"], pp["italic"]
            # rebuild text with explicit spaces to track offsets
            rebuilt = " ".join(lines)
            # place each line, splitting into italic/non-italic segments
            cursor = 0
            for ln in lines:
                start = rebuilt.find(ln, cursor)
                cursor = start + len(ln)
                if centered:
                    x = PW / 2 - tw(ln, pp["size"], pp["bold"], pp["italic"]) / 2
                else:
                    x = MARGIN + pp["indent_l"]
                k = 0
                seg_start = 0
                cur_fmt = fmt_at(start) if ln else (pp["bold"], pp["italic"])
                for k in range(1, len(ln) + 1):
                    f = fmt_at(start + k) if start + k < pos else cur_fmt
                    if f != cur_fmt or k == len(ln):
                        seg = ln[seg_start:k]
                        ax.text(x, yy, seg, ha="left", va="baseline",
                                fontsize=pp["size"], color="#1A1A1A", family="serif",
                                fontweight="bold" if cur_fmt[0] else "normal",
                                style="italic" if cur_fmt[1] else "normal")
                        x += tw(seg, pp["size"], cur_fmt[0], cur_fmt[1])
                        seg_start = k
                        cur_fmt = f
                yy -= lh
        else:
            _, tbl, y, _, rows, widths, th = item
            x = MARGIN + (CONTENT_W - sum(widths)) / 2
            cy = y
            for cells in rows:
                rowh = max((len(wrap_lines(c[0], c[1], widths[i] - 11, c[2])) *
                            c[1] * 1.15 + 5.0) for i, c in enumerate(cells))
                cx = x
                for i, (txt, size, bold) in enumerate(cells):
                    inner = widths[i] - 11
                    ls = wrap_lines(txt, size, inner, bold)
                    ty = cy - size
                    for ln in ls:
                        ax.text(cx + 5, ty, ln, ha="left", va="baseline",
                                fontsize=size, family="serif", color="#1A1A1A",
                                fontweight="bold" if bold else "normal")
                        ty -= size * 1.15
                    ax.add_patch(Rectangle((cx, cy - rowh), widths[i], rowh,
                                           facecolor="none", edgecolor="#DDDDDD",
                                           lw=0.35))
                    cx += widths[i]
                cy -= rowh

    ax.text(PW / 2, MARGIN / 2, str(idx + 1), ha="center", va="center",
            fontsize=7.5, color="#999999")
    fn = os.path.join(outdir, f"page_{idx+1:02d}.png")
    fig.savefig(fn, dpi=110)
    plt.close(fig)
    return fn


def main():
    outdir = os.path.join(ROOT, "output", "preview")
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir):
        if f.endswith(".png"):
            os.remove(os.path.join(outdir, f))
    blocks = extract()
    pages = paginate(blocks)
    for i, pg in enumerate(pages):
        draw_page(pg, i, outdir)
    print(f"{len(pages)} pages -> {outdir}")

    # overflow check
    worst = 0
    for i, pg in enumerate(pages):
        last = pg[-1]
        y = last[2]
        h = height_of(last[1], CONTENT_W) if last[0] == "p" else last[6]
        if y - h < CONTENT_BOT - 2:
            print(f"  !! page {i+1} overflows by {CONTENT_BOT - (y-h):.0f} pt")


if __name__ == "__main__":
    main()
