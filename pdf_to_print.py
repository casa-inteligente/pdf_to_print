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

import IPython as display
import pandas
import tabula
from tabula.io import read_pdf

#arquivo='teste.pdf'
#arquivo='FECHADO.pdf'
arquivo='www.sc.gov.br_ipen_RelatorioIpen_004_2ReltorioPorSetorImprimir.asp_cd_Unidade=8088&de_Celas=4421,4420,4414,4415,4416,4417,4418,5399,4424,6504,4422,4423,5746,5571,6527&cd_Galeria=.pdf'
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
#print(tabela.index)
print('\n\n\n--------\n\n\n')