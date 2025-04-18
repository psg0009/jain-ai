# ocr_test.py
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os

# ensure output directory exists
os.makedirs("ocr_raw", exist_ok=True)

# convert all pages
pages = convert_from_path('scans/acaranga.pdf', dpi=300)
for i, page in enumerate(pages, start=1):
    txt = pytesseract.image_to_string(page, lang='hin')
    with open(f"ocr_raw/page_{i:03d}.txt", "w", encoding="utf-8") as f:
        f.write(txt)
print(f"OCR’d {len(pages)} pages → ocr_raw/")
