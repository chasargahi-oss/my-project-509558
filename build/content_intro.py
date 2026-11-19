"""Introduction and Methods."""
from docx.shared import Pt
from docx_style import para, rich, h1, h2, h3


def introduction(doc):
    h1(doc, "Introduction", 1)

    para(doc, "Engineered nanoparticles (ENPs) are intentionally manufactured materials with at "
              "least one dimension typically in the 1\u2013100 nm range. They include metal and "
              "metal-oxide particles such as titanium dioxide (TiO\u2082), silver (Ag), zinc oxide "
              "(ZnO) and copper oxide (CuO), together with carbon-based and polymeric "
              "nanomaterials. Their high surface-area-to-volume ratio, tunable surface chemistry "
              "and capacity to release ions can produce biological effects that differ "
              "qualitatively from those of chemically identical bulk materials. These same "
              "properties underpin their industrial value, and global production and "
              "incorporation into consumer products have grown steadily over the past two "
              "decades (Keller & Lazareva, 2014; Nowack & Bucheli, 2007).", first_indent=1.0)

    para(doc, "The environmental consequence of that growth is a diffuse and largely "
              "unmeasured flux of engineered particles into aquatic systems. Wastewater "
              "treatment effluent, urban stormwater, residues from personal-care and sunscreen "
              "products, antifouling coatings, industrial discharge and disposal of nano-enabled "
              "goods all route ENPs toward coastal waters, which are the terminal receiving "
              "environment for most land-derived material. Material-flow modelling indicates "
              "that the majority of ENM mass released to technical compartments ultimately "
              "reaches water, soil or landfill, with wastewater effluent concentrations "
              "predicted to fall in the nanogram- to microgram-per-litre range depending on the "
              "material and the population density of the catchment (Keller & Lazareva, 2014).", first_indent=0.0)

    para(doc, "Once released, ENPs do not behave as inert, discrete particles. In seawater, "
              "high ionic strength compresses the electrical double layer and suppresses "
              "electrostatic repulsion, promoting hetero-aggregation with natural colloids and "
              "subsequent sedimentation. Particles may also dissolve, acquiring a biomolecular "
              "corona, undergo redox or surface transformation, or be transiently stabilized in "
              "the water column by extracellular polymeric substances released during algal "
              "blooms. These processes are not cosmetic refinements of exposure: they determine "
              "whether a particle remains bioavailable in the water column, accumulates in "
              "sediment where deposit feeders graze, or is converted into dissolved metal that "
              "acts through an entirely different toxicological mechanism (Abbas et al., 2020; Lead et al., 2018).", first_indent=0.0)

    para(doc, "The food-safety relevance of this chemistry follows from the scale and "
              "composition of the seafood sector. Global fisheries and aquaculture production "
              "reached 223.2 million tonnes in 2022, of which 185.4 million tonnes were aquatic "
              "animals, and aquaculture surpassed capture fisheries as the principal source of "
              "aquatic animals for the first time (FAO, 2024). Apparent per-capita consumption of aquatic "
              "animal foods reached 20.7 kg in 2022, and aquatic foods supplied about 15% of "
              "global animal protein, exceeding 50% of animal protein in several countries in "
              "Asia and Africa. A contaminant that accumulates in edible shellfish or finfish "
              "muscle therefore has a potential exposure pathway of global reach, and one that "
              "falls disproportionately on populations for whom seafood is a nutritional "
              "necessity rather than a dietary choice (FAO, 2024).", first_indent=0.0)

    para(doc, "Bivalve molluscs deserve particular attention within that pathway. Filter "
              "feeding processes large volumes of water and concentrates particulate material in "
              "gill mucus and the digestive gland, and bivalves are sessile, widely distributed "
              "and consumed whole. They are simultaneously the organisms most consistently "
              "reported to accumulate ENPs in laboratory studies and the seafood commodity group "
              "most frequently examined in monitoring work. Fish add a second route, through "
              "gill and intestinal uptake and through ingestion of contaminated prey, with "
              "muscle tissue representing the endpoint of greatest dietary relevance. "
              "Crustaceans, cephalopods and seaweeds have received far less attention, which is "
              "itself a significant gap given their commercial importance in many markets (Canesi et al., 2012; Rocha et al., 2015).",
         first_indent=0.0)

    para(doc, "Nanotechnology is also entering the seafood production system directly. "
              "Nanomaterials are investigated in aquaculture as antimicrobial agents, feed "
              "additives, water-treatment media, drug-delivery vehicles, diagnostic reagents and "
              "environmental sensors. Low experimental doses of some nanoparticles have been "
              "associated with improved feed conversion, antioxidant enzyme activity and "
              "non-specific immune responses. The same properties that make these applications "
              "attractive \u2014 small size, high reactivity and antimicrobial potency \u2014 may "
              "increase ecological risk if particles or their dissolution products are released "
              "in effluent or retained in cultured tissues. The aquaculture evidence base is "
              "therefore double-edged, and it is thin on the field-scale side that would matter "
              "for food-safety management (Khosravi-Katuli et al., 2017).", first_indent=0.0)

    para(doc, "Analytical chemistry has changed what can be asked. Single-particle inductively "
              "coupled plasma mass spectrometry (spICP-MS) introduces a dilute particle "
              "suspension into the plasma under conditions in which individual particles "
              "generate discrete ion clouds, so that pulse frequency reports particle-number "
              "concentration and pulse intensity reports particle mass and, with assumptions "
              "about density and shape, diameter. The technique combines high sensitivity, "
              "elemental specificity and the ability to separate dissolved from "
              "particle-associated metal in a single acquisition, and it has now been applied to "
              "canned seafood to quantify TiO\u2082, Ag and ZnO nanoparticles and to estimate "
              "dietary exposure (Grasso et al., 2020). Detection, however, is not identification of origin, and origin "
              "is exactly what a food-safety assessment requires.", first_indent=0.0)

    para(doc, "Regulatory frameworks have not kept pace with either the analytical or the "
              "toxicological literature. There are no globally harmonized maximum levels for "
              "ENPs in seafood, and health-based guidance values \u2014 acceptable daily intakes, "
              "reference doses or tolerable weekly intakes \u2014 are unavailable for most "
              "nanoparticle types. The European Food Safety Authority has published a structured "
              "risk-assessment guidance for nanomaterials in the food and feed chain, and the "
              "European Union withdrew titanium dioxide (E 171) from its list of permitted food "
              "additives in 2022 after the Panel on Food Additives and Flavourings concluded "
              "that a genotoxicity concern could not be excluded and that no acceptable daily "
              "intake could be established (EFSA Panel on Food Additives and Flavourings, 2021). "
              "That decision concerned a deliberate food additive, "
              "not an environmental contaminant of seafood, but it illustrates the regulatory "
              "asymmetry that currently prevails: the capacity to detect nanoparticle-scale "
              "metal in food has outpaced the capacity to decide what a given concentration "
              "means (EFSA Scientific Committee, 2021; EFSA Panel on Food Additives and Flavourings, 2021).", first_indent=0.0)

    para(doc, "The published literature on ENPs and seafood is correspondingly fragmented. "
              "Environmental chemists quantify particles in seawater and sediment; "
              "ecotoxicologists measure biomarkers in bivalves and fish at laboratory "
              "concentrations; analytical chemists report occurrence in canned products; and "
              "risk assessors attempt to convert those numbers into intake estimates. Each "
              "literature is internally coherent and methodologically defensible, but the "
              "conclusions drawn from one are routinely imported into another without adequate "
              "attention to the mismatch in exposure concentrations, particle forms and "
              "endpoints. The result is a field in which it is possible to find support for "
              "almost any position between complacency and alarm, and in which the boundary "
              "between what is known and what is assumed is rarely stated explicitly.",
         first_indent=0.0)

    para(doc, "This review therefore addresses a deliberately narrow question: what is the "
              "current evidence that engineered nanoparticles in marine environments accumulate "
              "in seafood, affect marine organisms, and pose a quantifiable risk to seafood "
              "safety and human consumers? To answer it defensibly, the review maintains a "
              "strict separation between three propositions that are frequently conflated in the "
              "literature: (i) that ENPs are detectable in seafood; (ii) that ENPs can cause "
              "toxicity under laboratory conditions; and (iii) that ENPs cause a demonstrated "
              "risk to seafood safety or human health at environmentally realistic exposures. As "
              "the synthesis below shows, the evidence strongly supports the first, moderately "
              "supports the second, and does not yet establish the third. Making that "
              "distinction explicit, and identifying precisely which measurements would close "
              "the gap, is the principal contribution of this review.", first_indent=0.0)

    # ---- scope
    h2(doc, "Scope, definitions and conceptual framework", "1.1")

    para(doc, "The review focuses on engineered inorganic nanoparticles of greatest relevance to "
              "marine and seafood exposure: TiO\u2082, Ag, ZnO, CuO, CeO\u2082 and related metal- or "
              "metal-oxide-bearing particles. Carbon-based nanomaterials and nanoplastics are "
              "considered where they intersect with seafood safety, but they are not the primary "
              "focus, because their detection strategies, environmental behaviour and "
              "toxicological evidence base differ substantially from those of metal-containing "
              "ENPs and would not support a single coherent synthesis. \u201cSeafood\u201d is taken "
              "to include finfish, bivalves, crustaceans, cephalopods and processed seafood "
              "products, with explicit attention to the degree to which findings from one "
              "commodity group can be generalized to others.", first_indent=0.0)

    para(doc, "Three terminological distinctions carry substantive weight throughout the "
              "review and are used consistently. First, a particle detected in food may be "
              "engineered, natural or incidental; these categories are not interchangeable, and "
              "the analytical difficulty of separating them is a recurrent theme. Second, "
              "bioaccumulation refers to net uptake and retention within an organism, whereas "
              "biomagnification refers to increasing concentration or burden with increasing "
              "trophic position. A particle may transfer through a food chain without "
              "biomagnifying, and several influential studies are misread on precisely this "
              "point. Third, a reference dose or health-based guidance value is a toxicological "
              "benchmark against which an exposure estimate can be compared; in its absence, an "
              "exposure estimate cannot be converted into a risk characterization, however "
              "precisely it is measured. Table 1 defines these and related terms as they are "
              "used here.", first_indent=0.0)
    _EMBED("T1")


    para(doc, "Figure 1 summarizes the conceptual framework that organizes the review. ENPs "
              "are released from production, use and disposal into coastal seawater and "
              "sediment, where physical and chemical transformations determine their subsequent "
              "bioavailability. Marine organisms encounter particles through waterborne uptake, "
              "filter feeding, sediment contact and dietary ingestion, with trophic transfer "
              "providing a route to higher consumers. Detection in edible tissue is the "
              "necessary condition for a food-safety concern, and dietary exposure assessment "
              "converts occurrence into intake. The final step \u2014 from intake to a "
              "characterized risk \u2014 requires chronic oral-toxicity data and a health-based "
              "guidance value, and it is at this step that the evidence chain currently breaks. "
              "The dashed element in the figure marks the point at which the framework becomes "
              "conditional rather than quantitative (Figure 1).", first_indent=0.0)
    _EMBED("F1")


    para(doc, "Two framing choices follow from this structure. The review is organized by "
              "evidence stream rather than by particle type, because the same particle behaves "
              "differently across matrices and the same matrix hosts many particles; organizing "
              "by stream makes the inferential gaps visible. And the review reports "
              "concentrations with the units and matrices used by the original investigators, "
              "resisting the temptation to harmonize them into a single nominal scale. That "
              "heterogeneity is itself a finding, and it is one reason why meta-analysis was "
              "not appropriate (Roma et al., 2020).", first_indent=0.0)


