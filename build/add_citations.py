"""Insert APA-style in-text citations at factually appropriate points.

Each edit is a (file, old, new) triple applied once. The old strings are
unique substrings of the paragraph text as written in the content modules.
"""
import sys, os

EDITS = []


def E(f, old, new):
    EDITS.append((f, old, new))


INTRO = "content_intro.py"
RES = "content_results.py"
DIS = "content_disc.py"

# ------------------------------------------------------------------ INTRO 1
E(INTRO,
  '"decades.", first_indent=1.0)',
  '"decades (Keller & Lazareva, 2014; Nowack & Bucheli, 2007).", first_indent=1.0)')

E(INTRO,
  '"the material and the population density of the catchment.", first_indent=0.0)',
  '"the material and the population density of the catchment (Keller & Lazareva, 2014).", first_indent=0.0)')

E(INTRO,
  '"the water column by extracellular polymeric substances released during algal "',
  '"the water column by extracellular polymeric substances released during algal "')

E(INTRO,
  '"acts through an entirely different toxicological mechanism.", first_indent=0.0)',
  '"acts through an entirely different toxicological mechanism (Abbas et al., 2020; '
  'Lead et al., 2018).", first_indent=0.0)')

E(INTRO,
  '"necessity rather than a dietary choice.", first_indent=0.0)',
  '"necessity rather than a dietary choice (FAO, 2024).", first_indent=0.0)')

E(INTRO,
  '"in many markets.", first_indent=0.0)',
  '"in many markets (Canesi et al., 2012; Rocha et al., 2015).", first_indent=0.0)')

E(INTRO,
  '"for food-safety management.", first_indent=0.0)',
  '"for food-safety management (Khosravi-Katuli et al., 2017).", first_indent=0.0)')

E(INTRO,
  '"dietary exposure. Detection, however, is not identification of origin, and origin "',
  '"dietary exposure (Grasso et al., 2020). Detection, however, is not identification of origin, and origin "')

E(INTRO,
  '"means.", first_indent=0.0)',
  '"means (EFSA Scientific Committee, 2021; EFSA Panel on Food Additives and '
  'Flavourings, 2021).", first_indent=0.0)')

E(INTRO,
  '"meaning.", first_indent=0.0)',
  '"meaning (Nugawela et al., 2025).", first_indent=0.0)')

E(INTRO,
  '"boundary between what is known and what is assumed is rarely stated explicitly.",',
  '"boundary between what is known and what is assumed is rarely stated explicitly '
  '(Meng & Nag, 2026; Zhang et al., 2025).",')

E(INTRO,
  '"not appropriate.", first_indent=0.0)',
  '"not appropriate (Roma et al., 2020).", first_indent=0.0)')

E(INTRO,
  '"biosafety assessment and design of nanomaterials entering the marine environment "',
  '"biosafety assessment and design of nanomaterials entering the marine environment "')

E(INTRO,
  '"ecotoxicology, food occurrence, dietary intake and regulatory "',
  '"ecotoxicology, food occurrence, dietary intake and regulatory "')

E(INTRO,
  '"statement.", first_indent=1.0)',
  '"statement (Page et al., 2021).", first_indent=1.0)')

# ------------------------------------------------------------------ METHODS
E(INTRO,
  '"additional scholarly sources. Seven complementary concept blocks were combined to "',
  '"additional scholarly sources. Seven complementary concept blocks were combined to "')

E(INTRO,
  '"nanoparticle type and seafood matrix.", first_indent=0.0)',
  '"nanoparticle type and seafood matrix (Laycock et al., 2022).", first_indent=0.0)')

# ------------------------------------------------------------------ RESULTS 3.2
E(RES,
  '"most consistently identified across the reviewed literature. Their relative "',
  '"most consistently identified across the reviewed literature (Batley et al., 2013; '
  'Nowack & Bucheli, 2007). Their relative "')

E(RES,
  '"origin. The same properties "',
  '"origin. The same properties "')

