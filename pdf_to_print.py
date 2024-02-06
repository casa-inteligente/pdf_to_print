#####	NOME:				pdf_to_print.py
#####	VERSÃO:				1.0
#####	DESCRIÇÃO:			Coleta informações de um arquivo em pdf e imprime em uma declaração
#####	DATA DA CRIAÇÃO:	24/11/2023
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	DISTRO:				Ubuntu GNU/Linux 22.04
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/casa-inteligente/pdf_to_print

#https://pythonacademy.com.br/blog/manipulando-arquivos-pdf-com-python
#https://www.youtube.com/watch?v=8eNxZI-3Bxs

#import IPython as display
import pandas
import tabula
from tabula.io import read_pdf
from PyPDF2 import PdfWriter
from PyPDF2 import PdfFileReader



#arquivo='teste.pdf'
arquivo='FECHADO.pdf'
#arquivo='www.sc.gov.br_ipen_RelatorioIpen_004_2ReltorioPorSetorImprimir.asp_cd_Unidade=8088&de_Celas=4421,4420,4414,4415,4416,4417,4418,5399,4424,6504,4422,4423,5746,5571,6527&cd_Galeria=.pdf'
paginas='all'


lista_tabela = tabula.io.read_pdf(arquivo,pages=paginas)

# for t in lista_tabela:
#     print(t,"\n--------------\n")


#qUANTIDADE DE PAGINAS
print("==============\n\n\n")
print(len(lista_tabela))
print("\n \n \n ==============\n\n\n")


#imprimi na tela os valores do pdf completo
for tabela in lista_tabela:
    print(tabela, "\n +++++++++++++++++++++\n")
    print(tabela.index)
    #print(tabela.find(''))
print('\n\n\n+++++++++++++++++++++++++++++\n\n\n')

#
# #removendo as coluna de situação
# tabela_limpa = tabela.drop(3, axis=0)
# print('\nimprime a tabela limpa, que não esta limpa ainda..... \n')
# print(tabela_limpa)

print('----Mostra tabela 1\n\n')
tabela1 = lista_tabela[0]
print(tabela1)
print('\n\n\n--------\n\n\n')

print('----Mostra tabela 2\n\n')
tabela2 = lista_tabela[1]
print(tabela2)
print("\n\n--tenta imprimir colunas\n\n")

#tabela2.find("NATAN")
#print(tabela.index)
print('\n\n\n--------\n\n\n')





# # Abrindo um arquivo PDF existente
# with open("www.sc.gov.br_ipen_RelatorioIpen_004_2ReltorioPorSetorImprimir.asp_cd_Unidade=8088&de_Celas=4421,4420,4414,4415,4416,4417,4418,5399,4424,6504,4422,4423,5746,5571,6527&cd_Galeria=.pdf", "rb") as input_pdf:
#     # Criando um objeto PdfFileReader
#     pdf_reader = PdfFileReader(input_pdf)
#
#     # Obtendo o número de páginas do arquivo PDF
#     num_pages = pdf_reader.numPages
#
#     # Lendo o texto de cada página
#     for page_number in range(num_pages):
#         page = pdf_reader.getPage(page_number)
#         text = page.extractText()
#         print("Texto da página", page_number + 1, ":", text)

#
# from reportlab.pdfgen import canvas
#
# def GeneratePDF(lista):
#     try:
#         nome_pdf = input('Informe o nome do PDF: ')
#         pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
#         x = 720
#         for nome,idade in lista.items():
#             x -= 20
#             pdf.drawString(247,x, '{} : {}'.format(nome,idade))
#         pdf.setTitle(nome_pdf)
#         pdf.setFont("Helvetica-Oblique", 14)
#         pdf.drawString(245,750, 'Lista de Convidados')
#         pdf.setFont("Helvetica-Bold", 12)
#         pdf.drawString(245,724, 'Nome e idade')
#         pdf.save()
#         print('{}.pdf criado com sucesso!'.format(nome_pdf))
#     except:
#         print('Erro ao gerar {}.pdf'.format(nome_pdf))
#
# lista = {'Rafaela': '19', 'Jose': '15', 'Maria': '22','Eduardo':'24'}
#
#
#
# GeneratePDF(tabela2)
#
# import PyPDF2
# import spacy
#
# # Carregar o modelo em inglês do spaCy
# #nlp = spacy.load('en_core_web_sm')
# nlp = spacy.load('pt_core_news_sm')
# # Abrir o arquivo PDF
# with open(arquivo, 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     text = ''
#     for page in range(reader.numPages):
#         text += reader.getPage(page).extractText()
#
# # Processar o texto com o spaCy
# doc = nlp(text)
#
# # Identificar e imprimir as entidades nomeadas que são pessoas
# for entity in doc.ents:
#     if entity.label_ == 'PERSON':
#         print(entity.text)