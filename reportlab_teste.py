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

nome_interno = 'fulano'
pdf_filename = nome_interno+".pdf"

numero_ipen = '123456'

page_size = A4
c = canvas.Canvas('imprimir/'+pdf_filename, pagesize=page_size)
c.setTitle("Termo de Recebimento")
c.setAuthor("Natan Ogliari")

### Cabeçalho
c.setFillColor(aColor='gray')  # Cor Cinza
c.setFont("Helvetica-Oblique", 10)
c.drawImage('logo.png', 2*cm, 760, width=60, height=60)
c.drawString(4.5*cm, 800, "ESTADO DE SANTA CATARINA")
c.drawString(4.5*cm, 785, "SECRETARIA DE ESTADO DA ADMINISTRAÇÃO PRISIONAL E SOCIOEDUCATIVA")
c.drawString(4.5*cm, 770, 'PRESÍDIO MARAVILHA')
################
#### Rodapé
#c.setFillColor(aColor='gray')  # Cor Cinza
c.setFillColor(aColor='gray', alpha=1)
#c.setFillColorRGB(.662 ,.662, .662, 1)
c.setFont("Helvetica-Oblique", 8)
c.drawCentredString(300, 70, 'POLÍCIA PENAL DE SANTA CATARINA', mode=None, charSpace=0)
c.drawCentredString(300, 60, 'Presídio de Maravilha', mode=None, charSpace=0)
c.drawCentredString(300, 50, 'Av. Sul Brasil, n. 1607, centro - CEP 89874-000 - Maravilha/SC', mode=None, charSpace=0)
c.drawCentredString(300, 40, 'Fone: (49) 3664 - 6672 / e-mail: pr29@pp.sc.gov.br', mode=None, charSpace=0)

### Titulo do documento
c.setFillColor(aColor='black')  # Cor preto
c.setFont("Helvetica-Bold", 12) #Negrito
c.drawString(230, 730, 'TERMO DE RECEBIMENTO')
c.drawString(2*cm, 680, 'Instruções:')
c.setFont("Helvetica-Oblique", 12) #Fonte normal
c.drawString(2*cm, 650, '01) Os internos devem assinalar a opção com um "X";')
c.drawString(2*cm, 630, '02) Na opção "Observação" descrever o que está sendo entregue (tamanho e quantidade')
c.drawString(2*cm, 610, 'de uniforme);')
c.drawString(2*cm, 590, '03) O termo de recebimento, devidamente assinado, deverá ser digitalizado e arquivado')
c.drawString(2*cm, 570, 'no IPEN do interno;')
c.rect(2*cm, 10*cm, 17*cm, 9*cm, fill=0)# para criar retangulo


## data do sistema no formato BR
hoje = dd.datetime.now()
hoje_br = hoje.strftime("%d/%m/%Y")
#print(hoje_br)
#Componente no nome
c.rect(2*cm, 19*cm, 17*cm, .5*cm, fill=0)# para criar retangulo
c.drawString(2*cm, 19.1*cm,'  INTERNO:       '+nome_interno)
#Componente Ipem
c.rect(2*cm, 18.5*cm, 8.5*cm,.5*cm, fill=0)# para criar retangulo
c.drawString(2*cm, 18.6*cm,'  IPEN:       '+numero_ipen)
#Componente data
c.rect(10.5*cm, 18.5*cm, 8.5*cm, .5*cm, fill=0)# para criar retangulo
c.drawString(10.5*cm, 18.6*cm, '  DATA:       '+hoje_br)
## Componentes das informaçõe das coisas entregues
## Componente do kit higiene
c.rect(2*cm, 18*cm, 4*cm, .5*cm, fill=0)# para criar retangulo
c.rect(6*cm, 18*cm, 13*cm, .5*cm, fill=0)# para criar retangulo
c.drawString(6*cm, 18.1*cm, ' Kit higiene')
## Componente Uniforme
c.rect(2*cm, 17.5*cm, 4*cm, .5*cm, fill=0)# para criar retangulo
c.rect(6*cm, 17.5*cm, 13*cm, .5*cm, fill=0)# para criar retangulo
c.drawString(6*cm, 17.6*cm,' Uniforme')
#Componente cobertor
c.rect(2*cm, 17*cm,4*cm,.5*cm, fill=0)# para criar retangulo
c.rect(6*cm, 17*cm,13*cm,.5*cm, fill=0)# para criar retangulo
c.drawString(6*cm, 17.1*cm,' Cobertor')

#Componente Observação
c.setFillColor(aColor='black')  # Cor preto
c.setFont("Helvetica-Bold", 12) #Negrito
c.rect(2*cm, 16.5*cm, 4*cm, .5*cm, fill=0)# para criar retangulo
c.drawString(2*cm, 16.6*cm,'    Observação:')
c.rect(6*cm, 16.5*cm, 13*cm, .5*cm, fill=0)# para criar retangulo

c.setFont("Helvetica-Oblique", 12)


## Componente recebido em
c.setFillColor(aColor='black')  # Cor preto
c.setFont("Helvetica-Bold", 12) #Negrito
c.drawString(2*cm, 220, 'Recebido em ______/______/__________.')

## Assinaura do interno
c.setFillColor(aColor='black')  # Cor preto
c.setFont("Helvetica-Bold", 12) #Negrito
c.drawString(2*cm, 170, '___________________________________')
c.drawString(2*cm, 155, 'Assinatura do interno.')


## Assinatura do servidor
c.setFillColor(aColor='black')  # Cor preto
c.setFont("Helvetica-Bold", 12) #Negrito
c.drawString(2*cm, 110, '___________________________________')
c.drawString(2*cm, 95, 'Assinatura do servidor (nome completo).')


c.showPage()
c.save() # Salva o documento e fecha
