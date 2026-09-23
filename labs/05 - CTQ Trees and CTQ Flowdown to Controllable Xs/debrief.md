<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 5

## CTQ Trees and CTQ Flowdown to Controllable Xs

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Translate VOC into measurable CTQs and cascade a business Y down to controllable Xs (A1, A4).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-05-ctq-tree-flowdown.xlsx`**

The flowdown must end at Xs a shift supervisor can change before lunch: fixture clamp pressure (bar), weld dwell time (s), electrode tip age (strokes) and seal ring durometer (Shore A). Ambient temperature and humidity are NOISE — you can measure them but not economically control them, so they belong in a robustness study (Lab 25), not a control plan. A CTQ that stops at 'improve quality' has not been flowed down. Note how the burst pressure measure, target and spec here are the SAME numbers used in Labs 14, 23-25 and 27 — that is the flowdown holding together across the whole project.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Every CTQ has an operational definition, a target and specification limits, and your flowdown reaches at least one layer of Xs that are directly controllable and testable.

## Where this sits in the capstone

A customer need is not measurable; a CTQ is. Re-derive the CTQ tree in full, then go beyond Green Belt with CTQ FLOWDOWN — cascading a business-level Y through sub-Ys until you reach process Xs a team can actually control. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
