from tkinter import *

janela = Tk()
janela.title('Label')
janela.geometry('250x250')

descricao = ['Nome: ', 'Idade: ', 'País: ']
cores = ['#fc3503', '#429639', '#6168e8']                # vermelho, verde e azul

for i in range(len(descricao)):
    #defino o nome da label, onde estara (no caso, na janela), largura, altura, o que estará escrito, fonte, cor da fonte (fg), cor do fundo
    # OBS: para descrever a fonte é necessario iniciar com letra maiuscula
    label = Label(janela, width=10, height=2, text = descricao[i], font=('Arial 15 bold'), fg=cores[i], bg='black')   
    # aqui descrevemos qual a posicao em relacao a linha e coluna, criando margem (pady)
    label.grid(row=i, column=0, pady=10)     

janela.mainloop()               # serve para rodar a aplicação 