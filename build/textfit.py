"""Text-measurement helpers so that every box exactly fits its label.

Strings are measured with a real renderer (get_window_extent) and cached,
so the returned sizes are exact for the configured DPI and font.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_CACHE = {}
_FIG = None
_REND = None
_DPI = 300


def _renderer():
    global _FIG, _REND
    if _REND is None:
        _FIG = plt.figure(figsize=(10, 2), dpi=_DPI)
        _FIG.canvas.draw()
        _REND = _FIG.canvas.get_renderer()
    return _REND


def text_size_in(text, fontsize, weight="normal", style="normal", dpi=None):
    """Exact (width_in, height_in) of a possibly multi-line string."""
    key = (text, fontsize, weight, style)
    if key in _CACHE:
        return _CACHE[key]
    rend = _renderer()
    t = _FIG.text(0.5, 0.5, text, fontsize=fontsize, fontweight=weight,
                  fontstyle=style, family="DejaVu Sans", linespacing=1.45)
    bb = t.get_window_extent(renderer=rend)
    t.remove()
    dpi = dpi or _DPI
    out = (bb.width / dpi, bb.height / dpi)
    _CACHE[key] = out
    return out


class Grid:
    """Data-coordinate canvas with a known figure size, so inches <-> data."""

    def __init__(self, axis, fig_w_in, fig_h_in, xlim=(0, 1), ylim=(0, 1)):
        self.ax = axis
        self.fw = fig_w_in
        self.fh = fig_h_in
        self.xlim = xlim
        self.ylim = ylim

    def px(self, inches):
        return inches / self.fw * (self.xlim[1] - self.xlim[0])

    def py(self, inches):
        return inches / self.fh * (self.ylim[1] - self.ylim[0])

    def fit(self, text, fontsize, weight="normal", pad_in=0.05, min_h_in=0.0):
        """Return (w, h) in data units that fully contain `text` plus padding."""
        w_in, h_in = text_size_in(text, fontsize, weight=weight)
        w_in += 2 * pad_in
        h_in = max(h_in + 2 * pad_in * 0.8, min_h_in)
        return self.px(w_in), self.py(h_in)


def wrap(text, fontsize, max_w_in, weight="normal"):
    """Greedy word-wrap to a maximum width in inches; honours existing newlines."""
    out_lines = []
    for para in text.split("\n"):
        words = para.split(" ")
        cur = ""
        for wd in words:
            trial = wd if not cur else cur + " " + wd
            if text_size_in(trial, fontsize, weight=weight)[0] <= max_w_in:
                cur = trial
            else:
                if cur:
                    out_lines.append(cur)
                cur = wd
        out_lines.append(cur)
    return "\n".join(out_lines)
