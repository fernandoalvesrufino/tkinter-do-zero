from tkinter import *

color_black = '#000000'           # criando variáveis contendo o código da cor preta

janela = Tk()                    
janela.title('Olá, mundo')      # nome que  será apresentado na parte superior da janela
janela.geometry('600x250')      # definindo o tamanho da janela (largura x altura)
janela.config(bg=color_black)   # definindo algumas configurações da janela

janela.iconphoto(False, PhotoImage(file='img/ola.png'))              # alterando o icone da janela
janela.resizable(height=True, width=False)                           # definindo se será ou não possível redimensionar altura e largura

janela.mainloop()               # serve para rodar a aplicação 