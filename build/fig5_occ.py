"""Figure 5 — Reported ENP occurrence in canned seafood (a) and dietary intake (b)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_common import *          # noqa
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
FW, FH = DOUBLE, 3.30


def make():
    fig = plt.figure(figsize=(FW, FH))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.18, 1.0], wspace=0.62,
                          left=0.080, right=0.905, top=0.855, bottom=0.225)

    # ---------------------- (a) TiO2-NP by product ------------------------
    ax = fig.add_subplot(gs[0, 0])
    prods = ["Canned\nclam", "Canned\ntuna", "Canned\nanchovy", "Canned\nmackerel"]
    means = [0.1116, 0.0380, 0.0092, 0.0085]
    mins = [0.0650, 0.0062, 0.0078, 0.0020]
    maxs = [0.1403, 0.1251, 0.0137, 0.0206]
    cols = [C["ti"], "#4E9BC9", "#7FB6D8", "#B0CFE4"]
    x = np.arange(len(prods))
    ax.bar(x, means, width=0.60, color=cols, edgecolor="#1A1A1A", linewidth=0.55,
           zorder=3, label="Mean")
    ax.errorbar(x, means, yerr=[np.array(means) - np.array(mins), np.array(maxs) - np.array(means)],
                fmt="none", ecolor="#1A1A1A", elinewidth=0.7, capsize=2.6, capthick=0.7,
                zorder=4)
    for xi, m in zip(x, means):
        ax.text(xi, m + 0.006, f"{m:.3f}", ha="center", va="bottom", fontsize=6.2,
                fontweight="bold", color="#1A1A1A")
    ax.set_xticks(x); ax.set_xticklabels(prods, fontsize=6.6, linespacing=1.2)
    ax.set_ylabel("TiO$_2$ nanoparticle concentration\n(mg kg$^{-1}$ wet weight)")
    ax.set_ylim(0, 0.165)
    ax.grid(axis="y", color="#EAEAEA", lw=0.5, zorder=0)
    ax.set_axisbelow(True)
    despine(ax)
    ax.set_title("(a)  TiO$_2$ nanoparticles in canned seafood", loc="left", pad=8, fontsize=7.9)
    ax.text(0.985, 0.905, "45 tuna · 36 mackerel · 27 anchovy · 37 clam samples",
            transform=ax.transAxes, ha="right", fontsize=5.6, color="#8A8A8A", style="italic")
    ax.text(0.015, 0.955, "TiO$_2$-NP fraction < 100 nm", transform=ax.transAxes,
            fontsize=5.8, color=C["ti"], fontweight="bold")

    # ---------------------- (b) intake: NP vs dissolved -------------------
    ax2 = fig.add_subplot(gs[0, 1])
    ylab = ["ZnO-NP\nadults", "ZnO-NP\nchildren", "Dissolved Zn\nadults", "Dissolved Zn\nchildren"]
    vals = [0.031, 0.067, 109.3, 240.1]
    colors = ["#B03A2E", "#D6604D", "#4393C3", "#2166AC"]
    yy = np.arange(len(ylab))[::-1]
    ax2.barh(yy, vals, height=0.60, color=colors, edgecolor="#1A1A1A", linewidth=0.55, zorder=3)
    ax2.set_yticks(yy); ax2.set_yticklabels(ylab, fontsize=6.5, linespacing=1.25)
    ax2.set_xscale("log")
    ax2.set_xlim(0.005, 900)
    ax2.set_xlabel("Estimated intake, one meal\n(µg kg$^{-1}$ body weight)", linespacing=1.4)
    for y_, v in zip(yy, vals):
        ax2.text(v * 1.25, y_, f"{v:g}", va="center", fontsize=6.2, fontweight="bold")
    ax2.grid(axis="x", color="#EAEAEA", lw=0.5, zorder=0)
    ax2.set_axisbelow(True)
    despine(ax2)
    ax2.set_title("(b)  Particle-bound vs. dissolved Zn", loc="left", pad=8, fontsize=7.9)
    ax2.axvspan(0.005, 0.45, color="#FDF0EE", zorder=1)
    ax2.text(0.0062, -0.78, "particle-bound", fontsize=5.6, color="#8C3B31", ha="left")
    ax2.text(700, -0.78, "dissolved metal", fontsize=5.6, color="#1F4E79", ha="right")
    ax2.set_ylim(-0.95, 3.62)
    ax2.text(0.98, 0.965, "3.5–4 orders of magnitude", transform=ax2.transAxes, ha="right",
             fontsize=6.0, color="#4D4D4D", style="italic")

    fig.savefig(os.path.join(OUT, "fig5_occurrence.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    make()
    print("fig5 ok")
