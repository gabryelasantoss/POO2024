from tkinter import *

janela = Tk()

info="Esse texto será\nexibido no rótulo\nem várias linhas."
rotulo1=Label(janela, text=info, justify="left")
rotulo1.grid(row=0, column=0)

logo=PhotoImage(file="logopy.png") 
rotulo2=Label(janela, image=logo)
rotulo2.grid(row=0, column=1)

botao = Button(janela, text="Sair", command=janela.quit)
botao.grid(row=1, column=0)
botao["width"]=10

janela.mainloop()

#adicionei a imagem, funcionou corretamente
