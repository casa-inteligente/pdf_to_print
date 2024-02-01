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

# BaseDocTemplate(self, pdf_filename,
#  pagesize=defaultPageSize,
#  pageTemplates=[],
#  showBoundary=0,
#  leftMargin=cm,
#  rightMargin=cm,
#  topMargin=cm,
#  bottomMargin=cm,
#  allowSplitting=1,
#  title=None,
#  author='Natan Ogliari',
#  _pageBreakQuick=1,
#  encrypt=None)





# Crie um arquivo PDF em branco
pdf_filename = "exemplo.pdf"
mydoc = canvas.Canvas(pdf_filename, pagesize=letter)
mydoc.setFont("Times-Roman", 11)
# Defina o título do documento
mydoc.setTitle("Termo de kit de axdva")

# Adicione texto ao PDF
mydoc.drawString(100, 750, "Olá, Mundo!")

# Salve o arquivo PDF
mydoc.showPage()
mydoc.save()
print("PDF criado com sucesso.")


data = [['Nome', 'jhj', 'Idade'],
        ['João','','25'],
        ['Maria', '','30']]


mydoc = SimpleDocTemplate(pdf_filename, pagesize=letter)
table = Table(data)

# Estilo da tabela
style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0.2, 0.4, 0.6)),  # Cor de fundo para cabeçalho
                    ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),  # Cor do texto no cabeçalho
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinhamento central
                    ('FONTNAME', (0, 0), (-1, 0), 'Times-BoldItalic')])  # Fonte negrito para cabeçalho



table.setStyle(style)
mydoc.build([table])





c = canvas.Canvas("documento_com_imagem.pdf", pagesize=letter)

### Cabeçalho
c.setFont("Helvetica-Oblique", 10)
c.drawImage('logo.png', 60, 700, width=60, height=60)

c.drawString(130, 745, "ESTADO DE SANTA CATARINA")
c.drawString(130, 730, "SECRETARIA DE ESTADO DA ADMINISTRAÇÃO PRISIONAL E SOCIOEDUCATIVA")
c.drawString(130,715, 'PRESÍDIO MARAVILHA')
################
#### Rodapé
c.setFont("Helvetica-Oblique", 8)
c.drawString(250,80, 'POLÍCIA PENAL DE SANTA CATARINA')
c.drawString(250,70, 'Presídio de Maravilha')
c.drawString(250,60, 'Av. Sul Brasil, n. 1607, centro - CEP 89874-000 - Maravilha/SC')
c.drawString(250,50, 'Fone: (49) 3664 - 6672 / e-mail: pr29@pp.sc.gov.br')


c.save() # Salva o documento e fecha


