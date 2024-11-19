from tkinter import *
janela=Tk()
Label(janela, text="Olá, Mundo!").grid(row=0, column=0)
Label(janela, text="Tudo bem?").grid(row=1, column=1)
janela.mainloop()

#funcionou corretamente, os textos estão embaixo um do outro e de lados opostos
#código mais limpo