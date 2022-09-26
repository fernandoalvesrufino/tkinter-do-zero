from tkinter import *
from turtle import width

janela = Tk()
janela.title('Label')
janela.geometry('250x250')

descricao = ['Nome: ', 'Idade: ', 'País: ']

for i in range(len(descricao)):
    #defino o nome da label, onde estara (no caso, na janela), largura, altura, o que estará escrito, fonte
    label = Label(janela, width=10, height=2, text = descricao[i], font=('Arial 15 bold'))   
    # aqui descrevemos qual a posicao em relacao a linha e coluna
    label.grid(row=i, column=0)     

janela.mainloop()               # serve para rodar a aplicação 