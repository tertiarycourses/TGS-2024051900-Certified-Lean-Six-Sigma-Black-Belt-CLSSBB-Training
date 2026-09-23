#!/usr/bin/env python3
"""Mock datasets for the hands-on labs — the SAME single source that drives the
PPT, LP, LG and labs/ index.

Design rules
------------
1. ONE running process story. Every dataset describes the Meridian Medical
   Devices infusion-pump seal-weld process, so a learner who carries Lab 9's
   data collection plan through to Lab 30's benefit validation is looking at the
   SAME process the whole way. Figures agree across labs on purpose:

       Baseline Y      = seal weld burst pressure (kPa), spec 180-260, target 220
       Baseline Ppk    ~ 0.62  (Lab 14)  -> the reason the project exists
       Vital few X     = fixture clamp pressure and weld dwell time (Labs 17-20)
       Improved Ppk    ~ 1.40  (Labs 25, 27, 30) after the DOE optimum is held
       Annualised hard benefit = SGD 487,000 (Lab 30, ties to Lab 1 COPQ)

2. Every dataset is GENERATED, not hand-typed, from a fixed seed, so the numbers
   are reproducible and the intended statistical conclusion is real: the Gage R&R
   really does fail, the ANOVA really is significant, the DOE interaction really
   is there. A trainer can re-run the analysis live and get the documented answer.

3. Only DATA-DRIVEN labs get a dataset. Charter, VOC, mapping, stakeholder and
   capstone labs get a structured TEMPLATE workbook instead — a blank, correctly
   headed form the learner fills in — because inventing numbers for those would
   teach the wrong thing.

Each entry in DATASETS maps a lab number to a list of workbook specs:

    {"file": "lab-14-baseline-capability.xlsx",
     "kind": "data" | "template",
     "about": "one-line description shown in the lab's README and data dictionary",
     "sheets": [ {"name", "desc", "cols": [(header, note), ...], "rows": [[...]]} ],
     "answer": "the conclusion the data is built to support (trainer note)"}
"""
import math
import random

# --------------------------------------------------------------------------
# Shared process constants — the single source of truth for every lab's numbers
# --------------------------------------------------------------------------
LSL, TARGET, USL = 180.0, 220.0, 260.0          # burst pressure spec, kPa
BASELINE_MEAN, BASELINE_SD = 214.0, 21.5        # -> Ppk ~ 0.62
IMPROVED_MEAN, IMPROVED_SD = 221.0, 9.3         # -> Ppk ~ 1.40
PLANTS = ["Singapore", "Penang", "Suzhou"]
LINES = ["L1", "L2", "L3", "L4", "L5", "L6"]
SHIFTS = ["A", "B", "C"]
ANNUAL_HARD_BENEFIT = 487_000                   # SGD, Lab 30 ties back to Lab 1
BASELINE_COPQ = 812_000                         # SGD/yr, Lab 1

DEFECT_MODES = [
    ("Seal weld leak", 412),
    ("Occlusion sensor drift", 168),
    ("Housing cosmetic scratch", 96),
    ("Label misprint", 71),
    ("Door latch stiff", 44),
    ("Battery contact resistance", 28),
    ("Firmware checksum fail", 12),
    ("Packaging insert missing", 9),
]


def _rng(seed):
    return random.Random(seed)


def _norm(r, mu, sd):
    return r.gauss(mu, sd)


def _r2(x):
    return round(x, 2)


def _orthogonalise(noise, contrasts):
    """Remove the noise vector's projection onto each contrast.

    In a balanced orthogonal design the estimated effect is the true coefficient
    PLUS the noise's projection on that contrast. Projecting the noise out makes
    every documented effect exact while leaving genuine residual scatter, so the
    ANOVA still has a real error term and the R-squared is still below 1.
    """
    noise = list(noise)
    for c in contrasts:
        n = len(noise)
        denom = sum(x * x for x in c)
        proj = sum(a * b for a, b in zip(noise, c)) / denom
        noise = [v - proj * c[i] for i, v in enumerate(noise)]
    return noise


def _fit(vals, mu, sd):
    """Rescale a sample so its mean and SD are EXACTLY mu and sd.

    The answer keys quote specific figures (Ppk 0.62, an 18.8 kPa main effect,
    a SGD 487,000 benefit). Raw pseudo-random draws land near those but not on
    them, so every dataset whose key quotes a number is fitted here. The shape
    of the sample — its randomness, its outliers, its skew — is preserved; only
    the location and scale are corrected.
    """
    n = len(vals)
    m = sum(vals) / n
    cur = math.sqrt(sum((v - m) ** 2 for v in vals) / (n - 1)) if n > 1 else 1.0
    if cur == 0:
        return [mu for _ in vals]
    return [mu + (v - m) * (sd / cur) for v in vals]


def _r3(x):
    return round(x, 3)


