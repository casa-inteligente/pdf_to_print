from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Crie um arquivo PDF em branco
c = canvas.Canvas("exemplo.pdf", pagesize=letter)
c.setFont("Helvetica", 11)
# Defina o título do documento
c.setTitle("Termo de kit de higienes")

# Adicione texto ao PDF
c.drawString(100, 750, "Olá, Mundo!")

# Salve o arquivo PDF
c.showPage()
c.save()
print("PDF criado com sucesso.")