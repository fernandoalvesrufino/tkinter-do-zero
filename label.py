from tkinter import *
from turtle import width

janela = Tk()
janela.title('Label')
janela.geometry('250x250')

#defino o nome da label, onde estara (no caso, na janela), largura, altura, o que estará escrito
label_nome = Label(janela, width=10, height=2, text = 'Fernando')   
label_nome.grid(row=0, column=0)                  # aqui descrevemos qual a posicao em relacao a linha e coluna

janela.mainloop()               # serve para rodar a aplicação 