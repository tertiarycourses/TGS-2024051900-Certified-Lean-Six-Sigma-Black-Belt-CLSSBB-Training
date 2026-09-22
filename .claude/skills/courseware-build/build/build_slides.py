#!/usr/bin/env python3
"""Build the CLSSBB slide deck — all-white Tertiary house style, DMAIC order.

Structure:
  Cover -> Admin (TRAQOM, trainers x2, ground rules, LMS, lesson plan x5 days,
  TSC, outcomes, course outline, briefing, assessment, assessment flow)
  -> Foundations -> D -> M -> A -> I -> C -> CAPSTONE  (each phase: concepts then labs)
  -> Wrap-up -> Assessment -> Assessment Flow -> Digital Attendance -> TRAQOM -> Thank You

Content comes entirely from course_data.py + data_domainN.py + concepts.py so the
PPT, LP, LG and labs stay 100% aligned.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
from data_domain6 import DOMAIN6
from lab_datasets import DATASETS
from components import (Deck, BLUE, TEAL, AMBER, RED, VIOLET, INK, GREY, LIGHT,
                        WHITE, LINE, DMAIC_COLORS)
import concepts

ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4 + DOMAIN5 + DOMAIN6


def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO = _find_repo(HERE)
ASSETS = os.path.join(REPO, "courseware", "assets")


def asset(name):
    p = os.path.join(ASSETS, name)
    return p if os.path.exists(p) else None


d = Deck(C, repo_assets=ASSETS)

# ============================================================ COVER
d.cover(logo=asset("tertiary-logo.png"))

# ============================================================ ADMIN
d.section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "")

d.flow_h("Digital Attendance (Mandatory)", [
    "Trainer displays the SSG digital attendance QR code",
    "Scan the QR code with your phone camera",
    "Key in your NRIC/FIN and submit",
    "Repeat for AM, PM and the assessment",
    "Keep 75% attendance to stay eligible for funding",
], kicker="TRAQOM · SSG DIGITAL ATTENDANCE", color=BLUE)

# --- two trainer profile cards (house hard rule) ---
d.trainer_slide("YOUR TRAINER · GENERAL", "Your Trainer",
                "General Trainer template —\nto be completed by the trainer",
                [("Name", ""), ("Title / Designation", ""), ("Qualifications", ""),
                 ("Areas of expertise", ""), ("Training & industry experience", ""), ("Contact", "")],
                initials="?", accent=GREY)
d.trainer_slide("YOUR TRAINER", C.TRAINER,
                "Principal Trainer\nTertiary Infotech Academy Pte. Ltd.",
                [("Role", "Principal Trainer, Tertiary Infotech Academy Pte. Ltd."),
                 ("Qualifications", "PhD; Certified Lean Six Sigma Black Belt practitioner and trainer."),
                 ("Delivers", "WSQ courses on Lean Six Sigma, quality management and data analytics."),
                 ("Experience", "Process improvement across manufacturing, service and technology sectors."),
                 ("Founder", "Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
                initials="AA", accent=BLUE)

d.content("Let's Know Each Other", [
    "Your name, organisation and role.",
    "Your Green Belt background and the projects you have run or supported.",
    "Your comfort level with statistics — regression, ANOVA, design of experiments.",
    "A REAL process at work you could improve — this becomes your capstone project.",
], kicker="ICE-BREAKER")

# --- The capstone runs from Day 1 (house rule for this course) ---
d.big_statement("Your Capstone Project Starts Today",
                "You will choose a real process from your own workplace in Lab 1, and every "
                "lab across the next five days adds one artifact to it. On Day 5 you present "
                "it to a steering committee - in addition to the WSQ assessment.",
                "HOW THIS COURSE WORKS", color=TEAL)

d.flow_h("How Your Capstone Is Built", [
    "Day 1 - select and charter your own workplace project",
    "Days 2-4 - every lab adds one artifact to that project",
    "Day 5 - consolidate the artifacts into an A3 storyboard",
    "Day 5 - present and defend it to the steering committee",
], kicker="THE CAPSTONE THREAD", color=TEAL)

# NOTE: assets/trainer-*.jpeg and assets/ground-rules.jpeg were screenshots of
# slides from a DIFFERENT course (CompTIA CySA+, TGS-2024049211) and carried that
# course's name and code in their footers. They have been deleted; these slides are
# rendered natively from this course's own components instead.
d.tile_grid("Ground Rules", [
    "Set your mobile phone to silent mode.",
    "Participate actively — no question is too small.",
    "Mutual respect: agree to disagree.",
    "One conversation at a time.",
    "Be punctual; return from breaks on time.",
    "75% attendance is required for certification.",
], kicker="HOUSEKEEPING", cols=2, size=15)

# --- Download course material ---
lms = asset("lms_download.png") or asset("lms-download.png")
if lms:
    d.image_slide("Download Your Course Material", lms,
                  kicker="COURSE PORTAL · lms-tms.tertiaryinfotech.com",
                  caption="Log in to lms-tms.tertiaryinfotech.com to download the slides, Learner Guide and lab files.")
else:
    d.flow_h("Download Your Course Material", [
        "Go to lms-tms.tertiaryinfotech.com",
        "Sign in with the account details given in class",
        "Open this course from your dashboard",
        "Download the slides, Learner Guide and lab files",
        "Keep them open — the assessment is open book",
    ], kicker="COURSE PORTAL · lms-tms.tertiaryinfotech.com", color=TEAL)

# --- Interactive problem-solving toolkit (browser-based, no licence needed) ---
d.tile_grid("Your Interactive Toolkit", [
    ("SIPOC", "Build a SIPOC map and agree process boundaries — alfredang.github.io/sipoc"),
    ("Fishbone Diagram", "Build an Ishikawa cause-and-effect diagram — alfredang.github.io/fishbone"),
    ("5 Whys", "Build and share a 5 Whys root-cause chain — alfredang.github.io/5whys"),
    ("Pareto Chart", "Team brainstorms and votes; the chart builds itself live — alfredang.github.io/paretochart"),
    ("NovaSPC", "Run charts, SPC charts and process capability from your CSV — alfredang.github.io/novaspc"),
    ("No installation", "All run in the browser. No licence, no setup — use them in the labs."),
], kicker="BROWSER-BASED TOOLS USED IN THE LABS", cols=2, size=14, accent=TEAL)

# --- Lesson plan: 5 days ---
d.two_col("Lesson Plan — Days 1 & 2",
          [("Day 1 — " + C.DAY_THEMES[1], 0),
           ("Digital attendance (AM) · Introductions", 1),
           ("The Black Belt role vs the Green Belt role", 1),
           ("Project portfolio selection and strategy alignment", 1),
           ("DMAIC recap at depth · Y = f(X) · sigma level", 1),
           ("Labs 1-3 — SELECT AND CHARTER YOUR CAPSTONE", 1),
           ("DEFINE: VOC, Kano, CTQ trees and CTQ flowdown", 1),
           ("Stakeholders, resistance and change leadership", 1),
           ("Labs 4-7 — VOC/Kano, CTQ flowdown, SIPOC, stakeholders", 1)],
          [("Day 2 — " + C.DAY_THEMES[2], 0),
           ("Digital attendance (AM)", 1),
           ("MEASURE recap: mapping, VSM, takt, eight wastes", 1),
           ("Data types, sampling and rational subgrouping", 1),
           ("Continuous Gage R&R at depth", 1),
           ("ATTRIBUTE MSA and Kappa analysis (Black Belt only)", 1),
           ("Nested and destructive gauge studies", 1),
           ("Non-normal capability, Cpk vs Ppk, Box-Cox", 1),
           ("Labs 8-14 — VSM, sampling, Gage R&R, Kappa, capability", 1)],
          kicker="SCHEDULE · 9:30am-6:30pm with a 1-hour lunch",
          lhead="Day 1", rhead="Day 2")

d.two_col("Lesson Plan — Days 3 & 4",
          [("Day 3 — " + C.DAY_THEMES[3], 0),
           ("Digital attendance (AM)", 1),
           ("ANALYZE recap: variation, run charts, Pareto, fishbone", 1),
           ("Hypothesis testing at depth and test selection", 1),
           ("MULTIPLE REGRESSION and model diagnostics (VIF, residuals)", 1),
           ("ANOVA, two-way ANOVA and interaction effects", 1),
           ("Non-parametric tests and multi-vari studies", 1),
           ("Chi-square and categorical association", 1),
           ("Labs 15-21 — regression, ANOVA, multi-vari, tollgate", 1)],
          [("Day 4 — " + C.DAY_THEMES[4], 0),
           ("Digital attendance (AM)", 1),
           ("IMPROVE recap: solutions, Lean tools, FMEA", 1),
           ("FULL FACTORIAL DOE — main effects and interactions", 1),
           ("Fractional factorial, confounding and resolution", 1),
           ("Response surface methodology and robust design", 1),
           ("CONTROL recap: SPC, chart selection, Cp/Cpk", 1),
           ("CUSUM, EWMA, short-run and multivariate SPC", 1),
           ("Labs 22-30 — DOE, RSM, FMEA, SPC, control plan", 1)],
          kicker="SCHEDULE · 9:30am-6:30pm with a 1-hour lunch",
          lhead="Day 3", rhead="Day 4")

d.two_col("Lesson Plan — Day 5",
          [("Day 5 — " + C.DAY_THEMES[5], 0),
           ("Digital attendance (AM)", 1),
           ("Consolidating your capstone artifacts from Labs 1-30", 1),
           ("The A3 storyboard — one page, seven sections", 1),
           ("Lab 31 — build your A3 storyboard", 1),
           ("Building the steering committee presentation", 1),
           ("Lab 32 — build and rehearse your presentation", 1)],
          [("Day 5 (continued)", 0),
           ("Lab 33 — CAPSTONE PRESENTATION AND DEFENCE", 1),
           ("Defending the analysis under challenge", 1),
           ("Peer presentations and observation", 1),
           ("Lessons learned and knowledge transfer", 1),
           ("Mentoring Green Belts — the coaching model", 1),
           ("Lab 34 — your Black Belt journey and 90-day plan", 1),
           ("TRAQOM survey · Course close", 1)],
          kicker="SCHEDULE · 9:30am-6:30pm with a 1-hour lunch",
          lhead="Day 5 AM", rhead="Day 5 PM")

# --- WSQ TSC alignment ---
d.content(f"Skills Framework — TSC: {C.TSC_TITLE}", [
    f"TSC Code: {C.TSC_CODE}",
] + C.TSC_ABILITIES + C.TSC_KNOWLEDGE, kicker="WSQ SKILLS FRAMEWORK", size=15)

d.tile_grid("Learning Outcomes", [
    ("LO1 — Lead a portfolio", "Select, charter and govern projects aligned to business strategy."),
    ("LO2 — Validate measurement", "Gage R&R for continuous data AND Kappa for attribute data."),
    ("LO3 — Advanced analysis", "Multiple regression, ANOVA, non-parametric and multi-vari studies."),
    ("LO4 — Design experiments", "Full and fractional factorial DOE and response surface methods."),
    ("LO5 — De-risk & validate", "FMEA, piloting and financial benefits with Finance sign-off."),
    ("LO6 — Advanced SPC", "CUSUM, EWMA, short-run and multivariate control charts."),
    ("LO7 — Lead change", "Resistance, stakeholder management and mentoring Green Belts."),
    ("LO8 — Deliver the capstone", "Present and defend a real project to a steering committee."),
], kicker="WHAT YOU'LL ACHIEVE", cols=2, size=14)

d.dmaic_wheel("Course Outline — DMAIC Reviewed in Depth, Then Extended", [
    ("D", "Define", ["VOC, Kano, CTQ recap", "CTQ FLOWDOWN", "Resistance & change", "Labs 4-7"]),
    ("M", "Measure", ["Gage R&R recap", "ATTRIBUTE MSA / KAPPA", "Nested & destructive", "Labs 8-14"]),
    ("A", "Analyze", ["Hypothesis recap", "MULTIPLE REGRESSION", "ANOVA, multi-vari", "Labs 15-21"]),
    ("I", "Improve", ["FMEA & Lean recap", "FULL & FRACTIONAL DOE", "RSM, robust design", "Labs 22-26"]),
    ("C", "Control", ["SPC recap", "CUSUM, EWMA, T-squared", "Benefits validation", "Labs 27-30"]),
], kicker="COURSE ROADMAP · 5 DAYS · 34 HANDS-ON LABS · CAPSTONE")

d.compare_panels("How This Course Steps Up From Green Belt", [
    ("GREEN BELT", "Leads one scoped project", [
        "Simple linear regression, one X",
        "Continuous Gage R&R only",
        "DOE mentioned in passing",
        "Shewhart control charts",
        "Supports the change effort",
    ]),
    ("BLACK BELT", "Leads a portfolio and mentors belts", [
        "Multiple regression, ANOVA, multi-vari",
        "Attribute MSA, Kappa, nested studies",
        "Full and fractional factorial DOE, RSM",
        "CUSUM, EWMA, short-run, multivariate",
        "Leads change and validates the money",
    ]),
], kicker="THE STEP UP", accent=VIOLET)

roadmap = asset("clssgb-dmaic-roadmap.png")
if roadmap:
    d.image_slide("The DMAIC Roadmap", roadmap, kicker="COURSE ROADMAP",
                  caption="Every topic and lab in this course sits inside one of these five phases.")

# --- Briefing BEFORE assessment (house hard rule) ---
d.tile_grid("Briefing for Assessment", [
    ("Clear your desk", "Phones and other materials go under the table or on the floor."),
    ("No photos or recording", "Assessment scripts must not be photographed or recorded."),
    ("No discussion", "The assessment is individual work — no talking once it starts."),
    ("Black or blue pen", "Use a black or blue pen for hard-copy assessments."),
    ("No correction fluid", "No liquid paper or correction tape — strike through instead."),
    ("Open book", "Slides, Learner Guide and approved materials only."),
], kicker="BEFORE YOU SIT THE ASSESSMENT", cols=2, size=15, accent=VIOLET)

d.tile_grid("Assessment", [
    ("Written Assessment (WA)", "Short-Answer Questions (SAQ) — 2 questions, 1 hour, open book (K1, K2)."),
    ("Case Study (CS)", "An applied DMAIC case study — 90 minutes, open book (A1-A5)."),
    ("Capstone (additional)", "Your project + steering committee presentation, on top of the WSQ assessment."),
    ("Built from Day 1", "Every lab from Lab 1 onwards adds one artifact to your capstone."),
    ("Attendance", C.ASSESSMENT["note"]),
    ("Appeals", "An appeal process is available if required."),
], kicker="FINAL ASSESSMENT", cols=1, size=14, accent=VIOLET)

# NOTE: courseware/assets/assessment-flow.jpeg is NOT used — it is a screenshot
# from a DIFFERENT course (CompTIA CySA+, TGS-2024049211) and names the wrong
# instrument ("Case Study"). This course is assessed by WA + PP, so the flow is
# always rendered natively from this course's own data.
ASSESSMENT_FLOW = [
    "TRAQOM survey — scan the QR code on the LMS",
    "Assessment digital attendance — scan the SSG QR",
    "Sit the WA (SAQ, 1 hour), then the Case Study (90 minutes)",
    "Submit your capstone report and present it to the steering committee",
    "Sign the Assessment Summary Record",
]
d.flow_h("Assessment Flow", ASSESSMENT_FLOW, kicker="ON ASSESSMENT DAY", color=VIOLET)

# NOTE: no Practice Exam slide — there is no Six Sigma practice exam on
# exams.tertiaryinfotech.com. The bundled clssgb-practice-exam.png has been
# deleted; do not reintroduce this slide for this course.

# ============================================================ FOUNDATIONS
concepts.foundations(d)

# ============================================================ DMAIC PHASES + LABS
PHASE_FN = {
    1: concepts.define_phase,
    2: concepts.measure_phase,
    3: concepts.analyze_phase,
    4: concepts.improve_phase,
    5: concepts.control_phase,
    6: concepts.capstone_phase,
}
TOPIC_ACTS = {t["num"]: [a for a in ACTIVITIES if a["topic"] == t["num"]] for t in C.TOPICS}


def render_labs(acts, phase_label):
    for a in acts:
        opt = a.get("elective", False)
        tag = f"LAB {a['num']}"
        d.activity_overview(tag, a["title"], a["desc"], a["build"], a["services"],
                            kicker=f"{phase_label} · HANDS-ON", elective=opt)
        steps = a["steps"]
        total = len(steps)
        # Truncate the eyebrow on a WORD boundary — a hard character cut breaks
        # mid-word ("...Affinity Diagra") on long lab titles.
        _t = a["title"]
        if len(_t) > 38:
            _t = _t[:38].rsplit(" ", 1)[0].rstrip(" ,.;:-") + "…"
        short = _t
        # Group the steps 6 to a slide: every step keeps its full wording, but the
        # deck stays near the ~500-slide target for this 5-day course.
        # Spread the steps EVENLY across the minimum number of slides (max 6 per
        # slide) so a lab never ends on a lonely single-step slide — 13 steps
        # becomes 5+4+4, not 6+6+1.
        PER = 6
        nslides = max(1, -(-total // PER))
        base, extra = divmod(total, nslides)
        idx = 0
        for k in range(nslides):
            take = base + (1 if k < extra else 0)
            d.steps_group(f"LAB {a['num']} · {short}", a["title"],
                          steps[idx:idx + take], idx + 1, total)
            idx += take
        d.test_slide(a["title"], a["test"], kicker=f"LAB {a['num']} · VERIFY")


# Foundations labs (topic 0) come right after the foundations concepts
render_labs(TOPIC_ACTS.get(0, []), "FOUNDATIONS")

for t in C.TOPICS:
    if t["num"] == 0:
        continue
    idx = t["num"] - 1
    col = DMAIC_COLORS[idx % len(DMAIC_COLORS)]
    d.section(f"DMAIC · {t['phase']}", t["title"], t["code"], t["subtitle"])
    # concept tiles: chunk at 8 so the grid never overflows
    cons = t["concepts"]
    for i in range(0, len(cons), 8):
        chunk = cons[i:i + 8]
        suffix = "" if len(cons) <= 8 else f" ({i // 8 + 1})"
        d.tile_grid(f"Key Concepts — {t['phase'].title()}{suffix}", chunk,
                    kicker=f"{t['phase']} · {t['weighting']} OF THE COURSE",
                    cols=2, size=14, accent=col)
    # teaching content for this phase
    PHASE_FN[t["num"]](d)
    # labs that belong to this phase
    acts = TOPIC_ACTS.get(t["num"], [])
    if acts:
        core = [a for a in acts if not a.get("elective")]
        opts = [a for a in acts if a.get("elective")]
        # Truncate on a WORD boundary, never mid-word. The caps are set above the
        # longest real lab title (83 chars) and build line (94), so in practice
        # nothing is cut at all — the clip is a safety net for future content.
        def clip(s, n):
            if len(s) <= n:
                return s
            cut = s.rfind(" ", 0, n)
            return (s[:cut] if cut > 0 else s[:n]).rstrip(" ,;:-—") + "…"

        def _with_data(a, body):
            """Append the workbook name so the deck, LG, LP and labs all cite the
            SAME file — a learner reading the slide knows which file to open."""
            files = [d["file"] for d in DATASETS.get(a["num"], [])]
            if not files:
                return clip(body, 108)
            return clip(body, 84) + "  •  Data: " + files[0]

        rows = []
        for a in core:
            rows.append((clip(f"Lab {a['num']} — {a['title']}", 88), _with_data(a, a["build"])))
        for a in opts:
            rows.append((clip(f"Lab {a['num']} (elective) — {a['title'].replace('Elective — ', '')}", 88),
                         _with_data(a, a["build"])))
        # tile_grid caps out around 6 rows at cols=1; chunk so nothing overflows
        for i in range(0, len(rows), 6):
            chunk = rows[i:i + 6]
            suffix = "" if len(rows) <= 6 else f" ({i // 6 + 1})"
            d.tile_grid(f"Hands-On Labs — {t['phase'].title()}{suffix}", chunk,
                        kicker="WHAT YOU'LL DO", cols=1, size=14, accent=col)
        render_labs(acts, f"DMAIC · {t['phase']}")
    # phase recap
    d.content(f"Recap — {t['phase'].title()}",
              [c[0] + " — " + c[1] for c in t["concepts"]][:6],
              kicker="PHASE RECAP", size=14)

# ============================================================ WRAP-UP
d.section("WRAP-UP", "Course Summary & Next Steps", "")
d.dmaic_wheel("What You Achieved — The Full DMAIC Journey", [
    ("D", "Define", ["Chartered your capstone", "Built the CTQ flowdown", "Mapped stakeholders", "Planned the change"]),
    ("M", "Measure", ["Proved the gage (R&R)", "Ran attribute MSA / Kappa", "Handled non-normal data", "Baselined capability"]),
    ("A", "Analyze", ["Fitted multiple regression", "Ran ANOVA & interactions", "Decomposed multi-vari", "Proved root cause"]),
    ("I", "Improve", ["Designed full factorials", "Screened with fractionals", "Optimised with RSM", "De-risked with FMEA"]),
    ("C", "Control", ["Built CUSUM & EWMA", "Applied T-squared", "Validated the benefit", "Handed over"]),
], kicker="YOUR CAPSTONE PACKAGE")

d.tile_grid("Your Integrated Capstone Package", [
    ("Portfolio & charter", "Weighted selection matrix, business case and governed charter."),
    ("Customer requirements", "VOC log, Kano classification and CTQ flowdown to controllable Xs."),
    ("Process baseline", "SIPOC, swimlane map, VSM, takt time and quantified waste."),
    ("Valid measurement", "Gage R&R, attribute Kappa study and a nested gauge design."),
    ("Performance baseline", "RTY, DPMO, sigma level, Cpk and Ppk with normality handled."),
    ("Proven root causes", "Regression model, ANOVA, multi-vari and chi-square evidence."),
    ("Optimised improvements", "DOE design, alias structure, RSM optimum and FMEA re-scoring."),
    ("Sustained control", "CUSUM/EWMA charts, control plan and Finance-validated benefit."),
], kicker="WHAT YOU BUILT", cols=2, size=13)

d.tile_grid("Capstone Readiness Checklist", [
    "Can you defend your project selection against the portfolio criteria?",
    "Can you prove your measurement system is valid for your data type?",
    "Can you state the power of your tests and justify your sample size?",
    "Can you interpret your regression coefficients in business language?",
    "Can you explain your DOE resolution and what effects were aliased?",
    "Can you show sustained performance on a control chart after handover?",
], kicker="BEFORE YOUR PRESENTATION", cols=1, size=14, accent=TEAL)

d.tile_grid("Capstone Readiness Checklist (2)", [
    "Can you separate hard, soft and cost-avoidance benefits?",
    "Can you name who in Finance validated your benefit, and over what period?",
    "Can you answer a confounding challenge with evidence rather than assertion?",
    "Can you state what stops this improvement decaying in six months?",
    "Can you coach a Green Belt through the analysis you just performed?",
], kicker="BEFORE YOUR PRESENTATION", cols=1, size=14, accent=TEAL)

d.tile_grid("Continuing Your Black Belt Journey", [
    ("Complete your capstone", "Take the project you started here through to real closure."),
    ("Mentor Green Belts", "Coach their analysis rather than performing it for them."),
    ("Master Black Belt", "The next step — leads programmes and develops Black Belts."),
    ("Log your projects", "Certification requires documented, benefit-validated projects."),
], kicker="NEXT STEPS", cols=2, size=15, accent=AMBER)

# ============================================================ CLOSE (house order)
# Assessment -> Assessment Flow -> Digital Attendance -> TRAQOM -> Thank You
d.big_statement("Final Assessment",
                "Sit the Written Assessment (SAQ, 1 hour) then the Case Study (90 minutes) — both "
                "open book. Your capstone project and presentation are delivered in addition.",
                "ASSESSMENT", color=VIOLET)

d.flow_h("Assessment Flow", ASSESSMENT_FLOW, kicker="ON ASSESSMENT DAY", color=VIOLET)

d.flow_h("Digital Attendance (Assessment)", [
    "Trainer displays the SSG digital attendance QR code",
    "Scan the QR code with your phone camera",
    "Key in your NRIC/FIN and submit",
    "Attendance must be recorded before you begin the papers",
], kicker="TRAQOM · SSG DIGITAL ATTENDANCE", color=BLUE)

d.flow_h("TRAQOM Survey", [
    "Open the TRAQOM survey link on the LMS",
    "Key in the last four characters of your NRIC/FIN",
    "Key in the six-digit course run ID",
    "Complete and submit — your feedback shapes this course",
], kicker="YOUR FEEDBACK", color=TEAL)

d.content("Certificate & Support", [
    "Two e-certificates are awarded on demonstrating competency and achieving at least 75% attendance.",
    "A SkillsFuture Statement of Attainment (SOA) is issued for the WSQ assessment.",
    "Email: enquiry@tertiaryinfotech.com",
    "Tel / WhatsApp: +65 6100 0613",
], kicker="AFTER THE COURSE")

d.big_statement("Thank You!",
                "Now go and finish the project you started here, then mentor the next Green "
                "Belt through theirs — that is what a Black Belt is for.",
                "END OF COURSE", color=BLUE)

# ============================================================ TRANSITIONS + SAVE
d.apply_transitions(kind="fade", dur_ms=700)

out = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
d.prs.save(out)
print(f"✅ {out}")
print(f"   {len(d.prs.slides._sldIdLst)} slides")
