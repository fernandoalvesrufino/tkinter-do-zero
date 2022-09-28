from tkinter import *
from turtle import color

janela = Tk()
janela.title('Entry')
janela.geometry('400x250')

label_nome = Label(janela, width=10, height=1, text='Nome: ',
                   font='Arial 10', anchor='w', bg='blue', fg='white')
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = Entry(janela, width=10, text='Arial 10')
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_idade = Label(janela, width=10, height=1, text='Idade: ',
                    font='Arial 10', anchor='w', bg='blue', fg='white')
label_idade.grid(row=1, column=0, padx=10, pady=5)
entry_idade = Entry(janela, width=10, text='Arial 10')
entry_idade.grid(row=1, column=1, padx=10, pady=5)

label_pais = Label(janela, width=10, height=1, text='País: ',
                   font='Arial 10', anchor='w', bg='blue', fg='white')
label_pais.grid(row=2, column=0, padx=10, pady=5)
entry_pais = Entry(janela, width=10, text='Arial 10')
entry_pais.grid(row=2, column=1, padx=10, pady=5)

# resposta ------------------------------------------------------------

label_nome = Label(janela, width=15, height=2,
                   text='Nome: Fernando', font='Arial 10', anchor='w')
label_nome.grid(row=0, column=2, padx=10, pady=5)

label_idade = Label(janela, width=15, height=2,
                    text='Idade: 100', font='Arial 10', anchor='w')
label_idade.grid(row=1, column=2, padx=10, pady=5)

label_pais = Label(janela, width=15, height=2,
                   text='País: Brasil', font='Arial 10', anchor='w')
label_pais.grid(row=2, column=2, padx=10, pady=5)


janela.mainloop()
