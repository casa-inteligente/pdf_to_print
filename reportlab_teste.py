#####	NOME:				report_teste.py
#####	VERSÃO:				1.0
#####	DESCRIÇÃO:			Coleta informações de um arquivo em pdf e imprime em uma declaração
#####	DATA DA CRIAÇÃO:	31/01/2024
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	DISTRO:				Ubuntu GNU/Linux 22.04
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/casa-inteligente/pdf_to_print

from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib.units import cm


pdf_filename = "exemplo.pdf"

c = canvas.Canvas("documento_com_imagem.pdf", pagesize=A4)

c.setTitle("Termo de kit de axdva")

### Cabeçalho
c.setFont("Helvetica-Oblique", 10)
c.drawImage('logo.png', 50, 760, width=60, height=60)
c.drawString(120, 800, "ESTADO DE SANTA CATARINA")
c.drawString(120, 785, "SECRETARIA DE ESTADO DA ADMINISTRAÇÃO PRISIONAL E SOCIOEDUCATIVA")
c.drawString(120, 770, 'PRESÍDIO MARAVILHA')
################
#### Rodapé
c.setFont("Helvetica-Oblique", 8)
c.drawString(247, 70, 'POLÍCIA PENAL DE SANTA CATARINA')
c.drawString(247, 60, 'Presídio de Maravilha')
c.drawString(247, 50, 'Av. Sul Brasil, n. 1607, centro - CEP 89874-000 - Maravilha/SC')
c.drawString(247, 40, 'Fone: (49) 3664 - 6672 / e-mail: pr29@pp.sc.gov.br')

### Titulo do documento
c.setFont("Helvetica-Oblique", 12)
c.drawString(230, 730, 'TERMO DE RECEBIMENTO')
c.drawString(60, 710, 'Instruções:')
c.drawString(60, 600, '01) Os internos devem assinalar a opção com um X;')
c.drawString(60, 580, '02) Na opção "Observação" descrever o que está sendo entregue (tamanho e ')
c.drawString(60, 560, 'quantidade de uniforme);')
c.drawString(60, 540, '03) O termo de recebimento, devidamente assinado, deverá ser digitalizado')
c.drawString(60, 520, 'e arquivado no IPEN do interno;')



c.save() # Salva o documento e fecha


