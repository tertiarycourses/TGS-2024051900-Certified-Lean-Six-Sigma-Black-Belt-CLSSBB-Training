<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Trainer Debrief — Lab 28

## CUSUM, EWMA and Short-Run SPC (Black Belt Only)

**Case study:** Meridian Medical Devices — seal weld burst pressure  
**Objective:** Detect small sustained shifts using CUSUM and EWMA, and chart high-mix processes (A5, K2).

> **TRAINER ONLY.** Do not hand this out before the lab is complete.

---

## Expected analysis

**`lab-28-cusum-ewma-shortrun.xlsx`**

SmallShift: a Shewhart I chart detects NOTHING — no point breaches 3 sigma, because a 0.75 sigma shift has an ARL of roughly 280 on an individuals chart. CUSUM (k=0.5, h=4) signals around observation 38-41; EWMA (lambda=0.2, L=2.7) signals around 39-42. Both detect the shift within ~10 points. That is the whole argument for CUSUM/EWMA: they accumulate evidence, a Shewhart chart has no memory. ShortRun: with only 15 units per part you cannot compute stable limits per part. Code each reading as a deviation-from-target (DNOM) or Z-transform it, then chart all three part numbers on ONE chart.

Every dataset is generated from a fixed seed, so these figures are reproducible — re-run the analysis on the shipped workbook and you will get these numbers.

## What good looks like

You have built CUSUM and EWMA charts and compared their detection speed against Shewhart on the same data, tested for autocorrelation, and justified your final chart selection for the control plan.

## Where this sits in the capstone

BLACK BELT ONLY. Shewhart charts are poor at detecting small sustained shifts — they may take dozens of subgroups to react to a 1-sigma drift, which is precisely how a process degrades unnoticed after a project closes. CUSUM and EWMA solve this, and short-run methods handle high-mix low-volume processes Shewhart cannot chart at all. CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your capstone project pack, which you present to the steering committee on Day 5.

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