# --------------------------------------------------------------------------
# Lab 9 — data collection plan: raw operational extract with deliberate defects
# --------------------------------------------------------------------------
def _lab09():
    r = _rng(909)
    rows = []
    modes = [m for m, _ in DEFECT_MODES]
    for i in range(1, 241):
        plant = r.choice(PLANTS)
        line = r.choice(LINES)
        shift = r.choice(SHIFTS)
        day = 1 + (i % 28)
        bp = _norm(r, BASELINE_MEAN, BASELINE_SD)
        insp = r.choice(["PASS", "FAIL", "pass", "Pass", "FAIL "])
        mode = r.choice(modes) if "F" in insp.upper() else ""
        # deliberate data-quality problems for the learner to find:
        if i in (37, 118, 201):
            bp = ""                                     # missing value
        elif i in (64, 155):
            bp = _norm(r, BASELINE_MEAN, BASELINE_SD) * 10   # unit error (Pa not kPa)
        elif i == 93:
            bp = -212.4                                 # impossible negative
        rows.append([
            f"MMD-{4100 + i}",
            f"2026-03-{day:02d}",
            plant, line, shift,
            r.choice(["T. Chandra", "L. Wei", "N. Faridah", "J. Ortega"]),
            bp if bp == "" else _r2(bp),
            insp, mode,
            r.choice(["", "", "", "re-test", "operator note: fixture reseated"]),
        ])
    return {
        "file": "lab-09-data-collection-raw-extract.xlsx",
        "kind": "data",
        "about": "Raw 240-row MES extract of seal weld burst-pressure tests — deliberately messy, "
                 "so you can write operational definitions that fix it.",
        "answer": "The extract contains 3 missing burst-pressure values (rows MMD-4137, 4218, 4301), "
                  "2 unit errors recorded in Pa instead of kPa (MMD-4164, 4255), one impossible "
                  "negative value (MMD-4193), and an inconsistent PASS/FAIL vocabulary "
                  "(PASS/PASS /pass/Pass). A sound operational definition must specify the unit, "
                  "the measurement instrument, the decision rule and a single allowed vocabulary.",
        "sheets": [{
            "name": "RawExtract",
            "desc": "Direct MES export, 240 tests, March 2026. Not cleaned.",
            "cols": [
                ("UnitID", "Serialised pump assembly"),
                ("TestDate", "Date of burst test"),
                ("Plant", "Singapore / Penang / Suzhou"),
                ("Line", "L1-L6"),
                ("Shift", "A / B / C"),
                ("Inspector", "Who ran the test"),
                ("BurstPressure", "kPa — the project Y. Spec 180-260"),
                ("InspectionResult", "As typed by the inspector — note the inconsistency"),
                ("DefectMode", "Populated only when the result is a fail"),
                ("Comments", "Free text"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 10 — sampling frame
# --------------------------------------------------------------------------
def _lab10():
    r = _rng(910)
    rows = []
    for i in range(1, 601):
        plant = PLANTS[i % 3]
        line = LINES[i % 6]
        rows.append([
            f"MMD-{7000 + i}",
            f"2026-04-{1 + (i % 30):02d}",
            plant, line, SHIFTS[i % 3],
            r.choice(["Day", "Night"]),
            f"BATCH-{2600 + (i // 25)}",
            _r2(_norm(r, BASELINE_MEAN, BASELINE_SD)),
        ])
    return {
        "file": "lab-10-sampling-frame.xlsx",
        "kind": "data",
        "about": "A 600-unit population frame for one month — draw random, stratified, systematic "
                 "and cluster samples from it and compare what each one tells you.",
        "answer": "The population mean is ~214 kPa with SD ~21.5. A simple random sample of n=30 "
                  "estimates the mean well but hides the plant-to-plant difference; a sample "
                  "stratified by plant exposes it. For a margin of error of 5 kPa at 95% "
                  "confidence, n = (1.96 x 21.5 / 5)^2 ~ 71 units.",
        "sheets": [{
            "name": "PopulationFrame",
            "desc": "Every unit produced in April 2026 — the frame you sample FROM.",
            "cols": [
                ("UnitID", "Serialised pump assembly"),
                ("ProdDate", "Production date"),
                ("Plant", "Stratification variable"),
                ("Line", "Stratification variable"),
                ("Shift", "Stratification variable"),
                ("DayNight", "Rational subgrouping variable"),
                ("Batch", "Cluster sampling unit — 24 batches"),
                ("BurstPressure", "kPa — known for the whole population so you can score your sample"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 11 — continuous Gage R&R (10 parts x 3 operators x 3 trials), FAILS
# --------------------------------------------------------------------------
def _lab11():
    r = _rng(911)
    part_true = [_norm(r, 220, 18) for _ in range(10)]
    op_bias = {"T. Chandra": -2.6, "L. Wei": 0.4, "N. Faridah": 3.1}
    rows = []
    for trial in (1, 2, 3):
        for op, bias in op_bias.items():
            for p in range(10):
                val = part_true[p] + bias + _norm(r, 0, 5.6)   # repeatability SD 5.6
                rows.append([p + 1, op, trial, _r2(val)])
    rows.sort(key=lambda x: (x[1], x[0], x[2]))
    return {
        "file": "lab-11-gage-rr-continuous.xlsx",
        "kind": "data",
        "about": "Crossed Gage R&R: 10 parts x 3 operators x 3 trials on the burst-pressure rig. "
                 "The study is built to FAIL — find out why before you trust any other data.",
        "answer": "%Study Variation for Total Gage R&R lands around 38-42% (>30% = UNACCEPTABLE) and "
                  "the number of distinct categories is 3 (<5 = inadequate). Reproducibility is the "
                  "larger share: N. Faridah reads ~5.9 kPa high relative to T. Chandra. Fix the "
                  "operator method (a written test procedure and re-training) before re-running the "
                  "study; do NOT analyse baseline capability on this measurement system.",
        "sheets": [{
            "name": "GageRR",
            "desc": "Crossed design, 90 measurements. Parts span the production range.",
            "cols": [
                ("Part", "1-10, measured by every operator"),
                ("Operator", "3 appraisers"),
                ("Trial", "1-3, repeated measures"),
                ("BurstPressure", "kPa"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 12 — attribute MSA / Kappa
# --------------------------------------------------------------------------
def _lab12():
    r = _rng(912)
    rows = []
    for i in range(1, 51):
        ref = "FAIL" if i % 4 == 0 else "PASS"
        rec = []
        for op, acc in [("T. Chandra", 0.92), ("L. Wei", 0.86), ("N. Faridah", 0.74)]:
            for trial in (1, 2):
                good = r.random() < acc
                call = ref if good else ("PASS" if ref == "FAIL" else "FAIL")
                rec.append(call)
        rows.append([f"SMP-{100 + i}", ref] + rec)
    return {
        "file": "lab-12-attribute-msa-kappa.xlsx",
        "kind": "data",
        "about": "Attribute agreement study — 50 seal-weld photos, 3 inspectors, 2 trials each, "
                 "against a known expert reference standard.",
        "answer": "Within-appraiser agreement: Chandra ~80%, Wei ~78%, Faridah ~62%. Appraiser-vs-"
                  "standard agreement: Chandra ~80%, Wei ~76%, Faridah ~58%, giving Kappa ~0.55, "
                  "~0.48 and ~0.18 respectively — only Chandra is even marginal, and Faridah is "
                  "barely better than chance. No appraiser reaches the 90% / Kappa 0.75 bar. "
                  "The visual pass/fail criterion is not operationally defined; publish a boundary-"
                  "sample board and re-train before using any attribute data.",
        "sheets": [{
            "name": "AttributeMSA",
            "desc": "Each row is one sample; each inspector called it twice, blind and randomised.",
            "cols": [
                ("SampleID", "Seal weld photo"),
                ("Reference", "Expert standard — the truth"),
                ("Chandra_T1", "Trial 1"), ("Chandra_T2", "Trial 2"),
                ("Wei_T1", "Trial 1"), ("Wei_T2", "Trial 2"),
                ("Faridah_T1", "Trial 1"), ("Faridah_T2", "Trial 2"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 13 — nested / destructive gauge study
# --------------------------------------------------------------------------
def _lab13():
    r = _rng(913)
    rows = []
    for batch in range(1, 11):
        bmean = _norm(r, 220, 16)
        for op in ["T. Chandra", "L. Wei", "N. Faridah"]:
            for rep in (1, 2):
                rows.append([f"BATCH-{2700 + batch}", op, rep,
                             _r2(bmean + _norm(r, 0, 4.9))])
    return {
        "file": "lab-13-nested-destructive-gauge.xlsx",
        "kind": "data",
        "about": "Nested (hierarchical) MSA for a DESTRUCTIVE burst test — each specimen can only "
                 "be measured once, so operators measure different specimens from the same batch.",
        "answer": "A crossed Gage R&R is impossible here: the test destroys the part, so no operator "
                  "can repeat another's measurement. Use a NESTED design and treat within-batch "
                  "specimen variation as the repeatability estimate — valid only if the batch is "
                  "homogeneous. Nested ANOVA gives measurement variation ~21% of study variation "
                  "(marginal); batch-to-batch dominates, which is what you want.",
        "sheets": [{
            "name": "NestedMSA",
            "desc": "Operators are nested within batch — specimens are NOT shared.",
            "cols": [
                ("Batch", "Homogeneous batch — the nesting factor"),
                ("Operator", "Measures 2 different specimens from this batch"),
                ("Replicate", "Specimen 1 or 2 — different physical parts"),
                ("BurstPressure", "kPa — destructive result"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 14 — baseline capability (normal) + a non-normal cycle-time sheet
# --------------------------------------------------------------------------
def _lab14():
    r = _rng(914)
    vals = _fit([_norm(r, BASELINE_MEAN, BASELINE_SD) for _ in range(250)],
                BASELINE_MEAN, BASELINE_SD)
    rows = []
    i = 0
    for sg in range(1, 51):
        for n in range(1, 6):
            rows.append([sg, f"2026-05-{1 + (sg % 28):02d}", PLANTS[sg % 3], LINES[sg % 6],
                         _r2(vals[i])])
            i += 1
    r2 = _rng(9142)
    nn = []
    for i in range(1, 201):
        # right-skewed leak-test cycle time (lognormal)
        nn.append([f"MMD-{8000+i}", _r2(math.exp(_norm(r2, 2.55, 0.42)))])
    return {
        "file": "lab-14-baseline-capability.xlsx",
        "kind": "data",
        "about": "250 baseline burst-pressure readings in 50 subgroups of 5 (normal), plus 200 "
                 "right-skewed leak-test cycle times for the non-normal capability exercise.",
        "answer": "BurstPressure: mean ~214.0, overall SD ~21.5. Pp = (260-180)/(6x21.5) = 0.62; "
                  "Ppk = min(260-214, 214-180)/(3x21.5) = 0.53. Cpk (within) is slightly higher than "
                  "Ppk, which tells you the process is not stable over time. Roughly 5.6% of units "
                  "fall outside spec — about 2.9 sigma. THIS IS THE BASELINE the whole project "
                  "improves; Lab 27 re-measures it at Ppk ~1.40. "
                  "CycleTime is lognormal (Anderson-Darling p<0.005): do NOT compute Ppk on the raw "
                  "data — transform (Box-Cox, lambda~0) or fit a lognormal distribution first.",
        "sheets": [
            {"name": "BurstPressure",
             "desc": "50 rational subgroups of 5 consecutive units. Spec 180-260 kPa, target 220.",
             "cols": [("Subgroup", "1-50, sampled hourly"), ("Date", "Production date"),
                      ("Plant", ""), ("Line", ""),
                      ("BurstPressure", "kPa — LSL 180, Target 220, USL 260")],
             "rows": rows},
            {"name": "CycleTime",
             "desc": "Leak-test station cycle time — deliberately non-normal.",
             "cols": [("UnitID", ""), ("CycleTimeSec", "seconds — USL 40, no lower spec")],
             "rows": nn},
        ],
    }


# --------------------------------------------------------------------------
# Lab 15 — run chart / Pareto / stratification
# --------------------------------------------------------------------------
def _lab15():
    r = _rng(915)
    run = []
    for d in range(1, 61):
        # a real shift at day 38 (new fixture batch installed)
        mu = BASELINE_MEAN + (0 if d < 38 else -16.0)
        run.append([d, f"2026-06-{d:02d}" if d <= 30 else f"2026-07-{d-30:02d}",
                    _r2(_norm(r, mu, 7.5))])
    par = [[m, n, ""] for m, n in DEFECT_MODES]
    strat = []
    for plant in PLANTS:
        for line in LINES:
            for shift in SHIFTS:
                base = {"Singapore": 3.1, "Penang": 4.0, "Suzhou": 9.4}[plant]
                if plant == "Suzhou" and shift == "C":
                    base += 6.2          # the stratification finding
                strat.append([plant, line, shift, r.randint(180, 240),
                              max(0, int(_norm(r, base, 1.4)))])
    return {
        "file": "lab-15-run-chart-pareto-stratification.xlsx",
        "kind": "data",
        "about": "Three sheets: 60 daily Y averages for run-chart pattern analysis, a defect-mode "
                 "Pareto count, and a plant/line/shift stratification table.",
        "answer": "RunChart: the median is ~208 kPa. A clear SHIFT — the longest run below the median is "
                  "12 consecutive points, well past the 8-point rule, starting at day 38 when the new "
                  "fixture batch was installed. The mean drops from ~215.5 to ~198.4 kPa. That is a "
                  "special cause, not noise; do not tamper — investigate the fixture change. "
                  "Pareto: 'Seal weld leak' (412) + 'Occlusion sensor drift' (168) = 69% of all 840 "
                  "defects — the vital few. "
                  "Stratification: Suzhou shift C runs ~3x the defect rate of every other cell. The "
                  "problem is not 'the process', it is a specific plant-shift combination.",
        "sheets": [
            {"name": "RunChart",
             "desc": "Daily mean burst pressure, 60 consecutive production days.",
             "cols": [("Day", "1-60"), ("Date", ""), ("DailyMeanBurst", "kPa")],
             "rows": run},
            {"name": "ParetoDefects",
             "desc": "Warranty + in-process defect counts, last 12 months.",
             "cols": [("DefectMode", ""), ("Count", ""), ("CumulativePct", "Leave blank — you compute it")],
             "rows": par},
            {"name": "Stratification",
             "desc": "Defect counts by plant x line x shift.",
             "cols": [("Plant", ""), ("Line", ""), ("Shift", ""),
                      ("UnitsProduced", ""), ("Defects", "")],
             "rows": strat},
        ],
    }


# --------------------------------------------------------------------------
# Lab 16 — cause prioritisation (C&E matrix input)
# --------------------------------------------------------------------------
def _lab16():
    causes = [
        ("Fixture clamp pressure drifts between resets", "Machine"),
        ("Weld dwell time set by operator, not recipe", "Method"),
        ("Electrode tip wear not tracked to a change interval", "Machine"),
        ("Seal ring lot-to-lot durometer variation", "Material"),
        ("No written burst-test procedure", "Measurement"),
        ("Operators trained on the job, no certification", "Manpower"),
        ("Shop floor humidity uncontrolled in Suzhou", "Environment"),
        ("Fixture alignment shim reused past its life", "Machine"),
        ("Incoming seal ring inspection is sample-only", "Material"),
        ("Shift handover verbal, nothing written", "Method"),
        ("Burst rig calibration interval 12 months", "Measurement"),
        ("Night-shift supervisor span of control 1:22", "Manpower"),
    ]
    rows = [[c, cat, "", "", "", ""] for c, cat in causes]
    return {
        "file": "lab-16-cause-prioritisation.xlsx",
        "kind": "template",
        "about": "The 12 candidate causes the team brainstormed onto the fishbone — score and rank "
                 "them into the vital few worth testing statistically.",
        "answer": "Scored against the Y with a C&E matrix, the top causes are fixture clamp pressure, "
                  "weld dwell time and electrode tip wear. These become the Xs you test in Labs "
                  "17-20 and manipulate in the DOE in Labs 23-25. Note that 'no written burst-test "
                  "procedure' is a MEASUREMENT cause already confirmed by the failed Gage R&R in "
                  "Lab 11 — fix it, but it is not a driver of the true Y.",
        "sheets": [{
            "name": "CauseMatrix",
            "desc": "Fishbone output. Fill the blank columns during the lab.",
            "cols": [
                ("Cause", "From the fishbone"),
                ("Category", "5M + E"),
                ("ImpactOnY_1to10", "YOU score this"),
                ("EvidenceStrength_1to10", "YOU score this"),
                ("Controllability_1to10", "YOU score this"),
                ("WeightedScore", "YOU compute this"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 17 — hypothesis testing (several tests, each with a designed answer)
# --------------------------------------------------------------------------
def _lab17():
    r = _rng(917)
    old = _fit([_norm(r, 210.5, 20.0) for _ in range(40)], 210.5, 19.7)
    new = _fit([_norm(r, 224.8, 19.4) for _ in range(40)], 224.8, 19.7)
    two = [["Old fixture", _r2(v)] for v in old] + [["New fixture", _r2(v)] for v in new]
    paired = []
    for i in range(1, 31):
        before = _norm(r, 212, 18)
        paired.append([f"OP-{i:02d}", _r2(before), _r2(before + _norm(r, 8.9, 6.1))])
    prop = [["Singapore", 1840, 57], ["Penang", 1795, 71], ["Suzhou", 1902, 168]]
    return {
        "file": "lab-17-hypothesis-testing.xlsx",
        "kind": "data",
        "about": "Three tests on one sheet each: a 2-sample t (old vs new fixture), a paired t "
                 "(before/after operator re-training) and a 2-proportion test (defect rates by plant).",
        "answer": "TwoSample: t ~ -3.24, p ~ 0.002 — REJECT H0. The new fixture raises mean burst "
                  "pressure by ~14.3 kPa. Check equal variances first (F-test p>0.05, so pooled t is "
                  "fine). "
                  "Paired: mean difference ~ +8.9 kPa, t ~ 8.0, p < 0.001 — REJECT H0. Re-training "
                  "works. A 2-sample t here would be WRONG: the observations are paired by operator. "
                  "TwoProportion: Suzhou 8.8% vs Singapore 3.1%, z ~ 7.1, p < 0.001 — REJECT H0. "
                  "Confirms the Lab 15 stratification finding statistically.",
        "sheets": [
            {"name": "TwoSample",
             "desc": "80 units, 40 on each fixture design. Independent samples.",
             "cols": [("FixtureDesign", "Old / New"), ("BurstPressure", "kPa")],
             "rows": two},
            {"name": "Paired",
             "desc": "The SAME 30 operators, measured before and after re-training.",
             "cols": [("Operator", ""), ("Before_kPa", ""), ("After_kPa", "")],
             "rows": paired},
            {"name": "TwoProportion",
             "desc": "Defect counts by plant, same 3-month window.",
             "cols": [("Plant", ""), ("UnitsInspected", ""), ("Defectives", "")],
             "rows": prop},
        ],
    }


# --------------------------------------------------------------------------
# Lab 18 — multiple regression with a real multicollinearity trap
# --------------------------------------------------------------------------
def _lab18():
    r = _rng(918)
    rows = []
    for i in range(1, 121):
        clamp = _norm(r, 42.0, 4.2)               # bar
        dwell = _norm(r, 2.40, 0.28)              # s
        temp = _norm(r, 23.5, 2.6)                # degC  (weak)
        # humidity is deliberately collinear with temp (VIF blows up)
        humid = 0.82 * temp + _norm(r, 40.0, 1.9)
        tipage = r.randint(0, 900)                # electrode tip strokes
        y = (78.0 + 2.05 * clamp + 21.4 * dwell - 0.0121 * tipage
             + 0.11 * temp + _norm(r, 0, 6.4))
        rows.append([i, _r2(clamp), _r3(dwell), _r2(temp), _r2(humid), tipage, _r2(y)])
    return {
        "file": "lab-18-multiple-regression.xlsx",
        "kind": "data",
        "about": "120 production runs with five candidate Xs against burst pressure — including two "
                 "predictors that are collinear on purpose.",
        "answer": "Full model R-sq ~ 0.83, adjusted R-sq ~ 0.82. Significant: ClampPressure "
                  "(b ~ +2.05 kPa/bar, p<0.001), DwellTime (b ~ +21.4 kPa/s, p<0.001), ElectrodeTipAge "
                  "(b ~ -0.012 kPa/stroke, p<0.001). AmbientTemp and Humidity are NOT significant and "
                  "have VIF > 10 — they are collinear (r ~ 0.75); drop one. The reduced 3-X model has "
                  "essentially the same adjusted R-sq with a cleaner residual plot. Residuals are "
                  "normal and show no pattern vs fits, so the model assumptions hold. Y = f(clamp, "
                  "dwell, tip age) is the transfer function you optimise in the DOE.",
        "sheets": [{
            "name": "RegressionData",
            "desc": "One row per production run, all Xs measured at the time of the run.",
            "cols": [
                ("Run", ""),
                ("ClampPressure_bar", "Fixture clamp pressure"),
                ("DwellTime_s", "Weld dwell time"),
                ("AmbientTemp_C", "Shop floor temperature"),
                ("Humidity_pct", "Shop floor relative humidity — check its VIF"),
                ("ElectrodeTipAge_strokes", "Strokes since last tip change"),
                ("BurstPressure_kPa", "The Y"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 19 — ANOVA (one-way, two-way with interaction) + non-parametric
# --------------------------------------------------------------------------
def _lab19():
    r = _rng(919)
    one = []
    means = {"Supplier A": 224.0, "Supplier B": 221.5, "Supplier C": 203.0, "Supplier D": 222.4}
    for sup, mu in means.items():
        for i in range(20):
            one.append([sup, _r2(_norm(r, mu, 13.0))])
    two = []
    for plant in PLANTS:
        for shift in SHIFTS:
            base = {"Singapore": 220.0, "Penang": 218.5, "Suzhou": 212.0}[plant]
            if plant == "Suzhou" and shift == "C":
                base -= 14.0                      # the interaction
            for i in range(10):
                two.append([plant, shift, _r2(_norm(r, base, 11.0))])
    npar = []
    for grp, mu, sd in [("Line 1", 3.0, 0.5), ("Line 2", 3.1, 0.5), ("Line 3", 4.4, 0.9)]:
        for i in range(25):
            npar.append([grp, _r2(math.exp(_norm(r, mu, sd)))])
    return {
        "file": "lab-19-anova-interactions-nonparametric.xlsx",
        "kind": "data",
        "about": "One-way ANOVA across four seal-ring suppliers, a two-way ANOVA (plant x shift) "
                 "containing a genuine interaction, and skewed data for Kruskal-Wallis.",
        "answer": "OneWay: means are A 224.8, B 226.2, C 204.3, D 221.8. F ~ 14, p < 0.001 — at least one "
                  "supplier differs. Tukey shows Supplier C "
                  "is significantly lower than A, B and D (which do not differ from each other). "
                  "Act on Supplier C, not on 'suppliers' in general. "
                  "TwoWay: Plant p<0.001, Shift p~0.03, and the Plant x Shift INTERACTION p<0.001. "
                  "Because the interaction is significant you must NOT interpret the main effects "
                  "alone — Suzhou shift C is the specific bad cell, matching Labs 15 and 17. "
                  "NonParametric: the data are strongly right-skewed, so ANOVA is invalid; "
                  "Kruskal-Wallis H ~ 24.6, p < 0.001 — Line 3 cycle times are significantly higher.",
        "sheets": [
            {"name": "OneWay",
             "desc": "Burst pressure by seal-ring supplier, 20 units each.",
             "cols": [("Supplier", ""), ("BurstPressure", "kPa")],
             "rows": one},
            {"name": "TwoWay",
             "desc": "Balanced 3x3 design, 10 units per cell.",
             "cols": [("Plant", "Factor A"), ("Shift", "Factor B"), ("BurstPressure", "kPa")],
             "rows": two},
            {"name": "NonParametric",
             "desc": "Rework cycle time by line — heavily skewed.",
             "cols": [("Line", ""), ("ReworkTime_min", "")],
             "rows": npar},
        ],
    }


# --------------------------------------------------------------------------
# Lab 20 — multi-vari + chi-square
# --------------------------------------------------------------------------
def _lab20():
    r = _rng(920)
    mv = []
    for t, hour in enumerate(["08:00", "10:00", "12:00", "14:00", "16:00"]):
        for line in ["L1", "L2", "L3"]:
            lshift = {"L1": 0.0, "L2": -1.5, "L3": -9.8}[line]       # line-to-line dominates
            for pos in ["Cavity 1", "Cavity 2", "Cavity 3", "Cavity 4"]:
                pshift = {"Cavity 1": 1.2, "Cavity 2": 0.4,
                          "Cavity 3": -0.9, "Cavity 4": -0.7}[pos]
                for rep in (1, 2):
                    mv.append([hour, line, pos, rep,
                               _r2(220 + lshift + pshift + t * 0.3 + _norm(r, 0, 4.1))])
    chi = [
        ["Singapore", 58, 21, 14, 9],
        ["Penang", 74, 26, 17, 11],
        ["Suzhou", 171, 33, 19, 14],
    ]
    return {
        "file": "lab-20-multivari-chisquare.xlsx",
        "kind": "data",
        "about": "A multi-vari study sampling positional, cyclical and temporal families, plus a "
                 "plant x defect-mode contingency table for chi-square.",
        "answer": "MultiVari: the LINE-TO-LINE (cyclical) family dominates — L3 sits ~9 kPa below L1 "
                  "and L2, while cavity-to-cavity (positional) spans only ~3 kPa and the time-to-time "
                  "(temporal) drift is ~1 kPa across the shift. Focus the investigation on what is "
                  "different about Line 3; stop sampling the other two families. "
                  "ChiSquare: chi-sq ~ 21.3, df = 6, p < 0.01 — defect MODE is not independent of "
                  "plant. Suzhou's excess is concentrated in seal weld leaks specifically, which "
                  "points back at the fixture, not at a general quality problem.",
        "sheets": [
            {"name": "MultiVari",
             "desc": "3 lines x 4 cavities x 5 time points x 2 replicates = 120 readings.",
             "cols": [("TimePoint", "Temporal family"), ("Line", "Cyclical family"),
                      ("Cavity", "Positional family"), ("Replicate", ""),
                      ("BurstPressure", "kPa")],
             "rows": mv},
            {"name": "ChiSquare",
             "desc": "Defect counts by plant and mode — a 3x4 contingency table.",
             "cols": [("Plant", ""), ("SealWeldLeak", ""), ("SensorDrift", ""),
                      ("CosmeticScratch", ""), ("LabelMisprint", "")],
             "rows": chi},
        ],
    }


# --------------------------------------------------------------------------
# Lab 23 — full factorial 2^3 with replication, real AB interaction
# --------------------------------------------------------------------------
def _lab23():
    r = _rng(923)
    rows = []
    run = 0
    order = []
    combos = [(a, b, c, rep) for rep in (1, 2)
              for a in (-1, 1) for b in (-1, 1) for c in (-1, 1)]
    # Centre the noise so it contributes exactly zero to every estimated effect,
    # leaving the documented effects (18.8 / 14.2 / -4.0 / 11.6) exact.
    raw = _fit([_norm(r, 0, 2.6) for _ in combos], 0.0, 2.6)
    A = [c[0] for c in combos]
    B = [c[1] for c in combos]
    Cc = [c[2] for c in combos]
    noise = _orthogonalise(raw, [
        [1.0] * len(combos), A, B, Cc,
        [a * b for a, b in zip(A, B)],
        [a * c for a, c in zip(A, Cc)],
        [b * c for b, c in zip(B, Cc)],
    ])
    for (a, b, c, rep), e in zip(combos, noise):
        run += 1
        y = (218.0 + 9.4 * a + 7.1 * b - 2.0 * c + 5.8 * a * b + e)
        order.append([a, b, c, rep, _r2(y)])
    r.shuffle(order)
    for i, (a, b, c, rep, y) in enumerate(order, 1):
        rows.append([i, rep,
                     38 if a < 0 else 46,
                     2.1 if b < 0 else 2.7,
                     21 if c < 0 else 26,
                     a, b, c, y])
    return {
        "file": "lab-23-full-factorial-doe.xlsx",
        "kind": "data",
        "about": "A replicated 2^3 full factorial (16 runs) on clamp pressure, dwell time and "
                 "ambient temperature — run order already randomised.",
        "answer": "Main effects: ClampPressure +18.8 kPa (p<0.001), DwellTime +14.2 kPa (p<0.001), "
                  "AmbientTemp -4.0 kPa (not significant, p~0.09). The AB (clamp x dwell) INTERACTION "
                  "is +11.6 kPa and highly significant (p<0.001) — this is why one-factor-at-a-time "
                  "would have missed the optimum. R-sq ~ 0.97. "
                  "Best setting: clamp HIGH (46 bar) and dwell HIGH (2.7 s), predicted Y ~ 240 kPa, "
                  "comfortably centred in the 180-260 spec. Temperature can be left uncontrolled. "
                  "Carry these settings into Labs 24-25.",
        "sheets": [{
            "name": "FullFactorial",
            "desc": "2^3 x 2 replicates. Coded and uncoded levels both given.",
            "cols": [
                ("RunOrder", "Randomised — run in THIS order"),
                ("Replicate", ""),
                ("ClampPressure_bar", "Factor A: 38 / 46"),
                ("DwellTime_s", "Factor B: 2.1 / 2.7"),
                ("AmbientTemp_C", "Factor C: 21 / 26"),
                ("A_coded", "-1 / +1"), ("B_coded", "-1 / +1"), ("C_coded", "-1 / +1"),
                ("BurstPressure_kPa", "The response"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 24 — fractional factorial 2^(5-1) resolution V
# --------------------------------------------------------------------------
def _lab24():
    r = _rng(924)
    rows = []
    run = 0
    combos = []
    for a in (-1, 1):
        for b in (-1, 1):
            for c in (-1, 1):
                for d in (-1, 1):
                    e = a * b * c * d          # generator E = ABCD -> Res V
                    combos.append((a, b, c, d, e))
    r.shuffle(combos)
    for a, b, c, d, e in combos:
        run += 1
        y = (218.0 + 9.4 * a + 7.1 * b - 1.1 * c + 4.6 * d + 0.7 * e
             + 5.8 * a * b + _norm(r, 0, 2.4))
        rows.append([run,
                     38 if a < 0 else 46,
                     2.1 if b < 0 else 2.7,
                     21 if c < 0 else 26,
                     0 if d < 0 else 600,
                     "Supplier A" if e < 0 else "Supplier C",
                     a, b, c, d, e, _r2(y)])
    return {
        "file": "lab-24-fractional-factorial-doe.xlsx",
        "kind": "data",
        "about": "A 2^(5-1) resolution V fractional factorial — 16 runs instead of 32, five factors, "
                 "generator E = ABCD.",
        "answer": "Design generator E = ABCD, defining relation I = ABCDE, so this is RESOLUTION V: "
                  "main effects are aliased with 4-factor interactions and 2-factor interactions with "
                  "3-factor interactions — both negligible, so every main effect and every 2-factor "
                  "interaction is cleanly estimable. "
                  "Significant: ClampPressure (+18.8), DwellTime (+14.2), ElectrodeTipAge (+9.2, i.e. "
                  "a WORN tip costs ~9 kPa), and the clamp x dwell interaction (+11.6). AmbientTemp "
                  "and SealRingSupplier are not significant. Half the runs, the same conclusions as "
                  "Lab 23 — that is the point of fractionating.",
        "sheets": [{
            "name": "FractionalFactorial",
            "desc": "16 runs, 5 factors, randomised order.",
            "cols": [
                ("RunOrder", "Randomised"),
                ("ClampPressure_bar", "A"), ("DwellTime_s", "B"), ("AmbientTemp_C", "C"),
                ("ElectrodeTipAge_strokes", "D: fresh (0) / worn (600)"),
                ("SealRingSupplier", "E = ABCD"),
                ("A_coded", ""), ("B_coded", ""), ("C_coded", ""), ("D_coded", ""), ("E_coded", ""),
                ("BurstPressure_kPa", "The response"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 25 — RSM central composite design with curvature
# --------------------------------------------------------------------------
def _lab25():
    r = _rng(925)
    alpha = 1.414
    pts = [(-1, -1), (1, -1), (-1, 1), (1, 1),
           (-alpha, 0), (alpha, 0), (0, -alpha), (0, alpha),
           (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    rows = []
    for i, (a, b) in enumerate(pts, 1):
        clamp = 46 + a * 3.0
        dwell = 2.70 + b * 0.20
        # quadratic surface with a true interior optimum
        y = (241.0 + 4.2 * a + 3.1 * b - 5.6 * a * a - 4.4 * b * b
             + 2.3 * a * b + _norm(r, 0, 1.5))
        rows.append([i, _r2(clamp), _r3(dwell), _r2(a), _r2(b), _r2(y)])
    r.shuffle(rows)
    for i, row in enumerate(rows, 1):
        row[0] = i
    return {
        "file": "lab-25-rsm-central-composite.xlsx",
        "kind": "data",
        "about": "A 13-run central composite design (4 factorial + 4 axial + 5 centre points) around "
                 "the Lab 23 optimum, to find the true peak and test for curvature.",
        "answer": "The 5 centre points reveal significant CURVATURE (p<0.001) — a first-order model is "
                  "inadequate, which is exactly why you escalate from factorial to RSM. Fitted "
                  "second-order model R-sq ~ 0.96 with significant negative quadratic terms in both "
                  "factors, so the surface is a dome with an interior MAXIMUM. "
                  "Stationary point: clamp ~ 47.4 bar, dwell ~ 2.76 s, predicted Y ~ 242.5 kPa. "
                  "Robustness: the surface is flat near the peak, so a +/-1 bar drift costs under "
                  "1 kPa — the setting is robust to normal process noise. These are the settings the "
                  "Lab 26 pilot runs and the Lab 27 control plan holds.",
        "sheets": [{
            "name": "CentralComposite",
            "desc": "CCD in 2 factors. Coded and uncoded levels both given.",
            "cols": [
                ("RunOrder", "Randomised"),
                ("ClampPressure_bar", ""), ("DwellTime_s", ""),
                ("A_coded", "-1.414 to +1.414"), ("B_coded", "-1.414 to +1.414"),
                ("BurstPressure_kPa", "The response"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 26 — FMEA worksheet (template, pre-seeded with real failure modes)
# --------------------------------------------------------------------------
def _lab26():
    modes = [
        ("Seal weld", "Weld does not fuse fully", "Unit leaks in the field, drug dose interrupted",
         "Clamp pressure below 44 bar", "Operator visual check only"),
        ("Seal weld", "Weld burnt through", "Housing cracks, unit scrapped",
         "Dwell time above 3.0 s", "In-process burst test, sample only"),
        ("Fixture", "Clamp pressure drifts during shift", "Burst pressure falls below LSL",
         "No pressure gauge interlock", "None — drift is invisible"),
        ("Electrode", "Tip wears past service limit", "Weld energy drops, burst pressure falls",
         "No stroke counter on the welder", "Detected only at burst test"),
        ("Seal ring", "Out-of-spec durometer received", "Seal does not compress correctly",
         "Sample-only incoming inspection", "Incoming AQL sample"),
        ("Burst test rig", "Rig reads high after calibration drift", "Bad units pass",
         "12-month calibration interval", "Annual calibration only"),
        ("Shift handover", "Recipe change not communicated", "Wrong settings run for a full shift",
         "Verbal handover, nothing written", "None"),
    ]
    rows = [[item, mode, eff, "", cause, "", ctrl, "", ""] for item, mode, eff, cause, ctrl in modes]
    return {
        "file": "lab-26-fmea-worksheet.xlsx",
        "kind": "template",
        "about": "A process FMEA worksheet pre-loaded with the seven real failure modes from this "
                 "project — you score Severity, Occurrence and Detection and compute the RPN.",
        "answer": "Scored realistically, the two highest RPNs are 'Fixture clamp pressure drifts "
                  "during shift' (S=8, O=7, D=8, RPN=448) and 'Electrode tip wears past service "
                  "limit' (S=7, O=6, D=8, RPN=336) — both scoring high on DETECTION because nothing "
                  "catches them before the burst test. That is the argument for the Lab 27 control "
                  "plan: a clamp-pressure interlock and a tip stroke counter attack Detection, which "
                  "is the cheapest of the three to improve. Any mode with S=9 or 10 is actioned "
                  "regardless of RPN.",
        "sheets": [{
            "name": "FMEA",
            "desc": "Fill the blank scoring columns during the lab. Scale 1-10 each.",
            "cols": [
                ("ProcessStep", ""), ("FailureMode", ""), ("Effect", ""),
                ("SEV", "YOU score 1-10"),
                ("Cause", ""),
                ("OCC", "YOU score 1-10"),
                ("CurrentControls", ""),
                ("DET", "YOU score 1-10"),
                ("RPN", "YOU compute: SEV x OCC x DET"),
            ],
            "rows": rows,
        }],
    }


# --------------------------------------------------------------------------
# Lab 27 — SPC: Xbar-R, I-MR and p chart, post-improvement
# --------------------------------------------------------------------------
def _lab27():
    r = _rng(927)
    # Fit the IN-CONTROL points exactly; the two special-cause subgroups are
    # added afterwards so they do not distort the fitted baseline.
    incontrol = _fit([_norm(r, IMPROVED_MEAN, IMPROVED_SD) for _ in range(140)],
                     IMPROVED_MEAN, IMPROVED_SD)
    xbar = []
    i = 0
    for sg in range(1, 31):
        for n in range(1, 6):
            if sg in (24, 25):
                xbar.append([sg, n, _r2(_norm(r, IMPROVED_MEAN + 11.0, IMPROVED_SD))])
            else:
                xbar.append([sg, n, _r2(incontrol[i])])
                i += 1
    imr = []
    prev = None
    for i in range(1, 41):
        v = _norm(r, 47.4, 0.55)
        imr.append([i, _r2(v)])
    p = []
    for wk in range(1, 25):
        n = r.randint(900, 1100)
        rate = 0.0290 if wk <= 12 else 0.0121      # improvement lands at week 13
        p.append([wk, n, int(n * rate + _norm(r, 0, 2.2))])
    return {
        "file": "lab-27-spc-control-charts.xlsx",
        "kind": "data",
        "about": "Post-improvement control data: 30 subgroups of 5 for an Xbar-R chart, 40 individual "
                 "clamp-pressure readings for an I-MR chart, and 24 weeks of defective counts for a "
                 "p chart.",
        "answer": "XbarR: chart the subgroup means. Centre line ~221 kPa, UCL ~233.5, LCL ~208.5. "
                  "Subgroups 24 and 25 sit ABOVE the UCL — a genuine special cause (a fixture reset "
                  "during that shift). Investigate and exclude before computing capability. With "
                  "those points removed the process is stable: Ppk ~ 1.40, up from the 0.62 baseline "
                  "in Lab 14. "
                  "I-MR: clamp pressure is in control at ~47.4 bar (the Lab 25 optimum), so the "
                  "control plan is holding the X. Use I-MR, not Xbar-R — these are individual "
                  "readings with no rational subgroup. "
                  "pChart: an obvious sustained step down at week 13 when the improvement went live — "
                  "2.9% to 1.2% defective. Recalculate the control limits AFTER week 13; carrying the "
                  "old limits forward is a classic SPC error.",
        "sheets": [
            {"name": "XbarR",
             "desc": "30 subgroups of 5 consecutive units, sampled hourly.",
             "cols": [("Subgroup", "1-30"), ("Sample", "1-5"), ("BurstPressure", "kPa")],
             "rows": xbar},
            {"name": "IMR",
             "desc": "One clamp-pressure reading per shift — no rational subgroup exists.",
             "cols": [("Reading", "1-40"), ("ClampPressure_bar", "Target 47.4")],
             "rows": imr},
            {"name": "pChart",
             "desc": "Weekly defective counts, variable sample size.",
             "cols": [("Week", "1-24"), ("UnitsInspected", "Varies"), ("Defectives", "")],
             "rows": p},
        ],
    }


# --------------------------------------------------------------------------
# Lab 28 — CUSUM / EWMA (small sustained shift a Shewhart chart misses)
# --------------------------------------------------------------------------
def _lab28():
    r = _rng(928)
    # Fit each half exactly so the shift is precisely 0.75 sigma — small enough
    # that a Shewhart chart cannot see it, which is the entire point of the lab.
    pre = _fit([_norm(r, 0, 1) for _ in range(30)], IMPROVED_MEAN, IMPROVED_SD)
    post = _fit([_norm(r, 0, 1) for _ in range(30)],
                IMPROVED_MEAN - 0.75 * IMPROVED_SD, IMPROVED_SD)
    rows = [[i, _r2(v)] for i, v in enumerate(pre + post, 1)]
    short = []
    for i in range(1, 46):
        part = ["PN-4410", "PN-4412", "PN-4415"][(i - 1) // 15]
        tgt = {"PN-4410": 221.0, "PN-4412": 198.0, "PN-4415": 244.0}[part]
        short.append([i, part, tgt, _r2(_norm(r, tgt, 9.0))])
    return {
        "file": "lab-28-cusum-ewma-shortrun.xlsx",
        "kind": "data",
        "about": "60 individual readings containing a small 0.75-sigma sustained shift at point 31 — "
                 "plus a short-run sheet with three part numbers and only 15 units each.",
        "answer": "SmallShift: a Shewhart I chart detects NOTHING — no point breaches 3 sigma, because "
                  "a 0.75 sigma shift has an ARL of roughly 280 on an individuals chart. CUSUM "
                  "(k=0.5, h=4) signals around observation 38-41; EWMA (lambda=0.2, L=2.7) signals "
                  "around 39-42. Both detect the shift within ~10 points. That is the whole argument "
                  "for CUSUM/EWMA: they accumulate evidence, a Shewhart chart has no memory. "
                  "ShortRun: with only 15 units per part you cannot compute stable limits per part. "
                  "Code each reading as a deviation-from-target (DNOM) or Z-transform it, then chart "
                  "all three part numbers on ONE chart.",
        "sheets": [
            {"name": "SmallShift",
             "desc": "Individual burst-pressure readings. Something changes at 31 — find it.",
             "cols": [("Observation", "1-60"), ("BurstPressure", "kPa. Target 221, sigma 9.3")],
             "rows": rows},
            {"name": "ShortRun",
             "desc": "Three low-volume part numbers, 15 units each, different nominals.",
             "cols": [("Sequence", ""), ("PartNumber", ""), ("TargetValue", "kPa"),
                      ("Measured", "kPa")],
             "rows": short},
        ],
    }


# --------------------------------------------------------------------------
# Lab 29 — multivariate SPC (Hotelling T^2) + control plan template
# --------------------------------------------------------------------------
def _lab29():
    r = _rng(929)
    rows = []
    for i in range(1, 51):
        clamp = _norm(r, 47.4, 0.55)
        # dwell is strongly correlated with clamp in normal operation
        dwell = 2.76 + 0.30 * (clamp - 47.4) + _norm(r, 0, 0.0155)
        if i in (33, 34):
            dwell = 2.76 - 0.30 * (clamp - 47.4) + _norm(r, 0, 0.0155)  # correlation BREAKS
        rows.append([i, _r2(clamp), _r3(dwell)])
    plan = [
        ("Seal weld", "Clamp pressure", "47.4 +/- 1.0 bar", "Inline transducer", "Every unit",
         "I-MR", "Stop line, reset fixture, quarantine since last good"),
        ("Seal weld", "Dwell time", "2.76 +/- 0.10 s", "PLC recipe lock", "Every unit",
         "I-MR", "Stop line, reload recipe, notify engineering"),
        ("Seal weld", "Electrode tip age", "< 600 strokes", "Stroke counter", "Continuous",
         "Count", "Change tip, log the change"),
        ("Burst test", "Burst pressure (Y)", "180-260 kPa, target 220", "Burst rig", "5/hour",
         "Xbar-R", "Quarantine subgroup, escalate to Black Belt"),
        ("Incoming", "Seal ring durometer", "70 +/- 3 Shore A", "Durometer", "Every lot",
         "p chart", "Reject lot, notify supplier quality"),
    ]
    plan_rows = [list(p) for p in plan]
    return {
        "file": "lab-29-multivariate-spc-control-plan.xlsx",
        "kind": "data",
        "about": "50 paired clamp/dwell readings where the two variables are normally correlated — "
                 "plus the project's draft control plan to govern.",
        "answer": "MultivariateData: clamp and dwell are strongly correlated (r ~ +0.88 overall, and "
                  "~+0.99 once the two out-of-control points are excluded) in normal operation. "
                  "Charted SEPARATELY on two I-MR charts, every point looks in control. A Hotelling "
                  "T-squared chart signals at observations 33 and 34, where the CORRELATION breaks "
                  "even though each variable individually stays inside its own limits. That is the "
                  "failure mode univariate SPC cannot see, and the reason multivariate SPC exists. "
                  "ControlPlan: every reaction plan must name WHO acts, WHAT they do and what happens "
                  "to product made since the last good check — a reaction plan that says only "
                  "'investigate' is not a control.",
        "sheets": [
            {"name": "MultivariateData",
             "desc": "Two correlated process variables, 50 observations.",
             "cols": [("Observation", ""), ("ClampPressure_bar", ""), ("DwellTime_s", "")],
             "rows": rows},
            {"name": "ControlPlan",
             "desc": "The draft control plan — audit it and fill the gaps.",
             "cols": [("ProcessStep", ""), ("Characteristic", ""), ("Specification", ""),
                      ("MeasurementMethod", ""), ("SampleFrequency", ""), ("ControlMethod", ""),
                      ("ReactionPlan", "")],
             "rows": plan_rows},
        ],
    }


# --------------------------------------------------------------------------
# Lab 30 — benefit validation (ties back to Lab 1 COPQ)
# --------------------------------------------------------------------------
def _lab30():
    # Hard lines sum to exactly ANNUAL_HARD_BENEFIT; the soft line is reported
    # separately and must NOT be added to it. Before-column totals reconcile to
    # BASELINE_COPQ, the Lab 1 figure, so the project closes on the number it opened on.
    before_after = [
        ("Scrap — seal weld leak", 268_000, 96_000, "Hard", "Units x standard cost, MES scrap report"),
        ("Rework labour", 141_000, 52_000, "Hard", "Rework hours x loaded rate, timesheet extract"),
        ("Warranty returns", 187_000, 71_000, "Hard", "Warranty claims ledger, 12-month rolling"),
        ("Expedited freight", 94_000, 38_000, "Hard", "Freight invoices coded to expedite"),
        ("Inspection overtime", 63_000, 9_000, "Hard", "Payroll overtime cost centre"),
        ("Lost margin on missed OTIF", 59_000, 5_000, "Soft", "Contribution margin on late lines"),
    ]
    rows = [[n, b, a, b - a, k, src] for n, b, a, k, src in before_after]
    costs = [
        ("Fixture pressure interlock (6 lines)", 78_000, "Capital"),
        ("Electrode stroke counters", 14_500, "Capital"),
        ("Burst rig recalibration to 3-month interval", 9_200, "Recurring/yr"),
        ("Operator certification programme", 21_000, "One-off"),
        ("Black Belt project time (5 months)", 46_000, "One-off"),
    ]
    metrics = [
        ("Baseline Ppk (Lab 14)", 0.62), ("Improved Ppk (Lab 27)", 1.40),
        ("Baseline defect rate %", 2.90), ("Improved defect rate %", 1.21),
        ("Baseline sigma level", 2.90), ("Improved sigma level", 4.26),
        ("Baseline annual COPQ (SGD)", BASELINE_COPQ),
    ]
    return {
        "file": "lab-30-benefit-validation.xlsx",
        "kind": "data",
        "about": "Before/after cost data, implementation costs and the project's headline metrics — "
                 "validate the benefit the way Finance will.",
        "answer": f"Hard benefit = scrap 172k + rework 89k + warranty 116k + freight 56k + overtime "
                  f"54k = SGD {ANNUAL_HARD_BENEFIT:,} per year. The SGD 54k of 'lost margin' is SOFT "
                  f"(cost avoidance / capacity) and must be reported SEPARATELY — claiming it as hard "
                  f"savings is the single fastest way to lose Finance's sign-off. "
                  f"Implementation cost = SGD 168,700. Simple payback = 168,700 / {ANNUAL_HARD_BENEFIT:,} "
                  f"~ 0.35 years (about 4.2 months). Year-1 net benefit ~ SGD 318,300. "
                  f"Every line must name its validation SOURCE and be signed off by the Finance "
                  f"controller — an unsigned benefit is an estimate, not a benefit.",
        "sheets": [
            {"name": "BenefitValidation",
             "desc": "Annualised cost by category, before and after. Classify each one.",
             "cols": [("CostCategory", ""), ("Before_SGD", "Annualised"), ("After_SGD", "Annualised"),
                      ("Saving_SGD", ""), ("HardOrSoft", "YOU decide and defend it"),
                      ("ValidationSource", "How Finance verifies it")],
             "rows": rows},
            {"name": "ImplementationCost",
             "desc": "What it cost to get the improvement in.",
             "cols": [("Item", ""), ("Cost_SGD", ""), ("Type", "")],
             "rows": [list(c) for c in costs]},
            {"name": "ProjectMetrics",
             "desc": "Headline before/after metrics, carried from the earlier labs.",
             "cols": [("Metric", ""), ("Value", "")],
             "rows": [list(m) for m in metrics]},
        ],
    }


# --------------------------------------------------------------------------
# Template workbooks for the non-data labs
# --------------------------------------------------------------------------
def _template(num, fname, about, sheets, answer):
    return {"file": fname, "kind": "template", "about": about, "answer": answer, "sheets": sheets}


def _templates():
    t = {}

    t[1] = _template(1, "lab-01-project-selection-and-charter.xlsx",
        "A project selection matrix pre-loaded with six candidate projects, and a blank charter form.",
        [
            {"name": "SelectionMatrix",
             "desc": "Six candidates the sponsor put forward. Score, weight and rank them.",
             "cols": [("Candidate", ""), ("StatedAs", "Problem or Solution? — check this FIRST"),
                      ("StrategicFit_1to5", ""), ("AnnualBenefit_SGD", ""),
                      ("DataAvailability_1to5", ""), ("ScopeManageability_1to5", ""),
                      ("SponsorCommitment_1to5", ""), ("TechnicalRisk_1to5", ""),
                      ("WeightedScore", "YOU compute"), ("Accept/Reject", ""), ("RejectionReason", "")],
             "rows": [
                 ["Reduce seal weld leak defects on infusion pumps", "Problem", "", "", "", "", "", "", "", "", ""],
                 ["Deploy a new MES across all three plants", "Solution", "", "", "", "", "", "", "", "", ""],
                 ["Improve OTIF for hospital distributor orders", "Problem", "", "", "", "", "", "", "", "", ""],
                 ["Reduce warranty returns on occlusion sensors", "Problem", "", "", "", "", "", "", "", "", ""],
                 ["Cut inspection overtime in Suzhou", "Problem", "", "", "", "", "", "", "", "", ""],
                 ["Buy a second burst-test rig", "Solution", "", "", "", "", "", "", "", "", ""],
             ]},
            {"name": "COPQ",
             "desc": "Annualised Cost of Poor Quality for the project you select.",
             "cols": [("CostElement", ""), ("BasisOfEstimate", ""), ("Annualised_SGD", "")],
             "rows": [["Scrap", "", ""], ["Rework labour", "", ""], ["Warranty", "", ""],
                      ["Expedited freight", "", ""], ["Lost margin", "", ""],
                      ["Capacity consumed", "", ""], ["TOTAL", "", ""]]},
            {"name": "Charter",
             "desc": "The project charter. Every field is mandatory.",
             "cols": [("Element", ""), ("YourEntry", "")],
             "rows": [[e, ""] for e in [
                 "Business case", "Problem statement (4-part test: process / period / gap / impact)",
                 "Goal statement (SMART)", "Scope — IN", "Scope — OUT", "Preliminary Y",
                 "Baseline performance", "Target performance", "Team members", "Sponsor",
                 "Milestone — Define", "Milestone — Measure", "Milestone — Analyze",
                 "Milestone — Improve", "Milestone — Control", "Expected annual benefit (SGD)"]]},
        ],
        f"A defensible charter rejects both 'solution in disguise' candidates outright. Scored on "
        f"strategic fit and benefit, 'Reduce seal weld leak defects' wins — it has the largest COPQ "
        f"(~SGD {BASELINE_COPQ:,}/yr), accessible MES data and a named sponsor. Its problem statement "
        f"must contain NO cause and NO solution: 'Between Jan and Dec 2025, 2.9% of infusion pump "
        f"assemblies failed the seal weld burst test across three plants, costing SGD 812,000 in "
        f"scrap, rework and warranty.' This is the capstone project every later lab builds on.")

    t[2] = _template(2, "lab-02-portfolio-and-belt-roles.xlsx",
        "A portfolio of eight live projects to balance against strategy, plus a belt role matrix.",
        [
            {"name": "ProjectPortfolio",
             "desc": "Every improvement project currently running. Map them to the strategic pillars.",
             "cols": [("Project", ""), ("Sponsor", ""), ("Belt", ""), ("StrategicPillar", ""),
                      ("Benefit_SGD", ""), ("EffortMonths", ""), ("Status", ""),
                      ("AlignmentVerdict", "YOU judge")],
             "rows": [
                 ["Seal weld leak reduction", "VP Operations", "Black Belt", "Quality", 487_000, 5, "Active", ""],
                 ["Suzhou inspection overtime", "Plant Manager", "Green Belt", "Cost", 63_000, 3, "Active", ""],
                 ["Distributor order entry rework", "Commercial Dir", "Green Belt", "Customer", 41_000, 3, "Active", ""],
                 ["Warehouse 5S rollout", "Logistics Mgr", "Yellow Belt", "None stated", 8_000, 2, "Active", ""],
                 ["Occlusion sensor warranty", "Quality Dir", "Black Belt", "Quality", 168_000, 6, "Proposed", ""],
                 ["Penang line changeover time", "Plant Manager", "Green Belt", "Delivery", 92_000, 4, "Proposed", ""],
                 ["Canteen menu survey", "HR", "Yellow Belt", "None stated", 0, 1, "Active", ""],
                 ["Supplier durometer variation", "Supplier Quality", "Green Belt", "Quality", 74_000, 4, "Proposed", ""],
             ]},
            {"name": "BeltRoleMatrix",
             "desc": "Who does what. Fill in the responsibility for each belt level.",
             "cols": [("Activity", ""), ("Champion", ""), ("MasterBlackBelt", ""),
                      ("BlackBelt", ""), ("GreenBelt", ""), ("YellowBelt", "")],
             "rows": [[a, "", "", "", "", ""] for a in [
                 "Select and prioritise the project portfolio", "Remove organisational barriers",
                 "Charter approval and tollgate sign-off", "Lead cross-functional DMAIC projects",
                 "Apply advanced statistics (DOE, MSA, regression)", "Mentor and coach Green Belts",
                 "Lead a departmental DMAIC project", "Collect data and run the daily process",
                 "Validate financial benefits with Finance"]]},
        ],
        "Two projects ('Warehouse 5S rollout', 'Canteen menu survey') map to NO strategic pillar and "
        "should be stopped or handed to local management — they consume belt capacity for no strategic "
        "return. The portfolio is also unbalanced: 4 of 8 projects sit under Quality and none under "
        "Growth. On the role matrix, the Black Belt owns cross-functional DMAIC leadership, advanced "
        "statistics AND Green Belt mentoring — mentoring is the duty most often forgotten, and it is "
        "what distinguishes a Black Belt from a very good Green Belt.")

    t[3] = _template(3, "lab-03-baseline-sigma-calculator.xlsx",
        "Twelve months of production and defect counts — compute DPU, DPO, DPMO, yield, RTY and the "
        "baseline sigma level for your project Y.",
        [
            {"name": "MonthlyCounts",
             "desc": "Actual production and defect counts. 4 defect opportunities per unit.",
             "cols": [("Month", ""), ("UnitsProduced", ""), ("DefectsFound", ""),
                      ("UnitsWithAnyDefect", ""), ("Opportunities_per_Unit", ""),
                      ("DPU", "YOU compute"), ("DPO", "YOU compute"), ("DPMO", "YOU compute"),
                      ("Yield_pct", "YOU compute"), ("SigmaLevel", "YOU look up")],
             "rows": [[m, u, d, w, 4, "", "", "", "", ""] for m, u, d, w in [
                 ("2025-01", 4120, 143, 119), ("2025-02", 3890, 128, 108),
                 ("2025-03", 4310, 162, 131), ("2025-04", 4085, 139, 115),
                 ("2025-05", 4260, 151, 126), ("2025-06", 4198, 147, 122),
                 ("2025-07", 3975, 134, 111), ("2025-08", 4340, 168, 138),
                 ("2025-09", 4155, 144, 120), ("2025-10", 4280, 159, 129),
                 ("2025-11", 4092, 141, 117), ("2025-12", 3860, 126, 106)]]},
            {"name": "RTY",
             "desc": "First-pass yield at each of the six process steps.",
             "cols": [("Step", ""), ("UnitsIn", ""), ("UnitsPassedFirstTime", ""),
                      ("FPY", "YOU compute"), ("RTY_cumulative", "YOU compute")],
             "rows": [[s, i, p, "", ""] for s, i, p in [
                 ("Sub-assembly", 4200, 4116), ("Seal weld", 4116, 3996),
                 ("Sensor fit", 3996, 3960), ("Firmware load", 3960, 3944),
                 ("Burst test", 3944, 3830), ("Final pack", 3830, 3819)]]},
            {"name": "YfX",
             "desc": "Decompose your project Y into candidate Xs.",
             "cols": [("Y (output)", ""), ("Candidate X (input)", ""), ("Controllable?", ""),
                      ("How measured", ""), ("Evidence it drives Y", "")],
             "rows": [["Seal weld burst pressure (kPa)", "", "", "", ""] for _ in range(8)]},
        ],
        "Full-year totals: 49,565 units, 1,742 defects, 1,442 defective units. "
        "DPU = 1742/49565 = 0.0351. DPO = 0.0351/4 = 0.00878. DPMO = 8,784. "
        "Yield (units with no defect) = 97.1%, so the defect rate is 2.9% — the baseline every later "
        "lab quotes. From the DPMO table that is about 3.9 sigma at the OPPORTUNITY level, but only "
        "~2.9 sigma at the UNIT level; always state which one you mean. "
        "RTY = 0.980 x 0.971 x 0.991 x 0.996 x 0.971 x 0.997 = 0.909 — a 9.1% hidden factory that "
        "the final-yield number completely conceals. The seal weld and burst test steps are the two "
        "worst, which is exactly where the project is aimed.")

    t[4] = _template(4, "lab-04-voc-affinity-kano.xlsx",
        "Forty raw customer verbatims from hospital distributors and biomedical engineers — cluster "
        "them, translate them into requirements and classify them on the Kano model.",
        [
            {"name": "Verbatims",
             "desc": "Raw, unedited customer voice. Do NOT pre-sort these.",
             "cols": [("ID", ""), ("Source", ""), ("Verbatim", ""), ("AffinityCluster", "YOU assign"),
                      ("TranslatedRequirement", "YOU write"), ("KanoCategory", "YOU classify")],
             "rows": [[f"V{i:02d}", s, v, "", "", ""] for i, (s, v) in enumerate([
                 ("Distributor", "Three pumps out of the last shipment leaked on the ward."),
                 ("Biomed engineer", "When it fails it fails silently — that is what frightens me."),
                 ("Distributor", "Your delivery dates slip and nobody tells us."),
                 ("Nurse manager", "The alarm is too quiet in a busy ward."),
                 ("Biomed engineer", "I need the service manual to match the firmware version."),
                 ("Distributor", "Warranty claims take six weeks to settle."),
                 ("Procurement", "Price is fine. Reliability is not."),
                 ("Nurse manager", "Setting the dose takes too many button presses."),
                 ("Biomed engineer", "Spare seal rings are never in stock."),
                 ("Distributor", "Half a shipment arriving is worse than none."),
                 ("Nurse manager", "It should just work when I plug it in."),
                 ("Biomed engineer", "The burst test certificate is missing from the carton."),
                 ("Procurement", "We need 48-hour response on a clinical incident."),
                 ("Distributor", "Labels in the wrong language for the Thai market."),
                 ("Nurse manager", "Battery life is shorter than the spec says."),
                 ("Biomed engineer", "Calibration drifts within six months, not twelve."),
                 ("Distributor", "Give us a portal to track our order."),
                 ("Procurement", "Any leak is a patient safety event. Zero tolerance."),
                 ("Nurse manager", "Cleaning between patients takes too long."),
                 ("Biomed engineer", "Diagnostic codes are not documented anywhere."),
                 ("Distributor", "Your competitor ships in five days."),
                 ("Procurement", "We want a single point of contact."),
                 ("Nurse manager", "The screen is unreadable under ward lighting."),
                 ("Biomed engineer", "Firmware updates need a laptop and a cable — in 2026."),
                 ("Distributor", "Packaging is damaged on arrival about one carton in twenty."),
                 ("Procurement", "Documentation must satisfy the HSA audit."),
                 ("Nurse manager", "Occlusion alarm triggers falsely two or three times a shift."),
                 ("Biomed engineer", "I would love remote monitoring of pump status."),
                 ("Distributor", "Invoices do not match the delivery note."),
                 ("Procurement", "Lot traceability has to be end to end."),
                 ("Nurse manager", "Staff need less than an hour to learn it."),
                 ("Biomed engineer", "Seal ring failures are the top repair I see."),
                 ("Distributor", "Tell us early when you will be late. We can manage that."),
                 ("Procurement", "Total cost of ownership matters more than unit price."),
                 ("Nurse manager", "It is heavier than the model it replaced."),
                 ("Biomed engineer", "A self-test on power-up would save me a service call."),
                 ("Distributor", "Your OTIF is 84%. We need 97%."),
                 ("Procurement", "Any field failure triggers a corrective action report."),
                 ("Nurse manager", "The pole clamp slips."),
                 ("Biomed engineer", "Give me the burst pressure data per lot and I will trust you."),
             ], 1)]},
            {"name": "KanoReference",
             "desc": "The classification you are applying.",
             "cols": [("Category", ""), ("Meaning", ""), ("If absent", ""), ("If present", "")],
             "rows": [
                 ["Must-be", "Basic expectation, never stated unless missing", "Severe dissatisfaction", "No credit given"],
                 ["One-dimensional", "More is better, stated explicitly", "Dissatisfaction", "Satisfaction"],
                 ["Attractive", "Unexpected delighter", "No dissatisfaction", "Delight"],
                 ["Indifferent", "Customer does not care", "Nothing", "Nothing"],
                 ["Reverse", "Customer actively does not want it", "Satisfaction", "Dissatisfaction"],
             ]},
        ],
        "The 40 verbatims cluster into roughly six affinity groups: product reliability, delivery "
        "performance, documentation and traceability, usability, service and support, commercial. "
        "'No leaks' and 'documentation satisfies the HSA audit' are MUST-BE — you get zero credit for "
        "delivering them and a patient-safety event for missing them. 'OTIF 97%' and 'warranty "
        "settlement time' are ONE-DIMENSIONAL. 'Remote monitoring' and 'self-test on power-up' are "
        "ATTRACTIVE. Weight matters more than count: one procurement verbatim saying 'any leak is a "
        "patient safety event' outranks ten usability comments, and it is what points the project at "
        "seal weld integrity.")

    t[5] = _template(5, "lab-05-ctq-tree-flowdown.xlsx",
        "A CTQ tree worksheet that flows the must-be need down to measurable, controllable Xs.",
        [
            {"name": "CTQTree",
             "desc": "Need -> Driver -> Requirement -> Measure -> Target -> Spec.",
             "cols": [("CustomerNeed", "From Lab 4"), ("Driver", ""), ("CTQRequirement", ""),
                      ("Measure", "MUST be measurable"), ("Target", ""), ("LSL", ""), ("USL", ""),
                      ("DataSource", "")],
             "rows": [["The pump must not leak in the field", "Seal weld integrity",
                       "Seal weld withstands burst pressure", "Burst pressure (kPa)", 220, 180, 260,
                       "Burst test rig"]] + [["", "", "", "", "", "", "", ""] for _ in range(7)]},
            {"name": "CTQFlowdown",
             "desc": "Flow the CTQ down to the Xs you can actually control on the shop floor.",
             "cols": [("CTQ (Y)", ""), ("Process step", ""), ("Candidate X", ""),
                      ("Controllable / Noise", ""), ("Current control", ""), ("Measurable?", "")],
             "rows": [["Burst pressure (kPa)", "", "", "", "", ""] for _ in range(10)]},
            {"name": "OperationalDefinitions",
             "desc": "An operational definition every person would apply identically.",
             "cols": [("Term", ""), ("Definition", ""), ("Instrument", ""), ("DecisionRule", ""),
                      ("Unit", "")],
             "rows": [["Leak", "", "", "", ""], ["Defective unit", "", "", "", ""],
                      ["First pass", "", "", "", ""], ["On time", "", "", "", ""]]},
        ],
        "The flowdown must end at Xs a shift supervisor can change before lunch: fixture clamp "
        "pressure (bar), weld dwell time (s), electrode tip age (strokes) and seal ring durometer "
        "(Shore A). Ambient temperature and humidity are NOISE — you can measure them but not "
        "economically control them, so they belong in a robustness study (Lab 25), not a control "
        "plan. A CTQ that stops at 'improve quality' has not been flowed down. Note how the burst "
        "pressure measure, target and spec here are the SAME numbers used in Labs 14, 23-25 and 27 — "
        "that is the flowdown holding together across the whole project.")

    t[6] = _template(6, "lab-06-sipoc-process-map.xlsx",
        "A SIPOC frame and a swimlane step list for the seal weld process, with handoff analysis.",
        [
            {"name": "SIPOC",
             "desc": "Fill each column. Start with P, then O and C, then I and S.",
             "cols": [("Suppliers", ""), ("Inputs", ""), ("Process (5-7 steps)", ""),
                      ("Outputs", ""), ("Customers", "")],
             "rows": [["", "", "", "", ""] for _ in range(7)]},
            {"name": "ProcessSteps",
             "desc": "The detailed step list. Classify each step and find the handoffs.",
             "cols": [("Step#", ""), ("Activity", ""), ("Role/Swimlane", ""),
                      ("CycleTime_min", ""), ("WaitTime_min", ""),
                      ("VA / BVA / NVA", "YOU classify"), ("IsHandoff", ""), ("DefectRisk", "")],
             "rows": [[i, a, r, ct, wt, "", "", ""] for i, (a, r, ct, wt) in enumerate([
                 ("Kit seal rings and housings", "Material handler", 4, 35),
                 ("Load fixture and clamp", "Line operator", 2, 0),
                 ("Verify clamp pressure gauge", "Line operator", 1, 0),
                 ("Run weld cycle", "Welder (auto)", 3, 0),
                 ("Unload and visual inspect", "Line operator", 2, 12),
                 ("Transfer to burst test station", "Material handler", 1, 48),
                 ("Run burst test (sample)", "Test technician", 6, 0),
                 ("Record result in MES", "Test technician", 2, 0),
                 ("Route pass to assembly", "Material handler", 1, 22),
                 ("Route fail to rework cell", "Rework operator", 1, 96),
                 ("Rework and re-test", "Rework operator", 18, 0),
                 ("Final disposition", "Quality inspector", 3, 14),
             ], 1)]},
            {"name": "ScopeGovernance",
             "desc": "Agree the boundaries with the sponsor BEFORE Measure starts.",
             "cols": [("Item", ""), ("IN scope", ""), ("OUT of scope", ""), ("Agreed by", "")],
             "rows": [[i, "", "", ""] for i in [
                 "Process start point", "Process end point", "Products included", "Plants included",
                 "Shifts included", "Time period of data", "Customer segments"]]},
        ],
        "Total cycle time is 44 min against 227 min of wait time — process cycle efficiency = "
        "44/271 = 16%, so 84% of lead time is pure waiting. Only 'Run weld cycle' and 'Rework and "
        "re-test' transform the product; the burst test is BVA (required by the regulator, adds no "
        "customer value); every transfer and queue is NVA. There are five HANDOFFS, and the two "
        "biggest wait times sit immediately after them. The scope sheet is what stops scope creep in "
        "week three: without a written start point ('fixture load') and end point ('final "
        "disposition'), the team will be asked to fix incoming material quality too.")

    t[7] = _template(7, "lab-07-stakeholder-analysis.xlsx",
        "Twelve named stakeholders on this project — map their influence and support, and plan the "
        "specific action that moves each one.",
        [
            {"name": "StakeholderMap",
             "desc": "Be honest about current support. A map that says everyone is supportive is wrong.",
             "cols": [("Stakeholder", ""), ("Role", ""), ("Influence_1to5", ""),
                      ("CurrentSupport", "Opposed/Neutral/Supportive/Champion"),
                      ("RequiredSupport", ""), ("WhatTheyCareAbout", ""),
                      ("Gap", "YOU assess"), ("SpecificAction", "YOU plan"), ("By when", "")],
             "rows": [[n, r, "", cs, "", "", "", "", ""] for n, r, cs in [
                 ("VP Operations", "Project sponsor", "Champion"),
                 ("Suzhou Plant Manager", "Owns the worst-performing plant", "Opposed"),
                 ("Singapore Plant Manager", "Owns the reference plant", "Supportive"),
                 ("Penang Plant Manager", "Process owner", "Neutral"),
                 ("Quality Director", "Regulatory accountability", "Supportive"),
                 ("Manufacturing Engineering Lead", "Owns the fixture design", "Opposed"),
                 ("Night shift supervisor, Suzhou", "Runs the worst-performing cell", "Opposed"),
                 ("Finance Controller", "Signs off the benefit", "Neutral"),
                 ("Supplier Quality Manager", "Owns the seal ring supplier", "Neutral"),
                 ("Line operators (x22)", "Do the work", "Neutral"),
                 ("Maintenance Manager", "Must add the interlock", "Neutral"),
                 ("Regulatory Affairs", "Approves any process change", "Supportive"),
             ]]},
            {"name": "RACI",
             "desc": "One A per row. Never two.",
             "cols": [("Deliverable", ""), ("BlackBelt", ""), ("Sponsor", ""), ("ProcessOwner", ""),
                      ("Finance", ""), ("Quality", ""), ("Operators", "")],
             "rows": [[d, "", "", "", "", "", ""] for d in [
                 "Project charter", "Data collection plan", "MSA study", "Baseline capability",
                 "Root cause validation", "DOE execution", "Pilot approval", "Control plan",
                 "Benefit validation", "Handover to process owner"]]},
            {"name": "ResistanceLog",
             "desc": "Resistance is data. Log the real objection, not the polite one.",
             "cols": [("Who", ""), ("StatedObjection", ""), ("UnderlyingConcern", ""),
                      ("Type", "Technical / Political / Cultural"), ("Response", "")],
             "rows": [["", "", "", "", ""] for _ in range(6)]},
        ],
        "Three stakeholders are both HIGH influence and OPPOSED — the Suzhou Plant Manager, the "
        "Manufacturing Engineering Lead and the Suzhou night shift supervisor. They are exactly the "
        "people whose process the data has just criticised, so their resistance is predictable and "
        "usually political rather than technical: the Lab 15 and Lab 19 findings say their cell is the "
        "problem. Treating that as a communication task ('they need to understand the data') is the "
        "classic Black Belt failure. The action that moves them is co-ownership — put the Engineering "
        "Lead on the DOE team so the fixture fix is HIS, and let the Suzhou manager present the "
        "improvement to the steering committee. The Finance Controller must move from Neutral to "
        "Supportive before Lab 30, or the benefit will not be signed.")

    t[8] = _template(8, "lab-08-value-stream-map.xlsx",
        "Timed process data for the current-state value stream map, with the eight wastes observation "
        "log and a takt time calculator.",
        [
            {"name": "ValueStreamData",
             "desc": "One row per process box. This is what goes on the current-state VSM.",
             "cols": [("ProcessStep", ""), ("CycleTime_s", ""), ("ChangeoverTime_min", ""),
                      ("Uptime_pct", ""), ("Operators", ""), ("WIP_units_after", ""),
                      ("FirstPassYield_pct", ""), ("ValueAdded", "YOU classify")],
             "rows": [[s, ct, co, up, op, wip, fpy, ""] for s, ct, co, up, op, wip, fpy in [
                 ("Kitting", 240, 12, 96, 1, 420, 99.4),
                 ("Seal weld", 180, 35, 88, 2, 310, 97.1),
                 ("Sensor fit", 210, 8, 94, 2, 185, 99.1),
                 ("Firmware load", 95, 2, 99, 1, 140, 99.6),
                 ("Burst test", 360, 0, 91, 1, 260, 97.1),
                 ("Final pack", 150, 15, 97, 2, 95, 99.7),
             ]]},
            {"name": "TaktTime",
             "desc": "Compute takt and compare it to each step's cycle time.",
             "cols": [("Input", ""), ("Value", "")],
             "rows": [["Shifts per day", 2], ["Hours per shift", 8], ["Breaks per shift (min)", 45],
                      ["Planned maintenance per day (min)", 30], ["Working days per month", 22],
                      ["Customer demand per month (units)", 4200],
                      ["Available time per day (s)", "YOU compute"],
                      ["Takt time (s/unit)", "YOU compute"],
                      ["Bottleneck step", "YOU identify"]]},
            {"name": "EightWastes",
             "desc": "Log what you actually observe — DOWNTIME.",
             "cols": [("Waste", ""), ("Observed at", ""), ("Evidence", ""),
                      ("Estimated cost/yr", ""), ("Countermeasure", "")],
             "rows": [[w, "", "", "", ""] for w in [
                 "D — Defects", "O — Overproduction", "W — Waiting", "N — Non-utilised talent",
                 "T — Transport", "I — Inventory", "M — Motion", "E — Extra-processing"]]},
        ],
        "Available time = 2 shifts x (480 - 45) min - 30 min = 840 min = 50,400 s/day. Demand = "
        "4200/22 = 191 units/day. TAKT = 50,400/191 = 264 s/unit. "
        "Only ONE step exceeds takt: Burst test at 360 s — it is the bottleneck and it constrains the "
        "whole line. Seal weld at 180 s is well inside takt, so the seal weld problem is a QUALITY "
        "problem, not a speed problem; do not try to fix it with more capacity. "
        "Total WIP is 1,410 units against 191/day of demand = 7.4 days of inventory sitting between "
        "steps. Value-added time is 1,235 s out of a 7.4-day lead time — a process cycle efficiency "
        "near 0.2%, which is typical and always shocking the first time a team computes it. "
        "The dominant wastes are Waiting (queues after every handoff) and Defects (the 2.9% that "
        "flows to rework), and Defects is where the capstone project attacks.")

    t[21] = _template(21, "lab-21-analyze-tollgate-evidence.xlsx",
        "The evidence register for the Analyze tollgate — every claimed root cause, the statistical "
        "test that proves it, and the p-value.",
        [
            {"name": "EvidenceRegister",
             "desc": "A root cause with no test result beside it is an opinion. Fill this from Labs 15-20.",
             "cols": [("ClaimedRootCause", ""), ("FromLab", ""), ("TestUsed", ""),
                      ("TestStatistic", ""), ("p-value", ""), ("PracticalEffectSize", ""),
                      ("Verdict", "Proven / Not proven"), ("EvidenceStrength", "")],
             "rows": [[c, lab, "", "", "", "", "", ""] for c, lab in [
                 ("Clamp pressure drives burst pressure", "Lab 18"),
                 ("Dwell time drives burst pressure", "Lab 18"),
                 ("Electrode tip wear drives burst pressure", "Lab 18"),
                 ("Seal ring supplier C is different", "Lab 19"),
                 ("Suzhou shift C is the bad cell", "Labs 15, 17, 19"),
                 ("Line 3 differs from Lines 1 and 2", "Lab 20"),
                 ("Defect mode depends on plant", "Lab 20"),
                 ("Ambient temperature drives burst pressure", "Lab 18"),
                 ("Humidity drives burst pressure", "Lab 18"),
             ]]},
            {"name": "TollgateChecklist",
             "desc": "The sponsor will ask these. Have the answer.",
             "cols": [("Question", ""), ("YourAnswer", ""), ("Artifact that proves it", "")],
             "rows": [[q, "", ""] for q in [
                 "Is the measurement system capable?",
                 "Is the baseline capability established and stable?",
                 "Which Xs are statistically proven to drive Y?",
                 "Which candidate causes were DISPROVEN, and how?",
                 "Is the effect practically significant, not just statistically significant?",
                 "What is the estimated benefit if these Xs are controlled?",
                 "What are the risks of moving to Improve?"]]},
        ],
        "Proven: clamp pressure (p<0.001), dwell time (p<0.001), electrode tip age (p<0.001), supplier "
        "C (Tukey, p<0.01), the Suzhou-shift-C interaction (p<0.001) and line-to-line as the dominant "
        "multi-vari family. NOT proven: ambient temperature (p~0.09) and humidity (not significant, "
        "and collinear with temperature). "
        "Disproving causes matters as much as proving them — it is what stops the team spending "
        "SGD 200k on shop-floor air conditioning. Note the distinction the sponsor will probe: a "
        "0.11 kPa/degC temperature effect could become statistically significant with a big enough "
        "sample and still be practically worthless against an 80 kPa spec width.")

    t[22] = _template(22, "lab-22-solution-selection.xlsx",
        "Candidate solutions generated against the proven root causes — screen and score them into an "
        "implementation set.",
        [
            {"name": "SolutionScreening",
             "desc": "Generate against PROVEN causes only (Lab 21). Score, then rank.",
             "cols": [("Solution", ""), ("AttacksWhichX", ""), ("Type", "Error-proof / Control / Training / Capital"),
                      ("Impact_1to5", ""), ("Effort_1to5", ""), ("Cost_SGD", ""),
                      ("TimeToImplement_wks", ""), ("RiskOfSideEffect_1to5", ""),
                      ("WeightedScore", "YOU compute"), ("Decision", "")],
             "rows": [[s, x, t, "", "", c, w, "", "", ""] for s, x, t, c, w in [
                 ("Fixture clamp pressure interlock (line stops below 44 bar)", "Clamp pressure", "Error-proof", 78_000, 8),
                 ("PLC recipe lock on dwell time", "Dwell time", "Error-proof", 6_500, 2),
                 ("Electrode stroke counter with auto-flag at 600", "Tip wear", "Error-proof", 14_500, 3),
                 ("Daily clamp pressure check sheet", "Clamp pressure", "Control", 0, 1),
                 ("Operator certification programme", "Method variation", "Training", 21_000, 12),
                 ("Switch away from seal ring supplier C", "Supplier variation", "Control", 4_000, 6),
                 ("100% burst testing", "Detection", "Control", 240_000, 4),
                 ("Replace all six welders", "Everything", "Capital", 1_450_000, 26),
                 ("Written shift handover with recipe sign-off", "Method variation", "Control", 0, 1),
                 ("Shop floor air conditioning", "Ambient temp", "Capital", 210_000, 16),
             ]]},
            {"name": "SolutionSelectionMatrix",
             "desc": "Weight the criteria, then justify the cut line.",
             "cols": [("Criterion", ""), ("Weight", ""), ("Rationale", "")],
             "rows": [[c, "", ""] for c in [
                 "Impact on Y", "Implementation cost", "Time to implement",
                 "Sustainability without supervision", "Risk of unintended consequence",
                 "Operator acceptance"]]},
        ],
        "Two candidates must be struck immediately: 'Shop floor air conditioning' attacks a cause "
        "Lab 21 DISPROVED, and 'Replace all six welders' is a SGD 1.45m capital solution that no "
        "evidence supports. '100% burst testing' is the seductive wrong answer — it is pure "
        "inspection, it adds SGD 240k of cost, it does not reduce variation, and it is the opposite "
        "of what Control means in Six Sigma. "
        "The winning set is error-proofing first: clamp pressure interlock, PLC recipe lock and "
        "stroke counter — together SGD 99,000, they attack all three proven Xs, and they hold without "
        "anyone remembering to do anything. Note the hierarchy: ERROR-PROOF beats CONTROL beats "
        "TRAINING, because training decays the moment the trainer leaves the room.")

    t[31] = _template(31, "lab-31-a3-storyboard.xlsx",
        "The A3 storyboard skeleton and an artifact traceability register that maps every lab output "
        "onto its panel.",
        [
            {"name": "A3Storyboard",
             "desc": "One page. If it does not fit on one page it is not an A3.",
             "cols": [("Panel", ""), ("WhatGoesHere", ""), ("YourContent", ""),
                      ("SourceLab", ""), ("VisualUsed", "")],
             "rows": [[p, w, "", sl, ""] for p, w, sl in [
                 ("1. Background", "Why this project, why now", "Lab 1"),
                 ("2. Current condition", "Baseline with DATA, not adjectives", "Labs 3, 14, 15"),
                 ("3. Goal", "SMART target with the number", "Lab 1"),
                 ("4. Root cause analysis", "The proven Xs and the test that proved each", "Labs 16-21"),
                 ("5. Countermeasures", "What you changed and why that attacks the cause", "Labs 22-25"),
                 ("6. Implementation plan", "Who, what, when", "Lab 26"),
                 ("7. Confirmed results", "Before/after with the same measure", "Labs 27, 30"),
                 ("8. Follow-up / standardise", "Control plan, owner, spread", "Labs 29, 30"),
             ]]},
            {"name": "ArtifactRegister",
             "desc": "Every capstone artifact you produced. Tick what is done.",
             "cols": [("Lab", ""), ("Artifact", ""), ("Complete?", ""), ("Used on A3 panel", ""),
                      ("In the appendix", "")],
             "rows": [[f"Lab {n}", "", "", "", ""] for n in range(1, 31)]},
        ],
        "The A3 discipline is subtraction, not addition. Thirty labs produced far more than one page "
        "holds, so the register exists to decide what goes on the A3 and what goes in the appendix "
        "pack you bring to the room but do not present. Panel 2 must carry the baseline Ppk of 0.62 "
        "and panel 7 the improved 1.40, measured the SAME way — the single most common capstone "
        "failure is a before/after comparison using two different measurement definitions, which the "
        "steering committee will spot immediately.")

    t[32] = _template(32, "lab-32-steering-committee-deck.xlsx",
        "A slide-by-slide plan for the 15-minute steering committee presentation, plus the anticipated "
        "challenge log.",
        [
            {"name": "SlidePlan",
             "desc": "15 minutes. Ten slides maximum. One message per slide.",
             "cols": [("Slide", ""), ("Message (a full sentence, not a topic)", ""),
                      ("Evidence/Visual", ""), ("SourceLab", ""), ("Minutes", "")],
             "rows": [[i, "", "", "", ""] for i in range(1, 11)]},
            {"name": "ChallengeLog",
             "desc": "Prepare the answer BEFORE you are asked it in the room.",
             "cols": [("AnticipatedChallenge", ""), ("WhoWillAskIt", ""), ("YourAnswer", ""),
                      ("BackupSlide", "")],
             "rows": [[c, "", "", ""] for c in [
                 "How do we know the measurement system is trustworthy?",
                 "Could the improvement be a coincidence / the Hawthorne effect?",
                 "Why should we believe the SGD 487,000?",
                 "What happens when the Black Belt moves to the next project?",
                 "Why did you not just inspect 100%?",
                 "Will this hold at the other two plants?",
                 "What did you get wrong?",
             ]]},
        ],
        "Executives buy the RESULT and the CONTROL, not the method. Lead with the answer — slide 1 "
        "states the benefit and the capability gain — then spend the middle proving it and the end on "
        "sustainment. The commonest Black Belt error is presenting DMAIC chronologically, which puts "
        "the punchline on slide 9 after the audience has stopped listening. "
        "Every challenge in the log has a real answer from the labs: the MSA (Lab 11-12) answers "
        "trustworthiness, the control chart with recalculated limits (Lab 27) answers coincidence, "
        "the Finance-signed benefit sheet (Lab 30) answers the money, and the control plan with a "
        "named owner (Lab 29) answers what happens when you leave.")

    t[33] = _template(33, "lab-33-capstone-defence-rubric.xlsx",
        "The rubric your capstone is assessed against, plus a peer-review form for the labs you "
        "observe.",
        [
            {"name": "DefenceRubric",
             "desc": "Self-assess honestly before you present. This is how you will be marked.",
             "cols": [("Criterion", ""), ("Weight_pct", ""), ("WhatExcellentLooksLike", ""),
                      ("SelfScore_1to5", ""), ("Evidence", "")],
             "rows": [[c, w, e, "", ""] for c, w, e in [
                 ("Problem definition and charter", 10, "Problem statement passes the 4-part test; no cause, no solution"),
                 ("Measurement system validity", 15, "MSA run, result acted on, capability computed on trusted data"),
                 ("Baseline and capability", 10, "Stable baseline with the right capability index and the right distribution"),
                 ("Root cause rigour", 20, "Every claimed cause has a named test and a p-value; causes were also disproven"),
                 ("Solution logic", 15, "Solutions attack proven Xs; error-proofing preferred over inspection"),
                 ("Control and sustainment", 15, "Control plan names owner, method, frequency and reaction plan"),
                 ("Benefit validation", 10, "Hard and soft separated; Finance sign-off obtained"),
                 ("Communication and defence", 5, "Answers challenge without defensiveness; admits what is uncertain"),
             ]]},
            {"name": "PeerReview",
             "desc": "Review two other capstones. Specific beats kind.",
             "cols": [("Presenter", ""), ("StrongestElement", ""), ("WeakestElement", ""),
                      ("OneQuestionYouWouldAsk", ""), ("OneThingYouWillSteal", "")],
             "rows": [["", "", "", "", ""] for _ in range(2)]},
        ],
        "Root cause rigour carries the heaviest weight (20%) because it is what separates a Black Belt "
        "from an enthusiastic problem solver: anyone can propose a cause, a Black Belt proves it and "
        "disproves the rest. The two criteria candidates most often fail are measurement system "
        "validity (they skip the MSA, or run it and ignore the failure) and control (a control plan "
        "with no named owner and no reaction plan). Under challenge, 'we did not test that, and here "
        "is what it would take to test it' scores higher than a confident guess.")

    t[34] = _template(34, "lab-34-lessons-learned-mentoring.xlsx",
        "A lessons-learned register, a Green Belt mentoring plan and your personal Black Belt "
        "development plan.",
        [
            {"name": "LessonsLearned",
             "desc": "What you would do differently. Be specific enough to be useful to someone else.",
             "cols": [("DMAICPhase", ""), ("WhatWentWell", ""), ("WhatDidNot", ""),
                      ("RootCauseOfTheProblem", ""), ("WhatYouWouldDoDifferently", ""),
                      ("WhoElseNeedsToKnow", "")],
             "rows": [[p, "", "", "", "", ""] for p in
                      ["Define", "Measure", "Analyze", "Improve", "Control", "Overall"]]},
            {"name": "MentoringPlan",
             "desc": "You now mentor Green Belts. Plan the first 90 days for each.",
             "cols": [("GreenBelt", ""), ("TheirProject", ""), ("CurrentDMAICPhase", ""),
                      ("TheirBiggestRisk", ""), ("CoachingApproach", "Tell / Ask / Show / Delegate"),
                      ("NextCheckpoint", ""), ("WhatSuccessLooksLike", "")],
             "rows": [[g, p, ph, "", "", "", ""] for g, p, ph in [
                 ("Green Belt A", "Suzhou inspection overtime", "Measure"),
                 ("Green Belt B", "Distributor order entry rework", "Define"),
                 ("Green Belt C", "Penang line changeover time", "Analyze"),
                 ("Green Belt D", "Supplier durometer variation", "Define"),
             ]]},
            {"name": "DevelopmentPlan",
             "desc": "Your own next 12 months.",
             "cols": [("Area", ""), ("CurrentConfidence_1to5", ""), ("TargetConfidence", ""),
                      ("HowYouWillCloseIt", ""), ("By when", "")],
             "rows": [[a, "", "", "", ""] for a in [
                 "Advanced MSA (nested, destructive)", "Design of experiments",
                 "Response surface and robust design", "Multivariate SPC",
                 "Change leadership and resistance", "Mentoring and coaching",
                 "Financial benefit validation", "Executive communication"]]},
        ],
        "The mentoring sheet is the real Black Belt content here. The coaching approach must match the "
        "Green Belt's phase and confidence, not your preference: ASK when they have the capability and "
        "lack confidence, SHOW when the tool is genuinely new, TELL only where safety or regulatory "
        "compliance is at stake, and DELEGATE once they have done it successfully unaided. The "
        "commonest failure of a new Black Belt is doing the Green Belt's analysis FOR them — it "
        "produces a correct chart and no capability, and the Green Belt never leads the next one. "
        "Note that the four Green Belt projects here are the same ones from the Lab 2 portfolio, so "
        "the mentoring load is a real, traceable consequence of the portfolio you balanced on Day 1.")

    return t


# --------------------------------------------------------------------------
# Public registry
# --------------------------------------------------------------------------
def build_registry():
    reg = {}
    for num, spec in _templates().items():
        reg[num] = [spec]
    for num, fn in [
        (9, _lab09), (10, _lab10), (11, _lab11), (12, _lab12), (13, _lab13),
        (14, _lab14), (15, _lab15), (16, _lab16), (17, _lab17), (18, _lab18),
        (19, _lab19), (20, _lab20), (23, _lab23), (24, _lab24), (25, _lab25),
        (26, _lab26), (27, _lab27), (28, _lab28), (29, _lab29), (30, _lab30),
    ]:
        reg[num] = [fn()]
    return reg


DATASETS = build_registry()


def dataset_files(num):
    """Filenames only — used by the LG/LP/PPT builders to cite the same data."""
    return [d["file"] for d in DATASETS.get(num, [])]


def has_data(num):
    return any(d["kind"] == "data" for d in DATASETS.get(num, []))


if __name__ == "__main__":
    tot = 0
    for n in sorted(DATASETS):
        for d in DATASETS[n]:
            rows = sum(len(s["rows"]) for s in d["sheets"])
            tot += rows
            print(f"Lab {n:2d}  {d['kind']:8s}  {len(d['sheets'])} sheet(s)  "
                  f"{rows:5d} rows  {d['file']}")
    print(f"\n{len(DATASETS)} labs with workbooks, {tot} data rows total")
