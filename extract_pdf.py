#!/usr/bin/env python3
import pdfplumber
import sys

def extract_pdf_text(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
            return text
    except Exception as e:
        print(f"Error extracting text: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    pdf_path = "Hasibullah Sahibzada-3ore.pdf"
    text = extract_pdf_text(pdf_path)
    if text:
        print(text)
    else:
        sys.exit(1)

