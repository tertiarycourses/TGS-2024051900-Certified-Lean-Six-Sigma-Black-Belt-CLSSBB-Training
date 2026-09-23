#!/usr/bin/env python3
"""Render each lab's worksheet.md and debrief.md to PDF.

The reference packs on the course Drive ship debrief.pdf beside debrief.md; we
also ship worksheet.pdf, because the worksheet is the one file learners actually
print and write on in class.

Markdown is rendered directly to PDF with ReportLab rather than going through
LibreOffice — there are 68 small documents and a soffice round-trip per file is
slow and needs a DOCX intermediate we would otherwise never use.

Run after build_labs.py:  python3 build_lab_pdfs.py
"""
import glob
import os
import re
import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, HRFlowable)

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C

NAVY = colors.HexColor("#1F3864")
GREY = colors.HexColor("#595959")

BODY = ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=15,
                      spaceAfter=6)
H1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=17, leading=21,
                    textColor=NAVY, spaceAfter=10, spaceBefore=2)
H2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13, leading=17,
                    textColor=NAVY, spaceAfter=7, spaceBefore=11)
H3 = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=11, leading=15,
                    textColor=NAVY, spaceAfter=5, spaceBefore=9)
QUOTE = ParagraphStyle("quote", parent=BODY, leftIndent=10, textColor=NAVY,
                       fontName="Helvetica-Oblique")
RULE = ParagraphStyle("rule", parent=BODY, textColor=colors.HexColor("#9B9B9B"))
SMALL = ParagraphStyle("small", parent=BODY, fontSize=8, textColor=GREY)


def esc(t):
    t = (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    # markdown inline -> reportlab inline
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+?)`", r'<font face="Courier">\1</font>', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", t)
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(GREY)
    canvas.drawString(18 * mm, 12 * mm,
                      f"{C.TITLE}  ·  {C.COURSE_CODE}  ·  Version {C.VERSION}")
    canvas.drawRightString(A4[0] - 18 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


def md_to_flow(md):
    flow = []
    lines = md.split("\n")
    i = 0
    tbl = []
    while i < len(lines):
        ln = lines[i].rstrip()

        # skip the HTML traceability comment
        if ln.startswith("<!--"):
            i += 1
            continue

        # table block
        if ln.startswith("|"):
            tbl.append(ln)
            i += 1
            if i < len(lines) and lines[i].rstrip().startswith("|"):
                continue
            rows = []
            for r in tbl:
                cells = [c.strip() for c in r.strip("|").split("|")]
                if all(set(c) <= set("-: ") for c in cells):
                    continue
                rows.append([Paragraph(esc(c), BODY) for c in cells])
            tbl = []
            if rows:
                ncol = max(len(r) for r in rows)
                rows = [r + [Paragraph("", BODY)] * (ncol - len(r)) for r in rows]
                avail = A4[0] - 36 * mm
                t = Table(rows, colWidths=[avail / ncol] * ncol, hAlign="LEFT")
                t.setStyle(TableStyle([
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BFBFBF")),
                    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]))
                flow.append(t)
                flow.append(Spacer(1, 7))
            continue

        if not ln.strip():
            i += 1
            continue
        if ln.startswith("### "):
            flow.append(Paragraph(esc(ln[4:]), H3))
        elif ln.startswith("## "):
            flow.append(Paragraph(esc(ln[3:]), H2))
        elif ln.startswith("# "):
            flow.append(Paragraph(esc(ln[2:]), H1))
        elif ln.startswith("> "):
            flow.append(Paragraph(esc(ln[2:]), QUOTE))
        elif ln.startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            if buf:
                flow.append(Paragraph(
                    '<font face="Courier" size="8">'
                    + "<br/>".join(esc(b) for b in buf) + "</font>", BODY))
        elif set(ln.strip()) == {"_"}:
            # A writing line. Draw it as a rule rather than underscore text,
            # which would wrap and leave a stub on the next line.
            flow.append(Spacer(1, 19))
            flow.append(HRFlowable(width="100%", thickness=0.5,
                                   color=colors.HexColor("#B4B4B4"),
                                   spaceBefore=0, spaceAfter=0))
        elif ln.strip() == "---":
            flow.append(Spacer(1, 5))
        elif re.match(r"^\s*[-*] ", ln):
            flow.append(Paragraph("• " + esc(re.sub(r"^\s*[-*] ", "", ln)),
                                  ParagraphStyle("li", parent=BODY, leftIndent=11)))
        elif re.match(r"^\s*\d+\. ", ln):
            flow.append(Paragraph(esc(ln.strip()),
                                  ParagraphStyle("ol", parent=BODY, leftIndent=11)))
        else:
            flow.append(Paragraph(esc(ln), BODY))
        i += 1
    return flow


def render(md_path, pdf_path):
    with open(md_path) as f:
        md = f.read()
    doc = SimpleDocTemplate(
        pdf_path, pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=16 * mm, bottomMargin=20 * mm,
        title=os.path.basename(pdf_path), author=C.ORG)
    doc.build(md_to_flow(md), onFirstPage=footer, onLaterPages=footer)


def main():
    repo = os.environ.get("COURSE_REPO")
    if not repo:
        d = HERE
        for _ in range(8):
            d = os.path.dirname(d)
            if os.path.isdir(os.path.join(d, "labs")):
                repo = d
                break
    labs = os.path.join(repo, "labs")
    n = 0
    # Lab folders are named "NN - Title"; skip archive/ and any loose files.
    for folder in sorted(glob.glob(os.path.join(labs, "[0-9][0-9] - *"))):
        if not os.path.isdir(folder):
            continue
        for stem in ("worksheet", "debrief"):
            md = os.path.join(folder, f"{stem}.md")
            if os.path.exists(md):
                render(md, os.path.join(folder, f"{stem}.pdf"))
                n += 1
    print(f"Rendered {n} lab PDFs in {labs}")


if __name__ == "__main__":
    main()
