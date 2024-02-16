# -*- coding: utf-8 -*-
#####	NOME:				com_def.py
#####	VERSÃO:				1.0
#####	DESCRIÇÃO:			Coleta informações de um arquivo em pdf e imprime em uma declaração
#####	DATA DA CRIAÇÃO:	31/01/2024
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	DISTRO:				Ubuntu GNU/Linux 22.04
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/casa-inteligente/pdf_to_print


import datetime as dd

import spacy.strings
from reportlab.lib.pagesizes import A4
import tabula
from tabula.io import read_pdf
from pathlib import Path
import pandas

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm


class Template:

    def GeneratePDF(self, nome_interno='TESTE', numero_ipen = '123456'):
         try:

             self.diretorio_saida = Path(r"\\10.40.22.35/Plantão/Para Impressão do termo de recebimento/Imprimir/")
             self.diretorio_saida.mkdir(parents=True, exist_ok=True)  # Cria diretorio caso não exista
             self.pdf_filename = nome_interno + ".pdf"
             self.page_size = A4
             self.nome_arq_out = f'{self.diretorio_saida}\{self.pdf_filename}' #Concatena o diretorio de saida dos termos

             #print("dir_saida: \t" + self.nome_arq_out)



             c = canvas.Canvas(self.nome_arq_out, pagesize=self.page_size)
             c.setTitle("Termo de Recebimento")
             c.setAuthor("Natan Ogliari")

             ### Cabeçalho
             c.setFillColor(aColor='gray')  # Cor Cinza
             c.setFont("Helvetica-Oblique", 10)
             c.drawImage('logo.png', 2 * cm, 760, width=60, height=60)
             c.drawString(4.5 * cm, 800, "ESTADO DE SANTA CATARINA")
             c.drawString(4.5 * cm, 785, "SECRETARIA DE ESTADO DA ADMINISTRAÇÃO PRISIONAL E SOCIOEDUCATIVA")
             c.drawString(4.5 * cm, 770, 'PRESÍDIO MARAVILHA')
             ################
             #### Rodapé
             # c.setFillColor(aColor='gray')  # Cor Cinza
             c.setFillColor(aColor='gray', alpha=1)
             # c.setFillColorRGB(.662 ,.662, .662, 1)
             c.setFont("Helvetica-Oblique", 8)
             c.drawCentredString(300, 70, 'POLÍCIA PENAL DE SANTA CATARINA', mode=None, charSpace=0)
             c.drawCentredString(300, 60, 'Presídio de Maravilha', mode=None, charSpace=0)
             c.drawCentredString(300, 50, 'Av. Sul Brasil, n. 1607, centro - CEP 89874-000 - Maravilha/SC', mode=None,
                                 charSpace=0)
             c.drawCentredString(300, 40, 'Fone: (49) 3664 - 6672 / e-mail: pr29@pp.sc.gov.br', mode=None, charSpace=0)

             ### Titulo do documento
             c.setFillColor(aColor='black')  # Cor preto
             c.setFont("Helvetica-Bold", 12)  # Negrito
             c.drawCentredString(10.5 * cm, 730, 'TERMO DE RECEBIMENTO')
             c.drawString(2 * cm, 680, 'Instruções:')
             c.setFont("Helvetica-Oblique", 12, leading=1)  # Fonte normal
             c.drawString(2 * cm, 650, '01) Os internos devem assinalar a opção com um "X";')
             c.drawString(2 * cm, 630,
                          '02) Na opção "Observação" descrever o que está sendo entregue (tamanho e quantidade')
             c.drawString(2 * cm, 610, 'de uniforme);')
             c.drawString(2 * cm, 590,
                          '03) O termo de recebimento, devidamente assinado, deverá ser digitalizado e arquivado')
             c.drawString(2 * cm, 570, 'no IPEN do interno;')
             c.rect(2 * cm, 10 * cm, 17 * cm, 9 * cm, fill=0)  # para criar retangulo

             ## data do sistema no formato BR
             hoje = dd.datetime.now()
             hoje_br = hoje.strftime("%d/%m/%Y")
             # print(hoje_br)
             # Componente no nome
             c.rect(2 * cm, 19 * cm, 17 * cm, .5 * cm, fill=0)  # para criar retangulo
             c.drawString(2 * cm, 19.1 * cm, '  INTERNO:       ' + nome_interno)
             # Componente Ipem
             c.rect(2 * cm, 18.5 * cm, 8.5 * cm, .5 * cm, fill=0)  # para criar retangulo
             c.drawString(2 * cm, 18.6 * cm, '  IPEN:       ' + numero_ipen)
             # Componente data
             c.rect(10.5 * cm, 18.5 * cm, 8.5 * cm, .5 * cm, fill=0)  # para criar retangulo
             c.drawString(10.5 * cm, 18.6 * cm, '  DATA:       ' + hoje_br)
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
             c.drawString(2 * cm, 155, nome_interno)

             ## Assinatura do servidor
             c.setFillColor(aColor='black')  # Cor preto
             c.setFont("Helvetica-Bold", 12)  # Negrito
             c.drawString(2 * cm, 110, '___________________________________')
             c.drawString(2 * cm, 95, 'Assinatura do servidor (nome completo).')

             # #para teste maluco
             # xlist = [2*cm , 10*cm ]
             # ylist = [2*cm , 20*cm ]
             #
             # c.grid(xlist, ylist)

             c.showPage()
             c.save()  # Salva o documento e fecha

         except:
             print('Erro ao gerar {}.pdf'.format(nome_interno))


