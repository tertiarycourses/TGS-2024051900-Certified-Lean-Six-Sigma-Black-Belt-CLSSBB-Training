<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 26

## FMEA, Pilot Design and Implementation Planning — In Depth

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** De-risk and pilot your capstone improvement before full rollout (A5).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-26-fmea-worksheet.xlsx`**

Scored realistically, the two highest RPNs are 'Fixture clamp pressure drifts during shift' (S=8, O=7, D=8, RPN=448) and 'Electrode tip wears past service limit' (S=7, O=6, D=8, RPN=336) — both scoring high on DETECTION because nothing catches them before the burst test. That is the argument for the Lab 27 control plan: a clamp-pressure interlock and a tip stroke counter attack Detection, which is the cheapest of the three to improve. Any mode with S=9 or 10 is actioned regardless of RPN.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your FMEA is re-scored post-mitigation with the severity override applied, pilot success criteria were defined before starting, and the improvement is tested statistically against the documented baseline.

## Where this sits in the capstone

Re-derive FMEA in full, then design the pilot that proves your improvement works before it is scaled. A Black Belt never rolls out an unpiloted change across sites — the cost of being wrong at scale is exactly what the pilot buys down. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
