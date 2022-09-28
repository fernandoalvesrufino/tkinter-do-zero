from tkinter import *

# função ---------------------------------
def obter():
    valor_informado = [entry_nome.get(), entry_idade.get(), entry_pais.get()]
    label_referencia = [label_nome_esperado, label_idade_esperado, label_pais_esperado]

    for i in range(3):
        if not valor_informado[i] == '':
            label_referencia[i]['text'] = valor_informado[i]
        else:
            label_referencia[i]['text'] = 'Valor não informado!'
    
    entry_nome.delete(0, END)
    entry_idade.delete(0, END)
    entry_pais.delete(0, END)

    
janela = Tk()
janela.title('Entry')
janela.geometry('400x250')
    
# labels ----------------------------------
label_nome = Label(janela, width=10, height=1, text='Nome: ', font='Arial 10', anchor='w', bg='blue', fg='white')
label_nome.grid(row=0, column=0, padx=10, pady=5)
label_idade = Label(janela, width=10, height=1, text='Idade: ',  font='Arial 10', anchor='w', bg='blue', fg='white')
label_idade.grid(row=1, column=0, padx=10, pady=5)
label_pais = Label(janela, width=10, height=1, text='País: ', font='Arial 10', anchor='w', bg='blue', fg='white')
label_pais.grid(row=2, column=0, padx=10, pady=5)

# entry ----------------------------------
entry_nome = Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)
entry_idade = Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=5)
entry_pais = Entry(janela)
entry_pais.grid(row=2, column=1, padx=10, pady=5)

# resposta ------------------------------------------------------------

label_nome_esperado = Label(janela, width=15, height=2, text='Ex: Fernando', font='Arial 10', anchor='w')
label_nome_esperado.grid(row=0, column=2, padx=10, pady=5)

label_idade_esperado = Label(janela, width=15, height=2, text='Ex: 100', font='Arial 10', anchor='w')
label_idade_esperado.grid(row=1, column=2, padx=10, pady=5)

label_pais_esperado = Label(janela, width=15, height=2,text='Ex: Brasil', font='Arial 10', anchor='w')
label_pais_esperado.grid(row=2, column=2, padx=10, pady=5)

botao = Button(janela, command=obter, width=8, height=1,text='Ver dados', relief='raised', bg='white')
botao.grid(row=3, column=0, padx=5, pady=20)


janela.mainloop()
