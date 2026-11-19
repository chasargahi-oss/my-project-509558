"""Figure 1 — Conceptual source-to-consumer exposure and effect pathway."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_common import *          # noqa
from textfit import Grid
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
FW, FH = DOUBLE * 1.0, 4.25


def make():
    fig, ax = plt.subplots(figsize=(FW, FH))
    ax.set_position([0, 0, 1, 1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    g = Grid(ax, FW, FH)
    FS = 6.6

    def box(x, y, text, fs=FS, fc="white", ec="#1A1A1A", bold=False,
            lw=0.7, pad=0.05):
        w, h = g.fit(text, fs, weight="bold" if bold else "normal", pad_in=pad)
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                     boxstyle="round,pad=0,rounding_size=0.008",
                     facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3))
        ax.text(x, y, text, ha="center", va="center", fontsize=fs, zorder=4,
                fontweight="bold" if bold else "normal", linespacing=1.45)
        return (x - w / 2, y - h / 2, w, h)

    def arr(p1, p2, lw=0.85, color="#1A1A1A", rad=0.0, ms=6.2, z=2):
        ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=ms,
                     linewidth=lw, color=color, zorder=z,
                     connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0))

    def line(p1, p2, lw=0.65, color="#5D6D7E", z=1):
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, lw=lw, zorder=z,
                solid_capstyle="round")

    # ---------------- column headers --------------------------------------
    heads = [(0.092, "SOURCES"), (0.300, "MARINE SYSTEM"),
             (0.510, "UPTAKE ROUTES"), (0.712, "SEAFOOD"),
             (0.897, "CONSUMER")]
    for x, t in heads:
        ax.text(x, 0.965, t, ha="center", fontsize=5.9, color="#7B7B7B",
                fontweight="bold")
        ax.plot([x - 0.050, x + 0.050], [0.948, 0.948], color="#D5D5D5", lw=0.6)

    # ---------------- 1. sources ------------------------------------------
    prod = box(0.100, 0.845, "Nanomaterial\nproduction and\nnano-enabled goods",
               fc="#E8F1F8", fs=6.3)
    src = ["Wastewater\neffluent", "Stormwater\nand runoff",
           "Antifouling coatings\nand consumer goods",
           "Aquaculture feeds\nand therapeutics"]
    ys = [0.690, 0.565, 0.440, 0.315]
    src_boxes = [box(0.100, y, t, fs=6.1) for t, y in zip(src, ys)]

    # ---------------- 2. marine system ------------------------------------
    sea = box(0.300, 0.780, "Coastal seawater\nand sediments", fc="#E4F2EE",
              bold=True, fs=7.4, pad=0.07)
    proc1 = box(0.300, 0.575, "Hetero-aggregation,\ndissolution,\nsedimentation",
                fs=6.1)
    proc2 = box(0.300, 0.355, "Corona formation,\ntransformation,\nresuspension",
                fs=6.1)

    # collector placed midway between the source stack and the sea box
    src_right = max(b[0] + b[2] for b in src_boxes + [prod])
    bus_x = src_right + (sea[0] - src_right) * 0.55
    line((bus_x, 0.315), (bus_x, 0.845))
    for b in src_boxes + [prod]:
        y = b[1] + b[3] / 2
        line((b[0] + b[2] + 0.002, y), (bus_x, y))
    arr((bus_x, 0.780), (sea[0] - 0.003, 0.780), lw=0.8, color="#5D6D7E")

    arr((0.300, 0.780 - sea[3] / 2 - 0.003), (0.300, 0.575 + proc1[3] / 2 + 0.003), lw=0.95)
    arr((0.300, 0.575 - proc1[3] / 2 - 0.003), (0.300, 0.355 + proc2[3] / 2 + 0.003), lw=0.95)

    # ---------------- 3. uptake routes -------------------------------------
    band_l, band_r = 0.396, 0.628
    ax.add_patch(Rectangle((band_l, 0.170), band_r - band_l, 0.690,
                           facecolor="#FDF4E8", edgecolor="none", zorder=0))
    ax.text((band_l + band_r) / 2, 0.845, "Route of uptake", ha="center",
            fontsize=5.9, style="italic", color="#9C6B21")
    routes = ["Waterborne\nuptake", "Filter feeding\n(bivalves)",
              "Dietary uptake and\ntrophic transfer",
              "Sediment contact\n(deposit feeders)", "Gill and gut\nuptake (fish)"]
    rys = [0.765, 0.640, 0.510, 0.375, 0.240]
    rboxes = []
    fan_o = (sea[0] + sea[2] + 0.004, 0.780)
    for t, y in zip(routes, rys):
        b = box(0.512, y, t, fs=6.1)
        rboxes.append(b)
        arr(fan_o, (b[0] - 0.004, y), lw=0.55, color="#B9770E", ms=4.4, rad=0.10)

    # ---------------- 4. seafood -------------------------------------------
    et = box(0.712, 0.700, "Edible tissues\nmuscle · digestive gland\ngill · mantle",
             fc="#FCEDEA", fs=6.3)
    pc = box(0.712, 0.430, "Processed and\ncanned seafood\nproducts", fc="#FCEDEA", fs=6.3)
    arr((0.712, 0.700 - et[3] / 2 - 0.003), (0.712, 0.430 + pc[3] / 2 + 0.003), lw=0.9)
    arr((0.628, 0.700), (et[0] - 0.009, 0.700), lw=0.95, ms=7)

    # ---------------- 5. consumer ------------------------------------------
    m = box(0.897, 0.775, "Seafood monitoring\nand dietary-exposure\nassessment",
            fc="#ECEAF6", fs=6.2)
    h = box(0.897, 0.550, "Human consumers\nadults · children\nhigh consumers",
            fc="#ECEAF6", fs=6.2)
    r = box(0.897, 0.265, "Chronic low-dose risk\nNOT YET\nCHARACTERISED",
            fc="#F6C6BF", ec="#922B21", fs=6.4, bold=True, lw=0.9)

    arr((et[0] + et[2] + 0.003, 0.725), (m[0] - 0.004, 0.795), lw=0.85, rad=-0.18)
    arr((pc[0] + pc[2] + 0.003, 0.440), (m[0] - 0.004, 0.768), lw=0.85, rad=0.18)
    arr((0.897, 0.775 - m[3] / 2 - 0.003), (0.897, 0.550 + h[3] / 2 + 0.003), lw=0.95)
    arr((0.897, 0.550 - h[3] / 2 - 0.003), (0.897, 0.265 + r[3] / 2 + 0.003),
        lw=1.0, color="#922B21")

    # ---------------- knowledge-gap strip ----------------------------------
    gap = ("KEY UNCERTAINTIES   ·   engineered versus natural particle identity   ·   laboratory-to-field concentration gap   ·   "
           "bioaccessibility after\ngastrointestinal digestion   ·   chronic oral toxicity   ·   absence of health-based guidance values")
    w, hh = g.fit(gap, 5.6, pad_in=0.06)
    ax.add_patch(FancyBboxPatch((0.5 - w / 2, 0.045), w, hh,
                 boxstyle="round,pad=0,rounding_size=0.008",
                 facecolor="#F2F4F5", edgecolor="#8FA0A8", linewidth=0.6,
                 linestyle=(0, (3, 2)), zorder=3))
    ax.text(0.5, 0.045 + hh / 2, gap, ha="center", va="center", fontsize=5.6,
            color="#3E5560", linespacing=1.6, zorder=4)

    fig.savefig(os.path.join(OUT, "fig1_pathway.png"))
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    make()
    print("fig1 ok")
