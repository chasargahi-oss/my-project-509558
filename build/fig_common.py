"""Shared plotting style for the ENP-seafood review figures.

All figures are rendered at 600 dpi and sized for a single column
(85 mm) or double column (170 mm) in a journal layout.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

MM = 1 / 25.4  # mm -> inch
DOUBLE = 170 * MM
SINGLE = 85 * MM
DPI = 600

# Colour-blind-safe qualitative palette (Okabe-Ito derived) + sequential ramp
C = {
    "ti":    "#0072B2",
    "ag":    "#E69F00",
    "zn":    "#009E73",
    "cu":    "#CC79A7",
    "ce":    "#56B4E9",
    "grey":  "#595959",
    "light": "#D9D9D9",
    "dark":  "#1A1A1A",
    "red":   "#B2182B",
    "blue2": "#2166AC",
    "amber": "#F4A582",
    "teal":  "#80CDC1",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8.0,
    "axes.labelsize": 8.5,
    "axes.titlesize": 9.0,
    "axes.titleweight": "bold",
    "axes.linewidth": 0.7,
    "axes.edgecolor": "#1A1A1A",
    "axes.labelcolor": "#1A1A1A",
    "xtick.labelsize": 7.2,
    "ytick.labelsize": 7.2,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.major.size": 2.6,
    "ytick.major.size": 2.6,
    "xtick.color": "#1A1A1A",
    "ytick.color": "#1A1A1A",
    "legend.frameon": False,
    "legend.fontsize": 7.0,
    "savefig.dpi": DPI,
    "savefig.bbox": "standard",
    "savefig.pad_inches": 0.0,
    "figure.dpi": 120,
    "lines.linewidth": 1.0,
    "patch.linewidth": 0.6,
})


def panel(ax, letter, x=-0.13, y=1.06):
    """Add a bold panel letter above the axes."""
    ax.text(x, y, letter, transform=ax.transAxes, fontsize=10.5,
            fontweight="bold", va="top", ha="left", color="#1A1A1A")


def despine(ax, keep=("left", "bottom")):
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(s in keep)
