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
c.drawImage('logo.png', 60, 700, width=60, height=60)
c.drawString(130, 745, "ESTADO DE SANTA CATARINA")
c.drawString(130, 730, "SECRETARIA DE ESTADO DA ADMINISTRAÇÃO PRISIONAL E SOCIOEDUCATIVA")
c.drawString(130,715, 'PRESÍDIO MARAVILHA')
################
#### Rodapé
c.setFont("Helvetica-Oblique", 8)
c.drawString(247, 80, 'POLÍCIA PENAL DE SANTA CATARINA')
c.drawString(247, 70, 'Presídio de Maravilha')
c.drawString(247, 60, 'Av. Sul Brasil, n. 1607, centro - CEP 89874-000 - Maravilha/SC')
c.drawString(247, 50, 'Fone: (49) 3664 - 6672 / e-mail: pr29@pp.sc.gov.br')

c.save() # Salva o documento e fecha


