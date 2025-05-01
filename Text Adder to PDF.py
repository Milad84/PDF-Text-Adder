import fitz   # PyMuPDF
import glob, os

INPUT_FOLDER  = r"C:\Users\milad\Downloads\PDFs withouth ID\PDFs withouth ID"
OUTPUT_FOLDER = r"C:\Users\milad\Downloads\Fixed PDFs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ─── Positioning for upper-right corner ───────────────────────────────────────
margin_right = 170   # points in from right edge
margin_top   = 51.5    # points down from top edge

for pdf_path in glob.glob(os.path.join(INPUT_FOLDER, "*.pdf")):
    doc  = fitz.open(pdf_path)
    page = doc[0]

    # only stamp if “ID:” really isn’t there
    if "ID:" not in page.get_text():
        w, h = page.rect.width, page.rect.height

        # **TOP-LEFT** origin, +X→right, +Y↓down
        x = w - margin_right
        y = margin_top

        page.insert_text(
            (x, y),
            "ID:",
            fontsize=10,
            fontname="helv"
        )

    out_path = os.path.join(OUTPUT_FOLDER, os.path.basename(pdf_path))
    doc.save(out_path)
    doc.close()
