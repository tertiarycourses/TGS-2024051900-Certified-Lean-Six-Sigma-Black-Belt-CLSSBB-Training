<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 25 — Response Surface Methodology and Robust Design (Black Belt Only)

**IMPROVE** · Optimise factor settings using RSM and make the process robust to noise (A5, K2).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | IMPROVE |
| Lab type | Core |
| Deliverable | An RSM study locating optimal settings plus a robust design analysis against noise factors. |
| Tools | Curvature & centre points, steepest ascent, central composite design, Box-Behnken, contour & surface plots, Taguchi, signal-to-noise, control vs noise factors |
| Data file | `lab-25-rsm-central-composite.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-25-rsm-central-composite.xlsx`** — *Dataset.* A 13-run central composite design (4 factorial + 4 axial + 5 centre points) around the Lab 23 optimum, to find the true peak and test for curvature.

| Sheet | What it contains | Rows |
|---|---|---|
| CentralComposite | CCD in 2 factors. Coded and uncoded levels both given. | 13 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Understand the limitation of 2-level designs: with only two levels per factor they fit a straight line and cannot detect curvature at all.
2. Add CENTRE POINTS to your factorial design to test for curvature. A significant centre-point effect means the true response is curved and a linear model will mislead you.
3. If no curvature is present and you are far from the optimum, use steepest ascent — move the factor settings in the direction of greatest improvement and re-experiment.
4. Once curvature appears, you are near the optimum and need a second-order design.
5. Learn the central composite design (CCD): a factorial core, plus centre points, plus axial (star) points that add the third level needed to estimate quadratic terms.
6. Learn the Box-Behnken alternative: fewer runs than CCD and it never requires extreme corner combinations, which matters when corners are unsafe or infeasible.
7. Design and run an RSM study on the 2-3 vital factors from Lab 24.
8. Fit the second-order model including linear, quadratic and interaction terms.
9. Generate contour and 3D surface plots to visualise the response surface and locate the optimum region.
10. Find the stationary point and classify it — maximum, minimum or saddle. A saddle point means the optimum lies at a boundary, not in the middle.
11. Use desirability functions if you must optimise several responses at once with competing optima.
12. Now robust design. Separate your factors into CONTROL factors (you set them) and NOISE factors (ambient conditions, material variation, operator, wear).
13. Understand the Taguchi insight: choose control factor settings at which the response is LEAST SENSITIVE to noise — a slightly lower mean with far less variation usually wins.
14. Compute the signal-to-noise ratio for candidate settings, using the correct form for your objective (smaller-is-better, larger-is-better or nominal-is-best).
15. Select the robust operating window and run confirmation trials under deliberately varied noise conditions.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Curvature is tested with centre points, your second-order model is visualised as a contour or surface plot with a classified stationary point, and the robust settings are confirmed under varied noise conditions.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-25-rsm-central-composite.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
