"""Figure 6 — Analytical workflow for ENP determination in seafood."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_common import *          # noqa
from textfit import Grid, wrap
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
FW, FH = DOUBLE, 3.55


def make():
    fig, ax = plt.subplots(figsize=(FW, FH))
    ax.set_position([0, 0, 1, 1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    g = Grid(ax, FW, FH)

    def node(xc, yc, text, fs=6.1, fc="white", ec="#1A1A1A", max_w=1.02,
             bold=False, lw=0.7):
        t = wrap(text, fs, max_w - 0.09, weight="bold" if bold else "normal")
        w, h = g.fit(t, fs, weight="bold" if bold else "normal", pad_in=0.05)
        ax.add_patch(FancyBboxPatch((xc - w / 2, yc - h / 2), w, h,
                     boxstyle="round,pad=0,rounding_size=0.006",
                     facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3))
        ax.text(xc, yc, t, ha="center", va="center", fontsize=fs, zorder=4,
                fontweight="bold" if bold else "normal", linespacing=1.45)
        return (xc - w / 2, yc - h / 2, w, h)

    def arr(p1, p2, lw=0.9, color="#1A1A1A", ms=6.0, rad=0.0):
        ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=ms,
                     linewidth=lw, color=color, zorder=2,
                     connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0))

    # stage ribbon labels
    ax.text(0.008, 0.960, "PRE-ANALYTICAL", fontsize=5.2, color="#8A9298",
            va="center", fontweight="bold")
    ax.text(0.578, 0.960, "DETERMINATION AND INTERPRETATION", fontsize=5.2,
            color="#8A9298", va="center", fontweight="bold")

    # --- row 1: sampling and digestion
    n1 = node(0.108, 0.845, "Seafood sample\nmuscle · digestive gland\ngill · whole soft tissue",
              max_w=1.36, fc="#E8F1F8")
    n2 = node(0.108, 0.640, "Homogenise and\nsub-sample", max_w=1.36)
    arr((n1[0] + n1[2] / 2, n1[1] - 0.004), (n2[0] + n2[2] / 2, n2[1] + n2[3] + 0.004))

    n3 = node(0.31, 0.680, "Enzymatic digestion\nmildest; preserves\nparticle integrity",
              max_w=1.30, fc="#EAF2E8", fs=5.9)
    n4 = node(0.31, 0.510, "Alkaline digestion\n(TMAH, ultrasound)\nmost widely used",
              max_w=1.30, fs=5.9)
    n5 = node(0.31, 0.340, "Acidic digestion\n(total element only;\ndissolves particles)",
              max_w=1.30, fc="#FBEAE6", fs=5.9)
    for n in (n3, n4, n5):
        arr((n2[0] + n2[2] + 0.004, 0.640), (n[0] - 0.004, n[1] + n[3] / 2), lw=0.65,
            color="#6E8E66", ms=5, rad=0.0)

    # --- separation
    n6 = node(0.50, 0.700, "Dilute to single-particle\nconditions\n(10$^5$–10$^7$ particles mL$^{-1}$)",
              max_w=1.30, fc="#EAF2E8", fs=5.9)
    n7 = node(0.50, 0.470, "Optional size separation\nAF4 / HDC / CPE", max_w=1.30, fs=5.9)
    arr((n4[0] + n4[2] + 0.004, 0.585), (n6[0] - 0.004, 0.685), lw=0.8, color="#6E8E66", ms=5)
    arr((n6[0] + n6[2] / 2, n6[1] - 0.004), (n7[0] + n7[2] / 2, n7[1] + n7[3] + 0.004), lw=0.8)

    # --- determination
    n8 = node(0.735, 0.700, "spICP-MS\nparticle number, mass and\nsize distribution; dissolved fraction",
              max_w=1.62, fc="#ECEAF6", fs=6.0)
    n9 = node(0.735, 0.445, "Orthogonal confirmation\nTEM/SEM–EDX · AF4–ICP-MS\nsingle-particle fingerprints",
              max_w=1.62, fc="#ECEAF6", fs=5.9)
    n10 = node(0.735, 0.190, "Occurrence + dietary exposure\nbenchmark against a\nhealth-based guidance value",
               max_w=1.62, fc="#F6E3DF", ec="#922B21", fs=5.9)
    arr((n6[0] + n6[2] + 0.004, 0.700), (n8[0] - 0.004, 0.700), lw=0.9, color="#6B5B95")
    arr((n7[0] + n7[2] + 0.004, 0.520), (n9[0] - 0.004, 0.455), lw=0.9, color="#6B5B95", rad=-0.1)
    arr((n8[0] + n8[2] / 2, n8[1] - 0.004), (n9[0] + n9[2] / 2, n9[1] + n9[3] + 0.004), lw=0.9)
    arr((n9[0] + n9[2] / 2, n9[1] - 0.004), (n10[0] + n10[2] / 2, n10[1] + n10[3] + 0.004),
        lw=0.9, color="#922B21")

    # QA/QC callout
    qa = node(0.31, 0.150, "QA/QC at every stage\nprocedural blanks · matrix spikes\nrecovery · size standards · CRMs",
              max_w=1.68, fc="#F4F6F7", ec="#7F8C8D", fs=5.7, lw=0.6)
    ax.text(0.5, 0.012,
            "Critical limitation: no certified reference material currently exists for engineered nanoparticles in a seafood matrix, so method trueness\n"
            "at environmentally relevant concentrations cannot yet be established.",
            ha="center", va="bottom", fontsize=5.4, color="#7B4B45", style="italic",
            linespacing=1.55)

    fig.savefig(os.path.join(OUT, "fig6_workflow.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    make()
    print("fig6 ok")
