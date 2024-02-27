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
            
    def GeneratePDF(self):
        try:
            self._page_size = A4 # Define o tamenho da folha
            self.pdf_filename = le_pdf.get_nome_interno() + ".pdf"
            self.nome_arq_out = f'{le_pdf.get_dir_saida()}\{self.pdf_filename}'
            #print(self.nome_arq_out)
            c = canvas.Canvas(self.nome_arq_out, pagesize=self._page_size)
            c.setTitle("Momorando de apenado")
            c.setAuthor("Natan Ogliari")

            ##
            ### Cabeçalho
            c.setFillColor(aColor='black', alpha=.8)  # Cor Cinza
            c.setFont("Helvetica-Oblique", 10)
            c.drawImage('figure/logo.png', 2 * cm, 750, width=60, height=60) #Logo do estado
            c.drawString(4.5 * cm, 800, "ESTADO DE SANTA CATARINA")
            c.drawString(4.5 * cm, 785, "SECRETARIA DE ESTADO DA ADMINISTRAÇÃO PRISIONAL E SOCIOEDUCATIVA")
            c.drawString(4.5 * cm, 770, 'PRESÍDIO MARAVILHA')
            c.drawString(4.5 * cm, 755, 'Setor - Coordenação Penal')
            ################ 

            ### Titulo do documento
            c.setFillColor(aColor='black')  # Cor preto
            c.setFont("Helvetica-Oblique", 12, leading=1)
            c.drawCentredString(10.5 * cm, 730, 'TERMO DE RECEBIMENTO')
            
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.rect(5.5 * cm, 0.5 * cm, 13 * cm, 14 * cm, fill=0)  # para criar retangulo
            
            #Componente Nome
            c.rect(2.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.rotate(90)
            c.drawString(0.8 * cm, -2.8 * cm, 'NOME')
            c.setFont("Helvetica-Oblique", 18, leading=1)  # Fonte normal
            c.drawCentredString(7 * cm, -3.2 * cm, f'{le_pdf.get_nome_interno()}')
            c.rotate(270)


            #Componente setor
            c.rect(4 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.rotate(90)
            c.drawString(0.8 * cm, -4.3 * cm, 'AO SETOR')
            c.setFont("Helvetica-Oblique", 18, leading=1)  # Fonte normal
            c.drawCentredString(7 * cm, -4.8 * cm, 'PENAL')
            c.rotate(270)
            ##Componente linhas para escrever o memorando
            
            c.rect(19 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(17.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(16.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(15.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(14.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(13.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(12.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(11.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(10.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(9.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(8.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(7.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(6.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            
            
            #Componente de data e assinatura
            c.rect(19 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(19 * cm, 0.5 * cm, 1 * cm, 3 * cm, fill=0)  # para criar retangulo
            c.rotate(90)
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.drawString(0.5 * cm, -18.8 * cm, 'APENADO')
            c.drawCentredString(1.1 * cm, -19.3 * cm, 'DATA')
            c.drawCentredString(4.5 * cm, -19.3 * cm, 'ASSINATURA')
            c.rotate(270)
            ##FIM componente data e assinatura
            c.showPage()
            c.save()
                    

        except:
            print(f'Erro ao gerar o memorando {self.pdf_filename}.pdf', sys.exc_info()[0])
    
class Le_pdf:

    def get_nome_interno(self):
        #print(self._nome_interno)
        return self._nome_interno
    def get_numero_ipen(self):
        return self._numero_ipen
    def get_dir_saida(self):
        return self._diretorio_saida

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


    def extrai_tabela(self, tabela):
        
        try:
            
            
            tabela = tabela['PRONTUÁRIO | NOME'].str.split(' - ', expand=True) #Cria duas colunas 
            tabela = tabela.rename(columns={0: 'IPEN'})#Altera o nome da coluna
            tabela = tabela.rename(columns={1: 'Nomes'})#Altera o nome da coluna
            tabela['Nomes'] = tabela['Nomes'].replace(to_replace=r'\r', value=' ', regex=True)#remove o \r
            #tabela = tabela.dropna()
            self._crit_stop = tabela.index.stop # Criterio de parada do for
            print(f'O numero de linhas da tabela é {self._crit_stop}')
            
            self._diretorio_saida = Path(r'\\10.40.22.35/Plantão/Para Impressão do termo de recebimento/Imprimir/')# define o diretorio a ser gravado os arq pdf
            self._diretorio_saida.mkdir(mode=777, parents=True, exist_ok=True) # Cria o diretorio caso não exista (Local inapropriado pois cria n vezes)
            
            #for x in range(self._crit_stop): #Intera sobre todas as linha
            for x in range(1):
                #print(f"Nomes do interno: {tabela['Nomes'][x]}")
                #print(f"Numero do prontuario: {tabela['IPEN'][x]}")
                self._nome_interno = tabela['Nomes'][x]
                self._numero_ipen = tabela['IPEN'][x]
                template.GeneratePDF()
                                
            
        except :
            print('Erro ao extrair dados da tabela ', sys.exc_info()[0])
        
        #finally: 
            #print("Programa encerrado devido a erros")

#Inicio do "main"
#print(sys.executable) #Imprimi o local do interpretador

template = Template() #Instância a classe Template
le_pdf = Le_pdf()

tabelas_lida = le_pdf.abre_pdf()


var_vezes = len(tabelas_lida) - 1 #Remove o cabechalho 

for x in range(var_vezes): #Intera sobre todas as tabelas
#for x in range(1):
    #print(tabelas_lida[x+1])
    dados_impri = le_pdf.extrai_tabela(tabelas_lida[x+1])


template.Imprimi_nova()