"""
SINGLE SOURCE OF TRUTH — Certified Lean Six Sigma Black Belt (CLSSBB) Training.

Content is grounded in:
  * "WSQ - Dr. Alfred Ang - Certified Lean Six Sigma Black Belt (CLSSBB)
    Training - v21.pptx" — the original 388-slide trainer deck. Its teaching
    diagrams are imported into courseware/assets/diagrams/ and shown verbatim so
    formulas are reproduced exactly as the trainer taught them.
  * "Six Sigma: A Complete Step-by-Step Guide" — The Council for Six Sigma
    Certification (CSSC). The CSSC scopes the belts by chapter: Green Belt =
    Ch 1-24, BLACK BELT = the full guide plus advanced statistics and DFSS.
  * The Green Belt course (TGS-2025055775) — this course is built as the
    deliberate STEP UP from it and must not merely repeat it.

STEP UP FROM GREEN BELT — THE DESIGN RULE OF THIS COURSE
---------------------------------------------------------
The Green Belt LEADS a scoped project; the BLACK BELT leads a PORTFOLIO, owns the
advanced statistics, and MENTORS Green Belts. The Green Belt course already
teaches DMAIC end to end across 496 slides. Repeating that would produce a longer
Green Belt course, not a Black Belt one.

So this course is deliberately split:
    ~45%  DMAIC RECAP IN DEPTH — not a fast skim. Every phase is re-taught
          thoroughly, because the Black Belt must be able to MENTOR Green Belts
          through these tools, and you cannot coach what you only half-recall.
          The recap re-derives each tool from first principles, then adds the
          Black Belt's leadership vantage point on top.
    ~55%  BLACK BELT ONLY depth the Green Belt course does not teach at all:
              Measure  : attribute MSA / Kappa, destructive & nested gauge studies
              Analyze  : multiple regression, ANOVA, non-parametric tests,
                         multi-vari studies, model diagnostics
              Improve  : full & fractional factorial DOE, confounding, resolution,
                         response surface methodology, robust design
              Control  : CUSUM, EWMA, short-run and multivariate SPC
              Lead     : portfolio selection, change leadership, resistance,
                         financial benefits validation, mentoring Green Belts

THE CAPSTONE RUNS FROM DAY 1
-----------------------------
Learners do NOT wait until Day 5 to start a project. On Day 1 each learner selects
their OWN workplace process and charters it. EVERY subsequent lab advances that
same project by one artifact — charter, MSA study, regression model, DOE design,
control plan. Day 5 consolidates the accumulated artifacts into an A3 storyboard
and a formal presentation to a simulated steering committee. The labs ARE the
capstone, built one piece at a time.

Every artifact (PPT, LP, LG, LG.md, labs index) is generated from this module +
data_domainN.py so they stay 100% aligned.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Certified Lean Six Sigma Black Belt (CLSSBB) Training"
SHORT_TITLE  = "Certified Lean Six Sigma Black Belt (CLSSBB) Training"
COURSE_CODE  = "TGS-2024051900"
VERSION      = "v4"
VERSION_DATE = "23 September 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 5

# ------------------------------------------------------------------ TSC alignment (WSQ)
TSC_TITLE = "Quality Process Control"
TSC_CODE  = "ELE-QUA-5006-1.1"
TSC_ABILITIES = [
    "A1: Lead improvement projects to meet process performance requirements.",
    "A2: Establish project scope of work and resourcing based on organisational requirements.",
    "A3: Analyse process performance data using advanced statistical methods to identify root causes of variation.",
    "A4: Measure process performance against defined quality standards and validate the measurement system.",
    "A5: Recommend, pilot and control improvement actions to sustain process performance.",
]
TSC_KNOWLEDGE = [
    "K1: DMAIC methodology and the advanced Lean Six Sigma body of knowledge.",
    "K2: Advanced statistical tools, experimental design and problem-solving techniques for process improvement.",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Lead a Lean Six Sigma project portfolio — select, charter and govern projects aligned to business strategy (A1, A2).",
    "LO2: Validate measurement systems for continuous AND attribute data using Gage R&R and Kappa analysis (A4).",
    "LO3: Analyse process data using multiple regression, ANOVA, non-parametric tests and multi-vari studies (A3).",
    "LO4: Design, run and interpret experiments using full and fractional factorial DOE and response surface methods (A3, K2).",
    "LO5: Select, de-risk and pilot improvements, and validate financial benefits with Finance sign-off (A5).",
    "LO6: Sustain the gain using advanced SPC — CUSUM, EWMA, short-run and multivariate control charts (A5, K1).",
    "LO7: Lead change and mentor Green Belts through resistance, stakeholder management and tollgate governance (A1, K1).",
    "LO8: Deliver a capstone improvement project and present it to a steering committee (A1-A5, K1, K2).",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(num=0, code="00", phase="FOUNDATIONS",
         title="The Black Belt Role, Portfolio Selection & Your Capstone",
         subtitle="BB vs GB · Portfolio selection · Strategy alignment · COPQ · Capstone chartering · DMAIC at altitude",
         weighting="10%",
         concepts=[
            ("The Black Belt role", "The Green Belt leads one project; the Black Belt leads a portfolio, owns the statistics and mentors Green Belts."),
            ("Project portfolio selection", "Rank candidate projects on strategic fit, financial benefit, data availability and risk — say no to the rest."),
            ("Strategy alignment (Hoshin)", "Every project must trace up to a business objective, or it will lose its sponsor mid-flight."),
            ("Cost of Poor Quality at scale", "Roll COPQ up across a portfolio so the programme, not just the project, has a dollar figure."),
            ("The capstone project", "You choose YOUR workplace process on Day 1 and build it across every lab of this course."),
            ("Chartering your capstone", "Problem, goal, scope, business case, sponsor and team — written on Day 1, refined at every tollgate."),
            ("DMAIC at altitude", "A fast, assumed-knowledge recap of the five phases from the Black Belt's leadership vantage point."),
            ("Tollgate governance", "The Black Belt runs the tollgate; the sponsor decides go, adjust or kill at the end of each phase."),
         ]),
    dict(num=1, code="D", phase="DEFINE",
         title="Define at Black Belt Depth — Charter, Stakeholders & Change",
         subtitle="VOC recap · Advanced CTQ flowdown · Charter governance · Stakeholder & resistance analysis · Change leadership",
         weighting="12%",
         concepts=[
            ("VOC, affinity and Kano — in depth", "Re-derive VOC capture, affinity clustering and Kano classification in full — you must be able to teach these, not just use them."),
            ("CTQ trees — in depth", "Build the CTQ tree from need to driver to measurable requirement, with targets, specification limits and defect definitions."),
            ("CTQ flowdown", "Cascade a business-level Y down through sub-Ys to the process Xs a team can actually control."),
            ("Charter governance", "The charter is a living contract — re-baselined at each tollgate, not written once and filed."),
            ("Stakeholder analysis", "Map influence against support, then plan a specific move for every high-influence, low-support stakeholder."),
            ("Resistance management", "Resistance is data. Diagnose whether it is technical, political or cultural before responding."),
            ("Change leadership", "ADKAR and Kotter — Awareness, Desire, Knowledge, Ability, Reinforcement across the project life."),
            ("Communication planning", "Different audiences need different messages at different cadences — plan it, do not improvise."),
            ("Mentoring Green Belts", "The Black Belt coaches Green Belt project definition rather than doing it for them."),
         ]),
    dict(num=2, code="M", phase="MEASURE",
         title="Measure at Black Belt Depth — Advanced Measurement Systems",
         subtitle="MSA recap · Attribute MSA & Kappa · Nested & destructive gauge studies · Capability for non-normal data · Sampling strategy",
         weighting="16%",
         concepts=[
            ("Process mapping & VSM — in depth", "Re-derive SIPOC, swimlane maps, value stream maps, takt time and the eight wastes in full."),
            ("Data, sampling and sample size — in depth", "Data types, operational definitions, sampling schemes and sample size formulas re-derived from first principles."),
            ("Continuous Gage R&R — in depth", "Full treatment of accuracy, repeatability, reproducibility, linearity, stability and %study variation."),
            ("Yield, DPMO and capability — in depth", "Classic yield, FPY, RTY, DPU, DPO, DPMO, sigma level and baseline Cp/Cpk, worked end to end."),
            ("Attribute MSA", "When the measurement is a judgement (pass/fail, grade), Gage R&R does not apply — attribute agreement does."),
            ("Kappa analysis", "Cohen's and Fleiss' Kappa quantify inspector agreement beyond chance. Kappa >= 0.75 is acceptable."),
            ("Nested gauge studies", "When parts cannot be measured twice by every operator, the crossed study is invalid — nest it."),
            ("Destructive testing MSA", "If measuring destroys the part, use near-identical part pairs and a nested design."),
            ("Non-normal capability", "Cp/Cpk assume normality. For non-normal data, transform (Box-Cox) or fit the correct distribution."),
            ("Ppk vs Cpk", "Cpk uses within-subgroup variation; Ppk uses total variation. Reporting the wrong one flatters the process."),
            ("Sampling strategy at scale", "Stratified and rational subgrouping decide what the control chart can even detect later."),
         ]),
    dict(num=3, code="A", phase="ANALYZE",
         title="Analyze at Black Belt Depth — Advanced Statistical Analysis",
         subtitle="Hypothesis recap · Multiple regression · ANOVA · Non-parametric tests · Multi-vari studies · Model diagnostics",
         weighting="22%",
         concepts=[
            ("Variation, run charts and Pareto — in depth", "Common vs special cause, run chart patterns, stratification and Pareto analysis re-derived in full."),
            ("Fishbone and 5 Whys — in depth", "Cause-and-effect analysis by 5M+E, 5 Whys discipline and multi-voting — the tools you will coach Green Belts through."),
            ("Hypothesis testing — in depth", "H0/Ha formulation, alpha, p-values, confidence levels, test selection and Type I/II errors, worked thoroughly."),
            ("Simple regression & correlation — in depth", "Correlation coefficients, the regression line and the causation trap — the foundation multiple regression builds on."),
            ("Multiple regression", "Model Y against several Xs at once — the Green Belt's simple linear regression will not do here."),
            ("Model diagnostics", "R-squared adjusted, residual plots, multicollinearity (VIF) — a model that fits is not yet a model that is valid."),
            ("ANOVA", "Compare three or more group means in one test instead of inflating alpha with repeated t-tests."),
            ("Two-way ANOVA & interactions", "Two factors at once reveals interaction effects that one-factor-at-a-time analysis hides entirely."),
            ("Non-parametric tests", "Mann-Whitney, Kruskal-Wallis and Mood's median when the data will not meet normality assumptions."),
            ("Multi-vari studies", "Separate positional, cyclical and temporal variation before spending money hunting the wrong X."),
            ("Chi-square & contingency", "Test association between categorical variables — defect type against shift, line or supplier."),
            ("From statistics to story", "Translate a coefficient and a p-value into money, risk and a decision the sponsor can make."),
         ]),
    dict(num=4, code="I", phase="IMPROVE",
         title="Improve at Black Belt Depth — Design of Experiments",
         subtitle="Solution selection · Lean countermeasures · FMEA · Full & fractional factorial DOE · Confounding · RSM · Robust design",
         weighting="18%",
         concepts=[
            ("Solution generation & selection — in depth", "Brainstorming, brainwriting, benchmarking and weighted solution selection matrices, re-derived in full."),
            ("Lean countermeasures — in depth", "5S, poka-yoke, pull, JIT, Heijunka, Jidoka and standard work — the Lean toolkit taught thoroughly."),
            ("FMEA and RPN — in depth", "Severity, Occurrence and Detection scoring, RPN calculation and the re-scored post-mitigation FMEA."),
            ("Why DOE beats OFAT", "One-factor-at-a-time misses interactions and wastes runs. DOE varies factors together, by design."),
            ("Full factorial design", "2^k designs estimate every main effect and every interaction — the gold standard when runs are affordable."),
            ("Main effects & interaction plots", "Read the design: a non-parallel interaction plot means the effect of one X depends on another."),
            ("Fractional factorial design", "2^(k-p) designs screen many factors in few runs by deliberately trading away high-order interactions."),
            ("Confounding & resolution", "Resolution III, IV and V describe exactly what you gave up. Know it before you interpret the result."),
            ("Response surface methodology", "Once the vital few Xs are known, RSM finds the optimum settings, not just the significant factors."),
            ("Robust design (Taguchi)", "Set the process so it performs well despite noise you cannot control — not just on average."),
            ("Piloting and scale-up", "Confirm the DOE optimum holds in production before rolling it out across sites."),
         ]),
    dict(num=5, code="C", phase="CONTROL",
         title="Control at Black Belt Depth — Advanced SPC & Sustaining",
         subtitle="SPC recap · CUSUM · EWMA · Short-run charts · Multivariate SPC · Control plan governance · Financial validation · Handover",
         weighting="12%",
         concepts=[
            ("SPC and control charts — in depth", "Chart anatomy, control limits, chart selection (Xbar-R, Xbar-S, I-MR, p, np, c, u) and out-of-control rules, in full."),
            ("Capability and control plans — in depth", "Cp, Cpk, Pp, Ppk, control limits vs specification limits, control plans, SOPs and response plans re-derived."),
            ("Limits of Shewhart charts", "Shewhart charts are slow to detect small sustained shifts — which is exactly what a drifting process does."),
            ("CUSUM charts", "Cumulative sum charts accumulate small deviations, detecting a sustained 1-sigma shift far faster."),
            ("EWMA charts", "Exponentially weighted moving average — tunable memory, strong for small shifts and autocorrelated data."),
            ("Short-run SPC", "High-mix low-volume processes never gather 25 subgroups per part. Standardise and chart across parts."),
            ("Multivariate SPC", "When several correlated characteristics matter, Hotelling's T-squared beats several separate charts."),
            ("Control plan governance", "The Black Belt audits control plans across the portfolio — not just their own project."),
            ("Financial benefits validation", "Benefits are not real until Finance signs them. Hard, soft and cost-avoidance are booked differently."),
            ("Handover and closure", "Transfer to the process owner, verify sustained performance, then formally close and harvest the lessons."),
         ]),
    dict(num=6, code="CAP", phase="CAPSTONE",
         title="Capstone Project & Steering Committee Presentation",
         subtitle="A3 storyboard · Consolidating your DMAIC artifacts · Presenting to sponsors · Defending the analysis · Programme leadership",
         weighting="10%",
         concepts=[
            ("The A3 storyboard", "One page tells the whole project: background, current state, analysis, countermeasures, results, next steps."),
            ("Consolidating your artifacts", "Every lab from Day 1 produced one piece of your capstone — now assemble them into one narrative."),
            ("Telling the data story", "Lead with the business impact, support it with the statistics — never the other way round."),
            ("Presenting to a steering committee", "Sponsors want the decision, the risk and the money in the first two minutes."),
            ("Defending the analysis", "Expect challenge on sample size, assumptions and confounding — prepare the evidence for each."),
            ("Handover and sustainability", "Show who owns the process now, how it is monitored, and what triggers escalation."),
            ("Lessons learned", "Harvest what transfers to the next project and to the Green Belts you will mentor."),
            ("Your Black Belt journey", "Certification, project logging, mentoring obligations and continuing practice."),
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "The Black Belt role, portfolio selection, capstone chartering and Define",
    2: "Measure — advanced measurement systems, attribute MSA and capability",
    3: "Analyze — multiple regression, ANOVA, non-parametric and multi-vari",
    4: "Improve and Control — DOE, RSM and advanced SPC",
    5: "Capstone project consolidation and steering committee presentation",
}

# ------------------------------------------------------------------ assessment
# The WSQ assessment is the Written Assessment (SAQ) + Case Study (CS), matching
# the papers registered on the LMS/Drive. The capstone project and its steering
# committee presentation are an ADDITIONAL course deliverable on top of that.
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 2 questions, 1 hour, open book (K1, K2).",
    practical="Case Study (CS) — an applied DMAIC case study, 90 minutes, open book (A1-A5).",
    capstone="Capstone Project & Presentation — an ADDITIONAL course deliverable on top of the "
             "WSQ assessment: the consolidated DMAIC storyboard built across Labs 1-30, presented "
             "and defended to a steering committee on Day 5.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
