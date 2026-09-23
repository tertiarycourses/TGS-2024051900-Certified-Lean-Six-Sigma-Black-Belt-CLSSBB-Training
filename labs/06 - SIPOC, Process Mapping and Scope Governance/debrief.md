<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 6

## SIPOC, Process Mapping and Scope Governance

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Map your capstone process and govern its scope through the charter (A2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-06-sipoc-process-map.xlsx`**

Total cycle time is 44 min against 227 min of wait time — process cycle efficiency = 44/271 = 16%, so 84% of lead time is pure waiting. Only 'Run weld cycle' and 'Rework and re-test' transform the product; the burst test is BVA (required by the regulator, adds no customer value); every transfer and queue is NVA. There are five HANDOFFS, and the two biggest wait times sit immediately after them. The scope sheet is what stops scope creep in week three: without a written start point ('fixture load') and end point ('final disposition'), the team will be asked to fix incoming material quality too.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

Your SIPOC's first and last steps match your charter scope exactly, your swimlane map marks every handoff and rework loop, and the map has been validated by walking the actual process.

## Where this sits in the capstone

Re-derive SIPOC and detailed process mapping in full, then apply them to bound your capstone. Scope creep kills more Black Belt projects than bad statistics — this lab builds the map that makes scope arguments objective. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
