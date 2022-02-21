# Use lógica em tudo!!!
import clipboard
from os.path import exists
import pandas as pd
from tkinter import *
from tkinter import messagebox
import os
from datetime import date

#dados:
modelos = [
    'Mandala fotogravação',
    'Coraçãozinho c/ gravação',
    'Relicário coração',
    'Relicário cartinha c/ gravação',
    'Relicário cartinha s/ gravação',
    'Formato personalizado'
]
vmodelosm1 = [ #Característica
    'Com frase',
    'Sem frase'
]
vmodelosm2 = [ #Formato
    'Redondo com furo',
    'Redondo sem furo',
    'Retangulo arredondado',
    'Retangulo',
    'Quadrado',
    'Coração padrão',
    'Personalizado'
]
vmodelosm3 = [ #Foto
    'Colorido',
    'Preto e branco'
]
vmodelosm4 = [ #Cor do banho
    'Ouro',
    'Ródio branco'
]

# criar o arquivo:

def pedidosHoje(): #executar apenas se não houver a planilha na pasta!!!!
    novo = {'Número do pedido': [], 'Modelo': [], 'Característica': [], 'Formato': [], 'Foto': [], 'Cor do banho': [], 'Gravar': []}
    dadosnovo = pd.DataFrame(data= novo)
    dadosnovo.to_excel('vendas.xlsx', index= False)

if exists('vendas.xlsx') is False:
    pedidosHoje()

#Criando as função aqui:

def gerar_relatorio():
    resposta = messagebox.askquestion('Confirmar', 'Você tem certeza que quer gerar o relatório? Isso fechara a semana atual!!!')
    if resposta == 'yes':
        relatorio = pd.read_excel('vendas.xlsx')
        relatorio = relatorio.fillna(value='Padrão')
        relatorio = relatorio.groupby(['Modelo', 'Formato', 'Cor do banho'], as_index=False, dropna=False).size()
        relatorio = relatorio.rename({'size': 'Quantidade'}, axis='columns')
        data = date.today()
        data = data.strftime('%d-%m-%Y')
        relatorio.loc[-1] = [f'Relatorio gerado em {data}', '', '', '']
        relatorio.to_html('quantidadepedido.html', index=False)
        if exists('./Relatorios-Anteriores') is False:
            os.mkdir('./Relatorios-Anteriores')

        if exists(f'./Relatorios-Anteriores/vendas{data}.xlsl') is True:
            messagebox.showinfo('', 'Erro: O arquivo ja existe na pasta Relatorios-Anteriores')
        else:
            os.rename('vendas.xlsx', f'./Relatorios-Anteriores/vendas{data}.xlsl')
            messagebox.showinfo('', 'Relatorio gerado com sucesso')

