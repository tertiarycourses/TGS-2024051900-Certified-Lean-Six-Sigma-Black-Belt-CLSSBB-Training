<!-- WSQ - Certified Lean Six Sigma Black Belt (CLSSBB) Training (TGS-2024051900) · Tertiary Infotech Academy Pte Ltd · v4 -->

# Lab 5 — CTQ Trees and CTQ Flowdown to Controllable Xs

**DEFINE** · Translate VOC into measurable CTQs and cascade a business Y down to controllable Xs (A1, A4).

| Field | Detail |
|---|---|
| Case study | Meridian Medical Devices — seal weld burst pressure |
| DMAIC phase | DEFINE |
| Lab type | Core |
| Deliverable | A CTQ tree with targets and specification limits, plus a flowdown to controllable Xs. |
| Tools | CTQ tree, need-driver-requirement, operational definitions, specification limits, Y-to-X cascade |
| Data file | `lab-05-ctq-tree-flowdown.xlsx` |

---

## The Scenario

Meridian Medical Devices manufactures infusion pump assemblies across three plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital distributors in 14 countries. The business is missing its on-time-in-full (OTIF) target, first-pass yield varies significantly between plants, and warranty returns are rising. The VP of Operations has appointed you as Black Belt to lead a portfolio of improvement projects — and to mentor the Green Belts running workstreams beneath you. Use this scenario ONLY if you cannot use a real process from your own workplace; your own process is always preferred.

## The Evidence

**`lab-05-ctq-tree-flowdown.xlsx`** — *Template.* A CTQ tree worksheet that flows the must-be need down to measurable, controllable Xs.

| Sheet | What it contains | Rows |
|---|---|---|
| CTQTree | Need -> Driver -> Requirement -> Measure -> Target -> Spec. | 8 |
| CTQFlowdown | Flow the CTQ down to the Xs you can actually control on the shop floor. | 10 |
| OperationalDefinitions | An operational definition every person would apply identically. | 4 |

Open the workbook from this folder. Every workbook opens on a **Data Dictionary** sheet defining each column, its unit and the specification limits — read it before you analyse anything.

## Step-by-Step

1. Recap the CTQ tree structure in full: Need -> Drivers -> Measurable Requirements, with each level more specific than the last.
2. Take your top VOC theme and drive it down: what is the need, what drives it, and what specifically must be measured?
3. For each CTQ, write a complete operational definition — what is measured, by whom, with what instrument, at what point, and what counts as a defect.
4. Set the target, the upper and lower specification limits, and the defect definition for each CTQ. A CTQ without limits cannot generate a defect count.
5. Verify each CTQ against the customer: would they agree this number represents what they asked for?
6. Now flow down. Write your business-level Y (e.g. OTIF percentage) at the top of a cascade diagram.
7. Break that Y into sub-Ys — the process-level outputs that roll up into it (pick accuracy, line yield, changeover time, carrier dwell).
8. Break each sub-Y into the Xs that drive it. Continue until you reach Xs a team can directly control or experiment on.
9. Mark on the cascade which Xs you will measure in Day 2, test statistically in Day 3, and experiment on in Day 4.

## The GenAI Prompt

Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft Copilot, Google Gemini or Claude. Replace anything in `<<double angle brackets>>` with your own details, then CHECK the answer against your own working — the tool is right, the AI is not always.

## Self-Check — Is Your Output Finished?

Every CTQ has an operational definition, a target and specification limits, and your flowdown reaches at least one layer of Xs that are directly controllable and testable.

## Deliverable

Save your output — it forms part of your CAPSTONE PROJECT PACK, which you consolidate into an A3 storyboard and present to the steering committee on Day 5.

---

*Files in this folder: [scenario.md](scenario.md) · [worksheet.md](worksheet.md) (and worksheet.pdf) · `lab-05-ctq-tree-flowdown.xlsx` · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*

*Certified Lean Six Sigma Black Belt (CLSSBB) Training · TGS-2024051900 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
