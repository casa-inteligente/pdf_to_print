# -*- coding: utf-8 -*-
#####	NOME:				com_def.py
#####	VERSÃO:				1.0.1
#####	DESCRIÇÃO:			Coleta informações de um arquivo em pdf e imprime em uma declaração
#####	DATA DA CRIAÇÃO:	31/01/2024
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


class Template:
    def Imprimi_usada(self):
        lista_impressora = win32print.EnumPrinters(2)# Lista de impressoras no PC
        for impressora in lista_impressora:
            print(f'Lista a impressora {impressora}')#indice 0 da impressora
        myImpressora = lista_impressora[0]
        ### Adicionado para pagar a bandeja manual

        handle = win32print.OpenPrinter(myImpressora)
        properties = win32print.GetPrinter(handle, 2) #Usualmente '2' é a bandeja manual
        properties['pDevMode'].BinSelection = 2
        win32print.SetPrinter(handle, 2, properties, 0)

        win32print.ClosePrinter(handle) #Fecha a configuração
        ### Fim da bandeja manual
        win32print.SetDefaultPrinter(myImpressora[2])

        #seta a pasta e impressão
        caminho = r"\\10.40.22.35\Plantão\Para Impressão do termo de recebimento\Imprimir"
        print(caminho)
        lista_arq_print = os.listdir(caminho)
        for arquivo in lista_arq_print:
            win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)

    def GeneratePDF(self, dados):
         try:
             #print("Esta dentro do termo")
             self.size_dados = dados.index.stop
             print(f'O criterio de parada é {self.size_dados}')
             #print(dados[[0,1]])
             #print(dados[:2])
             dados = dados.rename(columns={0: 'IPEM'})
             dados = dados.rename(columns={1: 'Nomes'})
             #print(dados['Nomes'])
             dados['Nomes'] = dados['Nomes'].replace(to_replace=r'\r', value=' ', regex=True) #Remove o carecter \r
             #print(dados['Nomes'])

             self.page_size = A4
             self.diretorio_saida = Path(r"\\10.40.22.35/Plantão/Para Impressão do termo de recebimento/Imprimir/")
             self.diretorio_saida.mkdir(mode=777, parents=True, exist_ok=True)  # Cria diretorio caso não exista

             x = 18
             nome_interno = dados['Nomes'][x]
             numero_ipen = dados['IPEM'][x]
             ############################################################################

             self.pdf_filename = nome_interno + ".pdf"
             self.nome_arq_out = f'{self.diretorio_saida}\{self.pdf_filename}' #Concatena o diretorio de saida dos termos

             ########## Início das configurações do termo de entrega
             c = canvas.Canvas(self.nome_arq_out, pagesize=self.page_size)
             c.setTitle("Termo de Recebimento")
             c.setAuthor("Natan Ogliari")

             ### Cabeçalho
             c.setFillColor(aColor='gray')  # Cor Cinza
             c.setFont("Helvetica-Oblique", 10)
             c.drawImage('figure/logo.png', 2 * cm, 760, width=60, height=60) #Logo do estado
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
             c.drawString(2 * cm, 19.1 * cm, f'  INTERNO: {nome_interno}')
             # Componente Ipem
             c.rect(2 * cm, 18.5 * cm, 8.5 * cm, .5 * cm, fill=0)  # para criar retangulo
             c.drawString(2 * cm, 18.6 * cm, f'  IPEN:      {numero_ipen}')
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

             c.showPage()
             c.save()  # Salva o documento e fecha

         except:
             print('Erro ao gerar {}.pdf'.format(nome_interno))


class Le_pdf:

    def extrai_tabela(self, lista_tabela):
        try:
            tabela1 = lista_tabela[0]
            self.tabela2_stop = (lista_tabela[1].index.stop)
            print(f"Numero de linhas da tabela é: {self.tabela2_stop}")
            tabela2 = lista_tabela[1]

            #print("NOVA--------------")

            #print(tabela2)
            self.lista_dados = le_pdf.extrai_numero(tabela2)

            return self.lista_dados

        except:
            print('Não foi possível extrair as tabelas.')
    def extrai_numero(self, texto):
        try:
            #print("Entrou na extração de numeros.")
            #self.aux = texto['PRONTUÁRIO | NOME'].str.split(' - ', expand=True)
            return texto['PRONTUÁRIO | NOME'].str.split(' - ', expand=True)
        except:
            print("Error ao extrair numeros da tabela")
    def abre_pdf(self, paginas='all'):
        try:
            self.diretorio_entrada = Path(r"\\10.40.22.35/Plantão/Para Impressão do termo de recebimento/")

            for arquivo in self.diretorio_entrada.glob('*.pdf'):
                print(arquivo)

            lista_tabela = tabula.io.read_pdf(arquivo, pages=paginas)
            self.numero_de_tabelas = len(lista_tabela)
            print('Possui {} tabelas' .format(self.numero_de_tabelas))
            return lista_tabela

        except:
            print('Erro ao abrir o arquivo {}'.format(arquivo))


#### Chamamento das funções

template = Template() #Instancia o template do termo
le_pdf = Le_pdf()

lista_tabela = le_pdf.abre_pdf()# não precisa passar o nome do documentos, pois ele acha um pdf na pasta
dados = le_pdf.extrai_tabela(lista_tabela)

template.GeneratePDF(dados)
#template.Imprimi_usada() # Descomentar para imprimir 