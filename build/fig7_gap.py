"""Figure 7 — The laboratory-to-environment concentration gap."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_common import *          # noqa
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
FW, FH = DOUBLE, 3.65


def make():
    fig, ax = plt.subplots(figsize=(FW, FH))
    fig.subplots_adjust(left=0.215, right=0.895, top=0.845, bottom=0.275)

    rows = [
        # label, low, high, colour, marker
        ("Measured coastal\nseawater (total metal)", 1e-5, 1e-3, "#4A7C9B", "o"),
        ("Modelled environmental\nconcentrations", 1e-6, 1e-4, "#6FA8C4", "o"),
        ("Reported effect\nconcentrations", 1e-3, 1e1, "#C0603E", "s"),
        ("Typical laboratory\nexposure", 1e-2, 1e2, "#8E3B2E", "s"),
    ]
    y = np.arange(len(rows))[::-1]

    for yy, (lab, lo, hi, col, mk) in zip(y, rows):
        ax.plot([lo, hi], [yy, yy], color=col, lw=5.2, solid_capstyle="round",
                alpha=0.90, zorder=3)
        ax.plot([lo, hi], [yy, yy], color="none", marker=mk, markersize=0,
                zorder=3)
        ax.text(hi * 1.6, yy, f"{lo:g} – {hi:g}", va="center", fontsize=6.0,
                color="#3D3D3D")

    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=6.6, linespacing=1.3)
    ax.set_xscale("log")
    ax.set_xlim(3e-7, 1e4)
    ax.set_xlabel("Concentration (mg L$^{-1}$)")
    ax.grid(axis="x", color="#E8E8E8", lw=0.5)
    ax.set_axisbelow(True)
    despine(ax)
    ax.set_ylim(-0.95, 3.55)

    # gap shading
    ax.axvspan(1e-3, 1e-2, color="#F7E1DC", zorder=1)
    ax.text(np.sqrt(1e-3 * 1e-2), 3.30, "exposure\nmismatch", ha="center",
            fontsize=5.6, color="#8C3B31", linespacing=1.3, style="italic")

    # two-sided arrow for the gap
    ax.annotate("", xy=(1e-2, 0.62), xytext=(1e-3, 0.62),
                arrowprops=dict(arrowstyle="<->", color="#922B21", lw=0.9))
    ax.text(3.16e-3, 0.40, "≈10–100×", ha="center", fontsize=5.8, color="#922B21",
            fontweight="bold")

    ax.set_title("Laboratory hazard studies operate above measured\nenvironmental concentrations",
                 loc="left", pad=9, fontsize=8.2, linespacing=1.35)

    ax.text(0.0, -0.195,
            "Indicative envelopes assembled from the studies reviewed here; they convey order-of-magnitude separation, not regulatory thresholds.\n"
            "Dissolved ions released from particles can approach the lower end of the reported effect range.",
            transform=ax.transAxes, fontsize=5.4, color="#6E6E6E", va="top",
            linespacing=1.55)

    fig.savefig(os.path.join(OUT, "fig7_gap.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    make()
    print("fig7 ok")
