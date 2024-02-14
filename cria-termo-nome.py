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


import spacy
from PyPDF2 import PdfFileReader
from pathlib import Path

# Carregando o modelo spaCy
nlp = spacy.load("pt_core_news_sm")

# Definindo o diretório de entrada e saída
diretorio_entrada = Path("C:/Users/AULA-1/Documents/GitHub/pdf_to_print/Arquivo_analisado/")
diretorio_saida = Path("C:/Users/AULA-1/Documents/GitHub/pdf_to_print/imprimir/")

# Criando o diretório de saída caso não exista
diretorio_saida.mkdir(parents=True, exist_ok=True)

# Processando cada arquivo PDF no diretório de entrada
for arquivo_pdf in diretorio_entrada.glob("*.pdf"):
    # Lendo o arquivo PDF
    arquivo_pdf = "ESTE.pdf" #Comentar esta linha
    with open(arquivo_pdf, "rb") as f:
        pdf_reader = PdfFileReader(f)

    # Extraindo o texto do PDF
    texto_pdf = ""
    for pagina in pdf_reader.pages:
        texto_pdf += pagina.extractText()

    # Identificando nomes no texto
    nomes = [entidade.text for entidade in nlp(texto_pdf).ents if entidade.label_ == "PER"]

    # Gerando o termo de compromisso para cada nome
    for nome in nomes:
        termo_compromisso = f"""
        TERMO DE COMPROMISSO

        Eu, {nome}, declaro que estou ciente dos termos e condições do presente acordo.

        Assinado em {data.strftime("%d/%m/%Y")}.

        ___________________
        {nome}
        """

        # Salvando o termo de compromisso em um arquivo PDF
        with open(diretorio_saida / f"{nome}_termo_compromisso.pdf", "wb") as f:
            f.write(termo_compromisso.encode("utf-8"))

    print(f"Termos de compromisso gerados para {arquivo_pdf.name}")