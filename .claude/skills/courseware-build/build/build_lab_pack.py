#!/usr/bin/env python3
"""Build the complete file pack for ONE lab folder, in the Tertiary Infotech
house activity-pack format.

The pattern is taken from the published Activities folders on the course Drive
(e.g. WSQ Generative AI for Problem Solving), where each activity folder holds:

    README.md      the activity brief — metadata table, scenario, evidence,
                   step-by-step, self-check
    scenario.md    the case study on its own, for printing/projection
    worksheet.md   the blank team worksheet with ruled fill-in lines
    debrief.md     the TRAINER debrief — expected answers and teaching points
    debrief.pdf    the same, print-ready
    prompt.txt     the GenAI prompt for the activity

To that we add, for this course:

    <lab-NN-*>.xlsx  the mock data (a dataset to analyse, or a blank template)
    worksheet.pdf    the worksheet, print-ready

Every file carries the same HTML header comment as the reference packs so the
course, code and version are traceable on any single loose file.
"""
import os

RULE = "_" * 84


def _hdr(C):
    return (f"<!-- WSQ - {C.TITLE} ({C.COURSE_CODE}) · {C.ORG} · "
            f"{C.VERSION} -->")


def _lines(n=2):
    """Ruled fill-in lines for the printed worksheet."""
    return ("\n\n".join([RULE] * n)) + "\n"


# --------------------------------------------------------------------------
# README.md — the activity brief
# --------------------------------------------------------------------------
def readme_md(a, C, tp, specs, scenario, tools_used):
    title = a["title"].replace("Elective — ", "")
    kind = "Elective" if a.get("elective") else "Core"
    o = [_hdr(C), "", f"# Lab {a['num']} — {title}", ""]
    o.append(f"**{tp['phase']}** · {a['objective']}")
    o.append("")
    o.append("| Field | Detail |")
    o.append("|---|---|")
    o.append(f"| Case study | Meridian Medical Devices — seal weld burst pressure |")
    o.append(f"| DMAIC phase | {tp['phase']} |")
    o.append(f"| Lab type | {kind} |")
    o.append(f"| Deliverable | {a['build']} |")
    o.append(f"| Tools | {a['services']} |")
    if tools_used:
        for name, url in tools_used:
            o.append(f"| Ed-tool | [{name}]({url}) |")
    if specs:
        o.append(f"| Data file | " + ", ".join(f"`{d['file']}`" for d in specs) + " |")
    o.append("")
    o.append("---")
    o.append("")
    o.append("## The Scenario")
    o.append("")
    o.append(scenario)
    o.append("")

    if specs:
        o.append("## The Evidence")
        o.append("")
        for d in specs:
            label = "Dataset" if d["kind"] == "data" else "Template"
            o.append(f"**`{d['file']}`** — *{label}.* {d['about']}")
            o.append("")
            o.append("| Sheet | What it contains | Rows |")
            o.append("|---|---|---|")
            for sh in d["sheets"]:
                o.append(f"| {sh['name']} | {sh['desc']} | {len(sh['rows'])} |")
            o.append("")
        o.append("Open the workbook from this folder. Every workbook opens on a "
                 "**Data Dictionary** sheet defining each column, its unit and the "
                 "specification limits — read it before you analyse anything.")
        o.append("")
        if any(d["kind"] == "data" for d in specs):
            o.append("> Use your OWN workplace data wherever you can obtain it. The "
                     "workbook is the fallback, and it describes the same Meridian "
                     "process as every other lab, so your figures reconcile across labs.")
            o.append("")

    o.append("## Step-by-Step")
    o.append("")
    for i, (instr, cmd) in enumerate(a["steps"], 1):
        line = f"{i}. {instr}"
        if cmd and cmd.startswith("http"):
            line += f" Open the tool: <{cmd}>"
        o.append(line)
        if cmd and not cmd.startswith("http"):
            o.append("")
            o.append("   ```")
            o.append(f"   {cmd}")
            o.append("   ```")
    o.append("")

    o.append("## The GenAI Prompt")
    o.append("")
    o.append("Copy the prompt in [prompt.txt](prompt.txt) into ChatGPT, Microsoft "
             "Copilot, Google Gemini or Claude. Replace anything in "
             "`<<double angle brackets>>` with your own details, then CHECK the "
             "answer against your own working — the tool is right, the AI is not "
             "always.")
    o.append("")

    o.append("## Self-Check — Is Your Output Finished?")
    o.append("")
    o.append(a["test"])
    o.append("")
    o.append("## Deliverable")
    o.append("")
    o.append("Save your output — it forms part of your CAPSTONE PROJECT PACK, which "
             "you consolidate into an A3 storyboard and present to the steering "
             "committee on Day 5.")
    o.append("")
    o.append("---")
    o.append("")
    o.append("*Files in this folder: "
             "[scenario.md](scenario.md) · [worksheet.md](worksheet.md) "
             "(and worksheet.pdf)"
             + (" · " + ", ".join(f"`{d['file']}`" for d in specs) if specs else "")
             + " · [debrief.md](debrief.md) (TRAINER) · [prompt.txt](prompt.txt)*")
    o.append("")
    o.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*")
    o.append("")
    return "\n".join(o)


