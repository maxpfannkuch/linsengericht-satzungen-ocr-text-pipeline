from pathlib import Path

src = Path("clean")
out = Path("dataset.txt")
files = sorted(src.glob("*.txt"))
print(f"Found {len(files)} cleaned txt files in {src.resolve()}")

with out.open("w", encoding="utf-8") as outfile:
    for f in files:
        print(f"Merging: {f.name}")
        outfile.write(f"===== {f.name} =====\n")
        outfile.write(f.read_text(encoding="utf-8", errors="ignore"))
        outfile.write("\n\n")

print(f"Done. Combined dataset written to {out.resolve()}")
