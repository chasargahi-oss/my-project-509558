"""Figure 3 — Evidence map: study themes (a) and confidence across the risk chain (b)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_common import *          # noqa
from textfit import Grid
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
FW, FH = DOUBLE, 3.55


def make():
    fig = plt.figure(figsize=(FW, FH))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.05, 1.0], wspace=0.70,
                          left=0.185, right=0.965, top=0.845, bottom=0.175)
    g = Grid(fig.axes[0] if fig.axes else None, FW, FH)

    # ------------------------------- (a) themes ---------------------------
    ax = fig.add_subplot(gs[0, 0])
    themes = ["Environmental fate\nand monitoring", "Bivalve and invertebrate\ntoxicology",
              "Fish toxicology", "Seafood occurrence\nand monitoring", "Trophic transfer",
              "Dietary exposure and\nrisk assessment", "Aquaculture applications\nand release"]
    vals = [11, 17, 14, 7, 3, 7, 4]
    cols = ["#4A7C9B", "#2E8B76", "#3E9C8E", "#B8860B", "#8E7CC3", "#C0603E", "#7A8B99"]
    y = np.arange(len(themes))[::-1]
    ax.barh(y, vals, color=cols, height=0.62, edgecolor="white", linewidth=0.7)
    for yy, v in zip(y, vals):
        ax.text(v + 0.4, yy, str(v), va="center", fontsize=7.0, fontweight="bold",
                color="#333333")
    ax.set_yticks(y)
    ax.set_yticklabels(themes, fontsize=6.3, linespacing=1.25)
    ax.set_xlim(0, 20)
    ax.set_xlabel("Number of included studies")
    ax.grid(axis="x", color="#E8E8E8", lw=0.5)
    ax.set_axisbelow(True)
    despine(ax)
    ax.set_title("(a)  Composition of the corpus (n = 50)", loc="left",
                 pad=9, fontsize=8.0)
    ax.text(0.0, -0.20, "Studies may address more than one theme, so bars do not sum to 50.",
            transform=ax.transAxes, fontsize=5.9, color="#7A7A7A", style="italic")

    # ------------------------------- (b) confidence ladder ----------------
    ax2 = fig.add_subplot(gs[0, 1])
    steps = [
        ("Occurrence in edible seafood", 4.0),
        ("Laboratory sub-lethal toxicity", 3.9),
        ("Bioaccumulation in bivalves", 3.7),
        ("Trophic transfer", 3.0),
        ("Environmental realism of doses", 2.1),
        ("Dietary risk characterisation", 1.4),
        ("Field-scale ecological effects", 0.9),
        ("Chronic human health effects", 0.8),
        ("Aquaculture production losses", 0.5),
    ]
    labels = [s[0] for s in steps]
    sc = [s[1] for s in steps]
    yy = np.arange(len(steps))[::-1]
    cmap = plt.get_cmap("RdYlBu")
    norm = plt.Normalize(0.2, 4.2)
    ax2.barh(yy, sc, color=[cmap(norm(v)) for v in sc], height=0.60,
             edgecolor="#4D4D4D", linewidth=0.5)
    ax2.set_yticks(yy)
    ax2.set_yticklabels(labels, fontsize=6.3)
    ax2.set_xlim(0, 5.0)
    ax2.set_xticks([0, 1, 2, 3, 4])
    ax2.set_xticklabels(["None", "Weak", "Mod.", "Mod.–\nstrong", "Strong"], fontsize=5.9, linespacing=1.2)
    ax2.set_xlabel("Confidence assigned in this review")
    ax2.grid(axis="x", color="#E8E8E8", lw=0.5)
    ax2.set_axisbelow(True)
    despine(ax2)
    ax2.set_title("(b)  Confidence in the evidence", loc="left", pad=8,
                  fontsize=8.0)
    ax2.axvline(3.5, color="#B03A2E", lw=0.7, ls=(0, (3, 2)), zorder=1)
    ax2.text(3.56, 1.30, "target for a\nquantitative\nrisk conclusion", fontsize=5.1,
             color="#B03A2E", ha="left", va="center", linespacing=1.35)
    ax2.set_ylim(-0.62, 8.62)

    fig.savefig(os.path.join(OUT, "fig3_evidence.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    make()
    print("fig3 ok")
