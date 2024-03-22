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
import pandas as pd
import pdfplumber
import tkinter as tk
from tkinter import filedialog

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
            pass
            #print("Remover este e habilitar a linha abaixo para imprimir")
            #win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)
    ### FIM ### def Imprimi_nova(self):
            
    def GeneratePDF(self):
        try:
            pass
                    

        except:
            print(f'Erro ao gerar o Termo de Kit de higiene {self.pdf_filename}')
    
class Le_pdf:

    def get_nome_interno(self):
        #print(self._nome_interno)
        return self._nome_interno
    def get_numero_ipen(self):
        return self._numero_ipen
    def get_dir_saida(self):
        return self._diretorio_saida
    def get_dir_arq(self):
        return self._arquivo

    def abre_pdf(self, paginas='all'):
        try:
            #self._diretorio_entrada = Path(r"\\10.40.22.35/Plantão/Para Impressão do termo de recebimento/")

            #for arquivo in self._diretorio_entrada.glob('*.pdf'):#Arquivo .pdf a ser analisado
                #print(arquivo)

            root.withdraw()
            self._arquivo = filedialog.askopenfilename() # escolhe o arquivo
            print('=================')
            print(self._arquivo)
            print('==================')

            with pdfplumber.open(self._arquivo) as pdf:
                 
                 self._all_tables = []

                 for pagina in pdf.pages:
                    self._tables = pagina.extract_tables()

                    for table in self._tables:
                        self._all_tables.append(table)
            
                 #print (self._all_tables)
            return self._all_tables

        except:
            print('Erro ao abrir o arquivo {}'.format(self._arquivo))


    def extrai_tabela(self, tabela):
        
        try:
            df  = pd.concat([pd.DataFrame(tabela) for tabela in self._all_tables])
            self._frist_colu = df.iloc[:,0]
            print(self._frist_colu)

          

        except :
            print('Erro ao extrair dados da tabela ', sys.exc_info()[0])
            return None

        
        #finally: 
            #print("Programa encerrado devido a erros")

#Inicio do "main"
#print(sys.executable) #Imprimi o local do interpretador

template = Template() #Instância a classe Template
le_pdf = Le_pdf()
root = tk.Tk()

tabelas_lida = le_pdf.abre_pdf()
le_pdf.extrai_tabela(tabelas_lida)

#var_vezes = len(tabelas_lida) - 1 #Remove o cabechalho 


#for x in range(var_vezes): #Intera sobre todas as tabelas
#for x in range(1):
    #print(tabelas_lida[x+1])
    #dados_impri = le_pdf.extrai_tabela(tabelas_lida[x+1])

#template.Imprimi_nova()
    
    #PDFPlumber

    # converter a tabela em txt ou csv