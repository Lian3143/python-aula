import requests
from tkinter import * #é mais vantajoso importar a biblioteca desta forma

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes['text'] = texto #definirá o texto que aparecerá após clicar no botão. 




janela = Tk() #definirá a criação da janela
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

janela.title('Cotação atual das moedas') #O comando TITLE serve para alterar o titulo da janela
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
janela.geometry('300x200') #vai definir o tamanho da janela
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


texto_de_orientação = Label(janela, text =' Clique no botão abaixo para exibir as cotações') #label serve para exibir textos. Primeiro você deverá especificar em qual janela ele fará parte e, após isso, colocara o comando TEXT = 'Digite o seu texto aqui '. 

texto_de_orientação.grid(column = 0, row=0, padx=20, pady=20) #column = coluna / row = linha. Esse comando .grid especificará onde vai ficar o texto na tela. você deve especificar a coluna e a linha. padx e pady significam padding.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

botao = Button(janela, text = 'Clique aqui para exibir as cotações ', command=pegar_cotacoes) #Isso adicionará um botão na tela. Primeiro, você vai dizer em que janela o botão deve ficar. Depois, vai dizer o texto que vai conter no botão e, logo após, irá definir um comando(função) para esse botão.

botao.grid(column=0, row=1) #isso mostrará onde o botão aparecerá, assim como o texto. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

texto_cotacoes = Label(janela, text=' ')
texto_cotacoes.grid(column=0, row=2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


janela.mainloop() #essa é sempre a última linha de código de um código, pois ele é quem fará com que a janela fique sempre em exibição, sem fechar automaticamente. 