def methods(doc):
    h1(doc, "Methods", 2)

    para(doc, "The review was conducted as a systematic review with narrative synthesis and is "
              "reported in accordance with the PRISMA 2020 statement (Page et al., 2021). A conventional PICO "
              "framework was not adopted because the research question spans environmental "
              "exposure, marine ecotoxicology, food occurrence, dietary intake and regulatory "
              "risk assessment rather than a single intervention\u2013comparator pair. A "
              "multi-concept structure was used instead, and the resulting search blocks, "
              "screening decisions and exclusion counts are reported in full below and in "
              "Figure 2.", first_indent=1.0)

    h2(doc, "Search strategy", "2.1")

    para(doc, "Searches were executed in Consensus, an AI-assisted research-discovery platform "
              "that indexes more than 220 million papers through Semantic Scholar, PubMed and "
              "additional scholarly sources. Seven complementary concept blocks were combined to "
              "ensure coverage across environmental sources, organism-level effects, seafood "
              "monitoring, human-health risk and aquaculture applications (Table 2). Searches "
              "were supplemented by backward and forward citation tracing from key reviews and "
              "empirical seafood-monitoring studies, and by bibliographic coupling and "
              "co-citation analysis to identify foundational and emerging literature that "
              "keyword searching alone would miss.", first_indent=0.0)
    _EMBED("T2")

    para(doc, "Because the search was executed through a single discovery platform rather than "
              "through independently queried bibliographic databases, database-specific yields, "
              "duplicate-removal counts and automation-assisted exclusions were not separately "
              "recorded. This is a material limitation for reproducibility and for full PRISMA "
              "2020 compliance, and it is reported as such rather than concealed by imputing "
              "values. The search was completed in November 2026, and the reference list was "
              "cross-checked against publisher and Crossref records to confirm bibliographic "
              "accuracy.", first_indent=0.0)


    h2(doc, "Eligibility criteria and study selection", "2.2")

    para(doc, "Records were screened for relevance to marine or seafood-related ENP exposure and "
              "effects. Priority was given to peer-reviewed empirical studies, systematic or "
              "narrative reviews with transparent evidence synthesis, environmental-monitoring "
              "studies, dietary-exposure assessments, and regulatory or risk-assessment "
              "analyses. Studies were eligible if they addressed metal, metal-oxide, carbon-based "
              "or polymeric ENPs in marine systems, seafood organisms, edible seafood or "
              "seafood-relevant food matrices, and reported an outcome related to environmental "
              "fate, uptake, toxicity, occurrence, trophic transfer, dietary exposure or risk "
              "assessment. Studies restricted to terrestrial systems, to human cell lines without "
              "a food-relevant exposure pathway, or to bulk materials without nanoscale relevance "
              "were excluded, as were editorials, conference abstracts without usable data, "
              "non-scholarly web content and reports without retrievable full text. Table 3 "
              "summarizes the criteria.", first_indent=0.0)
    _EMBED("T3")


    para(doc, "Of 509,800 records returned, 347 were eligible after title and abstract "
              "screening, and 50 were included in the qualitative synthesis after full-text "
              "assessment. The two-stage reduction is extreme, and the reasons are instructive. "
              "The search blocks combined broad terms such as \u201cnanoparticle*\u201d with "
              "equally broad terms such as \u201cseafood\u201d, which produces very large but "
              "mostly peripheral retrieval dominated by materials-science and pharmacology "
              "literature; the eligible fraction therefore reflects the specificity of the "
              "eligibility criteria rather than the exhaustiveness of the search. The reduction "
              "from 347 to 50 was driven principally by absence of a marine or seafood "
              "dimension, absence of any ENP exposure or occurrence measurement, and absence of "
              "a biological, dietary or risk-assessment outcome. Figure 2, presented with the "
              "figures at the end of the manuscript, gives the complete flow.", first_indent=0.0)
    _EMBED("F2")


    h2(doc, "Data extraction and synthesis", "2.3")

    para(doc, "Data were extracted into a structured template covering particle type, primary "
              "particle size, coating or surface modification, exposure medium and "
              "concentration, species and life stage, exposure route and duration, endpoint "
              "measured, tissue examined, analytical method and reported effect size. Included "
              "studies were grouped by evidence type: environmental fate and monitoring, "
              "organism-level toxicology, seafood occurrence, trophic transfer, dietary "
              "exposure, aquaculture, and regulatory assessment. Because heterogeneity in "
              "nanoparticle type, coating, size, exposure medium, species, endpoint and duration "
              "prevented formal meta-analysis, findings were synthesized narratively and "
              "quantitative results were reported as ranges rather than pooled estimates.",
         first_indent=0.0)

    para(doc, "Evidence strength was assessed qualitatively against four criteria: replication "
              "across independent research groups; consistency of biological endpoints across "
              "taxa and study designs; environmental realism of the exposure concentrations "
              "relative to measured or modelled field levels; and direct relevance to edible "
              "seafood tissues rather than to laboratory model systems alone. Each claim in the "
              "synthesis was assigned an evidence strength of strong, moderate, low to moderate, "
              "or weak on the basis of how many of these criteria were satisfied. This scheme is "
              "deliberately conservative: a claim supported by many studies that all use "
              "unrealistically high doses cannot be rated strong, because the criterion of "
              "environmental realism fails regardless of replication.", first_indent=0.0)

    h2(doc, "Analytical methods review", "2.4")

    para(doc, "Because the interpretive limits of the field are set largely by measurement, a "
              "dedicated methods synthesis was conducted alongside the substantive review. "
              "Studies reporting ENP detection in seafood or marine matrices were assessed for "
              "sample preparation strategy, particle-extraction efficiency, calibration "
              "approach, size-detection limit, use of orthogonal confirmation, and availability "
              "of certified reference materials. This synthesis is presented in Section 4 and "
              "informs the interpretation of every occurrence estimate discussed subsequently "
              "It is not a methodological appendix: the inability to distinguish engineered from "
              "natural particles is a substantive scientific finding, and it constrains the "
              "conclusions that can be drawn from the occurrence literature irrespective of how "
              "carefully that literature is assembled.", first_indent=0.0)
