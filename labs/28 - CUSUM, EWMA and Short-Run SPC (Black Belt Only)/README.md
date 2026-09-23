<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 28 — CUSUM, EWMA and Short-Run SPC (Black Belt Only)

**CONTROL** · Detect small sustained shifts using CUSUM and EWMA, and chart high-mix processes (A5, K2).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | CONTROL |
| Lab type | Core |
| Deliverable | CUSUM and EWMA charts on your capstone data plus a short-run standardised chart. |
| Tools | ARL, CUSUM, decision interval, V-mask, EWMA, lambda weighting, autocorrelation, short-run standardised charts, DNOM |
| Data file | `lab-28-cusum-ewma-shortrun.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-28-cusum-ewma-shortrun.xlsx`** — *Dataset.* 60 individual readings containing a small 0.75-sigma sustained shift at point 31 — plus a short-run sheet with three part numbers and only 15 units each.

| Sheet | What it contains | Rows |
|---|---|---|
| SmallShift | Individual burst-pressure readings. Something changes at 31 — find it. | 60 |
| ShortRun | Three low-volume part numbers, 15 units each, different nominals. | 45 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

> Use your OWN workplace data wherever you can obtain it. The workbook is the fallback, and it describes the same Meridian process as every other lab, so your figures reconcile across labs.

## Step-by-Step

1. Understand Average Run Length (ARL): the expected number of subgroups before a chart signals. For a 1-sigma shift, a Shewhart Xbar chart has an ARL around 44 — far too slow.
2. Understand the structural reason: a Shewhart chart considers only the CURRENT point and has no memory of the recent past.
3. Learn CUSUM: it accumulates deviations from target, so a small persistent bias adds up into a detectable signal rather than being repeatedly dismissed as noise.
4. Set up the CUSUM parameters: the reference value k (typically half the shift you want to detect) and the decision interval h (typically 4 or 5 sigma).
5. Build upper and lower CUSUM statistics for your capstone data and plot them against the decision interval.
6. Compare the CUSUM detection point against the Shewhart chart from Lab 27 on the same data — CUSUM typically detects a sustained small shift several subgroups sooner.
7. Learn EWMA: each point is a weighted average of all history, with weights decaying geometrically. Lambda controls the memory.
8. Choose lambda deliberately: small lambda (0.1-0.2) gives long memory and strong small-shift detection; large lambda (0.4+) approaches Shewhart behaviour.
9. Build the EWMA chart with its widening initial control limits, and note that EWMA also handles autocorrelated data far better than Shewhart.
10. Test your capstone data for autocorrelation. Chemical, batch and continuous-flow processes are frequently autocorrelated, which makes Shewhart limits far too narrow and generates constant false alarms.
11. Now short-run SPC. Understand the problem: high-mix low-volume processes never accumulate 25 subgroups of any single part number.
12. Learn the deviation-from-nominal (DNOM) approach: plot (measurement - part nominal) so different part numbers share one chart.
13. Learn the standardised approach for parts with differing variances: plot (measurement - nominal) / sigma_part, putting all parts on a common scale.
14. Build a short-run chart for a multi-product step in your capstone, or for Meridian's shared assembly line across pump variants.
15. Decide which chart type belongs in your capstone control plan and justify the choice against shift size, autocorrelation and product mix.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

You have built CUSUM and EWMA charts and compared their detection speed against Shewhart on the same data, tested for autocorrelation, and justified your final chart selection for the control plan.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-28-cusum-ewma-shortrun.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