def janela_registrar():
    def variacao():
        if variable.get() == 'Mandala fotogravação':
            def registrar1():
                pedido = pedido_entry.get()
                modelo = variable.get()
                caracteristica = variable2.get()
                formato = variable3.get()
                foto = variable4.get()
                corbanho = variable5.get()
                if pedido == '' or modelo == '' or caracteristica == '' or formato == '' or foto == '' or corbanho == '':
                    messagebox.showinfo('Erro', 'Todos os campos devem ser selecionados')
                else:
                    tabela = pd.read_excel('vendas.xlsx')
                    tabela = tabela.append(
                        {'Número do pedido': pedido, 'Modelo': modelo, 'Característica': caracteristica, 'Formato': formato, 'Foto': foto, 'Cor do banho': corbanho},
                        ignore_index=True)
                    tabela.to_excel('vendas.xlsx', index=False)
                    clipboard.copy(f'Pedido n°: {pedido}. \nModelo: {modelo} {caracteristica} \nFormato: {formato} \nFoto: {foto} \nCor do banho: {corbanho}')
                    messagebox.showinfo('', 'Dados registrados e copiado com sucesso!')
                    janela2.destroy()

            vmodelom1_label = Label(janela2, text='Característica:')
            vmodelom1_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

            variable2 = StringVar(janela2)
            variable2.set('')
            vmodelom1_entry = OptionMenu(janela2, variable2, *vmodelosm1)
            vmodelom1_entry.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

            vmodelom2_label = Label(janela2, text='Formato:')
            vmodelom2_label.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

            variable3 = StringVar(janela2)
            variable3.set('')
            vmodelom2_entry = OptionMenu(janela2, variable3, *vmodelosm2)
            vmodelom2_entry.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

            vmodelom3_label = Label(janela2, text='Foto:')
            vmodelom3_label.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

            variable4 = StringVar(janela2)
            variable4.set('')
            vmodelom3_entry = OptionMenu(janela2, variable4, *vmodelosm3)
            vmodelom3_entry.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

            vmodelom4_label = Label(janela2, text='Cor do banho:')
            vmodelom4_label.grid(row=6, column=0, padx=5, pady=5, columnspan=2)

            variable5 = StringVar(janela2)
            variable5.set('')
            vmodelom4_entry = OptionMenu(janela2, variable5, *vmodelosm4)
            vmodelom4_entry.grid(row=6, column=2, padx=5, pady=5, columnspan=2)

            botao3 = Button(janela2, text='Registrar', command=registrar1)
            botao3.grid(column=0, row=7, padx=5, pady=5, columnspan=4)

        elif variable.get() == 'Coraçãozinho c/ gravação':
            def registrar2():
                pedido = pedido_entry.get()
                modelo = variable.get()
                corbanho= variable5.get()
                gravar = gravar_entry.get()
                if pedido == '' or modelo == '' or corbanho == '' or gravar == '':
                    messagebox.showinfo('Erro', 'Todos os campos devem ser selecionados')
                else:
                    tabela = pd.read_excel('vendas.xlsx')
                    tabela = tabela.append(
                        {'Número do pedido': pedido, 'Modelo': modelo, 'Cor do banho': corbanho, 'Gravar': gravar},
                        ignore_index=True)
                    tabela.to_excel('vendas.xlsx', index=False)
                    clipboard.copy(f'Pedido n°: {pedido}. \nModelo: {modelo} \nCor do banho: {corbanho} \nGravar: {gravar}')
                    messagebox.showinfo('', 'Dados registrados e copiado com sucesso!')
                    janela2.destroy()

            vmodelom4_label = Label(janela2, text='Cor do banho:')
            vmodelom4_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

            variable5 = StringVar(janela2)
            variable5.set('')
            vmodelom4_entry = OptionMenu(janela2, variable5, *vmodelosm4)
            vmodelom4_entry.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

            gravar_label = Label(janela2, text='Gravar:')
            gravar_label.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

            gravar_entry = Entry(janela2)
            gravar_entry.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

            botao3 = Button(janela2, text='Registrar', command=registrar2)
            botao3.grid(column=0, row=5, padx=5, pady=5, columnspan=4)

        elif variable.get() == 'Relicário cartinha c/ gravação':
            def registrar3():
                pedido = pedido_entry.get()
                modelo = variable.get()
                corbanho= variable5.get()
                if pedido == '' or modelo == '' or corbanho == '':
                    messagebox.showinfo('Erro', 'Todos os campos devem ser selecionados')
                else:
                    tabela = pd.read_excel('vendas.xlsx')
                    tabela = tabela.append(
                        {'Número do pedido': pedido, 'Modelo': modelo, 'Cor do banho': corbanho},
                        ignore_index=True)
                    tabela.to_excel('vendas.xlsx', index=False)
                    clipboard.copy(f'Pedido n°: {pedido}. \nModelo: {modelo} \nCor do banho: {corbanho}')
                    messagebox.showinfo('', 'Dados registrados e copiado com sucesso!')
                    janela2.destroy()

            vmodelom4_label = Label(janela2, text='Cor do banho:')
            vmodelom4_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

            variable5 = StringVar(janela2)
            variable5.set('')
            vmodelom4_entry = OptionMenu(janela2, variable5, *vmodelosm4)
            vmodelom4_entry.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

            botao3 = Button(janela2, text='Registrar', command=registrar3)
            botao3.grid(column=0, row=5, padx=5, pady=5, columnspan=4)

        elif variable.get() == 'Relicário cartinha s/ gravação':
            def registrar4():
                pedido = pedido_entry.get()
                modelo = variable.get()
                corbanho= variable5.get()
                if pedido == '' or modelo == '' or corbanho == '':
                    messagebox.showinfo('Erro', 'Todos os campos devem ser selecionados')
                else:
                    tabela = pd.read_excel('vendas.xlsx')
                    tabela = tabela.append(
                        {'Número do pedido': pedido, 'Modelo': modelo, 'Cor do banho': corbanho},
                        ignore_index=True)
                    tabela.to_excel('vendas.xlsx', index=False)
                    clipboard.copy(f'Pedido n°: {pedido}. \nModelo: {modelo} \nCor do banho: {corbanho}')
                    messagebox.showinfo('', 'Dados registrados e copiado com sucesso!')
                    janela2.destroy()

            vmodelom4_label = Label(janela2, text='Cor do banho:')
            vmodelom4_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

            variable5 = StringVar(janela2)
            variable5.set('')
            vmodelom4_entry = OptionMenu(janela2, variable5, *vmodelosm4)
            vmodelom4_entry.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

            botao3 = Button(janela2, text='Registrar', command=registrar4)
            botao3.grid(column=0, row=5, padx=5, pady=5, columnspan=4)

        elif variable.get() == 'Formato personalizado':
            def registrar5():
                pedido = pedido_entry.get()
                modelo = variable.get()
                corbanho= variable5.get()
                if pedido == '' or modelo == '' or corbanho == '':
                    messagebox.showinfo('Erro', 'Todos os campos devem ser selecionados')
                else:
                    tabela = pd.read_excel('vendas.xlsx')
                    tabela = tabela.append(
                        {'Número do pedido': pedido, 'Modelo': modelo, 'Cor do banho': corbanho},
                        ignore_index=True)
                    tabela.to_excel('vendas.xlsx', index=False)
                    clipboard.copy(f'Pedido n°: {pedido}. \nModelo: {modelo} \nCor do banho: {corbanho}')
                    messagebox.showinfo('', 'Dados registrados e copiado com sucesso!')
                    janela2.destroy()

            vmodelom4_label = Label(janela2, text='Cor do banho:')
            vmodelom4_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

            variable5 = StringVar(janela2)
            variable5.set('')
            vmodelom4_entry = OptionMenu(janela2, variable5, *vmodelosm4)
            vmodelom4_entry.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

            botao3 = Button(janela2, text='Registrar', command=registrar5)
            botao3.grid(column=0, row=5, padx=5, pady=5, columnspan=4)

        else:
            def registrar6():
                pedido = pedido_entry.get()
                modelo = variable.get()
                corbanho= variable5.get()
                if pedido == '' or modelo == '' or corbanho == '':
                    messagebox.showinfo('Erro', 'Todos os campos devem ser selecionados')
                else:
                    tabela = pd.read_excel('vendas.xlsx')
                    tabela = tabela.append(
                        {'Número do pedido': pedido, 'Modelo': modelo, 'Cor do banho': corbanho},
                        ignore_index=True)
                    tabela.to_excel('vendas.xlsx', index=False)
                    clipboard.copy(f'Pedido n°:{pedido}. \nModelo: {modelo} \nCor do banho: {corbanho}')
                    messagebox.showinfo('', 'Dados registrados e copiado com sucesso!')
                    janela2.destroy()

            vmodelom4_label = Label(janela2, text='Cor do banho:')
            vmodelom4_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
            vmodelom4_label = Label(janela2, text='Cor do banho:')
            vmodelom4_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

            variable5 = StringVar(janela2)
            variable5.set('')
            vmodelom4_entry = OptionMenu(janela2, variable5, *vmodelosm4)
            vmodelom4_entry.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

            botao3 = Button(janela2, text='Registrar', command=registrar6)
            botao3.grid(column=0, row=4, padx=5, pady=5, columnspan=4)

    janela2 = Toplevel(janela)
    janela2.title('Registro de pedidos')

    pedido_label = Label(janela2, text='Número do pedido:')
    pedido_label.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    pedido_entry = Entry(janela2)
    pedido_entry.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

    modelo_label = Label(janela2, text='Modelo:')
    modelo_label.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    variable = StringVar(janela2)
    variable.set('Mandala fotogravação')
    modelo_entry = OptionMenu(janela2, variable, *modelos)
    modelo_entry.grid(row=2, column=2, padx=5, pady=5, columnspan=2)

    botao_refresh = Button(janela2, text='Carregar', command=variacao)
    botao_refresh.grid(row=2, column=5, padx=5, pady=5, columnspan=1)

#janela inicial
janela = Tk()
janela.title('Central de pedidos')

botao = Button(text='Registrar novo pedido', command=janela_registrar)
botao.grid(column=0, row=1, padx=5, pady=5, columnspan=4)

botao2 = Button(text='Gerar relatorio', command=gerar_relatorio)
botao2.grid(column=5, row=1, padx=5, pady=5, columnspan=4)

janela.mainloop()
