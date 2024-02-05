import os
from PyPDF2 import PdfFileReader
from reportlab.pdfgen import canvas

def extract_names_from_pdf(file_path):
    pdf = PdfFileReader(file_path)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

    # Supondo que os nomes estejam separados por novas linhas
    names = text.split('\n')
    return names

def create_appointments(names, output_dir):
    for name in names:
        output_path = os.path.join(output_dir, f"{name}_compromisso.pdf")
        c = canvas.Canvas(output_path)
        text = f"Compromisso para {name}"
        c.drawString(100, 800, text)
        c.save()

# Substitua 'input.pdf' pelo caminho do seu arquivo PDF
names = extract_names_from_pdf('FECHADO.pdf')

# Substitua 'output_dir' pelo diretório onde você deseja salvar os novos arquivos PDF
create_appointments(names, 'imprimir')
