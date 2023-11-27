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

arquivo='teste.pdf'
arquivo='FECHADO.pdf'
paginas='all'


lista_tabela = tabula.io.read_pdf(arquivo,pages=paginas)


print(len(lista_tabela))

#print (lista_tabela)

#imprimi na tela os valores

for tabela in lista_tabela:
    print(tabela)
    #print(tabela.find('RECOLHIDO(A)'))

len(lista_tabela)
print('------------------------------------------------------------------------')
#removendo as coluna de situação
tabela_limpa = tabela.drop(3, axis=0)
print('\nimprime a tabela limpa, que não esta limpa ainda..... \n')
print(tabela_limpa)