E(RES,
  '"original release.", first_indent=0.0)',
  '"original release (Hochella et al., 2019).", first_indent=0.0)')

E(RES,
  '"freshwater because of chloride complexation and pH effects. Once dissolution is "',
  '"freshwater because of chloride complexation and pH effects (Miao et al., 2010). Once dissolution is "')

E(RES,
  '"and for filter feeders that graze on suspended material. "',
  '"and for filter feeders that graze on suspended material (Abbas et al., 2020). "')

E(RES,
  '"overlying water. Reported seawater abundances reached 1.78 \\u00d7 10\\u2078 particles "',
  '"overlying water (Li et al., 2023). Reported seawater abundances reached 1.78 \\u00d7 10\\u2078 particles "')

E(RES,
  '"offshore.", first_indent=0.0)',
  '"offshore (Li et al., 2023).", first_indent=0.0)')

E(RES,
  '"attempts to move from concentration to risk in a marine setting. Using predicted "',
  '"attempts to move from concentration to risk in a marine setting (Li et al., 2023). Using predicted "')

E(RES,
  '"particles are accounted for.", first_indent=0.0)',
  '"particles are accounted for (Li et al., 2023).", first_indent=0.0)')

E(RES,
  '"exists.", first_indent=0.0)',
  '"exists (Keller & Lazareva, 2014).", first_indent=0.0)')

# ------------------------------------------------------------------ RESULTS 3.3
E(RES,
  '"contributions from gill mucus and, for small or dissolved fractions, direct "',
  '"contributions from gill mucus and, for small or dissolved fractions, direct "')

E(RES,
  '"branchial transfer. Table 5 summarizes the evidence by species group.",',
  '"branchial transfer (Baker et al., 2014; Canesi et al., 2012). Table 5 summarizes '
  'the evidence by species group.",')

E(RES,
  '"in gill and digestive gland, and all four reached adductor muscle. Silver-bearing "',
  '"in gill and digestive gland, and all four reached adductor muscle (Xu et al., 2020). Silver-bearing "')

E(RES,
  '"the total elemental concentration, governs accumulation.", first_indent=0.0)',
  '"the total elemental concentration, governs accumulation (Xu et al., 2020).", first_indent=0.0)')

E(RES,
  '"Nitzschia closterium to the scallop Chlamys farreri. Tissue burdens were higher "',
  '"Nitzschia closterium to the scallop Chlamys farreri (Wang et al., 2017). Tissue burdens were higher "')

E(RES,
  '"histopathological effects accompanied the accumulation.", first_indent=0.0)',
  '"histopathological effects accompanied the accumulation (Wang et al., 2017).", first_indent=0.0)')

E(RES,
  '"CeO\\u2082 nanoparticles transferred from "\n              "clamworm (Perinereis aibuhitensis) to juvenile turbot (Scophthalmus maximus), and "',
  '"CeO\\u2082 nanoparticles transferred from "\n              "clamworm (Perinereis aibuhitensis) to juvenile turbot (Scophthalmus maximus) (Yin et al., 2025), and "')

E(RES,
  '"measured.", first_indent=0.0)',
  '"measured (Yin et al., 2025).", first_indent=0.0)')

E(RES,
  '"tissues.", first_indent=0.0)',
  '"tissues (Corsi et al., 2014; Rocha et al., 2015).", first_indent=0.0)')

# ------------------------------------------------------------------ RESULTS 3.4
E(RES,
  '"in canned tuna to 89 nm in canned anchovy and clam.", first_indent=1.0)',
  '"in canned tuna to 89 nm in canned anchovy and clam (Grasso et al., 2020).", first_indent=1.0)')

E(RES,
  '"explicitly did not claim biomagnification.", first_indent=0.0)',
  '"explicitly did not claim biomagnification (Grasso et al., 2020).", first_indent=0.0)')

E(RES,
  '"total Ag intake from these products.", first_indent=0.0)',
  '"total Ag intake from these products (Grasso et al., 2021).", first_indent=0.0)')

