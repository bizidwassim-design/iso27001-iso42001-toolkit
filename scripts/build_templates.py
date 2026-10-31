#!/usr/bin/env python3
"""Generate the Excel templates in templates/ from the CSV sources in data/.

    pip install openpyxl && python scripts/build_templates.py

Outputs
  templates/Statement-of-Applicability.xlsx   ISO 27001 Annex A (93 controls) + ISO 42001 Annex A (38 controls)
  templates/Risk-Treatment-Plan.xlsx          treatment plan with sample (fictional) rows and progress formulas
  templates/RACI-Matrix.xlsx                  ISMS/AIMS responsibilities per activity
Everything in the workbooks is also available as CSV next to them, for people who do not use Excel.
"""
from __future__ import annotations

import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "templates"
OUT.mkdir(exist_ok=True)

NAVY = "1F3864"
HEADER_FONT = Font(name="Arial", bold=True, color="FFFFFF", size=10)
HEADER_FILL = PatternFill("solid", fgColor=NAVY)
BODY_FONT = Font(name="Arial", size=10)
INPUT_FONT = Font(name="Arial", size=10, color="0000FF")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def style_header(ws, row: int, ncols: int) -> None:
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font, cell.fill, cell.border = HEADER_FONT, HEADER_FILL, BORDER
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    ws.freeze_panes = ws.cell(row=row + 1, column=1)
    ws.auto_filter.ref = f"A{row}:{get_column_letter(ncols)}{row}"


def style_body(ws, first_row: int, last_row: int, ncols: int, input_cols: set[int] = frozenset()) -> None:
    for r in range(first_row, last_row + 1):
        for c in range(1, ncols + 1):
            cell = ws.cell(row=r, column=c)
            cell.font = INPUT_FONT if c in input_cols else BODY_FONT
            cell.border, cell.alignment = BORDER, WRAP


