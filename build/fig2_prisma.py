"""Figure 2 — PRISMA 2020 flow diagram."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_common import *          # noqa
from textfit import Grid, wrap
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
FW, FH = 150 * MM, 196 * MM


def make():
    fig, ax = plt.subplots(figsize=(FW, FH))
    ax.set_position([0, 0, 1, 1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    g = Grid(ax, FW, FH)

    # fixed column geometry, defined in inches then converted to data units
    IN_L0, IN_L1 = 0.44, 2.72        # main column
    IN_R0, IN_R1 = 3.02, 5.58        # exclusion column
    COL_L0, COL_L1 = g.px(IN_L0), g.px(IN_L1)
    COL_R0, COL_R1 = g.px(IN_R0), g.px(IN_R1)
    LXC = (COL_L0 + COL_L1) / 2
    RXC = (COL_R0 + COL_R1) / 2
    LW_IN, RW_IN = IN_L1 - IN_L0, IN_R1 - IN_R0

    def box(xc, y, text, max_w_in, fs=5.95, fc="white", ec="#1A1A1A",
            bold=False, lw=0.7):
        txt = wrap(text, fs, max_w_in - 0.10, weight="bold" if bold else "normal")
        w, h = g.fit(txt, fs, weight="bold" if bold else "normal", pad_in=0.055)
        ax.add_patch(FancyBboxPatch((xc - w / 2, y - h / 2), w, h,
                     boxstyle="round,pad=0,rounding_size=0.006",
                     facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3))
        ax.text(xc, y, txt, ha="center", va="center", fontsize=fs, zorder=4,
                fontweight="bold" if bold else "normal", linespacing=1.50)
        return (xc - w / 2, y - h / 2, w, h)

    def arr(p1, p2, lw=0.85, color="#1A1A1A", ms=6.0, z=2):
        ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=ms,
                     linewidth=lw, color=color, zorder=z, shrinkA=0, shrinkB=0))

    def stage(y0, y1, label, color):
        ax.add_patch(Rectangle((g.px(0.10), y0), g.px(0.19), y1 - y0,
                               facecolor=color, edgecolor="none", zorder=3))
        ax.text(g.px(0.195), (y0 + y1) / 2, label, rotation=90, ha="center",
                va="center", fontsize=5.0, fontweight="bold", color="white",
                zorder=4)

    # ------------------------------- IDENTIFICATION
    stage(0.845, 0.955, "IDENTIFICATION", "#4F7391")
    ident = box(LXC, 0.872,
                "Records identified through database searching and citation tracing "
                "(Consensus, Semantic Scholar, PubMed and additional sources)\n"
                "n = 509,800", max_w_in=LW_IN, fc="#E8F1F8", fs=5.9)
    rem = box(RXC, 0.872,
              "Records removed before screening\n"
              "duplicate records (n = n.r.)\n"
              "removed by automation tools (n = n.r.)\n"
              "removed for other reasons (n = n.r.)",
              max_w_in=RW_IN, fs=5.7)
    arr((ident[0] + ident[2] + 0.03, 0.872), (rem[0] - 0.025, 0.872), lw=0.7, ms=5)

    # ------------------------------- SCREENING
    stage(0.375, 0.790, "SCREENING", "#6E8C67")
    scr = box(LXC, 0.745, "Records screened at title and abstract level\nn = 509,800",
              max_w_in=LW_IN, fc="#EAF2E8", fs=5.9)
    arr((LXC, ident[1] - 0.006), (LXC, scr[1] + scr[3] + 0.006), lw=0.9)

    excl1 = box(RXC, 0.745, "Records excluded at title and abstract\nscreening\nn = 509,453",
                max_w_in=RW_IN, fs=5.8)
    arr((scr[0] + scr[2] + 0.03, 0.745), (excl1[0] - 0.025, 0.745), lw=0.7, ms=5)

    ret = box(LXC, 0.590, "Reports sought for retrieval\nn = 347",
              max_w_in=LW_IN, fc="#EAF2E8", fs=5.9)
    arr((LXC, scr[1] - 0.006), (LXC, ret[1] + ret[3] + 0.006), lw=0.9)
    nf = box(RXC, 0.590, "Reports not retrieved\nn = 0",
             max_w_in=RW_IN, fs=5.8)
    arr((ret[0] + ret[2] + 0.03, 0.590), (nf[0] - 0.025, 0.590), lw=0.7, ms=5)

    elig = box(LXC, 0.428, "Reports assessed for eligibility\n(full text)\nn = 347",
               max_w_in=LW_IN, fc="#EAF2E8", fs=5.9)
    arr((LXC, ret[1] - 0.006), (LXC, elig[1] + elig[3] + 0.006), lw=0.9)

    excl2 = box(RXC, 0.428,
                "Reports excluded (n = 297)\n"
                "not marine- or seafood-relevant (n = 96)\n"
                "no ENP exposure or occurrence data (n = 78)\n"
                "no biological, dietary or risk outcome (n = 61)\n"
                "non-peer-reviewed or no full text (n = 39)\n"
                "duplicate report of the same study (n = 23)",
                max_w_in=RW_IN, fs=5.55)
    arr((elig[0] + elig[2] + 0.03, 0.428), (excl2[0] - 0.025, 0.428), lw=0.7, ms=5)

    # ------------------------------- INCLUDED
    stage(0.185, 0.300, "INCLUDED", "#8A6584")
    inc = box(LXC, 0.232, "Studies included in qualitative synthesis\nn = 50",
              max_w_in=LW_IN, fc="#F1EAF0", fs=6.2)
    arr((LXC, elig[1] - 0.006), (LXC, inc[1] + inc[3] + 0.008), lw=0.95)

    # thematic breakdown (spans both columns)
    themes = [
        ("Environmental fate and monitoring", 11),
        ("Bivalve and invertebrate toxicology", 17),
        ("Fish toxicology", 14),
        ("Seafood occurrence and monitoring", 7),
        ("Trophic transfer", 3),
        ("Dietary exposure and risk assessment", 7),
        ("Aquaculture applications and release", 4),
    ]
    y0 = 0.148
    ax.text(0.5, y0 + 0.037, "Thematic composition of the included corpus",
            ha="center", fontsize=5.6, style="italic", color="#5A5A5A")
    # single-line chips
    x = 0.075
    yline = y0 - 0.012
    for label, n in themes:
        t = f"{label} ({n})"
        tw, th = g.fit(t, 5.1, pad_in=0.038)
        if x + tw > 0.935:
            x = 0.075
            yline -= th + 0.020
        ax.add_patch(FancyBboxPatch((x, yline - th / 2), tw, th,
                     boxstyle="round,pad=0,rounding_size=0.004",
                     facecolor="#F7F7F7", edgecolor="#B8B8B8", linewidth=0.45,
                     zorder=3))
        ax.text(x + tw / 2, yline, t, ha="center", va="center", fontsize=5.1,
                color="#3D3D3D", zorder=4)
        x += tw + 0.035

    ax.text(0.075, 0.035,
            "n.r. = not separately recorded by the search platform. Categories within each exclusion box sum to the stated total;\n"
            "studies in the included corpus may address more than one theme.",
            fontsize=5.0, color="#6E6E6E", ha="left", va="top", linespacing=1.5)

    fig.savefig(os.path.join(OUT, "fig2_prisma.png"), bbox_inches=None, pad_inches=0)
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    make()
    print("fig2 ok")
