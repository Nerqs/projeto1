#logica é sempre a resposta!!!
#criando um gerador de hashtag aleatoria baseado em um banco de dados externo

from random import shuffle
import pandas as pd
from tkinter import *
import clipboard

lista = []

#ler o banco de dados e pegar uma quantidade determinada pelo cliente de hashtags:
def hashtag():
    tabela = pd.read_excel('hashtags.xlsx')
    lista = list(tabela['Hashtags'])
    shuffle(lista)
    num = int(entry_gerador.get())
    lista = lista[0:num]
    dados_gerados['text'] = lista
    lista = str(lista)
    remove = "[,']"
    for i in range(0, len(remove)):
        lista = lista.replace(remove[i],'')
    clipboard.copy(lista)

#montar a interface:
janela = Tk()
janela.iconbitmap('icon.ico')
janela.title('Gerador de Hashtags')

label_gerador = Label(text='Digite quantas Hashtags você deseja:')
label_gerador.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

entry_gerador = Entry()
entry_gerador.grid(row=0, column=2, padx=5, pady=5, columnspan=2)

botao = Button(text='Gerar e Copiar', command=hashtag)
botao.grid(row=1, column=0, padx=5, pady=5, columnspan=4)

dados_gerados = Label(text='')
dados_gerados.grid(row=2, column=0, padx=5, pady=5, columnspan=4)

janela.mainloop()

