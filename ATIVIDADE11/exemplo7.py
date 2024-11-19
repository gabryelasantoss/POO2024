from tkinter import *

janela = Tk()

info = "Esse texto será\nexibido no rótulo\nem várias linhas."

rotulo = Label(janela, text=info, justify="left")
rotulo.grid(row=0, column=0)

info2 = """Assim também
é possível
ter várias linhas."""

botao = Button(janela, text="Sair", command=janela.quit)
botao.grid(row=2, column=0)
botao["width"] = 10

rotulo2 = Label(janela, text=info2, justify="right")
rotulo2.grid(row=3, column=0)


janela.mainloop()


#funcionou corretamente, ajustei largura do botão e algumas alterações pra que ele ficasse mais parecido com a imagem do slide
