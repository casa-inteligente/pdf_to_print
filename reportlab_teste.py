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
name_interno = 'fulano'
number_ipen = 123456

c = canvas.Canvas(pdf_filename, pagesize=A4)
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
c.setFillColor(aColor='gray')  # Cor Cinza
c.setFont("Helvetica-Oblique", 8)
c.drawString(247, 70, 'POLÍCIA PENAL DE SANTA CATARINA')
c.drawString(247, 60, 'Presídio de Maravilha')
c.drawString(247, 50, 'Av. Sul Brasil, n. 1607, centro - CEP 89874-000 - Maravilha/SC')
c.drawString(247, 40, 'Fone: (49) 3664 - 6672 / e-mail: pr29@pp.sc.gov.br')

### Titulo do documento
c.setFillColor(aColor='black')  # Cor preto
c.setFont("Helvetica-Bold", 12) #Negrito
c.drawString(230, 730, 'TERMO DE RECEBIMENTO')
c.drawString(60, 700, 'Instruções:')
c.setFont("Helvetica-Oblique", 12)
c.drawString(60, 680, '01) Os internos devem assinalar a opção com um X;')
c.drawString(60, 660, '02) Na opção "Observação" descrever o que está sendo entregue (tamanho e quantidade')
c.drawString(60, 640, 'de uniforme);')
c.drawString(60, 620, '03) O termo de recebimento, devidamente assinado, deverá ser digitalizado e arquivado')
c.drawString(60, 600, 'no IPEN do interno;')


## tabela com informações
# c = SimpleDocTemplate(pdf_filename, pagesize=A4)
# data = [['nome', 'uih', 'ohihj'],
#         ['nome', 'uih', 'ohihj'],
# ]
# table = Table(data)
# c.build([table])

hoje = dd.datetime.now()
hoje_br = hoje.strftime("%d/%m/%Y")
#print(hoje_br)
c.drawString(100, 450, hoje_br)


c.showPage()
c.save() # Salva o documento e fecha


