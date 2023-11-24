#####	NOME:				pdf_to_print.py
#####	VERSÃO:				1.0
#####	DESCRIÇÃO:			Coleta informações de um arquivo em pdf e imprime em uma declaração
#####	DATA DA CRIAÇÃO:	24/11/2023
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	DISTRO:				Ubuntu GNU/Linux 22.04
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/casa-inteligente/pdf_to_print


#https://www.youtube.com/watch?v=8eNxZI-3Bxs

import IPython as display
import pandas
import tabula
from tabula.io import read_pdf

arquivo="teste.pdf"
paginas="all"


lista_tabela = tabula.io.read_pdf(arquivo,pages=paginas)


print(len(lista_tabela))

for tabela in lista_tabela:
    display(tabela)