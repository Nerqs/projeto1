# Use lógica em tudo!!!
from os.path import exists
import pandas as pd
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk #usarei depois para colocar caixas de seleção

#preencher os dados:

# criar o arquivo:
data = datetime.now()
data = data.strftime('%d-%m-%Y')

def pedidosHoje(): #executar apenas se não houver a planilha na pasta!!!!
    novo = {'Nome do cliente': [], 'cpf/cnpj': [], 'Endereço': [], 'Telefone': []}
    dadosnovo = pd.DataFrame(data= novo)
    dadosnovo.to_excel(f'{data}.xlsx', index= False)

if exists(f'{data}.xlsx') is False:
    pedidosHoje()

#Criando as função aqui:
def registrar():
    nome = nome_entry.get()
    cpfcnpj = cpfcnpj_entry.get()
    endereco = endereco_entry.get()
    telefone = telefone_entry.get()
    tabela = pd.read_excel(f'{data}.xlsx')
    tabela = tabela.append({'Nome do cliente': nome, 'cpf/cnpj': cpfcnpj, 'Endereço': endereco, 'Telefone': telefone}, ignore_index=True)
    tabela.to_excel(f'{data}.xlsx', index= False)
    messagebox.showinfo('', 'Dados registrados com sucesso!')

def fechar():
    janela.quit()

#Criando uma interface(BETA):
janela = Tk()
janela.title('Registro de pedidos')

nome_label = Label(text='Nome completo/Razão Social:')
nome_label.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

nome_entry = Entry()
nome_entry.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

cpfcnpj_label = Label(text='Cpf/Cnpj:')
cpfcnpj_label.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

cpfcnpj_entry = Entry()
cpfcnpj_entry.grid(row=2, column=2, padx=5, pady=5, columnspan=2)

endereco_label = Label(text='Endereço:')
endereco_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

endereco_entry = Entry()
endereco_entry.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

telefone_label = Label(text='Telefone:')
telefone_label.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

telefone_entry = Entry()
telefone_entry.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

botao1 = Button(text='Registrar novo pedido', command=registrar)
botao1.grid(column=0, row=5, padx=5, pady=5, columnspan=2)

botao2 = Button(text='Fechar', command=fechar)
botao2.grid(column=2, row=5, padx=5, pady=5, columnspan=2)

janela.mainloop()
