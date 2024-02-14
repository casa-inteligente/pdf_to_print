# -*- coding: utf-8 -*-
# import PyPDF2
# from reportlab.pdfgen import canvas
#
# def extract_names_from_pdf(file_path):
#     pdf_file_obj = open(file_path, 'rb')
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
#     page_obj = pdf_reader.getPage(0)
#     text = page_obj.extract_text()
#     pdf_file_obj.close()
#     names = text.split('\n')
#     return names
#
# def create_pdf_for_each_name(names):
#     for name in names:
#         c = canvas.Canvas('imprimir/'+name+".pdf")
#         c.drawString(100, 750, "Compromisso para: "+name)
#         c.save()
#
# file_path = "teste.pdf"  # Substitua por seu arquivo PDF
# names = extract_names_from_pdf(file_path)
# create_pdf_for_each_name(names)


import re
import PyPDF2
from reportlab.pdfgen import canvas

def extrair_nomes(texto):
    # Esta é uma expressão regular simples para identificar nomes. Pode precisar ser ajustada.
    return re.findall(r'\b[A-Z][a-z]*\b', texto)

def criar_pdf(nome, termo):
    c = canvas.Canvas(f"imprimir/{nome}.pdf")
    c.drawString(100, 750, f"Termo de Compromisso para {nome}")
    c.drawString(100, 730, termo)
    c.save()

# Lendo o arquivo PDF
with open('ESTE.pdf', 'rb') as arquivo:
    leitor = PyPDF2.PdfFileReader(arquivo)
    texto = ''
    for pagina in range(leitor.numPages):
        texto += leitor.getPage(pagina).extractText()

# Extraindo os nomes
nomes = extrair_nomes(texto)

# Lendo o termo de compromisso
with open('termo_de_compromisso.txt', 'r') as arquivo:
    termo = arquivo.read()

# Criando um PDF para cada nome
for nome in nomes:
    criar_pdf(nome, termo)
