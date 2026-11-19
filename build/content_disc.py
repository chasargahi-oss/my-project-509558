"""Discussion, gaps, limitations, conclusion, declarations."""
from docx.shared import Pt
from docx_style import para, rich, h1, h2, h3

U = "\u00b5"


def discussion(doc):
    h1(doc, "Discussion", 4)

    para(doc, "The central finding of this review is a structural one. The evidence that ENPs "
              "are detectable in seafood is strong; the evidence that they can cause toxicity "
              "under laboratory conditions is strong; and the evidence that they cause a "
              "demonstrated risk to seafood safety or human health at environmentally realistic "
              "exposures is weak. These three propositions are frequently merged in the "
              "literature and in policy commentary, and separating them is the review's principal "
              "analytical contribution. Doing so does not diminish the concern: it locates the "
              "concern precisely, and it identifies the measurements that would resolve it (Nugawela et al., 2025).",
         first_indent=1.0)

    # ---------------------------------------------------------------- 4.1
    h2(doc, "What the evidence does and does not establish", "4.1")

    para(doc, "The occurrence evidence is the most direct and the most frequently "
              "misrepresented. spICP-MS has established that TiO\u2082, Ag and ZnO nanoparticles "
              "are present in canned seafood at concentrations that can be quantified with "
              "acceptable recovery, and that nanoparticle fractions constitute a substantial "
              "minority of the total elemental content for titanium. This is a genuine advance: "
              "fifteen years ago the question of whether engineered nanoparticles reached edible "
              "tissue in commercially distributed products was open. It is now answered in the "
              "affirmative for at least three materials in at least one product category in one "
              "market (Grasso et al., 2020).", first_indent=0.0)
    _EMBED("T12")

    para(doc, "What that evidence does not establish is origin. A nanoparticle detected in "
              "canned clam may be engineered, naturally occurring, or produced incidentally "
              "during processing or packaging, and no study in the reviewed corpus resolved this "
              "for seafood. This matters because the regulatory instruments that would apply to "
              "an intentionally added nanomaterial differ from those applicable to an "
              "environmental contaminant, and because the toxicological logic differs as well. "
              "Until source attribution is achievable, occurrence data support a monitoring "
              "conclusion \u2014 that nanoparticle-scale metal is present in the food supply "
              "\u2014 but not a risk conclusion about engineered nanoparticles specifically.",
         first_indent=0.0)

    para(doc, "The toxicity evidence has the opposite profile: it is mechanistically rich and "
              "environmentally thin. The consistency with which oxidative stress, lysosomal "
              "destabilization and genotoxicity are reported across taxa and laboratories is "
              "reassuring as to biological plausibility \u2014 these are not isolated findings "
              "from single groups \u2014 but the concentrations at which they occur are usually "
              "one to three orders of magnitude above measured environmental levels. The "
              "resulting inference problem is symmetrical and frequently misstated. High-dose "
              "effects do not demonstrate field risk, and the absence of field effects does not "
              "demonstrate safety, because the field monitoring required to detect chronic "
              "sublethal effects on population-relevant endpoints has not been conducted. "
              "Table 12 states the boundary explicitly (Roma et al., 2020).", first_indent=0.0)


    para(doc, "The exposure evidence is the weakest link in the chain, and it is weak for a "
              "reason that is structural rather than incidental. Dietary exposure has been "
              "estimated from occurrence data in a handful of products, with a single meal as "
              "the exposure unit and no characterization of between-brand, between-batch or "
              "between-season variability. Consumption surveys were not linked to measured "
              "concentrations in the same populations. Aggregate exposure from multiple "
              "food and non-food sources was not estimated. And the estimates rest on "
              "concentrations measured in one national market. The resulting numbers are best "
              "read as order-of-magnitude indications that nanoparticle intake from a seafood "
              "meal is small in absolute terms, which is useful but insufficient for risk "
              "characterization (Grasso et al., 2022).", first_indent=0.0)

    # ---------------------------------------------------------------- 4.2
    h2(doc, "Why the risk question remains unresolved", "4.2")

    para(doc, "Four distinct obstacles prevent closure, and they cannot be addressed by better "
              "execution of the same study designs. The first is source attribution. Existing "
              "methods measure elemental composition and particle size, not provenance. "
              "Distinguishing an engineered TiO\u2082 particle from a natural one requires "
              "information that elemental analysis does not provide \u2014 isotopic signatures, "
              "coating chemistry, crystalline polymorph ratios, associated trace-element "
              "fingerprints or morphometric population characteristics. Each of these is an "
              "active research area, none is validated for seafood matrices, and none has been "
              "applied systematically to the products in which ENPs have been detected (Hochella et al., 2019; Li et al., 2023).",
         first_indent=1.0)

    para(doc, "The second obstacle is the absence of health-based guidance values. Risk "
              "characterization for a food contaminant requires a reference point \u2014 a "
              "no-observed-adverse-effect level, a benchmark dose lower confidence limit, or a "
              "tolerable intake derived from one of them \u2014 expressed for the relevant "
              "particle form and route. For engineered nanoparticles in food, such values are "
              "essentially unavailable, and the European Food Safety Authority's structured "
              "guidance on nanomaterial risk assessment sets out the data required to derive "
              "them rather than supplying the values themselves (EFSA Scientific Committee, 2021). The 2021 opinion on titanium "
              "dioxide (E 171) illustrates the difficulty: the Panel was unable to establish an "
              "acceptable daily intake and identified a genotoxicity concern that could not be "
              "excluded, which led to the additive's withdrawal from the European Union market "
              "in 2022 (EFSA Panel on Food Additives and Flavourings, 2021). That decision arose from a full food-additive dossier for a material "
              "present at percent-level concentrations. Comparable dossiers do not exist for "
              "environmentally derived nanoparticles in seafood, and the toxicological data "
              "required to build them \u2014 chronic oral exposure, particle characterization in "
              "the food matrix, toxicokinetics and mode-of-action analysis \u2014 have not been "
              "generated for any seafood-relevant ENP. This is why a precautionary posture is "
              "the only scientifically defensible one: not because harm has been shown, but "
              "because the assessment cannot be completed.", first_indent=0.0)

    para(doc, "The third obstacle is ecological realism in experimental design. Standard "
              "single-species, single-particle, short-duration laboratory tests cannot represent "
              "the aged, transformed, hetero-aggregated particles that organisms actually "
              "encounter, nor the multi-stressor conditions of coastal environments, nor the "
              "multi-generational timescales over which chronic effects would manifest. "
              "Mesocosm and field studies that address these limitations are scarce, and where "
              "they exist they typically focus on community-level endpoints rather than on edible "
              "tissue. The fourth obstacle is analytical: the absence of certified reference "
              "materials and proficiency-testing schemes means that interlaboratory comparability "
              "cannot be demonstrated, which in turn prevents the construction of the "
              "longitudinal and geographic datasets on which food-safety monitoring depends.",
         first_indent=0.0)

    para(doc, "None of these obstacles is a reason for inaction, and two of them are being "
              "addressed with existing technology. Source attribution is a tractable "
              "instrumentation problem, and the analytical community has the tools \u2014 "
              "single-particle multi-element fingerprinting, isotope ratio measurement and "
              "automated particle morphology \u2014 to make progress. Reference materials are a "
              "production problem that a coordinated metrology programme could solve within a "
              "few years. The guidance-value and ecological-realism gaps are slower, because "
              "they require chronic studies and mesocosm infrastructure that no single laboratory "
              "can sustain (Corsi et al., 2014).", first_indent=0.0)

    # ---------------------------------------------------------------- 4.3
    h2(doc, "Comparison with regulatory frameworks", "4.3")

    para(doc, "Regulatory treatment of nanomaterials in food has developed unevenly across "
              "jurisdictions, and the unevenness is itself a source of uncertainty for seafood "
              "producers and importers. The European Union operates the most developed framework, "
              "combining a general food-law requirement that novel foods and novel food "
              "ingredients be authorized before marketing with specific guidance on the data "
              "required to assess nanomaterials, and with a definition of engineered nanomaterial "
              "that turns on the 50% particle-number criterion in the 1\u2013100 nm range. "
              "Implementation nevertheless relies heavily on case-by-case assessment, and there "
              "is no harmonized maximum level for ENPs in seafood. The withdrawal of E 171 "
              "demonstrates that the framework can act decisively when a dossier is complete, "
              "but it also demonstrates how much evidence is required before action is "
              "possible (EFSA Scientific Committee, 2021).", first_indent=0.0)

    para(doc, "Other jurisdictions rely more heavily on pre-market notification, "
              "ingredient-labelling requirements and general safety provisions. International "
              "harmonization remains limited: Codex Alimentarius has not established maximum "
              "levels for ENPs in seafood, and no international reference values exist for "
              "nanoparticle-scale metal in fish or shellfish. The practical consequence for "
              "seafood trade is that a product acceptable in one market may be unassessable in "
              "another, not because the hazard differs but because the assessment framework "
              "does.", first_indent=0.0)

    para(doc, "The regulatory gap has a specific structural cause worth naming. Food-safety "
              "regulation for chemical contaminants is built on maximum levels derived from "
              "toxicological reference points and consumption data. That architecture assumes "
              "that the contaminant's identity and form are stable and measurable, and it "
              "assumes that a reference point can be derived from chronic studies of the "
              "substance as consumed. Engineered nanoparticles violate both assumptions: their "
              "identity changes with environment and matrix, and chronic studies of the "
              "particle form as it occurs in seafood have not been performed. The framework "
              "therefore cannot simply be extended; it requires an additional evidentiary layer "
              "that does not currently exist. Recognizing this is more useful than criticizing "
              "regulators for inaction, because it identifies what would need to be built (Meng & Nag, 2026; Nugawela et al., 2025).",
         first_indent=0.0)

    # ---------------------------------------------------------------- 4.4
    h2(doc, "Implications for monitoring and aquaculture", "4.4")

    para(doc, "For monitoring programmes, the implication is that elemental analysis of seafood "
              "is no longer sufficient as a sentinel for nanomaterial contamination. Total "
              "titanium, silver or zinc concentrations conflate dissolved, bulk and "
              "nanoparticulate fractions whose hazard profiles differ, and the dissolved fraction "
              "usually dominates numerically. A monitoring design that can detect a change in "
              "nanoparticle burden must therefore include a particle-sizing measurement, which "
              "in practice means spICP-MS or an equivalent single-particle technique, together "
              "with orthogonal confirmation on a subsample. This has cost and capacity "
              "implications that most national food-control laboratories have not yet addressed, "
              "and it argues for a tiered design in which elemental screening identifies "
              "candidate products and particle-specific analysis is applied selectively (Laycock et al., 2022).",
         first_indent=1.0)

    para(doc, "For aquaculture, the implication is double-edged. Nanotechnology offers genuine "
              "potential benefits \u2014 improved feed efficiency, antimicrobial alternatives to "
              "critically important antibiotics, better water treatment and faster disease "
              "diagnosis \u2014 and dismissing these would be as unbalanced as ignoring the "
              "risks. But the sector's exposure assessment is essentially absent. There is very "
              "little field-scale evidence quantifying nanoparticle release from aquaculture "
              "operations, persistence in receiving waters, contamination of cultured organisms "
              "or production-level consequences. Because aquaculture now supplies more aquatic "
              "animals than capture fisheries and is the fastest-growing food-production sector, "
              "the exposure footprint of nano-enabled practices will grow whether or not it is "
              "measured. The appropriate response is a monitoring requirement attached to "
              "nano-enabled product approval, not a moratorium and not inaction (FAO, 2024; Khosravi-Katuli et al., 2017).", first_indent=0.0)

    para(doc, "There is a nutritional dimension that complicates the risk calculus and deserves "
              "explicit treatment. Seafood is a principal source of long-chain omega-3 fatty "
              "acids, high-quality protein, iodine, selenium, vitamin D and vitamin B\u2081\u2082, "
              "and consumption is associated with reduced cardiovascular and "
              "neurodevelopmental risk. Fish consumption advisories issued for methylmercury "
              "already illustrate the trade-off: over-restriction can cause net harm by "
              "displacing a beneficial food. Any ENP advisory would face the same trade-off "
              "under much greater uncertainty, because the hazard is unquantified rather than "
              "merely uncertain. This asymmetry is a strong argument against consumer advisories "
              "in the current state of knowledge, and a strong argument for investing in the "
              "measurements that would make an advisory evidence-based if one were needed.",
         first_indent=0.0)

    # ---------------------------------------------------------------- 4.5
    h2(doc, "Research gaps and priorities", "4.5")

    para(doc, "The gaps identified in this review are summarized in Table 13 with an explicit "
              "priority ranking and the type of study that would close each one. They are "
              "presented as a research agenda rather than a list of deficiencies, because each "
              "is addressable with existing or near-term methods. The ranking reflects two "
              "considerations: how much a gap constrains current risk inference, and how "
              "feasible closure is within a three- to five-year horizon.", first_indent=1.0)
    _EMBED("T13")


    para(doc, "The highest-priority gap is source attribution, because it invalidates every "
              "downstream inference in the occurrence literature and because the analytical path "
              "forward is identifiable. Isotope-ratio measurement, multi-element single-particle "
              "fingerprinting, polymorph-specific analysis and automated morphometric "
              "classification are each capable of contributing, and a coordinated programme "
              "combining them could establish provenance for the dominant materials within a few "
              "years. The second priority is reference materials, because without them "
              "interlaboratory comparison is impossible and monitoring data cannot be pooled "
              "across jurisdictions. The third is chronic oral toxicity at environmentally "
              "relevant concentrations, which is expensive and slow but is the only route to "
              "health-based guidance values, and the fourth is bioaccessibility, which determines "
              "whether ingested particles survive digestion in a form that can reach systemic "
              "circulation.", first_indent=0.0)

    para(doc, "Three further gaps deserve mention because they are systematically overlooked. "
              "Crustaceans, cephalopods and seaweeds are commercially important and almost "
              "entirely absent from the ENP literature, so the risk assessment for those "
              "commodities rests on extrapolation from bivalves with no empirical check. "
              "Transformation products \u2014 aged, coated, corona-associated or partially "
              "dissolved particles \u2014 are what organisms actually encounter, yet almost all "
              "toxicology uses pristine laboratory particles. And food-processing effects, "
              "including canning, freezing, cooking and packaging migration, have not been "
              "characterized for their impact on particle size, dissolution state or "
              "bioaccessibility, even though processed products dominate the occurrence "
              "literature. Each of these is a tractable study design, not a fundamental "
              "obstacle (Zhang et al., 2025).", first_indent=0.0)

    # ---------------------------------------------------------------- 4.6
    h2(doc, "Limitations of this review", "4.6")

    para(doc, "The review has limitations that should be weighed when interpreting its "
              "conclusions, and several are substantial enough to affect the strength of specific "
              "claims. The most important is the search architecture. Searches were executed "
              "through a single AI-assisted discovery platform rather than through independently "
              "queried bibliographic databases, so database-specific yields, duplicate-removal "
              "counts and automation-assisted exclusions could not be recorded separately. This "
              "departs from full PRISMA 2020 reporting requirements, and it means that the "
              "review's coverage cannot be independently reproduced with the same precision as a "
              "conventional multi-database search. Citation tracing and co-citation analysis were "
              "used to mitigate this, but they do not substitute for it.", first_indent=1.0)

    para(doc, "Second, screening and data extraction were performed by the review team without "
              "independent dual abstraction, so selection and extraction errors cannot be "
              "excluded, although the small corpus and explicit criteria limit the scope for "
              "systematic divergence. Third, the included studies differ so widely in "
              "nanoparticle type, coating, size, exposure medium and duration, species, endpoint "
              "and analytical method that pooling was impossible; the synthesis is therefore "
              "narrative, and quantitative statements throughout this review refer to ranges "
              "across heterogeneous studies rather than to pooled estimates.", first_indent=0.0)

    para(doc, "Fourth, several of the quantitative occurrence values rest on a small number of "
              "primary studies, in some cases a single study per material, and where that is the "
              "case the review says so. Replication across independent research groups using "
              "independently validated methods has not been achieved for any seafood product. "
              "Fifth, publication bias may inflate the apparent weight of positive findings, "
              "particularly in the toxicology literature, where null results at environmentally "
              "relevant concentrations are less likely to be published and less likely to be "
              "cited. Sixth, the review is restricted to English-language publications, so "
              "regional literatures that may hold relevant monitoring data \u2014 particularly "
              "from major aquaculture-producing countries \u2014 are underrepresented. Table 14 "
              "sets these limitations against the mitigation measures adopted and those still "
              "required.", first_indent=0.0)
    _EMBED("T14")


    # ---------------------------------------------------------------- 4.7
    h2(doc, "Conclusions and outlook", "4.7")

    para(doc, "Engineered nanoparticles in seafood present a risk that is plausible, "
              "analytically confirmed at the level of occurrence, mechanistically supported by a "
              "substantial experimental literature, and quantitatively undemonstrated at "
              "environmentally relevant exposures. That combination is uncomfortable for both "
              "the reassuring and the alarmist reading of the evidence, and it is the honest "
              "summary of the field as it stands. Nanoparticle-scale titanium, silver and zinc "
              "are present in commercially distributed seafood. Laboratory studies show that "
              "such particles can cause sublethal toxicity. The concentrations at which those "
              "effects occur are typically far above measured environmental levels, and the "
              "chronic, low-dose, food-matrix studies that would bridge the gap have not been "
              "performed.", first_indent=1.0)

    para(doc, "The route out of that impasse is specific rather than general, and it does not "
              "require a breakthrough. It requires source-attribution methods validated for "
              "seafood matrices; certified reference materials and proficiency-testing schemes; "
              "chronic oral-toxicity studies conducted with particles aged and characterized in "
              "the relevant food matrix; bioaccessibility testing under simulated human digestion; "
              "mesocosm and field studies at environmentally realistic concentrations with "
              "population-relevant endpoints; extension of monitoring to crustaceans, "
              "cephalopods and seaweeds; and a harmonized regulatory pathway that defines what "
              "evidence would trigger action before an incident forces the question (Meng & Nag, 2026). Each of "
              "these is a defined, fundable, achievable piece of work. Together they would "
              "convert an open question into a manageable one.", first_indent=0.0)

    para(doc, "Pending that work, a proportionate position is defensible and should be stated "
              "plainly. There is no basis for consumer advisories restricting seafood "
              "consumption on ENP grounds: measured intakes are low, the nutritional benefits of "
              "seafood are substantial and well established, and the hazard is unquantified "
              "rather than demonstrated. Equally, there is no basis for declaring seafood safe "
              "with respect to ENPs, because no assessment has been completed that could support "
              "such a declaration. The defensible position is that ENPs are an emerging "
              "contaminant of concern requiring structured monitoring, source control at the "
              "point of release, and targeted research investment, with the specific priorities "
              "set out in this review (Nugawela et al., 2025). Regulators should treat the analytical and toxicological "
              "gaps as a reason to build capability, not as a reason to defer. Producers and "
              "processors should characterize their supply chains while the methods are still "
              "being validated, so that baseline data exist before any regulatory requirement "
              "arrives. And the research community should stop reporting occurrence without "
              "provenance, and toxicity without environmental realism, because those two "
              "practices are what have kept this question open (Hanna et al., 2013; Miao et al., 2010).", first_indent=0.0)


