"""Figure 8 — Decision framework for interpreting a positive ENP detection in seafood."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_common import *          # noqa
from textfit import Grid, wrap
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
FW, FH = DOUBLE, 4.30


def make():
    fig, ax = plt.subplots(figsize=(FW, FH))
    ax.set_position([0, 0, 1, 1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    g = Grid(ax, FW, FH)

    def box(xc, yc, text, fs=5.99, fc="white", ec="#1A1A1A", max_w=1.70,
            bold=False, lw=0.7):
        t = wrap(text, fs, max_w - 0.10, weight="bold" if bold else "normal")
        w, h = g.fit(t, fs, weight="bold" if bold else "normal", pad_in=0.048)
        ax.add_patch(FancyBboxPatch((xc - w / 2, yc - h / 2), w, h,
                     boxstyle="round,pad=0,rounding_size=0.006",
                     facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3))
        ax.text(xc, yc, t, ha="center", va="center", fontsize=fs, zorder=4,
                fontweight="bold" if bold else "normal", linespacing=1.45)
        return (xc - w / 2, yc - h / 2, w, h)

    def arr(p1, p2, lw=0.85, color="#1A1A1A", ms=6.0, rad=0.0, ls="-"):
        ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=ms,
                     linewidth=lw, color=color, zorder=2, linestyle=ls,
                     connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0))

    def qnum(y, n, colour):
        ax.add_patch(plt.Circle((g.px(0.20), y), g.px(0.075), facecolor=colour,
                                edgecolor="none", zorder=4))
        ax.text(g.px(0.20), y, str(n), ha="center", va="center", fontsize=6.2,
                color="white", fontweight="bold", zorder=5)

    LXC, RXC = 0.300, 0.745

    top = box(LXC, 0.930, "Positive spICP-MS signal for Ti, Ag, Zn, Cu or Ce in an edible tissue",
              fc="#E8F1F8", max_w=2.62, fs=6.2)

    rows = [
        ("Particle morphology and elemental composition confirmed by TEM/SEM–EDX?",
         "Signal may reflect dissolved metal or\nionic interference: report as total\nelement, not as a nanoparticle", 0.760, "#4A7C9B"),
        ("Size distribution distinguishable from natural and incidental particle pools?",
         "Natural or processing-derived source\ncannot be excluded: retain only as\npreliminary occurrence data", 0.590, "#2E8B76"),
        ("Particle survives simulated gastrointestinal digestion in a bioaccessible form?",
         "Dissolution before systemic uptake:\nhazard assessment shifts to the\nreleased metal ion", 0.420, "#B8860B"),
        ("Chronic oral-toxicity data available at a comparable dose and particle form?",
         "Hazard cannot be characterised:\nretain as an emerging risk and\nprioritise targeted testing", 0.250, "#B03A2E"),
    ]

    prev_bottom = (LXC, top[1] - 0.004)
    qb = []
    for q, no_txt, y, col in rows:
        b = box(LXC, y, q, max_w=2.52, fs=5.95)
        qb.append(b)
        arr(prev_bottom, (LXC, y + b[3] + 0.006), lw=0.85)
        nb = box(RXC, y, no_txt, max_w=2.10, fs=5.75, fc="#F4F6F7", ec="#7F8C8D", lw=0.6)
        arr((b[0] + b[2] + 0.004, y), (nb[0] - 0.006, y), lw=0.7, ms=5.2)
        ax.text((b[0] + b[2] + nb[0]) / 2, y + 0.019, "no", ha="center",
                fontsize=5.5, style="italic", color="#7B7B7B")
        ax.text(LXC + 0.012, y - b[3] / 2 - 0.019, "yes", fontsize=5.5,
                style="italic", color="#2C6E49", fontweight="bold")
        qnum(y, len(qb), col)
        prev_bottom = (LXC, y - b[3] / 2 - 0.004)

    fin = box(LXC, 0.098, "DERIVE a margin of exposure against a reference point  ·  quantitative risk characterisation becomes possible",
              fc="#CBE3D2", ec="#2C6E49", max_w=2.62, bold=True, lw=0.95, fs=6.0)
    arr(prev_bottom, (LXC, fin[1] + fin[3] + 0.006), lw=1.0, color="#2C6E49")

    ax.text(RXC, 0.098,
            "Reached for very few nanoparticles today.\n"
            "The reference point would be a NOAEL or BMDL from a\n"
            "subchronic or chronic study of the same particle form.",
            ha="center", va="center", fontsize=5.35, color="#4F6B5B",
            linespacing=1.55, style="italic")

    ax.text(0.012, 0.012,
            "Every step should be documented with orthogonal measurements (TEM/EDX, AF4–ICP-MS) and validated against reference materials where available.",
            fontsize=5.3, color="#6E6E6E", ha="left", style="italic")

    fig.savefig(os.path.join(OUT, "fig8_decision.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    make()
    print("fig8 ok")
