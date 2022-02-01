# Use lógica em tudo!!!
import clipboard
from os.path import exists
import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #usarei depois para colocar caixas de seleção

#dados:
modelos = [
    'Redondin',
    'Quadradin',
    'Retangularzin',
    'Tortinho'
]
vmodelos = [
    'branco',
    'preto',
    'azul',
    'cinza',
    'vermelho',
    'coral'
]

# criar o arquivo:

def pedidosHoje(): #executar apenas se não houver a planilha na pasta!!!!
    novo = {'Número do pedido': [], 'Modelo': [], 'Variação do modelo': []}
    dadosnovo = pd.DataFrame(data= novo)
    dadosnovo.to_excel('vendas.xlsx', index= False)

if exists('vendas.xlsx') is False:
    pedidosHoje()

#Criando as função aqui:

def gerar_relatorio():
    relatorio = pd.read_excel('vendas.xlsx')
    print(relatorio)
    messagebox.showinfo('', 'Relatorio gerado com sucesso')

def janela_registrar():

    def registrar():
        pedido = pedido_entry.get()
        modelo = variable.get()
        vmodelo = variable2.get()
        tabela = pd.read_excel('vendas.xlsx')
        tabela = tabela.append(
            {'Número do pedido': pedido, 'Modelo': modelo, 'Variação do modelo': vmodelo},
            ignore_index=True)
        tabela.to_excel('vendas.xlsx', index=False)
        clipboard.copy(f'Pedido n°:{pedido}. \n{modelo} {vmodelo}')
        messagebox.showinfo('', 'Dados registrados e copiado com sucesso!')

    janela2 = Toplevel(janela)
    janela2.title('Registro de pedidos')

    pedido_label = Label(janela2, text='Número do pedido:')
    pedido_label.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    pedido_entry = Entry(janela2)
    pedido_entry.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

    modelo_label = Label(janela2, text='Modelo:')
    modelo_label.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    variable = StringVar(janela2)
    variable.set('Redondin')
    modelo_entry = OptionMenu(janela2, variable, *modelos)
    modelo_entry.grid(row=2, column=2, padx=5, pady=5, columnspan=2)

    vmodelo_label = Label(janela2, text='Variação do modelo:')
    vmodelo_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    variable2 = StringVar(janela2)
    variable2.set('')
    vmodelo_entry = OptionMenu(janela2, variable2, *vmodelos)
    vmodelo_entry.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

    botao3 = Button(janela2, text='Registrar', command=registrar)
    botao3.grid(column=0, row=4, padx=5, pady=5, columnspan=4)

#janela inicial
janela = Tk()
janela.title('Central de pedidos')

botao = Button(text='Registrar novo pedido', command=janela_registrar)
botao.grid(column=1, row=1, padx=5, pady=5, columnspan=2)

botao2 = Button(text='Gerar relatorio', command=gerar_relatorio)
botao2.grid(column=2, row=1, padx=5, pady=5, columnspan=2)

janela.mainloop()
