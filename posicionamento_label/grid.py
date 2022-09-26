# grid() - coloca os widgets em uma grade semelhante a uma planilha de Excel

from tkinter import *

janela = Tk()
janela.title('Label')
janela.geometry('250x250')

label_nome = Label(janela, width=10, height=2, text = 'Nome: ', font=('Arial 10'), fg='#fc3503', bg='black')   
label_nome.grid(row=0, column=0, padx=5, pady=10)
nome = Label(janela, width=10, height=2, text = 'Fernando', font=('Arial 10'), fg='#fc3503', bg='black')   
nome.grid(row=0, column=1, padx=5, pady=10)     

label_idade = Label(janela, width=10, height=2, text = 'Idade: ', font=('Arial 10'), fg='#429639', bg='black')   
label_idade.grid(row=1, column=0, padx=5, pady=10) 
idade = Label(janela, width=10, height=2, text = 'XX', font=('Arial 10'), fg='#429639', bg='black')   
idade.grid(row=1, column=1, padx=5, pady=10)  

label_pais = Label(janela, width=10, height=2, text = 'País: ', font=('Arial 10'), fg='#6168e8', bg='black')   
label_pais.grid(row=2, column=0, padx=5, pady=10)   
pais = Label(janela, width=10, height=2, text = 'Brasil', font=('Arial 10'), fg='#6168e8', bg='black')   
pais.grid(row=2, column=1, padx=5, pady=10)



janela.mainloop()               # serve para rodar a aplicação 