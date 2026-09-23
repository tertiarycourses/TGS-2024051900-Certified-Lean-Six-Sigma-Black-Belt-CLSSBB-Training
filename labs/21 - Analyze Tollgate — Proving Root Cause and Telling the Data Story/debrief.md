<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 21

## Analyze Tollgate — Proving Root Cause and Telling the Data Story

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Consolidate your analysis into a defensible root cause conclusion (A3, K1).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-21-analyze-tollgate-evidence.xlsx`**

Proven: clamp pressure (p<0.001), dwell time (p<0.001), electrode tip age (p<0.001), supplier C (Tukey, p<0.01), the Suzhou-shift-C interaction (p<0.001) and line-to-line as the dominant multi-vari family. NOT proven: ambient temperature (p~0.09) and humidity (not significant, and collinear with temperature). Disproving causes matters as much as proving them — it is what stops the team spending SGD 200k on shop-floor air conditioning. Note the distinction the sponsor will probe: a 0.11 kPa/degC temperature effect could become statistically significant with a big enough sample and still be practically worthless against an 80 kPa spec width.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Every candidate cause carries a verdict, proven causes are triangulated across multiple methods and quantified in dollars, and you have rehearsed a prepared response to each expected challenge.

## Where this sits in the capstone

The Analyze tollgate. Consolidate everything from Labs 15-20 into a proven root cause set, translate the statistics into business language, and rehearse the challenges you will face. Sponsors do not fund p-values; they fund decisions. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
