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
            #print(f'o caminho é: {caminho} \n Os arquivo excluidos serão: {arquivo}')
            #os.remove(os.path.join(caminho, arquivo))# Remove após a impressão
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
            #################################################################################################
            ### Cabeçalho
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.setFillColor(aColor='black')  # Cor preto
            #INICIO PRIMEIRO MEMORANDO
            #Componente Cabechalho
            c.setFont("Helvetica-Oblique", 11, leading=1)  # Fonte normal
            c.rotate(90)
            c.drawImage('figure/logo.png', 15 * cm, -3 * cm, width=2*cm, height=2*cm)
            c.drawString(17.5 * cm, -1.5 * cm, "ESTADO DE SANTA CATARINA")
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.drawString(17.5 * cm, -1.9 * cm, "SECRETARIA DE ESTADO DA ADIMINISTRAÇÃO PRISIONAL E SOCIOEDUCATIVA")
            c.drawString(17.5 * cm, -2.3 * cm, "PRESÍDIO DE MARAVILHA")
            c.rotate(270)


            ##Componente ESCRITA 
            c.rect(18 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(17 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(16 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(15 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(14 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(13 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(12 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(11 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(10 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(9 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(8 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(7 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            #c.rect(6 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            
            ##Componente assinatura e data
            c.rect(19.5 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo            
            c.rect(19.5 * cm, 15 * cm, 1 * cm, 3 * cm, fill=0)  # para criar retangulo
            c.rotate(90)
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.drawString(15 * cm, -19.3 * cm, 'APENADO')
            c.drawCentredString(15.5 * cm, -19.8 * cm, 'DATA')
            c.drawCentredString(19 * cm, -19.8 * cm, 'ASSINATURA')
            c.rotate(270)

            #Componente Nome e Matricula
            c.rect(4.8 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo "ao setor"
            c.rect(3.5 * cm, 15 * cm, 1 * cm, 11 * cm, fill=0)  # para criar retangulo "NOME"
            c.rect(3.5 * cm, 26 * cm, 1 * cm, 3.3 * cm) # para criar retangulo "Matricula"
            c.rect(2.5 * cm, 26 * cm, 1 * cm, 3.3 * cm, fill=0)  # para criar retangulo periiodo
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.rotate(90)
            c.drawString(15.5 * cm, -3.8 * cm, 'NOME')
            c.drawString(26.2 * cm, -3.8 * cm, 'MATRÍCULA')
            c.setFont("Helvetica-Oblique", 14, leading=1)  # Fonte normal
            c.drawCentredString(20 * cm, -4.3 * cm, f'{le_pdf.get_nome_interno()}')
            c.drawRightString(28.5 * cm, -4.3 * cm, f'{le_pdf.get_numero_ipen()}')
            c.drawCentredString(27.5 * cm, -3.3 * cm, 'abril')
            c.setFont("Helvetica-Oblique", 12, leading=1)  # Fonte normal
            c.drawRightString(25.8 * cm, -3.3 * cm, 'MEMORANDO DE APENADO')
            c.rotate(270)

            ## Componente ao setor
            #Componente setor
            c.rect(4.8 * cm, 15 * cm, 2 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            #c.rect(5.8 * cm, 15 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.rotate(90)
            c.drawString(15.8 * cm, -5.2 * cm, 'AO SETOR')
            c.setFont("Helvetica-Oblique", 12, leading=1)  # Fonte normal
            c.drawString(15.8 * cm, -5.6 * cm, '(  )PSICÓLOGA; (  )DIRETOR; (  )PECÚLIO; (  )EDUCAÇÃO;')
            c.drawString(15.7 * cm, -6.6 * cm, '(  )SOCIAL; (  )CHEFE DE SEGURANÇA e (  )OUTROS:__________')
            c.rotate(270)

            ############################################################################
            ##INICIO DO SEGUNDO MEMORANDO (PENAL)
            ##Componente cabechalho
            c.setFont("Helvetica-Oblique", 11, leading=1)  # Fonte normal
            c.rotate(90)
            c.drawImage('figure/logo.png', 0.2 * cm, -3 * cm, width=2*cm, height=2*cm)
            c.drawString(2.5 * cm, -1.5 * cm, "ESTADO DE SANTA CATARINA")
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.drawString(2.5 * cm, -1.9 * cm, "SECRETARIA DE ESTADO DA ADIMINISTRAÇÃO PRISIONAL E SOCIOEDUCATIVA")
            c.drawString(2.5 * cm, -2.3 * cm, "PRESÍDIO DE MARAVILHA")
            c.rotate(270)
            
            #Componente Nome e Matricula
            c.rect(3.5 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(3.5 * cm, 0.2 * cm, 1 * cm, 11 * cm, fill=0)  # para criar retangulo
            c.rect(2.5 * cm, 11.2 * cm, 1 * cm, 3.3 * cm, fill=0)  # para criar retangulo periiodo
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.rotate(90)
            c.drawString(0.8 * cm, -3.8 * cm, 'NOME')
            c.drawString(11.5 * cm, -3.8 * cm, 'MATRÍCULA')
            c.setFont("Helvetica-Oblique", 14, leading=1)  # Fonte normal
            c.drawCentredString(6 * cm, -4.3 * cm, f'{le_pdf.get_nome_interno()}')
            c.drawRightString(14.3 * cm, -4.3 * cm, f'{le_pdf.get_numero_ipen()}')
            c.drawCentredString(12.8 * cm, -3.3 * cm, 'abril')
            c.setFont("Helvetica-Oblique", 12, leading=1)  # Fonte normal
            c.drawRightString(11 * cm, -3.3 * cm, 'MEMORANDO DE APENADO')
            c.rotate(270)


            #Componente setor
            c.rect(4.8 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.rotate(90)
            c.drawString(0.8 * cm, -5.2 * cm, 'AO SETOR')
            c.setFont("Helvetica-Oblique", 14.3, leading=1)  # Fonte normal
            c.drawCentredString(7 * cm, -5.5 * cm, 'PENAL')
            c.rotate(270)

            ##Componente linhas para escrever o memorando
            #c.rect(6 * cm, 0.2 * cm, 13 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(18 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(17 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(16 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(15 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(14 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(13 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(12 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(11 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(10 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(9 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(8 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(7 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(6 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            
            
            #Componente de data e assinatura
            #c.rect(19.5 * cm, 0.5 * cm, 1 * cm, 14 * cm, fill=0)  # para criar retangulo
            c.rect(19.5 * cm, 0.2 * cm, 1 * cm, 14.3 * cm, fill=0)  # para criar retangulo
            c.rect(19.5 * cm, 0.2 * cm, 1 * cm, 3 * cm, fill=0)  # para criar retangulo
            c.rotate(90)
            c.setFont("Helvetica-Oblique", 8, leading=1)  # Fonte normal
            c.drawString(0.2 * cm, -19.3 * cm, 'APENADO')
            c.drawCentredString(.8 * cm, -19.8 * cm, 'DATA')
            c.drawCentredString(4.2 * cm, -19.8 * cm, 'ASSINATURA')
            c.rotate(270)
            ##FIM componente data e assinatura
            c.showPage()
            c.save()

        except OSError as e:
            print(f'Erro ao gerar o PDF, e erro é do tipo OSError\t{e}')            

        except NameError as f:
            print(f'Erro ao gerar o PDF, e erro é do tipo NameError\t{f}')
        except TypeError as t:
            print(f'Erro ao gerar o PDF, e erro é do tipo TypeError\t{t}')
        except:
            #print(f'Erro ao gerar o Termo de Kit de higiene {self.pdf_filename}')
            print('Erro ao gerar o PDF, Tipo de Erro\t', sys.exc_info()[0])
    
class Le_pdf:

    def get_nome_interno(self):
        #print(self._nome_interno)
        return self._nome_interno
    def get_numero_ipen(self):
        return self._numero_ipen
    def get_dir_saida(self):
         self._diretorio_saida = Path(r'\\10.40.22.35/Plantão/Para Impressão do termo de recebimento/Imprimir/')# define o diretorio a ser gravado os arq pdf
         self._diretorio_saida.mkdir(mode=777, parents=True, exist_ok=True) # Cria o diretorio caso não exista (Local inapropriado pois cria n vezes)
         return self._diretorio_saida
    

    def abre_pdf(self, paginas='all'):
        try:
            #self._diretorio_entrada = Path(r"\\10.40.22.35/Plantão/Para Impressão do termo de recebimento/")

            #for arquivo in self._diretorio_entrada.glob('*.pdf'):#Arquivo .pdf a ser analisado
                #print(arquivo)

            root.withdraw()
            self._arquivo = filedialog.askopenfilename() # escolhe o arquivo
            #print('=================')
            #print(self._arquivo)
            #print('==================')

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
            self._frist_colu = self._frist_colu.reset_index(drop=True)
            self._frist_colu = self._frist_colu.drop([0, 1, 2])
            self._frist_colu = self._frist_colu.reset_index(drop=True)
            
            #print(self._frist_colu)
            self._crit_stop = len(self._frist_colu)
            #print(f'O criterio de parada é:  {self._crit_stop}')
            #print('Irá gerar 138 Memorandos')
            #Gera os termos
            #implementar solicitação do mês referencia

            for x in range(self._crit_stop):
                self._numero_ipen, self._nome_interno = self._frist_colu[x].split('-',1)
                self._nome_interno = self._nome_interno.replace('\n', ' ') #Remove o \n
                #print(f"Numero: {self._numero_ipen}, Nome: {self._nome_interno}")
                template.GeneratePDF()
                print(f'Esta no número {x+1} de {self._crit_stop}, no memorando do: {le_pdf.get_nome_interno()}')
                
           
          
        except AttributeError as e:
            print(f'O erro é {e}')
        
        except :
            print('Erro ao extrair dados da tabela ', sys.exc_info()[0])
            

        
        #finally: 
            #print("Programa encerrado devido a erros")

#Inicio do "main"
#print(sys.executable) #Imprimi o local do interpretador

template = Template() #Instância a classe Template
le_pdf = Le_pdf()
root = tk.Tk()

tabelas_lida = le_pdf.abre_pdf()
le_pdf.extrai_tabela(tabelas_lida)


#template.Imprimi_nova()#Para impressão dos memorandos