E(RES,
  '"of zinc and the unresolved hazard of the nanoparticulate form. Table 6 summarizes "',
  '"of zinc and the unresolved hazard of the nanoparticulate form (Grasso et al., 2022). Table 6 summarizes "')

E(RES,
  '"between-season variability was not characterized.", first_indent=0.0)',
  '"between-season variability was not characterized (Grasso et al., 2020, 2021, 2022).", first_indent=0.0)')

# ------------------------------------------------------------------ RESULTS 3.5
E(RES,
  '"because nanoparticle Ag represented such a small fraction of total Ag.",',
  '"because nanoparticle Ag represented such a small fraction of total Ag '
  '(Grasso et al., 2020, 2021, 2022).",')

E(RES,
  '"<130 chars", first_indent=0.0)',
  '"<130 chars", first_indent=0.0)')

E(RES,
  '"and the current status of each.",',
  '"and the current status of each.",')

# ------------------------------------------------------------------ RESULTS 3.6
E(RES,
  '"change (Table 8). A synthesis of 134 ecotoxicological studies of metal ENPs in "',
  '"change (Table 8). A synthesis of 134 ecotoxicological studies of metal ENPs in "')

E(RES,
  '"duration, particle characteristics and sampled tissue.",',
  '"duration, particle characteristics and sampled tissue (Roma et al., 2020).",')

E(RES,
  '"approximately 0.39 \\u00b5M in one series. In mussels, prolonged exposure to ZnO "',
  '"approximately 0.39 \\u00b5M in one series (Miao et al., 2010). In mussels, prolonged exposure to ZnO "')

E(RES,
  '"because energy allocation governs growth and reproduction. For CuO, "',
  '"because energy allocation governs growth and reproduction (Hanna et al., 2013). For CuO, "')

E(RES,
  '"the two mechanisms remains analytically difficult.", first_indent=0.0)',
  '"the two mechanisms remains analytically difficult (Buffet et al., 2011).", first_indent=0.0)')

E(RES,
  '"a single harmonized approach.", first_indent=0.0)',
  '"a single harmonized approach (Balbi et al., 2014; Lead et al., 2018).", first_indent=0.0)')

E(RES,
  '"in both directions.", first_indent=0.0)',
  '"in both directions (Batley et al., 2013; Corsi et al., 2014).", first_indent=0.0)')

# ------------------------------------------------------------------ RESULTS 3.7
E(RES,
  '"histopathological damage.", first_indent=0.0)',
  '"histopathological damage (Khosravi-Katuli et al., 2017).", first_indent=0.0)')

# ------------------------------------------------------------------ RESULTS 3.8
E(RES,
  '"materials during sample handling.", first_indent=1.0)',
  '"materials during sample handling (Laycock et al., 2022).", first_indent=1.0)')

E(RES,
  '"tissues remain unstudied.", first_indent=0.0)',
  '"tissues remain unstudied (Laycock et al., 2022).", first_indent=0.0)')

E(RES,
  '"for routine quantification of "\n              "metal-containing ENPs. Table 10 compares the available methods.", first_indent=0.0)',
  '"for routine quantification of "\n              "metal-containing ENPs (Sun et al., 2022). Table 10 compares the available methods.", first_indent=0.0)')

E(RES,
  '"validated for each nanoparticle type and seafood matrix.", first_indent=0.0)',
  '"validated for each nanoparticle type and seafood matrix (Sun et al., 2022).", first_indent=0.0)')

E(RES,
  '"domain, and it is a precondition for any harmonized monitoring programme.",',
  '"domain, and it is a precondition for any harmonized monitoring programme '
  '(Laycock et al., 2022).",')

# ------------------------------------------------------------------ DISCUSSION
E(DIS,
  '"identifies the measurements that would resolve it.",',
  '"identifies the measurements that would resolve it (Nugawela et al., 2025).",')

E(DIS,
  '"market.", first_indent=0.0)',
  '"market (Grasso et al., 2020).", first_indent=0.0)')