class Le_pdf:

    def extrai_tabela(self, lista_tabela):
        try:
            tabela1 = lista_tabela[1]
            tabela2 = lista_tabela[2]
            tabela3 = lista_tabela[3]
            tabela4 = lista_tabela[4]
            tabela5 = lista_tabela[5]
            tabela6 = lista_tabela[6]
            tabela7 = lista_tabela[7]
            tabela8 = lista_tabela[8]
            tabela9 = lista_tabela[9]
            tabela10 = lista_tabela[10]
            tabela11 = lista_tabela[11]
            tabela12 = lista_tabela[12]
            tabela13 = lista_tabela[13]
            tabela14 = lista_tabela[14]
            tabela15 = lista_tabela[15]
            tabela16 = lista_tabela[16]
            tabela17 = lista_tabela[17]

            #print(tabela1)
            #tabela1.drop_duplicates(ignore_index=True, keep=False)
            print("NOVA--------------")
            #print(tabela1.head(20))#Imprimi as primeiras posições setadas
            #tabela1 = tabela1.dropna()#Exclui as Linhas vazias
            print(tabela1)
            tabela_nova = lista_tabela[1]

            return tabela_nova

        except:
            print('Não foi possível extrair tabelas.')

    def abre_pdf(self, arquivo='ESTE', paginas='all'):
        try:
            self.diretorio_entrada = Path(r"\\10.40.22.35/Plantão/Para Impressão do termo de recebimento/")

            for arquivo in self.diretorio_entrada.glob('*.pdf'):
                print(arquivo)

            lista_tabela = tabula.io.read_pdf(arquivo, pages=paginas)
            nome_interno = 'FULANO'
            numero_tabelas = len(lista_tabela)
            print('Possui {} tabelas' .format(numero_tabelas))

            #Para apagar Linha: axis=0
            #Para apagar Coluna: axis=1
            #lista_tabela = lista_tabela.drop("691874", axis=0) # eixo 0 linha; eixo 1 coluna

            #tabula.io.convert_into(arquivo, 'imprimir/ds.csv', pages='all') #Exporta para .csv

            #dados = pd.read_csv('imprimir/ds.csv')


            # re =  lista_tabela[0].index
            # print(re)
            # for tabela in lista_tabela: #grava as tabelas em tabela
            #     #print(tabela, "\n +++++++++++++++++++++\n")
            #     print(tabela.index)
            #Le_pdf.extrai_tabela(lista_tabela)
            #lista_tabela.remove('DENTRO DA REGRA')
            #A lista_tabela[0] é o cabelçhalho do documento i index inicia em [ZERO]

            #tabela2 = tabela2.drop('TRABALHO INTERNO157, 157, 61, 61, 61,553362 JOEL DE OLIVEIRA155, 121, 33 | COM FOTO,TRABALHO INTERNODENTRO DA REGRA', axis=0)
            #print( tabela2.head())

            #print(tabela2)
            #tabela2[[0 ,1]] = tabela["coloca_aqui_nome_coluna"].str.split("\r", expend=True)

            #tabela_var.columns = tabela_var.iloc[20] #Muda o cabachalho da tabela



            print("\n INICIO DOS TESTE DE EXTRAÇÃO DE DADOS SEPARADOS\n")
            #print(tabela_var)
            return lista_tabela

        except:
            print('Erro ao abrir o arquivo {}'.format(arquivo))




template = Template() #Instancia o template do termo
le_pdf = Le_pdf()

lista_tabela = le_pdf.abre_pdf('Arquivo_analisado/ESTE')
#nome_interno = le_pdf.extrai_tabela(lista_tabela)
# for x in nome_interno:
#     print(nome_interno[x])
#     print("=======================")

template.GeneratePDF()
