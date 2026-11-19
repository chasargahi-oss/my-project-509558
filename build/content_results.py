"""Results."""
from docx.shared import Pt
from docx_style import para, rich, h1, h2, h3

U = "\u00b5"
SUP2 = "\u2082"


def results(doc):
    h1(doc, "Results", 3)

    h2(doc, "Character of the included evidence", "3.1")

    para(doc, "The 50 included studies spanned environmental fate and monitoring, marine "
              "ecotoxicology, seafood occurrence, trophic transfer, dietary exposure, "
              "aquaculture applications and risk assessment. Their distribution is heavily "
              "skewed (Figure 3a). Bivalve and invertebrate toxicology accounts for the largest "
              "share, followed closely by fish toxicology and environmental fate and monitoring. "
              "Seafood occurrence studies, trophic-transfer experiments, dietary-exposure "
              "assessments and aquaculture studies together constitute less than half the "
              "corpus, and the number of studies that connect an environmental measurement to a "
              "food-safety outcome is smaller still. This distribution is the single most "
              "important structural feature of the evidence base, because it means that the "
              "literature is dense where the question is mechanistic and thin where the "
              "question is regulatory.", first_indent=1.0)
    _EMBED("F3")

    para(doc, "The strongest evidence base concerns bivalve molluscs, particularly mussels "
              "(Mytilus spp.), clams (Ruditapes and Scrobicularia spp.), scallops (Chlamys "
              "farreri) and cockles. These species are simultaneously ecologically important "
              "filter feeders and commercially relevant commodities, which makes them unusually "
              "efficient objects of study: a finding of accumulation in a mussel is "
              "simultaneously an ecological observation and a food-safety observation. The same "
              "efficiency does not extend to fish, where muscle tissue is the dietary endpoint of "
              "interest but the toxicological literature concentrates on gill, liver and brain, "
              "and it extends least of all to crustaceans, cephalopods and seaweeds, which are "
              "commercially significant in many markets but almost absent from the ENP "
              "literature.", first_indent=0.0)


    para(doc, "Four evidence streams organize the remainder of this section: environmental fate "
              "and monitoring (Section 3.2); uptake, accumulation and trophic transfer (Section "
              "3.3); occurrence in commercial seafood and dietary exposure (Sections 3.4 and "
              "3.5); and ecotoxicological effects, including aquaculture (Sections 3.6 and "
              "3.7). Each stream is reported on its own terms before being integrated in the "
              "Discussion.", first_indent=0.0)

    # ---------------------------------------------------------------- 3.2
    h2(doc, "Sources, environmental fate and measured concentrations", "3.2")

    para(doc, "ENPs reach coastal systems from both diffuse and point sources. Wastewater "
              "effluent, stormwater runoff, sunscreen and cosmetic residues, antifouling "
              "coatings, industrial discharge and aquaculture-related releases are the pathways "
              "most consistently identified across the reviewed literature (Batley et al., 2013; Nowack & Bucheli, 2007). Their relative "
              "importance varies with material: TiO\u2082 is dominated by diffuse use in paints, "
              "coatings, cosmetics and food, whereas Ag is concentrated in antimicrobial "
              "applications and textiles, and ZnO in sunscreens, rubber and feed additives. "
              "Because the production volumes and use patterns of these materials differ by an "
              "order of magnitude or more, so do their predicted environmental concentrations.",
         first_indent=1.0)
    _EMBED("T4")

    para(doc, "Once in seawater, ENPs undergo rapid physical and chemical transformation "
              "(Table 4). High ionic strength compresses the electrical double layer, reducing "
              "electrostatic repulsion and promoting hetero-aggregation with natural organic "
              "matter and mineral colloids; the resulting aggregates settle, moving particles "
              "from the water column into sediment. This is a food-safety relevant redistribution "
              "rather than a removal, because the benthic and filter-feeding organisms that "
              "dominate shellfish production are precisely those exposed to settled material. "
              "Sediment-bound particles can also be resuspended by storms, trawling and "
              "bioturbation, creating episodic exposure in the water column long after the "
              "original release (Hochella et al., 2019).", first_indent=0.0)


    para(doc, "Dissolution is the second decisive process, and it is the one most often "
              "underweighted in food-safety discussion. For ZnO in particular, toxicity to the "
              "marine diatom Thalassiosira pseudonana has been attributed essentially entirely "
              "to released Zn\u00b2\u207a, with dissolution accelerated in seawater relative to "
              "freshwater because of chloride complexation and pH effects (Miao et al., 2010). Once dissolution is "
              "complete, the particle-specific hazard has become an ionic-metal hazard, for "
              "which conventional toxicological frameworks and, in the case of zinc, nutritional "
              "context already exist. A review that reports only particle concentrations without "
              "the dissolved fraction therefore reports an incomplete exposure. The "
              "methodological corollary \u2014 that spICP-MS should report both \u2014 has been "
              "adopted by the most rigorous seafood studies and should become standard.",
         first_indent=0.0)

    para(doc, "Not all particles settle. Extracellular polymeric substances released during "
              "algal blooms can stabilize nanoparticles in suspension, at least transiently, and "
              "natural organic matter can either promote or retard aggregation depending on "
              "coating, ionic composition and pH. The consequence is episodic water-column "
              "bioavailability superimposed on a general sedimentation trend, which matters for "
              "planktonic larvae and for filter feeders that graze on suspended material (Abbas et al., 2020). "
              "Predicting exposure from annual-average release estimates alone will therefore "
              "systematically understate exposure during bloom conditions and following "
              "resuspension events.", first_indent=0.0)

    para(doc, "Measured environmental concentrations are sparse, and this sparsity is itself a "
              "finding. Where single-particle measurements exist, they show strong gradients with "
              "proximity to anthropogenic sources. In a systematic survey of Laizhou Bay, China, "
              "Ti-based particles dominated both seawater and sediment, followed by Zn-, Ag-, Cu- "
              "and Au-based particles, with the highest water-column abundances near the Yellow "
              "River estuary and generally smaller particle sizes in sediment than in the "
              "overlying water (Li et al., 2023). Reported seawater abundances reached 1.78 \u00d7 10\u2078 particles "
              "L\u207b\u00b9 for Ti-based particles and 1.27 \u00d7 10\u2078 particles L\u207b\u00b9 for "
              "Zn-based particles (Figure 4a). Mass-based concentrations of metal-bearing "
              "nanoparticles in anthropogenically influenced coastal waters have been reported in "
              "the range of 0.1\u20131.0 " + U + "g L\u207b\u00b9 for several elements, declining "
              "offshore (Li et al., 2023).", first_indent=0.0)
    _EMBED("F4")


    para(doc, "Risk characterization ratios calculated for that bay provide one of the few "
              "attempts to move from concentration to risk in a marine setting (Li et al., 2023). Using predicted "
              "no-effect concentrations derived from engineered-particle toxicity data, Ag-based "
              "particles were assigned the lowest PNEC (72.8 ng L\u207b\u00b9), followed by ZnO "
              "(2.66 " + U + "g L\u207b\u00b9), CuO (7.83 " + U + "g L\u207b\u00b9) and TiO\u2082 "
              "(72.0 " + U + "g L\u207b\u00b9). One station near the Yellow River estuary was "
              "classified as high risk for both Ag- and Ti-based particles, with risk "
              "characterization ratios of 1.73 and 1.66 respectively, and combined RCR values "
              "identified one high-risk, twenty medium-risk and one low-risk station out of "
              "twenty-two. Two caveats travel with these numbers and should travel with any "
              "citation of them: the PNECs were derived from engineered-particle toxicity data "
              "and applied to particles of unknown origin, and the authors themselves noted that "
              "the true risk is likely lower once transformation and the presence of natural "
              "particles are accounted for (Li et al., 2023).", first_indent=0.0)

    para(doc, "Modelled environmental concentrations for many engineered nanomaterials remain "
              "below predicted no-effect concentrations under average conditions, and that "
              "conclusion has been reached repeatedly across a decade of modelling and "
              "monitoring work. It should not be read as reassurance. Average conditions are "
              "constructed precisely by averaging away the point sources, outfalls, harbours and "
              "aquaculture facilities where exposure is concentrated, and those are the locations "
              "where shellfish beds and farms are sited. The relevant quantity for seafood safety "
              "is the localized and episodic exposure distribution, not the regional mean, and "
              "the monitoring network required to characterize that distribution does not yet "
              "exist.", first_indent=0.0)

    # ---------------------------------------------------------------- 3.3
    h2(doc, "Uptake, bioaccumulation and trophic transfer", "3.3")

    para(doc, "Marine organisms encounter ENPs through four routes: direct waterborne uptake "
              "across gill or body surfaces; ingestion of contaminated particles or prey; "
              "contact with contaminated sediment; and filter feeding, which combines the first "
              "three by concentrating particulate material from large water volumes. In bivalves, "
              "particles are trapped in gill mucus and transported to the digestive gland, where "
              "lysosomal uptake, oxidative stress and DNA damage have been reported. In fish, "
              "uptake occurs principally via the gut following drinking, with additional "
              "contributions from gill mucus and, for small or dissolved fractions, direct "
              "branchial transfer (Baker et al., 2014; Canesi et al., 2012). Table 5 summarizes the evidence by species group.",
         first_indent=1.0)
    _EMBED("T5")


    para(doc, "Quantitative evidence of accumulation in commercially farmed shellfish comes from "
              "a single but unusually informative study. In oysters, mussels, scallops, clams and "
              "ark shells sampled from an offshore aquaculture farm, Ti-, Cu-, Zn- and "
              "Ag-bearing nanoparticles were detected in all five species, with mean diameters of "
              "65.4\u201370.9, 72.2\u201389.6, 97.8\u2013108.3 and 42.9\u201351.0 nm respectively. "
              "Particle-number concentrations in tissue (0.88\u20133.26 \u00d7 10\u2077 particles "
              "g\u207b\u00b9 fresh weight) exceeded those in the surrounding seawater "
              "(0.46\u20130.79 \u00d7 10\u2077 particles mL\u207b\u00b9), which is the numerical "
              "signature of bioaccumulation. All four particle types accumulated preferentially "
              "in gill and digestive gland, and all four reached adductor muscle (Xu et al., 2020). Silver-bearing "
              "particles had the highest number-based bioconcentration factors, attributable to "
              "their smallest mean diameter in seawater (30.5 nm), and clams showed the lowest "
              "bioconcentration factors of the four particle types. That inverse relationship "
              "between size and accumulation efficiency is consistent with the broader "
              "literature and has a practical implication: the particle-size distribution, not "
              "the total elemental concentration, governs accumulation (Xu et al., 2020).", first_indent=0.0)

    para(doc, "Trophic transfer has been demonstrated in controlled marine food chains, and the "
              "demonstrations are more specific than the general claim that ENPs biomagnify. In "
              "a microalga\u2013scallop system, TiO\u2082 nanoparticles transferred from the diatom "
              "Nitzschia closterium to the scallop Chlamys farreri (Wang et al., 2017). Tissue burdens were higher "
              "after aqueous exposure than after dietary exposure, which is an important "
              "qualification: the dietary route was demonstrably operative but was not the "
              "dominant one. Transmission electron microscopy with energy-dispersive X-ray "
              "analysis confirmed TiO\u2082 nanoparticles in digestive-gland nuclei irrespective of "
              "exposure route, establishing that particles can not only be ingested but can reach "
              "intracellular compartments. Lysosomal membrane destabilization, DNA damage and "
              "histopathological effects accompanied the accumulation (Wang et al., 2017).", first_indent=0.0)

    para(doc, "The counter-example is equally instructive. CeO\u2082 nanoparticles transferred from "
              "clamworm (Perinereis aibuhitensis) to juvenile turbot (Scophthalmus maximus) (Yin et al., 2025), and "
              "Ce concentrations in turbot increased with the accumulated burden in the prey. "
              "But biomagnification did not occur along this food chain, and the particles "
              "underwent biotransformation from Ce(IV) to Ce(III) during transfer. The "
              "consequences were nevertheless food-relevant: CeO\u2082 accumulated in muscle, "
              "reduced crude protein, total amino acid and delicious amino acid contents, and "
              "altered texture, with the deterioration attributed to muscle metabolic disturbance "
              "and intestinal dysbiosis along a gut\u2013muscle axis. Approximately 3.73% of the "
              "administered Ce reached muscle. This study matters for two reasons. It shows that "
              "biomagnification is not a general property of ENPs \u2014 a point frequently lost in "
              "secondary citation \u2014 and it shows that seafood quality can be affected through "
              "mechanisms that have nothing to do with metal toxicity as conventionally "
              "measured (Yin et al., 2025).", first_indent=0.0)

    para(doc, "Taken together, these results support a carefully bounded conclusion: ENP "
              "movement through marine food webs is plausible, demonstrated in specific systems, "
              "and highly context-dependent. Particle identity, size, coating, dissolution "
              "behaviour, feeding strategy, gut retention time and environmental conditions all "
              "influence whether exposure leads to accumulation, clearance or trophic "
              "amplification. The evidence does not support a general claim that ENPs "
              "biomagnify, and it does support the narrower claim that they can transfer from "
              "primary producers to consumers and reach intracellular compartments in edible "
              "tissues (Corsi et al., 2014; Rocha et al., 2015).", first_indent=0.0)

    # ---------------------------------------------------------------- 3.4
    h2(doc, "Occurrence in commercial seafood", "3.4")

    para(doc, "The most direct evidence that ENPs reach consumers comes from spICP-MS "
              "measurements of processed seafood. TiO\u2082 nanoparticles smaller than 100 nm were "
              "detected in every canned seafood sample tested across four product categories, "
              "with the highest mean concentration in canned clam (0.112 mg kg\u207b\u00b9) and "
              "progressively lower means in canned tuna (0.038 mg kg\u207b\u00b9), anchovy "
              "(0.009 mg kg\u207b\u00b9) and mackerel (0.009 mg kg\u207b\u00b9) (Figure 5a). "
              "Nanoparticles constituted between 32% and 59% of the total TiO\u2082 particle "
              "fraction depending on product, and mean nanoparticle diameters ranged from 72 nm "
              "in canned tuna to 89 nm in canned anchovy and clam (Grasso et al., 2020).", first_indent=1.0)
    _EMBED("F5")

    para(doc, "A detail in that study deserves emphasis because it bears directly on source "
              "attribution. None of the products examined declared E171 on the label, which "
              "indicates that titanium dioxide was not intentionally added as a colorant during "
              "processing. The detected titanium therefore reflects either environmental "
              "bioaccumulation by the organism, contamination in the industrial processing "
              "environment, or migration from packaging, and the study could not apportion "
              "between these. The authors noted that the longest-lived and largest-bodied "
              "organisms (tuna and mackerel) carried smaller-diameter particles and a higher "
              "nanoparticle fraction than the small pelagic fish and clam, and interpreted this "
              "as consistent with preferential retention of smaller particles \u2014 but "
              "explicitly did not claim biomagnification (Grasso et al., 2020).", first_indent=0.0)

    para(doc, "Silver nanoparticles were quantified in canned anchovy, clam, mackerel and tuna, "
              "with mean diameters of 31\u201336 nm and modal diameters of 26\u201328 nm, and with "
              "particle-number concentrations of the order of 10\u2077 particles g\u207b\u00b9. "
              "Nanoparticulate Ag mass concentrations were very low "
              "(0.0004\u20130.0028 mg kg\u207b\u00b9), and dissolved Ag exceeded nanoparticle Ag in "
              "every product category: dissolved Ag means were 0.0455 mg kg\u207b\u00b9 in tuna, "
              "0.0245 mg kg\u207b\u00b9 in mackerel, 0.0406 mg kg\u207b\u00b9 in anchovy and "
              "0.0148 mg kg\u207b\u00b9 in clam. Packaging was examined by scanning electron "
              "microscopy with energy-dispersive X-ray analysis to test whether the can lining "
              "was a source, and Ag was not detected in the packaging polymer at the points "
              "sampled. The authors concluded that seafood is a plausible uptake route for "
              "Ag-NPs but that nanoparticle-associated Ag contributes only a small fraction of "
              "total Ag intake from these products (Grasso et al., 2021).", first_indent=0.0)

    para(doc, "ZnO nanoparticles were detected in canned seafood at 0.003\u20130.010 mg kg\u207b\u00b9 "
              "with mean diameters of 61.3\u201378.6 nm. Molluscs showed slightly higher "
              "concentrations and larger particle sizes than fish products, but the study did not "
              "find a clear bioaccumulation trend by trophic level or species size, and the "
              "authors framed the finding in terms of a balance between the nutritional benefit "
              "of zinc and the unresolved hazard of the nanoparticulate form (Grasso et al., 2022). Table 6 summarizes "
              "reported occurrence across the three materials, and Figure 5b sets "
              "particle-associated intake against dissolved-metal intake from the same meal.",
         first_indent=0.0)
    _EMBED("T6")



    para(doc, "Three interpretive limits apply to the whole occurrence literature, and they are "
              "severe enough to constrain what can be claimed. First, detection of a metal in "
              "nanoparticle form does not establish that the particle was engineered. Natural "
              "titanium-bearing minerals, food-processing artifacts, packaging interactions and "
              "analytical uncertainty all complicate source attribution, and no study in the "
              "reviewed corpus resolved this question for seafood. Second, the matrices examined "
              "are narrow: canned products dominate the quantitative evidence, and findings for "
              "canned tuna, mackerel, anchovy and clam cannot be generalized to fresh fish, "
              "farmed seafood, wild-caught shellfish or other markets without further "
              "measurement. Third, the reported concentrations are means of samples drawn from "
              "specific brands and batches in a single national market, and between-brand and "
              "between-season variability was not characterized (Grasso et al., 2020, 2021, 2022).", first_indent=0.0)

    # ---------------------------------------------------------------- 3.5
    h2(doc, "Dietary exposure estimates", "3.5")

    para(doc, "Dietary-exposure estimates are preliminary but provide the essential bridge "
              "between occurrence data and human-health risk assessment. Using measured "
              "concentrations, meal sizes of 227 g for adults and 114 g for children, and body "
              "weights of 70 kg and 16 kg respectively, the estimated intake of ZnO nanoparticles "
              "from a single seafood meal was 0.010\u20130.031 " + U + "g kg\u207b\u00b9 body weight "
              "for adults and 0.022\u20130.067 " + U + "g kg\u207b\u00b9 for children. Comparable "
              "single-meal estimates for TiO\u2082 nanoparticles ranged from 0.007 to "
              "0.455 " + U + "g kg\u207b\u00b9 for adults, with the highest values from clam "
              "meals. For Ag, nanoparticle-associated intake was negligible in absolute terms "
              "because nanoparticle Ag represented such a small fraction of total Ag (Grasso et al., 2020, 2021, 2022).",
         first_indent=1.0)
    _EMBED("T7")

    para(doc, "These figures are low, and their lowness is frequently cited as a reason for "
              "reassurance. That inference is not warranted, for a reason that is logical rather "
              "than empirical. Converting an intake estimate into a risk characterization "
              "requires a health-based guidance value \u2014 a reference dose, acceptable daily "
              "intake or tolerable weekly intake \u2014 and no such value exists for any of the "
              "seafood-relevant ENPs. Without it, an intake cannot be converted into a hazard "
              "quotient, a margin of exposure or an acceptable-daily-intake percentage. The "
              "absence of a reference value is therefore not evidence of safety; it is evidence "
              "that the risk-assessment framework is incomplete at precisely the step that "
              "matters. Table 7 sets out the components of a complete dietary-risk assessment "
              "and the current status of each.", first_indent=0.0)


    para(doc, "The second feature of the exposure estimates is the magnitude of the "
              "particle-versus-dissolved distinction. For ZnO, dissolved zinc intake from a "
              "mollusc meal was estimated at 109.3 " + U + "g kg\u207b\u00b9 body weight for "
              "adults and 240.1 " + U + "g kg\u207b\u00b9 for children, against particle-associated "
              "intakes of 0.010\u20130.031 and 0.022\u20130.067 " + U + "g kg\u207b\u00b9 "
              "respectively \u2014 a difference of three to four orders of magnitude "
              "(Figure 5b). This does not establish that dissolved zinc is more hazardous; zinc "
              "is an essential nutrient, and the dissolved fraction includes the nutritional "
              "content of the meal. It does establish that total elemental concentration cannot "
              "stand as a proxy for nanoparticle-specific exposure, and that any exposure "
              "assessment which reports only the elemental total will mis-specify the hazard it "
              "purports to describe.", first_indent=0.0)

    para(doc, "Children receive higher intake per unit body weight because they consume less "
              "food overall but may eat similar or larger portions relative to body mass, and "
              "this pattern is consistent across the TiO\u2082 and ZnO estimates. Children are "
              "therefore a plausibly more sensitive subgroup for exposure-based risk assessment. "
              "Whether they are more sensitive on the hazard side depends on absorption, "
              "metabolism, developmental stage and mode of action, none of which has been "
              "characterized for seafood-derived ENP exposure. A further unresolved issue is "
              "aggregation of exposure across sources: seafood is one route among several, and "
              "food additives, packaging migration, drinking water and other incidental "
              "exposures may contribute substantially to total nanoparticle intake. No study in "
              "the corpus attempted a total-diet aggregate exposure estimate for ENPs.",
         first_indent=0.0)

    # ---------------------------------------------------------------- 3.6
    h2(doc, "Ecotoxicological effects", "3.6")

    para(doc, "Laboratory studies consistently show that metal and metal-oxide ENPs can induce "
              "sublethal toxicity in marine organisms. The most frequently reported endpoints "
              "are oxidative stress, lysosomal membrane destabilization, DNA damage, immune "
              "modulation, altered energy metabolism, developmental impairment and behavioural "
              "change (Table 8). A synthesis of 134 ecotoxicological studies of metal ENPs in "
              "marine fauna found that Ti-, Zn-, Cu- and Ag-based nanoparticles were the most "
              "frequently studied and that molluscs \u2014 especially bivalves \u2014 were the "
              "predominant taxonomic focus, with toxicity depending on concentration, exposure "
              "duration, particle characteristics and sampled tissue (Roma et al., 2020).", first_indent=1.0)
    _EMBED("T8")


    para(doc, "The mechanistic literature is strongest where it separates particle-specific "
              "from dissolved-ion effects, and that separation frequently changes the "
              "interpretation. For ZnO, toxicity to Thalassiosira pseudonana was attributed "
              "essentially entirely to dissolved Zn\u00b2\u207a, with an IC\u2085\u2080 of "
              "approximately 0.39 " + U + "M in one series (Miao et al., 2010). In mussels, prolonged exposure to ZnO "
              "nanoparticles reduced growth and survival, but at concentrations substantially "
              "above those generally measured in ambient seawater, and long-term exposure altered "
              "the organism's energy budget \u2014 an effect that is sublethal but ecologically "
              "consequential, because energy allocation governs growth and reproduction (Hanna et al., 2013). For CuO, "
              "behavioural impairment and oxidative-stress responses were reported in the deposit-"
              "feeding bivalve Scrobicularia plana at copper concentrations of 10 " + U + "g "
              "L\u207b\u00b9, closer to environmentally relevant levels; the same study found no "
              "additional labile copper in the exposure medium, indicating that particle-"
              "associated effects can occur without measurable dissolution, although separating "
              "the two mechanisms remains analytically difficult (Buffet et al., 2011).", first_indent=0.0)

    para(doc, "The distinction matters because the two mechanisms imply different regulatory "
              "responses. If toxicity is ionic, existing water-quality criteria for dissolved "
              "metals provide a defensible basis for management, and the nanoparticle is "
              "principally a delivery mechanism for a known toxicant. If toxicity is genuinely "
              "particle-specific \u2014 arising from surface reactivity, shape, or intracellular "
              "localization that dissolved ions cannot achieve \u2014 then existing criteria are "
              "inapplicable and new benchmarks are required. The literature supports both "
              "mechanisms operating simultaneously and in material-specific proportions, which "
              "is the least convenient possible answer for risk assessment because it rules out "
              "a single harmonized approach (Balbi et al., 2014; Lead et al., 2018).", first_indent=0.0)

    para(doc, "A recurring interpretive problem is the concentration gap. Many mechanistic "
              "experiments use milligram-per-litre exposures, whereas environmental measurements "
              "are typically in the nanogram- to low-microgram-per-litre range, and the "
              "difference between the two is commonly one to three orders of magnitude. "
              "Figure 7 makes the separation explicit. Effects observed at high experimental "
              "doses therefore cannot be assumed to occur at environmentally relevant exposures, "
              "and the reverse inference \u2014 that because effects are absent at "
              "environmentally relevant doses no hazard exists \u2014 is equally unsafe, because "
              "chronic low-dose exposure over a lifetime is not well represented by acute "
              "high-dose experiments. The gap is a limitation on inference in both directions (Batley et al., 2013; Corsi et al., 2014).",
         first_indent=0.0)
    _EMBED("F7")



    # ---------------------------------------------------------------- 3.7
    h2(doc, "Aquaculture applications and unintended release", "3.7")

    para(doc, "Nanotechnology is used or investigated in aquaculture for antimicrobial "
              "purposes, feed supplementation, water treatment, drug delivery, disease "
              "diagnostics and environmental sensing. At low experimental doses, some "
              "nanoparticles have been associated with improved feed conversion, antioxidant "
              "enzyme activity and non-specific immune responses, and a substantial applied "
              "literature examines these benefits in species of commercial interest. At higher "
              "doses the same materials can produce oxidative stress, tissue accumulation and "
              "histopathological damage (Khosravi-Katuli et al., 2017).", first_indent=1.0)

    para(doc, "The aquaculture evidence base is asymmetric in a way that has direct "
              "food-safety consequences. There is growing interest in applications and a "
              "reasonable body of laboratory work on benefits and toxicity, but very little "
              "field-scale evidence quantifying nanoparticle release, environmental persistence, "
              "contamination of cultured organisms, or production losses under commercial "
              "operating conditions. Nanoparticle-containing feeds, therapeutics, coatings and "
              "discharge water could each introduce ENPs into receiving environments or into the "
              "cultured product itself, and the relative importance of these routes is unknown. "
              "The same properties that make nanoparticles useful in aquaculture \u2014 small "
              "size, high reactivity, antimicrobial activity \u2014 are those that raise "
              "ecological concern if released, which means that the sector's growth is also a "
              "growth in potential exposure. This is a case in which the absence of evidence of "
              "harm reflects the absence of measurement rather than the absence of a "
              "mechanism.", first_indent=0.0)

    # ---------------------------------------------------------------- 3.8
    h2(doc, "Detection and analytical methods", "3.8")

    para(doc, "Detecting ENPs in seawater, sediment and seafood is analytically demanding "
              "because target particles occur at very low concentrations within complex "
              "biological and mineral matrices. Seafood tissue contains salts, proteins, lipids, "
              "pigments, natural mineral particles and endogenous metals, each of which can "
              "interfere with particle separation, identification and quantification. In "
              "seawater, the high chloride content and ionic strength add further difficulties, "
              "including spectral and non-spectral interferences and rapid dissolution of some "
              "materials during sample handling (Laycock et al., 2022).", first_indent=1.0)

    para(doc, "Single-particle ICP-MS is the most important quantitative technique currently "
              "available for metal-containing ENPs in environmental and food matrices. In "
              "spICP-MS, a dilute sample suspension is introduced into the plasma so that, under "
              "appropriate dilution and dwell-time conditions, individual particles generate "
              "discrete ion clouds and produce time-resolved signal pulses above the dissolved "
              "background. Pulse frequency yields particle-number concentration, while pulse "
              "intensity yields particle mass and, with assumptions about composition, density "
              "and shape, diameter. The technique's strengths are high sensitivity, elemental "
              "specificity, high throughput, and the ability to report dissolved and "
              "particle-associated metal from a single acquisition with minimal sample "
              "perturbation (Table 9).", first_indent=0.0)
    _EMBED("T9")

    para(doc, "Its limitations are equally consequential. spICP-MS measures elemental "
              "composition rather than identifying a nanomaterial, and it cannot reliably "
              "distinguish particles below its size-detection limit from dissolved ions or small "
              "complexes. Converting pulse intensity into diameter requires assumptions about "
              "density, shape and composition that may be inappropriate for rods, plates, "
              "aggregates or coated particles, and those assumptions introduce substantial "
              "uncertainty in complex food matrices. Agglomerates and aggregates are not "
              "resolved, so aggregation can reduce apparent particle number while increasing "
              "apparent particle size \u2014 simultaneously lowering and raising different "
              "exposure metrics. Carbon-based and polymeric particles are generally unsuitable "
              "for the technique because they are destroyed during digestion and carbon is "
              "poorly ionized. A systematic review of spICP-MS applied to biological samples "
              "concluded that methodological effort has concentrated on a small number of "
              "compositions and that important tissues remain unstudied (Laycock et al., 2022).", first_indent=0.0)


    para(doc, "Because spICP-MS is an elemental screening and quantification technique, "
              "confirmation requires complementary methods. Transmission and scanning electron "
              "microscopy can visualize individual particles, determine morphology, assess "
              "aggregation state and, coupled with energy-dispersive X-ray spectroscopy, provide "
              "elemental composition; electron microscopy is widely regarded as a reference "
              "method for particle-size determination but is slower, less sensitive and less "
              "routinely available in food-control laboratories. Asymmetric-flow field-flow "
              "fractionation coupled to ICP-MS separates particles by size before elemental "
              "detection and is useful for characterizing size fractions and particle "
              "associations, though particle losses to membranes and operator expertise constrain "
              "throughput. Raman and Fourier-transform infrared spectroscopies are more relevant "
              "to carbon-based particles and nanoplastics than to routine quantification of "
              "metal-containing ENPs. Table 10 compares the available methods.", first_indent=0.0)
    _EMBED("T10")


    para(doc, "Sample preparation is a major determinant of analytical validity, and it is the "
              "stage at which most studies are least well controlled. Seafood tissues commonly "
              "require enzymatic, alkaline or acidic digestion to release particles from the "
              "biological matrix. Enzymatic digestion is the mildest and best preserves particle "
              "integrity but is slow and incompletely characterized for many matrices; alkaline "
              "digestion with tetramethylammonium hydroxide under ultrasound is the most widely "
              "used approach in the seafood literature and has been validated for TiO\u2082, Ag "
              "and ZnO; acidic digestion dissolves particles entirely and is suitable only for "
              "total-element determination, yet is sometimes used to confirm recovery. Digestion "
              "can alter particle size, promote aggregation or dissolution and destroy the "
              "original particle\u2013matrix relationship, so extraction conditions must be "
              "validated for each nanoparticle type and seafood matrix (Sun et al., 2022).", first_indent=0.0)

    para(doc, "Quality assurance requires procedural blanks, matrix spikes, recovery studies, "
              "replicate analyses and particle-size standards. The studies reviewed here report "
              "recoveries in the range of approximately 85\u2013115% and instrumental limits of "
              "detection in the low nanogram-per-millilitre range, which is adequate for the "
              "concentrations encountered. The decisive gap is not instrumental sensitivity but "
              "metrological traceability: certified reference materials and proficiency-testing "
              "materials for engineered nanoparticles in biological or food matrices are "
              "essentially unavailable. Without them, method trueness cannot be established at "
              "environmentally relevant concentrations, and interlaboratory comparability cannot "
              "be demonstrated. This is the single most important unmet need in the analytical "
              "domain, and it is a precondition for any harmonized monitoring programme (Laycock et al., 2022).",
         first_indent=0.0)

    para(doc, "The analytical limitations have direct consequences for risk assessment, and "
              "they propagate through every downstream inference. Occurrence data may "
              "overestimate or underestimate ENP exposure if extraction alters particle "
              "integrity or if naturally occurring particles are misclassified as engineered. "
              "Particle-size estimates depend on assumptions about shape and density that are "
              "rarely tested for the material in question. Aggregation, which is the norm rather "
              "than the exception in seawater and in digested food matrices, is not resolved and "
              "therefore distorts both number and size metrics. And the absence of reference "
              "materials means that systematic bias between laboratories cannot be detected. For "
              "these reasons, current seafood measurements should be interpreted as "
              "screening-level evidence of nanoparticle occurrence rather than as definitive "
              "proof of engineered-particle identity or human-health hazard. Table 11 specifies "
              "the minimum evidence that would be required to support a defensible "
              "seafood-safety finding, and Figure 6 summarizes the workflow that would generate "
              "it.", first_indent=0.0)
    _EMBED("T11")
    _EMBED("F6")


    para(doc, "Figure 8 converts these requirements into a four-step decision framework for "
              "interpreting a positive detection. The sequence is deliberately ordered by "
              "evidentiary cost: each step is a precondition for the next, and a negative answer "
              "at any step changes the appropriate conclusion rather than merely lowering "
              "confidence. A signal that fails the first test is a dissolved-metal measurement "
              "and should be reported as total element. A particle that passes morphological "
              "confirmation but cannot be distinguished from natural or processing-derived "
              "particles remains provisional occurrence data. A particle that is not "
              "bioaccessible after digestion shifts the hazard assessment to the released ion. "
              "And a particle that is bioaccessible but lacks chronic oral-toxicity data cannot "
              "be risk-characterized at all. Only when all four tests are passed does a margin "
              "of exposure become calculable \u2014 which, at present, no seafood-relevant ENP "
              "achieves.", first_indent=0.0)
    _EMBED("F8")

