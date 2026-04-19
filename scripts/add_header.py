from pathlib import Path

folder = Path("clean")
files = sorted(folder.glob("*.txt"))
print(f"Found {len(files)} cleaned txt files in {folder.resolve()}")

for f in files:
    print(f"Adding header: {f.name}")
    content = f.read_text(encoding="utf-8", errors="ignore").strip()

    header = f"""DOCUMENT: {f.stem}
SOURCE: {f.stem}.pdf
LANGUAGE: de

CONTENT

"""

    f.write_text(header + content + "\n", encoding="utf-8")

print("Done. Headers added.")
