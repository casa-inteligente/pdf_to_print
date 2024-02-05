#####	NOME:				report_teste.py
#####	VERSÃO:				1.0
#####	DESCRIÇÃO:			Coleta informações de um arquivo em pdf e imprime em uma declaração
#####	DATA DA CRIAÇÃO:	31/01/2024
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	DISTRO:				Ubuntu GNU/Linux 22.04
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/casa-inteligente/pdf_to_print
import dateutil.utils
import datetime as dd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib.units import cm


pdf_filename = "exemplo.pdf"
nome_interno = 'fulano'
numero_ipen = '123456'

page_size = A4
c = canvas.Canvas('imprimir/'+pdf_filename, pagesize=page_size)
c.setTitle("Termo de Recebimento")

### Cabeçalho
c.setFillColor(aColor='gray')  # Cor Cinza
c.setFont("Helvetica-Oblique", 10)
c.drawImage('logo.png', 50, 760, width=60, height=60)
c.drawString(120, 800, "ESTADO DE SANTA CATARINA")
c.drawString(120, 785, "SECRETARIA DE ESTADO DA ADMINISTRAÇÃO PRISIONAL E SOCIOEDUCATIVA")
c.drawString(120, 770, 'PRESÍDIO MARAVILHA')
################
#### Rodapé
#c.setFillColor(aColor='gray')  # Cor Cinza
c.setFillColorRGB(.7 ,.7, .7)
c.setFont("Helvetica-Oblique", 8)
c.drawCentredString(300,70, 'POLÍCIA PENAL DE SANTA CATARINA', mode=None, charSpace=0)
c.drawCentredString(300, 60, 'Presídio de Maravilha', mode=None, charSpace=0)
c.drawCentredString(300, 50, 'Av. Sul Brasil, n. 1607, centro - CEP 89874-000 - Maravilha/SC', mode=None, charSpace=0)
c.drawCentredString(300, 40, 'Fone: (49) 3664 - 6672 / e-mail: pr29@pp.sc.gov.br', mode=None, charSpace=0)

### Titulo do documento
c.setFillColor(aColor='black')  # Cor preto
c.setFont("Helvetica-Bold", 12) #Negrito
c.drawString(230, 730, 'TERMO DE RECEBIMENTO')
c.drawString(2*cm, 680, 'Instruções:')
c.setFont("Helvetica-Oblique", 12)
c.drawString(2*cm, 650, '01) Os internos devem assinalar a opção com um "X";')
c.drawString(2*cm, 630, '02) Na opção "Observação" descrever o que está sendo entregue (tamanho e quantidade')
c.drawString(2*cm, 610, 'de uniforme);')
c.drawString(2*cm, 590, '03) O termo de recebimento, devidamente assinado, deverá ser digitalizado e arquivado')
c.drawString(2*cm, 570, 'no IPEN do interno;')
c.rect(2*cm,10*cm,17*cm,9*cm, fill=0)# para criar retangulo

## tabela com informações
# c = SimpleDocTemplate(pdf_filename, pagesize=A4)
# data = [['Interno', nome_interno],
#         ['IPEN:', numero_ipen+'|'],
# ]
# table = Table(data)
# c.build([table])
## data do sistema no formato BR
hoje = dd.datetime.now()
hoje_br = hoje.strftime("%d/%m/%Y")
#print(hoje_br)
#Componente no nome
c.rect(2*cm, 19*cm,17*cm,.5*cm, fill=0)# para criar retangulo
c.drawString(2*cm, 19.1*cm,'  INTERNO:       '+nome_interno)
#Componente Ipem
c.rect(2*cm, 19*cm,17*cm,.5*cm, fill=0)# para criar retangulo
c.drawString(2*cm, 19.1*cm,'  INTERNO:       '+nome_interno)

## Componente recebido em
c.setFillColor(aColor='black')  # Cor preto
c.setFont("Helvetica-Bold", 12) #Negrito
c.drawString(2*cm, 250, 'Recebido em ______/______/__________.')

## Assinaura do interno
c.setFillColor(aColor='black')  # Cor preto
c.setFont("Helvetica-Bold", 12) #Negrito
c.drawString(2*cm, 170, '___________________________________')
c.drawString(2*cm, 155, 'Assinatura do interno.')


## Assinatura servidor
c.setFillColor(aColor='black')  # Cor preto
c.setFont("Helvetica-Bold", 12) #Negrito
c.drawString(2*cm, 110, '___________________________________')
c.drawString(2*cm, 95, 'Assinatura do servidor (nome completo).')


c.showPage()
c.save() # Salva o documento e fecha


