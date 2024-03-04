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
            pass
            #print("Remover este e habilitar a linha abaixo para imprimir")
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
            #################################################################################################
            ### Cabeçalho
            c.setFillColor(aColor='black', alpha=.8)  # Cor Cinza
            c.setFont("Helvetica-Oblique", 10)
            c.drawImage('figure/logo.png', 2 * cm, 760, width=60, height=60) #Logo do estado
            c.drawString(4.5 * cm, 800, "ESTADO DE SANTA CATARINA")
            c.drawString(4.5 * cm, 785, "SECRETARIA DE ESTADO DA ADMINISTRAÇÃO PRISIONAL E SOCIOEDUCATIVA")
            c.drawString(4.5 * cm, 770, 'PRESÍDIO MARAVILHA')
            ################
            #### Rodapé
            # c.setFillColor(aColor='gray')  # Cor Cinza
            c.setFillColor(aColor='black', alpha=.8)
            # c.setFillColorRGB(.662 ,.662, .662, 1)
            c.setFont("Helvetica-Oblique", 8)
            c.drawCentredString(300, 70, 'POLÍCIA PENAL DE SANTA CATARINA', mode=None, charSpace=0)
            c.drawCentredString(300, 60, 'Presídio de Maravilha', mode=None, charSpace=0)
            c.drawCentredString(300, 50, 'Av. Sul Brasil, n. 1607, centro - CEP 89874-000 - Maravilha/SC', mode=None, charSpace=0)
            c.drawCentredString(300, 40, 'Fone: (49) 3664 - 6672 / e-mail: pr29@pp.sc.gov.br', mode=None, charSpace=0)

            ### Titulo do documento
            c.setFillColor(aColor='black')  # Cor preto
            c.setFont("Helvetica-Bold", 12)  # Negrito
            c.drawCentredString(10.5 * cm, 730, 'TERMO DE RECEBIMENTO')
            c.drawString(2 * cm, 680, 'Instruções:')
            c.setFont("Helvetica-Oblique", 12, leading=1)  # Fonte normal
            c.drawString(2 * cm, 650, '01) Os internos devem assinalar a opção com um "X";')
            c.drawString(2 * cm, 630, '02) Na opção "Observação" descrever o que está sendo entregue (tamanho e quantidade')
            c.drawString(2 * cm, 610, 'de uniforme);')
            c.drawString(2 * cm, 590, '03) O termo de recebimento, devidamente assinado, deverá ser digitalizado e arquivado')
            c.drawString(2 * cm, 570, 'no IPEN do interno;')
            c.rect(2 * cm, 10 * cm, 17 * cm, 9 * cm, fill=0)  # para criar retangulo

            ## data do sistema no formato BR
            hoje = dd.datetime.now()
            hoje_br = hoje.strftime("%d/%m/%Y")
            # print(hoje_br)
            # Componente no nome
            c.rect(2 * cm, 19 * cm, 17 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.drawString(2 * cm, 19.1 * cm, f'  INTERNO: {le_pdf.get_nome_interno()}')
            # Componente Ipem
            c.rect(2 * cm, 18.5 * cm, 8.5 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.drawString(2 * cm, 18.6 * cm, f'  IPEN:      {le_pdf.get_numero_ipen()}')
            # Componente data
            c.rect(10.5 * cm, 18.5 * cm, 8.5 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.drawString(10.5 * cm, 18.6 * cm, f'    DATA:  {hoje_br}')
            ## Componentes das informaçõe das coisas entregues
            ## Componente do kit higiene
            c.rect(2 * cm, 18 * cm, 4 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.rect(6 * cm, 18 * cm, 13 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.drawString(6 * cm, 18.1 * cm, ' Kit higiene')
            ## Componente Uniforme
            c.rect(2 * cm, 17.5 * cm, 4 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.rect(6 * cm, 17.5 * cm, 13 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.drawString(6 * cm, 17.6 * cm, ' Uniforme')
            # Componente cobertor
            c.rect(2 * cm, 17 * cm, 4 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.rect(6 * cm, 17 * cm, 13 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.drawString(6 * cm, 17.1 * cm, ' Cobertor')

            # Componente Observação
            c.setFillColor(aColor='black')  # Cor preto
            c.setFont("Helvetica-Bold", 12)  # Negrito
            c.rect(2 * cm, 16.5 * cm, 4 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.drawString(2 * cm, 16.6 * cm, '    Observação:')
            c.rect(6 * cm, 16.5 * cm, 13 * cm, .5 * cm, fill=0)  # para criar retangulo

            c.setFillColor(aColor='black')  # Cor preto
            c.setFont("Helvetica-Oblique", 12)
            c.rect(2 * cm, 16 * cm, 17 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.drawString(2 * cm, 16.1 * cm, '  Se uniforme, quantidade e tamanho.')
            c.rect(2 * cm, 15.5 * cm, 17 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.drawAlignedString(15 * cm, 15.6 * cm, "KIT DE HIGIENE: 01 ESCOVA DE DENTE, 01 CREME DENTAL, 03 ROLOS DE PAPEL")
            c.drawAlignedString(18.5 * cm, 15.1 * cm, "HIGIÊNICO, 04 BARBEADORES, 01 DESODORANTE LIQUIDO E 01 SABONETE.    ")
            c.rect(2 * cm, 15 * cm, 17 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.rect(2 * cm, 14.5 * cm, 17 * cm, .5 * cm, fill=0)  # para criar retangulo
            c.rect(2 * cm, 14 * cm, 17 * cm, .5 * cm, fill=0)  # para criar retangulo

            c.setFont("Helvetica-Oblique", 12)
            ## Componente recebido em
            c.setFillColor(aColor='black')  # Cor preto
            c.setFont("Helvetica-Bold", 12)  # Negrito
            c.drawString(2 * cm, 220, 'Recebido em ______/______/__________.')

            ## Assinaura do interno
            c.setFillColor(aColor='black')  # Cor preto
            c.setFont("Helvetica-Bold", 12)  # Negrito
            c.drawString(2 * cm, 170, '___________________________________')
            c.drawString(2 * cm, 155, le_pdf.get_nome_interno())

            ## Assinatura do servidor
            c.setFillColor(aColor='black')  # Cor preto
            c.setFont("Helvetica-Bold", 12)  # Negrito
            c.drawString(2 * cm, 110, '___________________________________')
            c.drawString(2 * cm, 95, 'Assinatura do servidor (nome completo).')

            c.showPage()
            c.save()  # Salva o documento e fecha
            ##################################################################################################
                    

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

    def abre_pdf(self, paginas='all'):
        try:
            self._diretorio_entrada = Path(r"\\10.40.22.35/Plantão/Para Impressão do termo de recebimento/")

            for arquivo in self._diretorio_entrada.glob('*.pdf'):#Arquivo .pdf a ser analisado
                print(arquivo)

            self._lista_tabela = tabula.io.read_pdf(arquivo, pages=paginas)
            self.numero_de_tabelas = len(self._lista_tabela)
            #print('Possui {} tabelas para uso e um cabechalho' .format(self.numero_de_tabelas-1))
            return self._lista_tabela

        except:
            print('Erro ao abrir o arquivo {}'.format(arquivo))


    def extrai_tabela(self, tabela):
        
        try:
            if 'PRONTUÁRIO | NOME' in tabela.columns:
                tabela = tabela['PRONTUÁRIO | NOME'].str.split(' - ', expand=True) #Cria duas colunas 
                tabela = tabela.rename(columns={0: 'IPEN'})#Altera o nome da coluna
                tabela = tabela.rename(columns={1: 'Nomes'})#Altera o nome da coluna
                tabela['Nomes'] = tabela['Nomes'].replace(to_replace=r'\r', value=' ', regex=True)#remove o \r
            else:
                print(f'Erro: A coluna "PRONTUÁRIO | NOME" não existe na tabela.')
                # Adiciona a coluna com valor padrão
                tabela['PRONTUÁRIO | NOME'] = 'Valor padrão'
                return tabela
        except :
            print('Erro ao extrair dados da tabela ', sys.exc_info()[0])
            return None
        
        #finally: 
            #print("Programa encerrado devido a erros")

#Inicio do "main"
#print(sys.executable) #Imprimi o local do interpretador

template = Template() #Instância a classe Template
le_pdf = Le_pdf()

tabelas_lida = le_pdf.abre_pdf()


var_vezes = len(tabelas_lida) - 1 #Remove o cabechalho 

todas_as_tabelas = []
for x in range(var_vezes): #Intera sobre todas as tabelas
#for x in range(1):
    #print(tabelas_lida[x+1])
    dados_impri = le_pdf.extrai_tabela(tabelas_lida[x+1])
    todas_as_tabelas.append(dados_impri)
tabelas_final = pd.concat(todas_as_tabelas)
#print(tabelas_final)



#or x in range(var_vezes): #Intera sobre todas as tabelas
#for x in range(1):
    #print(tabelas_lida[x+1])
    #dados_impri = le_pdf.extrai_tabela(tabelas_lida[x+1])
    #todas_as_tabelas.append(dados_impri)
#tabelas_final = pd.concat(todas_as_tabelas)
#print(tabelas_final)
#template.Imprimi_nova()