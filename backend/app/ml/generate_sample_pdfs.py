from pathlib import Path

import pymupdf

OUTPUT_DIR = Path(__file__).resolve().parents[3] / "frontend" / "public" / "samples"

SAMPLES = {
    "sample-pay-stub.pdf": (
        "Pay Stub (synthetic sample)",
        [
            "Sample Synthetic Co.",
            "Pay Stub for Jordan Rivera",
            "Pay Period: 2026-08-15",
            "Gross Income: $5,200.00",
            "Deductions: $1,180.00",
            "Net Pay: $4,020.00",
            "Employee ID: EMP-4821",
        ],
    ),
    "sample-bank-statement.pdf": (
        "Bank Statement (synthetic sample)",
        [
            "Account Statement",
            "Account Holder: Jordan Rivera",
            "Statement Period: August 2026",
            "Opening Balance: $3,410.00",
            "Total Deposits: $4,020.00",
            "Total Withdrawals: $2,860.00",
            "Balance: $4,570.00",
            "Account Number: 1234-5678-9012",
        ],
    ),
    "sample-budget-sheet.pdf": (
        "Budget Sheet (synthetic sample)",
        [
            "Monthly Budget Sheet",
            "Prepared for: Jordan Rivera",
            "Month: August 2026",
            "Net Pay: $4,020.00",
            "Housing: $1,450.00",
            "Food: $520.00",
            "Transportation: $310.00",
            "Other: $400.00",
            "Total Expenses: $2,680.00",
        ],
    ),
}


def _write_pdf(path: Path, title: str, lines: list[str]) -> None:
    doc = pymupdf.open()
    page = doc.new_page(width=612, height=792)
    page.insert_text((72, 90), title, fontsize=16, fontname="helv")
    y = 130
    for line in lines:
        page.insert_text((72, y), line, fontsize=11, fontname="helv")
        y += 24
    doc.save(path)
    doc.close()


def generate() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for filename, (title, lines) in SAMPLES.items():
        _write_pdf(OUTPUT_DIR / filename, title, lines)
    print(f"Wrote {len(SAMPLES)} sample PDFs to {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