def declarations(doc):
    h1(doc, "Declarations")

    def block(title, text):
        rich(doc, [(title + "  ", {"bold": True, "size": 11}),
                   (text, {"size": 11})],
             align="justify", line=1.4, space_after=8)

    block("Ethics approval and consent to participate.",
          "Not applicable. This review synthesized published literature and did not involve "
          "human participants, human tissue or animal experimentation by the authors.")

    block("Consent for publication.",
          "Not applicable. No individual person's data are included in this article.")

    block("Availability of data and materials.",
          "All data discussed in this review are reported in the cited primary publications. "
          "The search strings, eligibility criteria and screening decisions are reported in "
          "Tables 2 and 3 and in Figure 2. No new primary data were generated. The extracted "
          "data template used for the synthesis is available from the corresponding author on "
          "reasonable request.")

    block("Competing interests.",
          "The authors declare that they have no known competing financial interests or "
          "personal relationships that could have appeared to influence the work reported in "
          "this article.")

    block("Funding.",
          "This research received no specific grant from any funding agency in the public, "
          "commercial or not-for-profit sectors.")

    block("Authors' contributions.",
          "Alireza Hemmati: Conceptualization, Methodology, Investigation (literature search "
          "and verification), Formal analysis, Data curation, Writing \u2013 original draft, "
          "Writing \u2013 review and editing, Visualization, Supervision, Project administration. "
          "Shiva Yousefi: Methodology, Investigation (literature search and verification), "
          "Formal analysis, Validation, Writing \u2013 review and editing. Both authors read and "
          "approved the final manuscript and agree to be accountable for all aspects of the "
          "work.")

    block("Use of artificial intelligence.",
          "Artificial-intelligence tools were used solely to support language editing, "
          "formatting and structural organization of the manuscript. All literature searching, "
          "study selection, data extraction, interpretation and conclusions were performed and "
          "verified by the authors, who take full responsibility for the content.")

    block("Acknowledgements.",
          "The authors thank the developers of the open scholarly indexing infrastructure on "
          "which the literature search depended.")

    # ---- references
    h1(doc, "References")

    from refs import REFS
    from italics import ref_segments, italianize
    for i, (key, txt) in enumerate(REFS, 1):
        parts = []
        if i == 1:
            parts.append((f"{i}.  ", {}))
        else:
            parts.append((f"{i}.  ", {}))
        for seg, ital in ref_segments(txt):
            for chunk, lat in italianize(seg):
                parts.append((chunk, {"italic": ital or lat}))
        rich(doc, parts, size=10, align="left", line=1.3, space_after=6,
             left_indent=0.75, first_indent=-0.75)
