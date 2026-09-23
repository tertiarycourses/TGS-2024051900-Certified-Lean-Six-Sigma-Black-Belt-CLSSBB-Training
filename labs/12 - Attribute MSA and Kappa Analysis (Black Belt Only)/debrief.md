<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 12

## Attribute MSA and Kappa Analysis (Black Belt Only)

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Validate a judgement-based measurement system using attribute agreement and Kappa (A4, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-12-attribute-msa-kappa.xlsx`**

Within-appraiser agreement: Chandra ~80%, Wei ~78%, Faridah ~62%. Appraiser-vs-standard agreement: Chandra ~80%, Wei ~76%, Faridah ~58%, giving Kappa ~0.55, ~0.48 and ~0.18 respectively — only Chandra is even marginal, and Faridah is barely better than chance. No appraiser reaches the 90% / Kappa 0.75 bar. The visual pass/fail criterion is not operationally defined; publish a boundary-sample board and re-train before using any attribute data.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your study includes borderline items and a known standard, you have computed within-appraiser, between-appraiser and versus-standard agreement plus Kappa, and you have an action plan for any Kappa below 0.75.

## Where this sits in the capstone

BLACK BELT ONLY — the Green Belt course does not teach this. When the measurement is a human judgement (pass/fail, cosmetic grade, claim approve/reject), Gage R&R does not apply at all. Attribute agreement analysis and Cohen's/Fleiss' Kappa are the correct tools, and most organisations discover their inspectors agree far less than assumed. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
