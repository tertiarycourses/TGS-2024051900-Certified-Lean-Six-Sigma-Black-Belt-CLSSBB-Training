#!/usr/bin/env python3
"""Write one lab's mock-data workbook as a styled .xlsx.

Every workbook gets:
  * a cover/Data Dictionary sheet defining each column, its unit and its spec
  * one sheet per dataset, frozen header row, autofilter, sensible column widths
  * the course footer in the sheet header so a printed copy is traceable

Called by build_labs.py — not run directly.
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# House style — matches the all-white deck: dark navy headers, no heavy fills.
NAVY = "1F3864"
LIGHT = "D9E2F3"
GREY = "F2F2F2"

H_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
T_FONT = Font(name="Calibri", size=16, bold=True, color=NAVY)
S_FONT = Font(name="Calibri", size=10, italic=True, color="595959")
B_FONT = Font(name="Calibri", size=11, bold=True, color=NAVY)
N_FONT = Font(name="Calibri", size=11)

H_FILL = PatternFill("solid", fgColor=NAVY)
L_FILL = PatternFill("solid", fgColor=LIGHT)
G_FILL = PatternFill("solid", fgColor=GREY)

THIN = Side(style="thin", color="BFBFBF")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def _autosize(ws, maxw=52):
    widths = {}
    for row in ws.iter_rows():
        for c in row:
            if c.value is None:
                continue
            L = max(len(x) for x in str(c.value).split("\n"))
            widths[c.column] = min(max(widths.get(c.column, 10), L + 3), maxw)
    for col, w in widths.items():
        ws.column_dimensions[get_column_letter(col)].width = w


def _dictionary(wb, spec, act, C):
    ws = wb.create_sheet("Data Dictionary", 0)
    ws.sheet_view.showGridLines = False
    r = 1
    ws.cell(r, 1, f"Lab {act['num']} — {act['title'].replace('Elective — ', '')}").font = T_FONT
    r += 1
    ws.cell(r, 1, f"{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION}").font = S_FONT
    r += 2

    ws.cell(r, 1, "About this workbook").font = B_FONT
    r += 1
    c = ws.cell(r, 1, spec["about"])
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=r, start_column=1, end_row=r + 2, end_column=6)
    ws.row_dimensions[r].height = 30
    r += 4

    kind = ("This workbook contains REAL (simulated) process data for you to analyse."
            if spec["kind"] == "data" else
            "This workbook is a TEMPLATE. The blank columns are the ones you complete "
            "during the lab.")
    ws.cell(r, 1, kind).font = Font(name="Calibri", size=11, italic=True, color=NAVY)
    r += 2

    ws.cell(r, 1, "Sheets in this workbook").font = B_FONT
    r += 1
    for h in ("Sheet", "What it contains", "Rows"):
        pass
    hdr = ["Sheet", "What it contains", "Rows"]
    for i, h in enumerate(hdr, 1):
        cell = ws.cell(r, i, h)
        cell.font = H_FONT
        cell.fill = H_FILL
        cell.border = BOX
    r += 1
    for sh in spec["sheets"]:
        for i, v in enumerate([sh["name"], sh["desc"], len(sh["rows"])], 1):
            cell = ws.cell(r, i, v)
            cell.border = BOX
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    r += 1

    ws.cell(r, 1, "Column definitions").font = B_FONT
    r += 1
    hdr = ["Sheet", "Column", "Definition / unit"]
    for i, h in enumerate(hdr, 1):
        cell = ws.cell(r, i, h)
        cell.font = H_FONT
        cell.fill = H_FILL
        cell.border = BOX
    r += 1
    for sh in spec["sheets"]:
        for col, note in sh["cols"]:
            for i, v in enumerate([sh["name"], col, note], 1):
                cell = ws.cell(r, i, v)
                cell.border = BOX
                cell.alignment = Alignment(wrap_text=True, vertical="top")
                if i == 2:
                    cell.font = Font(name="Calibri", size=11, bold=True)
            r += 1
    r += 1

    ws.cell(r, 1, "Specification limits used throughout this course").font = B_FONT
    r += 1
    for label, val in [
        ("Project Y", "Seal weld burst pressure"),
        ("Unit", "kPa"),
        ("Lower spec limit (LSL)", 180),
        ("Target", 220),
        ("Upper spec limit (USL)", 260),
    ]:
        ws.cell(r, 1, label).font = Font(name="Calibri", size=11, bold=True)
        ws.cell(r, 2, val)
        r += 1

    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["B"].width = 34
    ws.column_dimensions["C"].width = 62
    return ws


def _data_sheet(wb, sh):
    ws = wb.create_sheet(sh["name"][:31])
    ws.cell(1, 1, sh["desc"]).font = S_FONT
    headers = [c[0] for c in sh["cols"]]
    for i, h in enumerate(headers, 1):
        cell = ws.cell(3, i, h)
        cell.font = H_FONT
        cell.fill = H_FILL
        cell.border = BOX
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for ri, row in enumerate(sh["rows"], 4):
        for ci, v in enumerate(row, 1):
            cell = ws.cell(ri, ci, v)
            cell.border = BOX
            cell.font = N_FONT
            if v == "":
                cell.fill = G_FILL          # the blanks the learner fills in
    last = 3 + len(sh["rows"])
    ws.freeze_panes = "A4"
    ws.auto_filter.ref = f"A3:{get_column_letter(len(headers))}{last}"
    ws.sheet_view.showGridLines = False
    _autosize(ws)
    return ws


def write_workbook(path, spec, act, C):
    wb = Workbook()
    wb.remove(wb.active)
    for sh in spec["sheets"]:
        _data_sheet(wb, sh)
    _dictionary(wb, spec, act, C)
    wb.active = 0
    wb.save(path)
    return path
