# pack() - coloca os widgets em um dos quatro lados. Novos widgets sao colocados ao lado dos ja existentes

from tkinter import *

janela = Tk()
janela.title('Label')
janela.geometry('250x250')

label_nome = Label(janela, width=10, height=2, text = 'Nome: ', font=('Arial 10'), fg='#fc3503', bg='black')   
label_nome.pack(side=LEFT)
nome = Label(janela, width=10, height=2, text = 'Fernando', font=('Arial 10'), fg='#fc3503', bg='black')   
nome.pack(side=LEFT)     

label_idade = Label(janela, width=10, height=2, text = 'Idade: ', font=('Arial 10'), fg='#429639', bg='black')   
label_idade.pack(side=LEFT) 
idade = Label(janela, width=10, height=2, text = 'XX', font=('Arial 10'), fg='#429639', bg='black')   
idade.pack(side=LEFT)  

label_pais = Label(janela, width=10, height=2, text = 'País: ', font=('Arial 10'), fg='#6168e8', bg='black')   
label_pais.pack(side=LEFT)   
pais = Label(janela, width=10, height=2, text = 'Brasil', font=('Arial 10'), fg='#6168e8', bg='black')   
pais.pack(side=LEFT)



janela.mainloop()               # serve para rodar a aplicação 