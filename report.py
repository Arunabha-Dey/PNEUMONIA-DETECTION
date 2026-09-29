# report.py
from fpdf import FPDF
from PIL import Image
from pathlib import Path
import io

class ReportPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Pneumonia Detection Report", ln=True, align="C")
        self.ln(4)

def create_report(patient_name, age, notes, prediction, score, image_pil, out_path="report.pdf"):
    pdf = ReportPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 8, f"Patient Name: {patient_name}", ln=True)
    pdf.cell(0, 8, f"Age: {age}", ln=True)
    pdf.cell(0, 8, f"Prediction: {prediction} (score: {score:.3f})", ln=True)
    pdf.ln(4)
    pdf.multi_cell(0, 6, f"Notes: {notes}")
    pdf.ln(6)

    # Add image: resize to keep small
    img_io = io.BytesIO()
    image_pil.save(img_io, format="PNG")
    img_io.seek(0)
    # FPDF requires a filename or BytesIO - use temp file approach by saving local
    temp_img = Path("temp_uploaded.png")
    with open(temp_img, "wb") as f:
        f.write(img_io.read())
    pdf.image(str(temp_img), x=15, w=180)
    if temp_img.exists():
        temp_img.unlink()
    pdf.output(out_path)
    return out_path