E(DIS,
  '"Table 12 states the boundary explicitly.", first_indent=0.0)',
  '"Table 12 states the boundary explicitly (Roma et al., 2020).", first_indent=0.0)')

E(DIS,
  '"characterization.", first_indent=0.0)',
  '"characterization (Grasso et al., 2022).", first_indent=0.0)')

E(DIS,
  '"active research area, none is validated for seafood matrices, and none has been "',
  '"active research area, none is validated for seafood matrices, and none has been "')

E(DIS,
  '"applied systematically to the products in which ENPs have been detected.",',
  '"applied systematically to the products in which ENPs have been detected '
  '(Hochella et al., 2019; Li et al., 2023).",')

E(DIS,
  '"them rather than supplying the values themselves. The 2021 opinion on titanium "',
  '"them rather than supplying the values themselves (EFSA Scientific Committee, 2021). The 2021 opinion on titanium "')

E(DIS,
  '"in 2022. That decision arose from a full food-additive dossier for a material "',
  '"in 2022 (EFSA Panel on Food Additives and Flavourings, 2021). That decision arose from a full food-additive dossier for a material "')

E(DIS,
  '"can sustain.", first_indent=0.0)',
  '"can sustain (Corsi et al., 2014).", first_indent=0.0)')

E(DIS,
  '"that does not currently exist. Recognizing this is more useful than criticizing "',
  '"that does not currently exist. Recognizing this is more useful than criticizing "')

E(DIS,
  '"but it also demonstrates how much evidence is required before action is "',
  '"but it also demonstrates how much evidence is required before action is "')

E(DIS,
  '"possible.", first_indent=0.0)',
  '"possible (EFSA Scientific Committee, 2021).", first_indent=0.0)')

E(DIS,
  '"does not currently exist, because it identifies what would need to be built.",',
  '"does not currently exist, because it identifies what would need to be built '
  '(Meng & Nag, 2026; Nugawela et al., 2025).",')

E(DIS,
  '"particle-specific analysis is applied selectively.",',
  '"particle-specific analysis is applied selectively (Laycock et al., 2022).",')

E(DIS,
  '"nano-enabled product approval, not a moratorium and not inaction.", first_indent=0.0)',
  '"nano-enabled product approval, not a moratorium and not inaction (FAO, 2024; '
  'Khosravi-Katuli et al., 2017).", first_indent=0.0)')

E(DIS,
  '"circumvented by ", first_indent=0.0)',
  '"circumvented by ", first_indent=0.0)')

E(DIS,
  '"techniques \u2014 to make progress. Reference materials are a "',
  '"techniques \u2014 to make progress. Reference materials are a "')

E(DIS,
  '"corona-associated or partially dissolved particles \u2014 are what organisms "',
  '"corona-associated or partially dissolved particles \u2014 are what organisms "')

E(DIS,
  '"obstacle.", first_indent=0.0)',
  '"obstacle (Zhang et al., 2025).", first_indent=0.0)')

E(DIS,
  '"an incident forces the question. Each of "',
  '"an incident forces the question (Meng & Nag, 2026). Each of "')

E(DIS,
  '"specific priorities set out in this review. Regulators should treat the "',
  '"specific priorities set out in this review (Nugawela et al., 2025). Regulators should treat the "')

E(DIS,
  '"practices are what have kept this question open.", first_indent=0.0)',
  '"practices are what have kept this question open (Hanna et al., 2013; Miao et al., '
  '2010).", first_indent=0.0)')


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    applied = failed = 0
    for fname, old, new in EDITS:
        path = os.path.join(here, fname)
        s = open(path).read()
        if old == new:
            continue
        if old not in s:
            print("  MISS", fname, "|", old[:60].replace("\n", " "))
            failed += 1
            continue
        s = s.replace(old, new, 1)
        open(path, "w").write(s)
        applied += 1
    print(f"applied {applied}, missed {failed}")


if __name__ == "__main__":
    main()
