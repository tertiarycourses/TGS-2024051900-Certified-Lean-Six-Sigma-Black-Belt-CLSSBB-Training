<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 22

## Solution Generation, Selection and Lean Countermeasures — In Depth

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Generate and select improvements targeting your proven root causes (A5).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-22-solution-selection.xlsx`**

Two candidates must be struck immediately: 'Shop floor air conditioning' attacks a cause Lab 21 DISPROVED, and 'Replace all six welders' is a SGD 1.45m capital solution that no evidence supports. '100% burst testing' is the seductive wrong answer — it is pure inspection, it adds SGD 240k of cost, it does not reduce variation, and it is the opposite of what Control means in Six Sigma. The winning set is error-proofing first: clamp pressure interlock, PLC recipe lock and stroke counter — together SGD 99,000, they attack all three proven Xs, and they hold without anyone remembering to do anything. Note the hierarchy: ERROR-PROOF beats CONTROL beats TRAINING, because training decays the moment the trainer leaves the room.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Every solution traces to a proven root cause, criteria weights are agreed with the sponsor, and your selected set collectively addresses the majority of the quantified Y gap.

## Where this sits in the capstone

Re-derive solution generation and the full Lean countermeasure toolkit, then select rigorously with a weighted matrix. Every solution must attack a PROVEN root cause from Lab 21 — solutions that address unproven causes are how projects quietly fail. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
