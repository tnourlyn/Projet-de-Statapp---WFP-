import os
import re
import sys
import pandas as pd

OUT_DIR = "csv_from_xlsx"
SEP = ","  # mets ";" si Excel FR

def safe(s: str) -> str:
    s = s.strip().replace(" ", "_")
    return re.sub(r"[^\w\-]+", "", s)[:120] or "sheet"

def main():
    if len(sys.argv) < 2:
        print("Usage: python xls_to_csv.py <fichier.xlsx>")
        sys.exit(1)

    xlsx = sys.argv[1]
    if not os.path.exists(xlsx):
        print("❌ Fichier introuvable:", xlsx)
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)

    xls = pd.ExcelFile(xlsx, engine="openpyxl")
    print("Onglets:", xls.sheet_names)

    base = safe(os.path.splitext(os.path.basename(xlsx))[0])

    for sheet in xls.sheet_names:
        df = pd.read_excel(xlsx, sheet_name=sheet, engine="openpyxl")
        df = df.dropna(axis=1, how="all")
        out = os.path.join(OUT_DIR, f"{base}__{safe(sheet)}.csv")
        df.to_csv(out, index=False, sep=SEP)
        print("✅", out, "| shape:", df.shape)

if __name__ == "__main__":
    main()
