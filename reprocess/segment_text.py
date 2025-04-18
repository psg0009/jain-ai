import os
import re
import json

OCR_DIR = "ocr_raw"
OUTPUT_FILE = "processed/segments.jsonl"
os.makedirs("processed", exist_ok=True)

entries = []
for filename in sorted(os.listdir(OCR_DIR)):
    if not filename.endswith(".txt"):
        continue

    page_id = filename.replace(".txt", "")
    with open(os.path.join(OCR_DIR, filename), "r", encoding="utf-8") as f:
        text = f.read()

    # Basic sentence/verse segmentation using danda (।)
    sentences = [s.strip() for s in re.split(r"[।॥]", text) if s.strip()]

    for idx, sentence in enumerate(sentences):
        entries.append({
            "page": page_id,
            "line_id": f"{page_id}_{idx+1}",
            "text": sentence
        })

# Save as newline-delimited JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for entry in entries:
        out.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f" Saved {len(entries)} sentences to {OUTPUT_FILE}")
