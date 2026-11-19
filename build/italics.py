"""Utilities for applying scientific italics to plain text."""
import re

# Latin binomials and other italicised terms used in this manuscript.
LATIN = [
 "Mytilus", "Mytilus galloprovincialis", "Mytilus edulis",
 "Ruditapes", "Ruditapes philippinarum", "Ruditapes decussatus",
 "Scrobicularia plana", "Hediste diversicolor",
 "Chlamys farreri", "Nitzschia closterium", "Thalassiosira pseudonana",
 "Perinereis aibuhitensis", "Scophthalmus maximus",
 "M. galloprovincialis", "S. plana", "H. diversicolor",
 "Ostrea", "Crassostrea gigas", "Anadara", "Tegillarca",
 "Nitzschia", "Thalassiosira", "Chlamys", "Scophthalmus", "Perinereis",
 "Ruditapes", "Scrobicularia", "Mytilus", "Hediste", "Mercenaria",
 "Macoma", "Cerastoderma", "Pecten", "Argopecten",
]
LATIN.sort(key=len, reverse=True)

# Build one alternation; word-boundary aware.
_LATIN_RE = re.compile(r"(?<![A-Za-z])(" + "|".join(re.escape(t) for t in LATIN) +
                       r")(?![A-Za-z])")


def italianize(text):
    """Return a list of (chunk, italic_bool) spans for Latin names."""
    out = []
    pos = 0
    for m in _LATIN_RE.finditer(text):
        if m.start() > pos:
            out.append((text[pos:m.start()], False))
        out.append((m.group(0), True))
        pos = m.end()
    if pos < len(text):
        out.append((text[pos:], False))
    return out or [(text, False)]


def ref_segments(ref):
    """Split an APA reference into spans, italicising the journal title + volume.

    Recognised shape: ... Title. Journal Name, 12(3), 45–67. https://doi.org/...
    Returns list of (text, italic).
    """
    m = re.search(r"\.\s([A-Z][^.]*?),\s(\d+)(\(\d+[^)]*\))?,\s", ref)
    if not m:
        # book / report: no journal
        return [(ref, False)]
    lead = ref[: m.start() + 2]           # include ". "
    journal = m.group(1)
    vol = m.group(2)
    issue = m.group(3) or ""
    rest = ref[m.end():]
    return [(lead, False),
            (journal, True), (", ", False),
            (vol, True), (issue + ", ", False),
            (rest, False)]
