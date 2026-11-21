"""Generate numbered, publication-style figures for the revised manuscript.

All values are taken from the summary statistics reported in Tables 1, 4, 5 and 8
of the revised manuscript; no data are generated or imputed.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    "font.family": "DejaVu Serif",
    "font.size": 9,
    "axes.linewidth": 0.8,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

OUT = Path(__file__).resolve().parent.parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)

NATIVE = "#2c7a5a"      # green  -> native
INTRO = "#b4562a"       # orange -> introduced

species = ["P. dactylifera", "Z. spina-christi", "E. camaldulensis",
           "P. cineraria", "C. viminalis", "C. erectus"]
prov = ["N", "N", "I", "N", "I", "I"]
soc_m = [2.46, 1.34, 1.21, 0.99, 0.98, 0.59]
soc_sd = [0.84, 0.42, 0.73, 0.51, 0.33, 0.41]
letters = ["a", "ab", "abc", "bc", "bc", "c"]
colors = [NATIVE if p == "N" else INTRO for p in prov]

labels = ["P. dactylifera", "Z. spina-christi", "E. camaldulensis",
          "P. cineraria", "C. viminalis", "C. erectus"]


def style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(direction="out", length=3, width=0.8)


# ---------------------------------------------------------------- Figure 1
fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0),
                         gridspec_kw={"width_ratios": [2.3, 1]})
ax = axes[0]
x = np.arange(len(species))
ax.bar(x, soc_m, yerr=soc_sd, color=colors, edgecolor="black", linewidth=0.6,
       capsize=3, error_kw={"linewidth": 0.8}, width=0.68, zorder=2)
ax.set_xticks(x)
ax.set_xticklabels(species, rotation=32, ha="right", fontstyle="italic")
for xi, m, sd, lt in zip(x, soc_m, soc_sd, letters):
    ax.text(xi, m + sd + 0.12, lt, ha="center", va="bottom", fontsize=8)
ax.set_ylabel("SOC concentration (%)")
ax.set_ylim(0, 3.9)
ax.set_title("(a) Species identity", loc="left", fontsize=9)
style(ax)

ax = axes[1]
pm = [1.60, 0.93]
ps = [0.87, 0.55]
ax.bar([0, 1], pm, yerr=ps, color=[NATIVE, INTRO], edgecolor="black",
       linewidth=0.6, capsize=3, error_kw={"linewidth": 0.8}, width=0.6, zorder=2)
ax.set_xticks([0, 1])
ax.set_xticklabels(["Native\n(n = 18)", "Introduced\n(n = 18)"])
ax.set_ylabel("SOC concentration (%)")
ax.set_ylim(0, 3.0)
ax.set_title("(b) Provenance", loc="left", fontsize=9)
ax.annotate("", xy=(0, 2.62), xytext=(1, 2.62),
            arrowprops=dict(arrowstyle="-", lw=0.8, color="black"))
ax.text(0.5, 2.68, r"$\Delta$ = 0.67 (95% CI 0.21–1.14)" + "\n" + r"$g$ = 0.90, $p$ = 0.010",
        ha="center", va="bottom", fontsize=7)
style(ax)
fig.savefig(OUT / "Figure1.png")
plt.close(fig)

# ---------------------------------------------------------------- Figure 2
fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0),
                         gridspec_kw={"width_ratios": [1, 2.1]})
ax = axes[0]
dep = [1.51, 1.02]
ax.bar([0, 1], dep, color=["#4c4c4c", "#9a9a9a"], edgecolor="black",
       linewidth=0.6, width=0.6, zorder=2)
ax.set_xticks([0, 1])
ax.set_xticklabels(["0–10 cm", "10–30 cm"])
ax.set_ylabel("SOC concentration (%)")
ax.set_ylim(0, 1.9)
for xi, v in zip([0, 1], dep):
    ax.text(xi, v + 0.04, f"{v:.2f}", ha="center", va="bottom", fontsize=8)
ax.text(0.5, 1.72, r"$t_{17}$ = 3.70, $p$ = 0.002", ha="center", fontsize=7.5)
ax.set_title("(a) All trees (n = 18)", loc="left", fontsize=9)
style(ax)

ax = axes[1]
stocks_shallow = [39.6, 21.2, 19.4, 17.4, 16.8, 12.4]
stocks_deep = [58.7, 32.8, 29.1, 20.6, 21.4, 8.2]
x = np.arange(len(species))
ax.bar(x - 0.19, stocks_shallow, width=0.38, color="#d9d9d9", edgecolor="black",
       linewidth=0.6, label="0–10 cm", zorder=2)
ax.bar(x + 0.19, stocks_deep, width=0.38, color="#6b6b6b", edgecolor="black",
       linewidth=0.6, label="10–30 cm", zorder=2)
ax.set_xticks(x)
ax.set_xticklabels(species, rotation=32, ha="right", fontstyle="italic")
ax.set_ylabel(r"SOC stock (Mg C ha$^{-1}$)")
ax.legend(frameon=False, loc="upper right")
ax.set_title("(b) By species and increment (BD = 1.4 g cm$^{-3}$)", loc="left", fontsize=9)
style(ax)
fig.savefig(OUT / "Figure2.png")
plt.close(fig)

# ---------------------------------------------------------------- Figure 3
sand = [62.40, 43.30, 63.32, 49.97, 57.07, 55.91]
silt = [26.20, 43.03, 26.44, 35.87, 28.60, 30.68]
clay = [11.40, 13.67, 10.24, 14.17, 14.33, 13.41]
sand_sd = [3.64, 5.49, 14.85, 3.97, 4.52, 3.58]
x = np.arange(len(species))
fig, ax = plt.subplots(figsize=(7.0, 3.1))
ax.bar(x, sand, width=0.66, color="#e8d9b5", edgecolor="black", linewidth=0.6,
       label="Sand", yerr=sand_sd, capsize=3, error_kw={"linewidth": 0.7}, zorder=2)
ax.bar(x, silt, bottom=sand, width=0.66, color="#9db8c9", edgecolor="black",
       linewidth=0.6, label="Silt", zorder=2)
ax.bar(x, clay, bottom=np.array(sand) + np.array(silt), width=0.66,
       color="#7d5a50", edgecolor="black", linewidth=0.6, label="Clay", zorder=2)
ax.set_xticks(x)
ax.set_xticklabels(species, rotation=30, ha="right", fontstyle="italic")
ax.set_ylabel("Particle-size fraction (%)")
ax.set_ylim(0, 108)
ax.axhline(100, color="black", lw=0.6, ls=":")
ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.13))
style(ax)
fig.savefig(OUT / "Figure3.png")
plt.close(fig)

# ---------------------------------------------------------------- Figure 4
tot = [98.4, 54.0, 48.5, 38.2, 38.0, 20.6]
tot_sd = [32.5, 14.7, 8.0, 10.2, 16.5, 5.0]
order = [0, 1, 3, 2, 4, 5]  # keep species order used elsewhere
sp_o = ["P. dactylifera", "Z. spina-christi", "E. camaldulensis",
        "P. cineraria", "C. viminalis", "C. erectus"]
tot = [98.4, 54.0, 48.5, 38.0, 38.2, 20.6]
tot_sd = [32.5, 14.7, 8.0, 16.5, 10.2, 5.0]
col_o = [NATIVE, NATIVE, INTRO, NATIVE, INTRO, INTRO]
lo = [v * 1.2 / 1.4 for v in tot]
hi = [v * 1.6 / 1.4 for v in tot]
fig, ax = plt.subplots(figsize=(7.0, 3.2))
x = np.arange(6)
ax.bar(x, tot, yerr=tot_sd, width=0.62, color=col_o, edgecolor="black",
       linewidth=0.6, capsize=3, error_kw={"linewidth": 0.8}, zorder=2,
       label="BD = 1.4 g cm$^{-3}$ (mean ± SD)")
for xi, l, h in zip(x, lo, hi):
    ax.plot([xi, xi], [l, h], color="black", lw=1.4, solid_capstyle="butt", zorder=3)
    ax.plot([xi - 0.11, xi + 0.11], [l, l], color="black", lw=1.0, zorder=3)
    ax.plot([xi - 0.11, xi + 0.11], [h, h], color="black", lw=1.0, zorder=3)
ax.plot([], [], color="black", lw=1.4, label="Range for BD 1.2–1.6 g cm$^{-3}$")
ax.set_xticks(x)
ax.set_xticklabels(sp_o, rotation=30, ha="right", fontstyle="italic")
ax.set_ylabel(r"SOC stock, 0–30 cm (Mg C ha$^{-1}$)")
ax.set_ylim(0, 135)
ax.legend(frameon=False, loc="upper right", fontsize=7.5)
style(ax)
fig.savefig(OUT / "Figure4.png")
plt.close(fig)

# ---------------------------------------------------------------- Figure 5
load = {"Organic carbon": (0.38, 0.84), "Sand": (0.98, -0.27),
        "Silt": (-0.85, 0.52), "Clay": (-0.72, -0.54)}
fig, ax = plt.subplots(figsize=(4.6, 4.2))
ax.axhline(0, color="0.6", lw=0.7)
ax.axvline(0, color="0.6", lw=0.7)
for k, (u, v) in load.items():
    ax.annotate("", xy=(u, v), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", lw=1.1, color="#1f4e79",
                                shrinkA=0, shrinkB=0))
    ax.text(u * 1.10, v * 1.10, k, fontsize=8, ha="center", va="center")
circ = plt.Circle((0, 0), 1.0, fill=False, lw=0.6, ls=":", color="0.5")
ax.add_patch(circ)
ax.set_xlim(-1.15, 1.25)
ax.set_ylim(-1.0, 1.05)
ax.set_xlabel("PC1 (56.8% of variance) — texture axis")
ax.set_ylabel("PC2 (32.6%) — carbon axis")
ax.set_aspect("equal")
style(ax)
fig.savefig(OUT / "Figure5.png")
plt.close(fig)

print("figures written to", OUT)
