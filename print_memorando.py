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
        self._lista_impressora = win32print.EnumPrinters(2) #Lista impressoras conectadas ao computador
        for impressora in self._lista_impressora:
            print("lsita")

#print(sys.executable) #Imprimi o local do interpretador

template = Template() #Instancia a classe Template

template.Imprimi_nova()