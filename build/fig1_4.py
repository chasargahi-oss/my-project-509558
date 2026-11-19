"""Figure 1 - Conceptual exposure-and-effect pathway for ENPs in seafood systems.
Figure 4 - Source-to-offshore exposure gradient.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_common import *          # noqa
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")


def box(ax, x, y, w, h, text, fc="#FFFFFF", ec="#1A1A1A", fs=6.9, bold=False, lw=0.7, r=0.012):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0.004,rounding_size={r}",
                       facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal", zorder=4, linespacing=1.35)
    return p


def arrow(ax, p1, p2, style="-|>", lw=0.85, color="#1A1A1A", ls="-", rad=0.0, ms=6):
    a = FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=ms, linewidth=lw,
                        color=color, linestyle=ls, zorder=2,
                        connectionstyle=f"arc3,rad={rad}", shrinkA=1, shrinkB=1)
    ax.add_patch(a)


# ----------------------------------------------------------------- FIGURE 1
def figure1():
    fig, ax = plt.subplots(figsize=(DOUBLE, 4.55))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    # --- column headers -----------------------------------------------------
    heads = [(0.115, "SOURCES"), (0.315, "MARINE SYSTEM"), (0.520, "EXPOSURE & UPTAKE"),
             (0.735, "FOOD CHAIN & SEAFOOD"), (0.930, "HUMAN HEALTH")]
    for x, t in heads:
        ax.text(x, 0.965, t, ha="center", va="center", fontsize=6.2,
                color="#6E6E6E", fontweight="bold")

    # band shading
    ax.add_patch(Rectangle((0.0, 0.0), 1.0, 0.925, facecolor="#FAFAFA",
                           edgecolor="none", zorder=0))

    # --- row 1: release -----------------------------------------------------
    y1, hb = 0.815, 0.095
    box(ax, 0.020, y1, 0.195, hb,
        "Nanomaterial production\nand nano-enabled products", fc="#EAF2F8")
    box(ax, 0.245, y1, 0.155, hb, "Wastewater\neffluent", fc="#FFFFFF")
    box(ax, 0.245, y1 - 0.115, 0.155, hb, "Stormwater\nand runoff", fc="#FFFFFF")
    box(ax, 0.245, y1 - 0.23, 0.155, hb, "Antifouling coatings,\nconsumer goods", fc="#FFFFFF", fs=6.4)
    box(ax, 0.245, y1 - 0.345, 0.155, hb, "Aquaculture feeds,\ntherapeutics, effluent", fc="#FFFFFF", fs=6.4)

    box(ax, 0.435, 0.735, 0.175, 0.175,
        "Coastal seawater\nand sediments", fc="#E8F4F0", bold=True, fs=7.6)
    box(ax, 0.435, 0.430, 0.175, 0.145,
        "Aggregation\nDissolution\nSedimentation", fc="#FFFFFF", fs=6.5)
    box(ax, 0.435, 0.230, 0.175, 0.145,
        "Corona formation\nTransformation\nResuspension", fc="#FFFFFF", fs=6.5)

    # arrows release -> coastal
    for yy in (y1 + hb / 2, y1 - 0.115 + hb / 2, y1 - 0.23 + hb / 2, y1 - 0.345 + hb / 2):
        arrow(ax, (0.401, yy), (0.433, 0.80 if yy > 0.6 else 0.78), rad=0.0, lw=0.7)
    arrow(ax, (0.215, y1 + hb / 2), (0.243, y1 + hb / 2))

    arrow(ax, (0.5225, 0.735), (0.5225, 0.578), lw=0.9)
    arrow(ax, (0.5225, 0.430), (0.5225, 0.378), lw=0.9)

    # --- organisms ----------------------------------------------------------
    ax.add_patch(Rectangle((0.635, 0.185), 0.175, 0.700, facecolor="#FDF6EC",
                           edgecolor="none", zorder=0))
    ax.text(0.7225, 0.855, "Route of exposure", ha="center", fontsize=6.2,
            color="#8A6D3B", style="italic")
    routes = [("Waterborne\nuptake", 0.775), ("Filter feeding\n(bivalves)", 0.665),
              ("Dietary uptake\nand trophic transfer", 0.555), ("Sediment contact\n(deposit feeders)", 0.445),
              ("Gill and gut\nabsorption (fish)", 0.335)]
    for txt, yy in routes:
        box(ax, 0.648, yy - 0.045, 0.149, 0.086, txt, fc="#FFFFFF", fs=6.2)

    # --- edible tissue ------------------------------------------------------
    box(ax, 0.648, 0.045, 0.149, 0.105, "Edible tissues\n(muscle, digestive gland,\ngill, mantle)",
        fc="#FDEDEC", bold=False, fs=6.2)
    for _, yy in routes:
        arrow(ax, (0.7225, yy - 0.049), (0.7225, 0.152), lw=0.55, color="#8A6D3B", ms=5)

    # --- human --------------------------------------------------------------
    box(ax, 0.828, 0.475, 0.150, 0.115, "Seafood monitoring\nand dietary exposure\nassessment",
        fc="#EDEAF5", fs=6.3)
    box(ax, 0.828, 0.290, 0.150, 0.115, "Human consumers\n(adults, children,\nhigh consumers)",
        fc="#EDEAF5", fs=6.3)
    box(ax, 0.828, 0.075, 0.150, 0.145,
        "Chronic low-dose\nrisk: not yet\ncharacterized\n(no reference dose)",
        fc="#F5B7B1", ec="#922B21", fs=6.3, bold=True)

    arrow(ax, (0.797, 0.098), (0.826, 0.53), rad=-0.25, lw=1.0)
    arrow(ax, (0.903, 0.475), (0.903, 0.408), lw=0.9)
    arrow(ax, (0.903, 0.290), (0.903, 0.223), lw=0.9, color="#922B21")

    # ---- feedback loop: uncertainty ----------------------------------------
    ax.add_patch(FancyBboxPatch((0.020, 0.045), 0.575, 0.115,
                 boxstyle="round,pad=0.004,rounding_size=0.012",
                 facecolor="#F4F6F7", edgecolor="#7F8C8D", linewidth=0.6,
                 linestyle=(0, (3, 2)), zorder=3))
    ax.text(0.307, 0.128, "CRITICAL KNOWLEDGE GAPS", ha="center", fontsize=5.9,
            fontweight="bold", color="#566573")
    ax.text(0.307, 0.078,
            "Source attribution  ·  concentration gap between laboratory and field  ·  bioaccessibility after digestion\n"
            "chronic oral toxicity  ·  absence of health-based guidance values",
            ha="center", va="center", fontsize=5.9, color="#34495E", linespacing=1.5)

    fig.savefig(os.path.join(OUT, "fig1_pathway.png"))
    plt.close(fig)


# ----------------------------------------------------------------- FIGURE 4
def figure4():
    """Source-to-offshore gradient: fate processes and reported concentration envelopes."""
    fig = plt.figure(figsize=(DOUBLE, 2.9))
    gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.25], wspace=0.30)
    zones = [
        ("Point-source\nzone", "#FDEDEC", "#922B21",
         "Wastewater outfall,\nharbour, urban runoff,\naquaculture discharge"),
        ("Nearshore\ncoastal water", "#FDF6EC", "#B9770E",
         "Dilution, hetero-aggregation,\npartial dissolution"),
        ("Shelf and\noffshore water", "#EAF2F8", "#1F618D",
         "Further dilution,\ntransformation, low inputs"),
    ]
    for i, (title, fc, ec, body) in enumerate(zones):
        a = fig.add_subplot(gs[0, i])
        a.set_xlim(0, 1); a.set_ylim(0, 1); a.axis("off")
        a.add_patch(FancyBboxPatch((0.02, 0.02), 0.96, 0.96,
                    boxstyle="round,pad=0.01,rounding_size=0.03",
                    facecolor=fc, edgecolor=ec, linewidth=0.9))
        a.text(0.5, 0.86, title, ha="center", fontsize=7.6, fontweight="bold", color=ec)
        a.text(0.5, 0.58, body, ha="center", va="center", fontsize=6.2, color="#2C3E50",
               linespacing=1.5)
        a.annotate("", xy=(0.5, 0.36), xytext=(0.5, 0.26),
                   arrowprops=dict(arrowstyle="-|>", color=ec, lw=1.4))
        txt = ["Highest particle input\nHighest sedimentation\nGreatest benthic exposure",
               "Variable aggregation\nEpisodic bloom stabilisation\nIntermediate exposure",
               "Lowest measured\nparticle numbers\nLowest exposure"][i]
        a.text(0.5, 0.17, txt, ha="center", va="center", fontsize=5.8,
               color="#566573", linespacing=1.5)
        # taxa
        taxa = ["Bivalves, deposit feeders,\nlarvae, zooplankton",
                "Plankton, juvenile fish,\nshellfish beds",
                "Pelagic fish,\nmigratory species"][i]
        a.text(0.5, 0.055, taxa, ha="center", va="center", fontsize=5.6,
               style="italic", color="#6E6E6E")

    for i in range(3):
        x0 = 0.02 + (i + 1) * 0.2425
        fig.add_artist(FancyArrowPatch((x0 + 0.012, 0.5), (x0 + 0.043, 0.5),
                       arrowstyle="-|>", mutation_scale=8, lw=1.1, color="#6E6E6E",
                       transform=fig.transFigure))

    # Panel b: reported seawater particle concentrations
    ax = fig.add_subplot(gs[0, 3])
    labels = ["Ti-based", "Zn-based", "Cu-based", "Ag-based"]
    vals = [1.78e8, 1.27e8, 6.0e7, 3.5e7]
    cols = [C["ti"], C["zn"], C["cu"], C["ag"]]
    y = np.arange(len(labels))[::-1]
    ax.barh(y, vals, color=cols, height=0.62, edgecolor="white", linewidth=0.6)
    ax.set_yticks(y); ax.set_yticklabels(labels)
    ax.set_xscale("log")
    ax.set_xlim(1e7, 1e9)
    ax.set_xlabel("Particle number concentration (particles L$^{-1}$)")
    ax.set_title("Reported coastal seawater concentrations", pad=5)
    for yy, v in zip(y, vals):
        ax.text(v * 1.12, yy, f"{v/1e7:.1f}×10$^7$", va="center", fontsize=6.1)
    ax.grid(axis="x", color="#E5E5E5", lw=0.5, zorder=0)
    ax.set_axisbelow(True)
    despine(ax)
    ax.text(0.0, -0.30, "Data: Laizhou Bay, China (Li et al., 2023);\nmean of 24 stations",
            transform=ax.transAxes, fontsize=5.6, color="#7F8C8D", va="top")

    fig.savefig(os.path.join(OUT, "fig4_gradient.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    figure1()
    figure4()
    print("ok")
