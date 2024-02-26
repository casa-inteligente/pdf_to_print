# -*- coding: utf-8 -*-
#####	NOME:				print_memorando.py
#####	VERSÃO:				1.0.1
#####	DESCRIÇÃO:			Coleta informações de um arquivo em pdf e imprime memorando com nome e identificadores.
#####	DATA DA CRIAÇÃO:	26/02/2024
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	DISTRO:				Ubuntu GNU/Linux 22.04
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/casa-inteligente/pdf_to_print

import win32api
import win32print
import datetime as dd
import os
from reportlab.lib.pagesizes import A4
import tabula
from tabula.io import read_pdf
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import sys

class Template:
    def Imprimi_nova(self):
        lista_impressora = win32print.EnumPrinters(2)# Lista de impressoras no PC
        #for impressora in lista_impressora:
            #print(f'Lista a impressora {impressora}')#indice 0 da impressora
        myImpressora = lista_impressora[0]
       
        ### Adicionado para pagar a bandeja manual
        handle = win32print.OpenPrinter(myImpressora[2])
        
        
        #property = win32print.GetPrinter(handle, 2) #Usualmente '2' é a bandeja manual
        #property['pDevMode'].__dict__['BinSelection'] = 2
        #print(property['pDevMode'])
        #property['pDevMode'].BinSelection = 2

        #win32print.SetPrinter(handle, 2, property, 0)
        #win32print.ClosePrinter(handle) #Fecha a configuração
        ### Fim da bandeja manual


        win32print.SetDefaultPrinter(myImpressora[2])

        #seta a pasta e impressão
        caminho = r"\\10.40.22.35\Plantão\Para Impressão do termo de recebimento\Imprimir"
        #print(caminho)
        lista_arq_print = os.listdir(caminho)
        for arquivo in lista_arq_print:
            print("Remover este a habilitar a linha abaixo para imprimir")
            #win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)
    ### FIM ### def Imprimi_nova(self):
            
    def GeneratePDF(self, dados):
        try:
            pass
        except:
            print(f'Erro ao gerar o memorando {nome_interno}.pdf')
class Le_pdf:

    def abre_pdf(self, paginas='all'):
        try:
            self._diretorio_entrada = Path(r"\\10.40.22.35/Plantão/Para Impressão do termo de recebimento/")

            for arquivo in self._diretorio_entrada.glob('*.pdf'):
                print(arquivo)

            self._lista_tabela = tabula.io.read_pdf(arquivo, pages=paginas)
            self.numero_de_tabelas = len(self._lista_tabela)
            print('Possui {} tabelas para uso e um cabechalho' .format(self.numero_de_tabelas-1))
            return self._lista_tabela

        except:
            print('Erro ao abrir o arquivo {}'.format(arquivo))


    def extrai_tabela(self, lista_tabela):
        try:
            lista_tabela['PRONTUÁRIO | NOME'].str.split(' - ', expand=True)

            print(lista_tabela)
        except:
            print(f'Erro ao extrair daods da tabela {lista_tabela}')

#print(sys.executable) #Imprimi o local do interpretador

template = Template() #Instancia a classe Template
le_pdf = Le_pdf()

tabelas_lida = le_pdf.abre_pdf()
var_vezes = len(tabelas_lida) - 1 #Remove o cabechalho 
for x in range(var_vezes):
    #print(tabelas_lida[x+1])
    dados_impri = le_pdf.extrai_tabela(tabelas_lida[x+1])


template.Imprimi_nova()