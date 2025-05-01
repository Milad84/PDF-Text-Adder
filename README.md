# PDF-Text-Adder
This is a short script that gives you the option to add a text component to a batch of PDFs

.
├── README.md           ← this file
├── stamp_id.py         ← main stamping script
└── examples/           ← sample PDFs for testing (optional)



# PDF ID Stamper

A small Python utility that automatically “stamps” an `ID:` label into the top-right corner of PDF reports that are missing it. Particularly useful for standardizing batches of traffic-data or speed-study PDFs before downstream ETL (e.g., in FME).

---

## 📦 Features

- Recursively scans a folder of PDFs for missing `ID:` labels  
- Injects `ID:` text at a configurable offset from the top-right corner  
- Preserves PDFs that already contain `ID:`  
- Outputs fixed PDFs to a separate folder  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6+  
- [PyMuPDF (fitz)](https://pypi.org/project/PyMuPDF/)  

```bash
pip install PyMuPDF

