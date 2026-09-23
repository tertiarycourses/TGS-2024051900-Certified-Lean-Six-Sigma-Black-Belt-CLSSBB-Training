<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 9

## Data Types, Operational Definitions and the Data Collection Plan

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Build a rigorous data collection plan for your capstone (A4).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-09-data-collection-raw-extract.xlsx`**

The extract contains 3 missing burst-pressure values (rows MMD-4137, 4218, 4301), 2 unit errors recorded in Pa instead of kPa (MMD-4164, 4255), one impossible negative value (MMD-4193), and an inconsistent PASS/FAIL vocabulary (PASS/PASS /pass/Pass). A sound operational definition must specify the unit, the measurement instrument, the decision rule and a single allowed vocabulary.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Every capstone metric has a written operational definition that two people apply identically, stratification fields are captured at source, and the plan has survived a dry run.

## Where this sits in the capstone

Re-derive data classification and operational definitions in full, then build the data collection plan that will feed every statistical test in Days 3 and 4. Bad data collected now cannot be rescued by clever statistics later. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

## The running process — figures that must reconcile

| Checkpoint | Value | Established in |
|---|---|---|
| Baseline defect rate | 2.9% | Lab 3 |
| Measurement system | FAILS Gage R&R (~40% study variation) | Lab 11 |
| Baseline capability | Pp 0.62 / Ppk 0.53 | Lab 14 |
| Proven Xs | clamp pressure, dwell time, electrode tip age | Labs 18-21 |
| DOE optimum | clamp 47.4 bar, dwell 2.76 s | Labs 23-25 |
| Improved capability | Ppk 1.40 | Lab 27 |
| Annual hard benefit | SGD 487,000 vs SGD 812,000 COPQ | Labs 1, 30 |

If a learner's number disagrees with the column above, they have either used their own workplace data (fine — say so) or made an error (find it).

---

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd · TRAINER ONLY*