# --------------------------------------------------------------------------
# scenario.md
# --------------------------------------------------------------------------
def scenario_md(a, C, tp, specs, scenario):
    title = a["title"].replace("Elective — ", "")
    o = [_hdr(C), "", f"# Scenario — Lab {a['num']}", "", f"## {title}", ""]
    o.append(f"**{tp['phase']}** · Meridian Medical Devices")
    o.append("")
    o.append("---")
    o.append("")
    o.append(scenario)
    o.append("")
    o.append("## Your brief")
    o.append("")
    o.append(a["desc"])
    o.append("")
    o.append("## What you must produce")
    o.append("")
    o.append(a["build"])
    o.append("")
    if specs:
        o.append("## The data you are given")
        o.append("")
        for d in specs:
            o.append(f"- **`{d['file']}`** — {d['about']}")
        o.append("")
    o.append("---")
    o.append("")
    o.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*")
    o.append("")
    return "\n".join(o)


# --------------------------------------------------------------------------
# worksheet.md — the blank team form
# --------------------------------------------------------------------------
def worksheet_md(a, C, tp, specs):
    title = a["title"].replace("Elective — ", "")
    o = [_hdr(C), "", f"# Team Worksheet — Lab {a['num']}", "", f"## {title}", ""]
    o.append("**Team members:** " + "_" * 44 + "  ")
    o.append("**Date:** " + "_" * 20)
    o.append("")
    o.append("---")
    o.append("")
    o.append("### 1. Our understanding of the problem")
    o.append("")
    o.append(_lines(3))
    o.append("### 2. Our working")
    o.append("")
    if specs:
        o.append(f"*Use the data in "
                 + ", ".join(f"`{d['file']}`" for d in specs) + ".*")
        o.append("")
    o.append(_lines(5))
    o.append("### 3. What we produced")
    o.append("")
    o.append(f"*Deliverable: {a['build']}*")
    o.append("")
    o.append(_lines(4))
    o.append("### 4. What the evidence does NOT tell us")
    o.append("")
    o.append(_lines(2))
    o.append("### 5. Our conclusion")
    o.append("")
    o.append(_lines(3))
    o.append("### 6. Step notes")
    o.append("")
    for i, (instr, _cmd) in enumerate(a["steps"], 1):
        o.append(f"**Step {i}.** {instr}")
        o.append("")
        o.append(RULE)
        o.append("")
    o.append("### 7. Self-check")
    o.append("")
    o.append(a["test"])
    o.append("")
    o.append("Complete?  ☐ Yes   ☐ Not yet")
    o.append("")
    o.append("---")
    o.append("")
    o.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*")
    o.append("")
    return "\n".join(o)