def widths(ws, sizes: list[int]) -> None:
    for i, w in enumerate(sizes, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(name: str, header: list[str], rows: list[list[str]]) -> None:
    with (OUT / name).open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def intro(ws, title: str, lines: list[str]) -> None:
    ws["A1"] = title
    ws["A1"].font = Font(name="Arial", bold=True, size=14, color=NAVY)
    for i, line in enumerate(lines, start=2):
        ws.cell(row=i, column=1, value=line).font = Font(name="Arial", size=10, italic=True)


# ---------------------------------------------------------------- Statement of Applicability
def build_soa(wb: Workbook) -> None:
    status_dv = DataValidation(type="list", formula1='"Implemented,Partially implemented,Planned,Not applicable"', allow_blank=True)
    just_dv = DataValidation(type="list", formula1='"Risk assessment,Legal / contractual,Business requirement,Best practice,Not applicable"', allow_blank=True)
    header = ["Control ID", "Control title", "Domain", "Applicable? (Y/N)", "Justification for inclusion / exclusion",
              "Implementation status", "Control owner", "Implementation description / reference", "Evidence location", "Last review"]

    for sheet, source, label in (
        ("ISO 27001 Annex A", "iso27001-annex-a-controls.csv", "ISO/IEC 27001:2022 Annex A — 93 controls"),
        ("ISO 42001 Annex A", "iso42001-annex-a-controls.csv", "ISO/IEC 42001:2023 Annex A — 38 controls"),
    ):
        ws = wb.create_sheet(sheet)
        intro(ws, f"Statement of Applicability — {label}",
              ["Blue cells are inputs. Mark every control Y or N and justify the decision — auditors read this document first.",
               "Status: Implemented / Partially implemented / Planned / Not applicable."])
        start = 4
        for c, h in enumerate(header, start=1):
            ws.cell(row=start, column=c, value=h)
        style_header(ws, start, len(header))
        rows = read_csv(source)
        csv_rows = []
        for i, r in enumerate(rows, start=start + 1):
            ws.cell(row=i, column=1, value=r["control_id"])
            ws.cell(row=i, column=2, value=r["control_title"])
            ws.cell(row=i, column=3, value=r["domain"])
            ws.cell(row=i, column=4, value="Y")
            csv_rows.append([r["control_id"], r["control_title"], r["domain"], "Y", "", "", "", "", "", ""])
        last = start + len(rows)
        style_body(ws, start + 1, last, len(header), input_cols={4, 5, 6, 7, 8, 9, 10})
        ws.add_data_validation(status_dv); ws.add_data_validation(just_dv)
        status_dv.add(f"F{start + 1}:F{last}"); just_dv.add(f"E{start + 1}:E{last}")
        yn = DataValidation(type="list", formula1='"Y,N"', allow_blank=False); ws.add_data_validation(yn); yn.add(f"D{start + 1}:D{last}")
        ws.conditional_formatting.add(f"F{start + 1}:F{last}", FormulaRule(formula=[f'$F{start + 1}="Implemented"'], fill=PatternFill("solid", fgColor="C6E0B4")))
        ws.conditional_formatting.add(f"F{start + 1}:F{last}", FormulaRule(formula=[f'$F{start + 1}="Partially implemented"'], fill=PatternFill("solid", fgColor="FFE699")))
        ws.conditional_formatting.add(f"F{start + 1}:F{last}", FormulaRule(formula=[f'$F{start + 1}="Planned"'], fill=PatternFill("solid", fgColor="F4B183")))
        widths(ws, [11, 42, 16, 12, 34, 20, 18, 40, 28, 12])
        write_csv(f"statement-of-applicability-{'iso27001' if '27001' in sheet else 'iso42001'}.csv", header, csv_rows)

    # Summary sheet in front
    ws = wb.create_sheet("Summary", 0)
    intro(ws, "Statement of Applicability — summary", ["Counts update automatically from the two Annex A sheets."])
    ws["A4"], ws["B4"], ws["C4"] = "Status", "ISO 27001 Annex A", "ISO 42001 Annex A"
    style_header(ws, 4, 3)
    for i, status in enumerate(["Implemented", "Partially implemented", "Planned", "Not applicable", "Not yet assessed"], start=5):
        ws.cell(row=i, column=1, value=status)
        for col, sheet in ((2, "'ISO 27001 Annex A'"), (3, "'ISO 42001 Annex A'")):
            if status == "Not yet assessed":
                ws.cell(row=i, column=col, value=f'=COUNTA({sheet}!A5:A200)-COUNTA({sheet}!F5:F200)')
            else:
                ws.cell(row=i, column=col, value=f'=COUNTIF({sheet}!F5:F200,A{i})')
    ws["A10"] = "Total controls"
    ws["B10"] = "=COUNTA('ISO 27001 Annex A'!A5:A200)"
    ws["C10"] = "=COUNTA('ISO 42001 Annex A'!A5:A200)"
    ws["A11"], ws["B11"], ws["C11"] = "% implemented", "=IFERROR(B5/B10,0)", "=IFERROR(C5/C10,0)"
    ws["B11"].number_format = ws["C11"].number_format = "0%"
    style_body(ws, 5, 11, 3)
    widths(ws, [24, 20, 20])


# ---------------------------------------------------------------- Risk Treatment Plan
def build_rtp(wb: Workbook) -> None:
    ws = wb.create_sheet("Risk Treatment Plan")
    intro(ws, "Risk Treatment Plan (ISO 27001 §6.1.3 / ISO 42001 §6.1.3)",
          ["One row per risk requiring treatment. Sample rows are FICTIONAL — delete them. Blue cells are inputs; status colours and the summary update automatically."])
    header = ["Risk ID", "Risk description", "Asset / AI system", "Inherent score", "Treatment option", "Treatment actions (controls)",
              "Annex A controls", "Owner", "Budget", "Start", "Due", "Status", "Residual score", "Residual accepted by", "Notes"]
    start = 4
    for c, h in enumerate(header, start=1):
        ws.cell(row=start, column=c, value=h)
    style_header(ws, start, len(header))
    samples = [
        ["R-07", "Ransomware via unpatched edge VPN appliance", "Remote access gateway", 20, "Mitigate", "Patch within 7 days; MFA on VPN; EDR on servers; immutable backups", "A.8.8, A.5.17, A.8.7, A.8.13", "Head of Infrastructure", "35 000", "2026-10-01", "2026-11-30", "In progress", 8, "CIO", ""],
        ["R-12", "Business email compromise of finance staff", "Finance mailboxes / payment process", 16, "Mitigate", "Payment call-back procedure; DMARC p=reject; targeted awareness", "A.5.10, A.6.3, A.8.23", "CFO", "5 000", "2026-10-15", "2026-12-15", "Planned", 6, "", ""],
        ["R-19", "Sensitive data pasted into public generative-AI tools", "Workforce use of AI assistants", 15, "Mitigate", "Approved AI platform; AI acceptable-use policy; DLP rules; impact assessment", "A.5.12, A.8.12 / ISO 42001 A.6.2.2, A.9.2", "CIO", "12 000", "2026-11-01", "2027-01-31", "Planned", 6, "", "ISO 42001 scope"],
        ["R-03", "Single logistics SaaS provider with no exit plan", "Transport management SaaS", 12, "Transfer", "Contract exit clause; quarterly data export test; secondary provider identified", "A.5.19, A.5.20, A.5.23", "COO", "0", "2026-11-01", "2027-02-28", "Not started", 8, "", ""],
        ["R-31", "AI pricing model drifts and produces discriminatory quotes", "Dynamic pricing model (AI system)", 12, "Mitigate", "Bias testing before release; monthly drift monitoring; human review threshold", "ISO 42001 A.6.2.4, A.6.2.6, A.7.4", "Head of Data", "8 000", "2026-12-01", "2027-03-31", "Not started", 4, "", "AI impact assessment ref AIA-004"],
    ]
    for i, row in enumerate(samples, start=start + 1):
        for c, v in enumerate(row, start=1):
            ws.cell(row=i, column=c, value=v)
    last = start + 40
    style_body(ws, start + 1, last, len(header), input_cols=set(range(1, 16)))
    opt = DataValidation(type="list", formula1='"Mitigate,Transfer,Avoid,Accept"', allow_blank=True)
    st = DataValidation(type="list", formula1='"Not started,Planned,In progress,Done,Overdue"', allow_blank=True)
    ws.add_data_validation(opt); ws.add_data_validation(st)
    opt.add(f"E{start + 1}:E{last}"); st.add(f"L{start + 1}:L{last}")
    for status, color in (("Done", "C6E0B4"), ("In progress", "FFE699"), ("Overdue", "F4B183"), ("Not started", "D9D9D9")):
        ws.conditional_formatting.add(f"L{start + 1}:L{last}", FormulaRule(formula=[f'$L{start + 1}="{status}"'], fill=PatternFill("solid", fgColor=color)))
    ws.conditional_formatting.add(f"K{start + 1}:K{last}", FormulaRule(formula=[f'AND($K{start + 1}<>"",$K{start + 1}<TODAY(),$L{start + 1}<>"Done")'], font=Font(color="C00000", bold=True)))
    widths(ws, [8, 38, 24, 9, 12, 44, 24, 18, 10, 11, 11, 13, 9, 18, 24])

    s = wb.create_sheet("RTP Summary")
    intro(s, "Risk treatment — summary", ["Updates automatically from the plan."])
    s["A4"], s["B4"] = "Status", "Risks"
    style_header(s, 4, 2)
    for i, status in enumerate(["Not started", "Planned", "In progress", "Done", "Overdue"], start=5):
        s.cell(row=i, column=1, value=status)
        s.cell(row=i, column=2, value=f"=COUNTIF('Risk Treatment Plan'!L5:L44,A{i})")
    s["A10"], s["B10"] = "Total risks in plan", "=COUNTA('Risk Treatment Plan'!A5:A44)"
    s["A11"], s["B11"] = "Average inherent score", "=IFERROR(AVERAGE('Risk Treatment Plan'!D5:D44),0)"
    s["A12"], s["B12"] = "Average residual score", "=IFERROR(AVERAGE('Risk Treatment Plan'!M5:M44),0)"
    s["B11"].number_format = s["B12"].number_format = "0.0"
    style_body(s, 5, 12, 2)
    widths(s, [26, 12])
    write_csv("risk-treatment-plan.csv", header, [[str(x) for x in r] for r in samples])


# ---------------------------------------------------------------- RACI
def build_raci(wb: Workbook) -> None:
    rows = read_csv("raci-matrix.csv")
    roles = [k for k in rows[0].keys() if k not in ("activity", "clause")]
    ws = wb.create_sheet("RACI")
    intro(ws, "RACI matrix — ISMS / AIMS activities",
          ["R = Responsible, A = Accountable (exactly one per row), C = Consulted, I = Informed. Rename the roles to match your organisation."])
    header = ["Activity", "Clause / control"] + roles + ["Check: one A"]
    start = 4
    for c, h in enumerate(header, start=1):
        ws.cell(row=start, column=c, value=h)
    style_header(ws, start, len(header))
    first_role, last_role = get_column_letter(3), get_column_letter(2 + len(roles))
    for i, r in enumerate(rows, start=start + 1):
        ws.cell(row=i, column=1, value=r["activity"])
        ws.cell(row=i, column=2, value=r["clause"])
        for j, role in enumerate(roles, start=3):
            ws.cell(row=i, column=j, value=r[role] or None).alignment = Alignment(horizontal="center", vertical="top")
        ws.cell(row=i, column=len(header), value=f'=IF(COUNTIF({first_role}{i}:{last_role}{i},"A")=1,"OK","Check")')
    last = start + len(rows)
    style_body(ws, start + 1, last, len(header), input_cols=set(range(3, 3 + len(roles))))
    for j in range(3, 3 + len(roles)):
        for i in range(start + 1, last + 1):
            ws.cell(row=i, column=j).alignment = Alignment(horizontal="center", vertical="top")
    dv = DataValidation(type="list", formula1='"R,A,C,I,R/A"', allow_blank=True)
    ws.add_data_validation(dv); dv.add(f"{first_role}{start + 1}:{last_role}{last}")
    check_col = get_column_letter(len(header))
    ws.conditional_formatting.add(f"{check_col}{start + 1}:{check_col}{last}", FormulaRule(formula=[f'${check_col}{start + 1}="Check"'], fill=PatternFill("solid", fgColor="F4B183")))
    widths(ws, [44, 18] + [14] * len(roles) + [12])
    write_csv("raci-matrix.csv", ["activity", "clause"] + roles, [[r["activity"], r["clause"]] + [r[role] for role in roles] for r in rows])


def main() -> None:
    for name, builder in (("Statement-of-Applicability.xlsx", build_soa), ("Risk-Treatment-Plan.xlsx", build_rtp), ("RACI-Matrix.xlsx", build_raci)):
        wb = Workbook()
        wb.remove(wb.active)
        builder(wb)
        wb.calculation.fullCalcOnLoad = True
        wb.save(OUT / name)
        print("wrote", OUT / name)


if __name__ == "__main__":
    main()
