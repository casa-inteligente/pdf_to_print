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
        for impressora in lista_impressora:
            print(f'Lista a impressora {impressora}')#indice 0 da impressora
        myImpressora = lista_impressora[0]
        print(type(myImpressora))
        print(myImpressora[2])
        ### Adicionado para pagar a bandeja manual
        handle = win32print.OpenPrinter(myImpressora[2])
        print(type(handle)
        
        #properties = win32print.GetPrinter(handle, 2) #Usualmente '2' é a bandeja manual
        #properties['pDevMode'].__dict__['BinSelection'] = 2
       
        #properties['pDevMode'].BinSelection = 2

        #win32print.SetPrinter(handle, 2, properties, 0)

        win32print.ClosePrinter(handle) #Fecha a configuração
        ### Fim da bandeja manual
        win32print.SetDefaultPrinter(myImpressora[2])

        #seta a pasta e impressão
        caminho = r"\\10.40.22.35\Plantão\Para Impressão do termo de recebimento\Imprimir"
        #print(caminho)
        lista_arq_print = os.listdir(caminho)
        for arquivo in lista_arq_print:
            print("d")
            #win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)
    ### FIM ### def Imprimi_nova(self):

#print(sys.executable) #Imprimi o local do interpretador

template = Template() #Instancia a classe Template

template.Imprimi_nova()