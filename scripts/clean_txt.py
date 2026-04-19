import re
from pathlib import Path

src = Path("txt")
dst = Path("clean")
dst.mkdir(exist_ok=True)

files = sorted(src.glob("*.txt"))
print(f"Found {len(files)} txt files in {src.resolve()}")

for f in files:
    print(f"Cleaning: {f.name}")
    text = f.read_text(encoding="utf-8", errors="ignore")

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Rejoin words split across lines with hyphenation
    text = re.sub(r'(\w)-\n(\w)', r'\1\2', text)

    # Replace single line breaks inside flowing text with spaces
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

    # Normalize repeated spaces and tabs
    text = re.sub(r'[ \t]+', ' ', text)

    # Reduce too many blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    text = text.strip() + "\n"

    out = dst / f.name
    out.write_text(text, encoding="utf-8")
    print(f"Saved: {out}")

print("Done. Cleaned files are in 'clean/'.")