# --------------------------------------------------------------------------
# debrief.md — TRAINER answers
# --------------------------------------------------------------------------
def debrief_md(a, C, tp, specs):
    title = a["title"].replace("Elective — ", "")
    o = [_hdr(C), "", f"# Trainer Debrief — Lab {a['num']}", "", f"## {title}", ""]
    o.append(f"**Case study:** Meridian Medical Devices — seal weld burst pressure  ")
    o.append(f"**Objective:** {a['objective']}")
    o.append("")
    o.append("> **TRAINER ONLY.** Do not hand this out before the lab is complete.")
    o.append("")
    o.append("---")
    o.append("")
    if specs:
        o.append("## Expected analysis")
        o.append("")
        for d in specs:
            o.append(f"**`{d['file']}`**")
            o.append("")
            o.append(d["answer"])
            o.append("")
        o.append("Every dataset is generated from a fixed seed, so these figures are "
                 "reproducible — re-run the analysis on the shipped workbook and you "
                 "will get these numbers.")
        o.append("")
    o.append("## What good looks like")
    o.append("")
    o.append(a["test"])
    o.append("")
    o.append("## Where this sits in the capstone")
    o.append("")
    o.append(a["desc"])
    o.append("")
    o.append("## The running process — figures that must reconcile")
    o.append("")
    o.append("| Checkpoint | Value | Established in |")
    o.append("|---|---|---|")
    o.append("| Baseline defect rate | 2.9% | Lab 3 |")
    o.append("| Measurement system | FAILS Gage R&R (~40% study variation) | Lab 11 |")
    o.append("| Baseline capability | Pp 0.62 / Ppk 0.53 | Lab 14 |")
    o.append("| Proven Xs | clamp pressure, dwell time, electrode tip age | Labs 18-21 |")
    o.append("| DOE optimum | clamp 47.4 bar, dwell 2.76 s | Labs 23-25 |")
    o.append("| Improved capability | Ppk 1.40 | Lab 27 |")
    o.append("| Annual hard benefit | SGD 487,000 vs SGD 812,000 COPQ | Labs 1, 30 |")
    o.append("")
    o.append("If a learner's number disagrees with the column above, they have either "
             "used their own workplace data (fine — say so) or made an error (find it).")
    o.append("")
    o.append("---")
    o.append("")
    o.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG} · "
             f"TRAINER ONLY*")
    o.append("")
    return "\n".join(o)


# --------------------------------------------------------------------------
# prompt.txt — the GenAI prompt
# --------------------------------------------------------------------------
def prompt_txt(a, C, specs):
    title = a["title"].replace("Elective — ", "")
    o = []
    o.append(f"GenAI prompt — Lab {a['num']}: {title}")
    o.append(f"{C.TITLE} ({C.COURSE_CODE})")
    o.append("")
    o.append("Paste into ChatGPT, Microsoft Copilot, Google Gemini or Claude.")
    o.append("Replace anything in <<double angle brackets>> with your own details.")
    o.append("Then CHECK the answer against your own working.")
    o.append("")
    o.append("-" * 72)
    o.append("")
    o.append("Act as a Lean Six Sigma Black Belt coach.")
    o.append("")
    o.append("CONTEXT: Meridian Medical Devices manufactures infusion pump assemblies")
    o.append("across three plants (Singapore, Penang, Suzhou) on six production lines.")
    o.append("The project Y is seal weld burst pressure in kPa, with a specification of")
    o.append("180-260 kPa and a target of 220 kPa.")
    o.append("")
    o.append(f"MY TASK: {a['objective']}")
    o.append("")
    o.append(f"WHAT I MUST PRODUCE: {a['build']}")
    o.append("")
    o.append(f"TOOLS AND TECHNIQUES IN SCOPE: {a['services']}")
    o.append("")
    if specs:
        o.append("MY DATA:")
        for d in specs:
            o.append(f"  {d['file']} — {d['about']}")
            for sh in d["sheets"]:
                cols = ", ".join(c[0] for c in sh["cols"])
                o.append(f"    sheet '{sh['name']}' ({len(sh['rows'])} rows): {cols}")
        o.append("")
        o.append("<<Paste the relevant rows, or attach the workbook.>>")
        o.append("")
    o.append("MY OWN WORKPLACE CONTEXT (use this instead of Meridian if given):")
    o.append("  Process: <<your process>>")
    o.append("  The Y I am improving: <<your metric and its unit>>")
    o.append("  Current performance: <<your baseline>>")
    o.append("")
    o.append("PRODUCE:")
    o.append("1. The analysis or artifact described above, laid out so I can put it")
    o.append("   straight into my capstone project pack.")
    o.append("2. The arithmetic shown in full, so I can check every number myself.")
    o.append("3. The assumptions you made, listed explicitly.")
    o.append("4. What this analysis does NOT tell me, and what I would need to")
    o.append("   collect next to answer that.")
    o.append("5. One question a sceptical steering committee would ask about this")
    o.append("   result, and how I should answer it.")
    o.append("")
    o.append("Do not invent data. If something you need is missing, ask me for it.")
    o.append("")
    o.append("-" * 72)
    o.append("")
    o.append("CHECK THE OUTPUT. Statistical arithmetic from a language model is often")
    o.append("wrong. Where this lab uses an ed-tool or Excel, that result is the one")
    o.append("to trust. Note any disagreement in section 4 of your worksheet — finding")
    o.append("the AI's error is part of the lab.")
    o.append("")
    return "\n".join(o)
