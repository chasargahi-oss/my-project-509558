"""Front matter: title page, abstract, highlights, keywords."""
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx_style import para, rich, h1, h2, set_run

TITLE = ("Engineered nanoparticles pose an emerging but incompletely characterized "
         "risk to seafood safety: a systematic review")

SHORT_TITLE = "Engineered nanoparticles and seafood safety"


def title_page(doc):
    para(doc, "", size=12, line=1.0, space_after=10)
    para(doc, "REVIEW ARTICLE", size=10, bold=True, align="center", line=1.0,
         space_after=12, color="6E6E6E")
    para(doc, TITLE, size=17, bold=True, align="center", line=1.32,
         space_after=14)
    para(doc, "Running title: " + SHORT_TITLE, size=10.5, italic=True,
         align="center", line=1.0, space_after=24, color="4D4D4D")

    rich(doc, [("Alireza Hemmati", {"bold": True, "size": 12.5}),
               ("1,", {"size": 12.5}),
               ("*", {"bold": True, "size": 12.5}),
               (" and Shiva Yousefi", {"bold": True, "size": 12.5}),
               ("2", {"size": 12.5})],
         align="center", line=1.0, space_after=16)

    aff = [("1", "Department of Health, Safety and Environment (HSE), The Workers' House "
                 "University of Applied Science and Technology, Lamerd, Fars Province, Iran"),
           ("2", "Department of Natural Resources and Environment, Shiraz University, "
                 "Shiraz, Iran")]
    for n, t in aff:
        rich(doc, [(n, {"sup": True, "size": 9.5}),
                   ("  " + t, {"size": 9.5})],
             align="left", line=1.25, space_after=4)

    para(doc, "", size=6, line=1.0, space_after=10)

    para(doc, "Corresponding author", size=10, bold=True, align="left", line=1.0,
         space_after=5)
    lines = [
        ("Dr Alireza Hemmati", True),
        ("Department of Health, Safety and Environment (HSE), The Workers' House "
         "University of Applied Science and Technology, Lamerd, Fars Province, Iran", False),
        ("Telephone: +98 917 982 0340", False),
        ("E-mail: hemati@uasl.ir  |  alirezahemmati02@gmail.com", False),
        ("ORCID: 0000-0002-0064-6739", False),
    ]
    for t, b in lines:
        para(doc, t, size=9.5, bold=b, align="left", line=1.2, space_after=2)

    para(doc, "", size=6, line=1.0, space_after=5)
    para(doc, "Co-author ORCID: Shiva Yousefi \u2014 0009-0001-9338-7026",
         size=9.5, align="left", line=1.2, space_after=2)

    para(doc, "", size=6, line=1.0, space_after=12)
    para(doc, "Manuscript type: Systematic review", size=9.5, align="left",
         line=1.2, space_after=2)
    para(doc, "Word count (abstract): 383", size=9.5, align="left", line=1.2, space_after=2)
    para(doc, "Word count (main text, Introduction to Conclusion, excluding abstract, "
              "references, tables and figure captions): 10,464",
         size=9.5, align="left", line=1.2, space_after=2)
    para(doc, "Tables: 14   |   Figures: 8   |   References: 32", size=9.5,
         align="left", line=1.2, space_after=2)
    para(doc, "Declarations: no funding; no competing interests; no ethics approval required",
         size=9.5, align="left", line=1.2, space_after=2)

    doc.add_page_break()


