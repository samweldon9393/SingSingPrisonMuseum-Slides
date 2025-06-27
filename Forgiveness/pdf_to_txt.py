from pathlib import Path
from pdfminer.high_level import extract_text

pdf_dir = Path("./transcripts")
output_dir = pdf_dir / "../txt"
output_dir.mkdir(exist_ok=True)

for pdf_file in pdf_dir.glob("*.pdf"):
    text = extract_text(pdf_file)
    output_file = output_dir / (pdf_file.stem + ".txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
