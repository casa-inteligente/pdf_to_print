import PyPDF2
from reportlab.pdfgen import canvas

def create_pdf(name):
    c = canvas.Canvas(f"Termo_de_Compromisso_{name}.pdf")
    text = f"""
    TERMO DE COMPROMISSO

    Eu, {name}, comprometo-me a cumprir as obrigações e responsabilidades que me foram atribuídas.
    """
    c.drawString(100, 750, text)
    c.save()

def read_names_from_pdf(file_name):
    #pdf_file = open(file_name, 'rb')
    pdf_file = open('FECHADO.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    page = pdf_reader.getPage(0)
    names = page.extractText().split('\n')
    pdf_file.close()
    return names

file_name = 'fef.pdf'
names = read_names_from_pdf(file_name)

for name in names:
    create_pdf(name)