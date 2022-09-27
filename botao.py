# Aqui foi criado uma janela com um botão, onde cada vez que é clicado incrementa-se um valor a uma variável. Uma label é atualizada e apresenta o numero
# se é par ou ímpar

from tkinter import *

cor_preta = '#000000'
cor_branca = '#FFFFFF'
cor_amarela = '#fcb603'
cor_azul = '#0000ff'
cor_vermelha = '#FF0000'

janela = Tk()
janela.title('Botão')
janela.geometry('250x250')

global contador
contador = 0

def executar():

  global contador

  texto_1 = 'Ímpar'
  texto_2 = 'Par'

  if contador % 2 == 0:
    resultado = str(contador) + ' - ' + texto_2
    label['text'] = resultado
    label['bg'] = cor_azul
  else:
    resultado = str(contador) + ' - ' + texto_1
    label['text'] = resultado
    label['bg'] = cor_vermelha

  contador += 1

label = Label(janela, width=20, height=2, text='Deseja iniciar?', relief='flat', fg=cor_branca, bg=cor_preta)
label.grid(row=0, column=0, padx=5, pady=10)

botao = Button(janela, command=executar, width=10, height=1, text='Clique aqui', relief='raised', fg=cor_preta, bg=cor_branca)
botao.grid(row=0, column=1, padx=5, pady=10)



janela.mainloop()
