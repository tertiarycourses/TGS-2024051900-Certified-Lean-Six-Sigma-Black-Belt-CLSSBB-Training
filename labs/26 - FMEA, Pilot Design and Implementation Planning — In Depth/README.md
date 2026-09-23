<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 26 — FMEA, Pilot Design and Implementation Planning — In Depth

**IMPROVE** · De-risk and pilot your capstone improvement before full rollout (A5).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | IMPROVE |
| Lab type | Core |
| Deliverable | A completed FMEA with re-scored RPNs and a full pilot plan with success criteria. |
| Tools | FMEA, severity/occurrence/detection, RPN, risk mitigation, pilot design, success criteria, implementation planning, cost-benefit |
| Data file | `lab-26-fmea-worksheet.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-26-fmea-worksheet.xlsx`** — *Template.* A process FMEA worksheet pre-loaded with the seven real failure modes from this project — you score Severity, Occurrence and Detection and compute the RPN.

| Sheet | What it contains | Rows |
|---|---|---|
| FMEA | Fill the blank scoring columns during the lab. Scale 1-10 each. | 7 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

## Step-by-Step

1. Recap FMEA in full: failure mode, effect, cause, current controls, and the three ratings that combine into the risk priority number.
2. Recap the scoring scales precisely: Severity (impact if it occurs), Occurrence (likelihood) and Detection (probability of catching it BEFORE the customer does — note the inverted scale).
3. Build the FMEA for your selected improvement. For each process step, ask what could fail, what happens if it does, and what would cause it.
4. Score S, O and D on 1-10 scales and calculate RPN = S x O x D.
5. Apply the severity override rule: any failure mode with Severity 9-10 requires action regardless of how low its RPN is.
6. Rank by RPN and define mitigation for every high-RPN mode, targeting the component you can most cheaply move — usually Detection, sometimes Occurrence.
7. RE-SCORE after mitigation and record the residual RPN. An FMEA without re-scoring has not demonstrated that risk was actually reduced.
8. Design the pilot: scope (which line, site or segment), duration, sample size and the exact data to be collected.
9. Define quantitative success criteria BEFORE the pilot starts, expressed against your Lab 3 baseline. Criteria defined afterwards get rationalised.
10. Plan the comparison: before/after, or better, a control group running the unchanged process concurrently to rule out external effects.
11. Define the stop conditions — what result would cause you to halt the pilot rather than push through.
12. Build the implementation plan: tasks, owners, dates, training, communication, systems changes and documentation updates.
13. Complete the cost-benefit analysis: implementation cost, annualised benefit, payback period and NPV where the investment is material.
14. Run the pilot (or design it fully for post-course execution) and test the results statistically against the baseline — a visual improvement is not proof.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Your FMEA is re-scored post-mitigation with the severity override applied, pilot success criteria were defined before starting, and the improvement is tested statistically against the documented baseline.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-26-fmea-worksheet.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
