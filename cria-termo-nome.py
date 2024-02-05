import PyPDF2
from reportlab.pdfgen import canvas

def extract_names_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    page_obj = pdf_reader.getPage(0)
    text = page_obj.extract_text()
    pdf_file_obj.close()
    names = text.split('\n')
    return names

def create_pdf_for_each_name(names):
    for name in names:
        c = canvas.Canvas(name+".pdf")
        c.drawString(100, 750, "Compromisso para: "+name)
        c.save()

file_path = "teste.pdf"  # Substitua por seu arquivo PDF
names = extract_names_from_pdf(file_path)
create_pdf_for_each_name(names)
