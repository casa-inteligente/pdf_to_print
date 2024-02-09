# -*- coding: utf-8 -*-
#####	NOME:				nao_sei-de-nada.py
#####	VERSÃO:				1.0
#####	DESCRIÇÃO:			Coleta informações de um arquivo em pdf e imprime em uma declaração
#####	DATA DA CRIAÇÃO:	31/01/2024
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	DISTRO:				Ubuntu GNU/Linux 22.04
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/casa-inteligente/pdf_to_print


import datetime as dd
from reportlab.lib.pagesizes import A4
import tabula
from tabula.io import read_pdf
import pandas

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm