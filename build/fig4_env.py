"""Figure 4 — Environmental occurrence and particle-size context."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_common import *          # noqa
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
FW, FH = DOUBLE, 3.15


def make():
    fig = plt.figure(figsize=(FW, FH))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.0], wspace=0.52,
                          left=0.092, right=0.975, top=0.845, bottom=0.255)

    # (a) seawater particle number concentrations, Laizhou Bay
    ax = fig.add_subplot(gs[0, 0])
    metals = ["Ti", "Zn", "Ag", "Cu", "Au"]
    vals = [1.78e8, 1.27e8, 3.5e7, 2.6e7, 8.0e5]
    cols = [C["ti"], C["zn"], C["ag"], C["cu"], "#9E9E9E"]
    x = np.arange(len(metals))
    ax.bar(x, vals, color=cols, width=0.62, edgecolor="#1A1A1A", linewidth=0.55, zorder=3)
    ax.set_yscale("log")
    ax.set_ylim(1e5, 6e8)
    ax.set_xticks(x); ax.set_xticklabels(metals, fontsize=6.8)
    ax.set_ylabel("Particles L$^{-1}$ (seawater)")
    def sci(v):
        m, e = f"{v:.1e}".split("e")
        return f"{float(m):.1f}×10$^{{{int(e)}}}$"
    for xi, v in zip(x, vals):
        ax.text(xi, v * 1.42, sci(v), ha="center", fontsize=5.7)
    ax.set_xlabel("Element of the detected particle")
    ax.grid(axis="y", color="#EAEAEA", lw=0.5, zorder=0)
    ax.set_axisbelow(True)
    despine(ax)
    ax.set_title("(a)  Metal-bearing particles in coastal seawater", loc="left",
                 pad=8, fontsize=7.9)
    ax.text(0.5, -0.245, "Laizhou Bay, China; mean of 24 stations",
            transform=ax.transAxes, ha="center", fontsize=5.5, color="#8A8A8A",
            style="italic")

    # (b) particle size comparison across matrices
    ax2 = fig.add_subplot(gs[0, 1])
    groups = [
        ("Seawater\n(ambient)", 16, 30, "#4A7C9B"),
        ("Canned seafood\n(Ag-NP)", 31, 36, C["ag"]),
        ("Canned seafood\n(ZnO-NP)", 61, 79, C["zn"]),
        ("Canned seafood\n(TiO$_2$-NP)", 72, 89, C["ti"]),
        ("Offshore bivalves\n(Zn-bearing)", 98, 108, C["cu"]),
    ]
    yy = np.arange(len(groups))[::-1]
    for y_, (lab, lo, hi, col) in zip(yy, groups):
        ax2.plot([lo, hi], [y_, y_], color=col, lw=5.0, solid_capstyle="round", zorder=3)
        ax2.text(hi + 4.0 if hi + 4.0 < 118 else hi - 4.0, y_,
                 f"{lo}–{hi}", va="center", fontsize=5.9, color="#3D3D3D",
                 ha="left" if hi + 4.0 < 118 else "right")
    ax2.set_yticks(yy)
    ax2.set_yticklabels([g[0] for g in groups], fontsize=6.3, linespacing=1.25)
    ax2.set_xlim(0, 140)
    ax2.set_xlabel("Reported mean particle diameter (nm)")
    ax2.axvline(100, color="#B03A2E", lw=0.8, ls=(0, (3, 2)), zorder=1)
    ax2.text(101.5, 4.42, "100 nm", fontsize=5.5, color="#B03A2E", va="top")
    ax2.grid(axis="x", color="#EAEAEA", lw=0.5, zorder=0)
    ax2.set_axisbelow(True)
    despine(ax2)
    ax2.set_title("(b)  Particle size across matrices", loc="left", pad=8, fontsize=7.9)
    ax2.set_ylim(-1.25, 4.6)

    fig.savefig(os.path.join(OUT, "fig4_occurrence_env.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    make()
    print("fig4 ok")