BLOCKS = [
 ("Background.",
  "Engineered nanoparticles (ENPs) \u2014 metal, metal-oxide, carbon-based and polymeric "
  "materials with at least one dimension between 1 and 100 nm \u2014 enter coastal waters "
  "through wastewater, runoff, coatings and consumer products. Their accumulation in seafood "
  "and effects on consumers remain unresolved, and the evidence is fragmented across "
  "environmental chemistry, marine ecotoxicology, analytical chemistry and food-safety risk "
  "assessment."),
 ("Objective.",
  "To synthesize evidence on ENP sources and fate, bioaccumulation in seafood species, "
  "detection in commercial products, ecotoxicological effects, dietary exposure and "
  "regulatory readiness, and to establish what the evidence does and does not show about "
  "risk to seafood safety and consumers."),
 ("Methods.",
  "Seven concept blocks were combined in Consensus, a discovery platform indexing Semantic "
  "Scholar, PubMed and further scholarly sources, with backward and forward citation "
  "tracing. From 509,800 records, 347 were eligible after title and abstract screening and "
  "50 were included after full-text assessment. Reporting follows PRISMA 2020. "
  "Heterogeneity precluded meta-analysis; evidence strength was appraised against "
  "replication, endpoint consistency, environmental realism and relevance to edible tissue."),
 ("Results.",
  "Single-particle inductively coupled plasma mass spectrometry identified TiO\u2082 "
  "nanoparticles below 100 nm in every canned seafood sample tested, highest in clam "
  "(0.112 mg kg\u207b\u00b9); Ag nanoparticles of 31\u201336 nm in anchovy, clam, mackerel and "
  "tuna; and ZnO nanoparticles at 0.003\u20130.010 mg kg\u207b\u00b9. Estimated intake from one "
  "meal was 0.010\u20130.031 \u00b5g kg\u207b\u00b9 body weight for adults and "
  "0.022\u20130.067 \u00b5g kg\u207b\u00b9 for children, three to four orders of magnitude "
  "below dissolved-metal intake from the same meal. Laboratory studies consistently report "
  "oxidative stress, lysosomal destabilization, genotoxicity and immune modulation, with "
  "bivalves providing the most consistent mechanistic evidence. Trophic transfer is "
  "demonstrated in controlled food chains \u2014 TiO\u2082 from Nitzschia closterium to "
  "Chlamys farreri, and CeO\u2082 from clamworm to turbot \u2014 but biomagnification is not "
  "universal."),
 ("Conclusions.",
  "ENPs are an analytically confirmed emerging contaminant of concern for seafood safety, "
  "but current evidence does not establish a demonstrated population-level or "
  "consumer-health risk. The decisive uncertainties are source attribution, the "
  "10\u2013100-fold gap between laboratory effect concentrations and measured environmental "
  "levels, the near-absence of chronic oral-toxicity and bioaccessibility data, and the lack "
  "of health-based guidance values for any seafood-relevant ENP. Priorities are "
  "environmentally realistic field and mesocosm studies, validated provenance methods, "
  "certified reference materials and harmonized reference values. Until these exist, "
  "proportionate source control and standardized monitoring are better justified than "
  "premature claims of either safety or demonstrated harm."),
]

HIGHLIGHTS = [
 "Metal and metal-oxide nanoparticles are detectable in commercially available canned seafood by spICP-MS.",
 "Measured dietary intake from seafood is low, but no health-based guidance value exists for any seafood-relevant ENP.",
 "Laboratory toxicity is well replicated; field and mesocosm evidence linking exposure to population effects is absent.",
 "Source attribution \u2014 engineered versus natural versus incidental particles \u2014 remains the central analytical barrier.",
 "A four-step decision framework is proposed to convert a positive detection into a defensible risk statement.",
]


def abstract_page(doc):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(0)
    h.paragraph_format.space_after = Pt(8)
    h.paragraph_format.line_spacing = 1.1
    set_run(h.add_run("Abstract"), size=14, bold=True)

    for label, text in BLOCKS:
        rich(doc, [(label + "  ", {"bold": True, "size": 9.5, "color": "1A1A1A"}),
                   (text, {"size": 9.5})],
             align="justify", line=1.05, space_after=5)

    para(doc, "", size=4, line=1.0, space_after=2)

    rich(doc, [("Keywords:  ", {"bold": True, "size": 9}),
               ("engineered nanoparticles; seafood safety; marine ecotoxicology; "
                "bioaccumulation; dietary exposure; single-particle ICP-MS; aquaculture; "
                "risk assessment; PRISMA 2020", {"size": 9})],
         align="left", line=1.05, space_after=7)

    para(doc, "Highlights", size=10, bold=True, align="left", line=1.0, space_after=3)
    for t in HIGHLIGHTS:
        rich(doc, [("\u25aa  ", {"size": 8.2, "color": "2C6E49"}),
                   (t, {"size": 8.2})],
             align="left", line=1.0, space_after=1.5, left_indent=0.4)

    doc.add_page_break()
