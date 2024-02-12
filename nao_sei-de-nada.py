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
from pdf2image import convert_from_path
import cv3
import numpy as np
import pytesseract

pdf_file = 'ESTE.pdf'
pages = convert_from_path(pdf_file)

def deskew (image):
    gray = cv3.cvtColor(image, cv3.COLORS_BGR2GRAY)
    gray = cv3.bitwise_not(gray)
    coords = np.column_stack(np.where(gray > 0))
    angle = cv3.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = - angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv3.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv3.warpAffine(image, M, (w, h), flags=cv3.INTER_CUBIC, borderMode=cv3.BORDER_REPLICATE)

    return rotated


def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

extracted_text = []

for page in pages:
    # Step 2: Preprocess the image (deskew)
    preprocessed_image = deskew(np.array(page))

    # Step 3: Extract text using OCR
    text = extract_text_from_image(preprocessed_image)
    extracted_text.append(text)