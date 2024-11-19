from tkinter import *
janela=Tk()

rotulo = Label (janela,text="Olá, Alba!")
rotulo.grid (row=0, column=0)

rotulo2 = Label (janela,text="Tudo bem?")
rotulo2.grid (row=0, column=1)

janela.mainloop()

#substitui o "Olá, mundo!" por: "Olá, Alba!" c:
#Funcionou corretamente, abriu uma janela com o texto "Olá, Mundo!" em cima e "Tudo bem?" embaixo
#mudando a coluna para 1, o segundo texto apareceu ao lado