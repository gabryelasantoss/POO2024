from tkinter import *

janela=Tk()
janela.title("Calculadora")
janela.geometry("300x150+100+100")

rotulo1=Label(janela, text="Valor 1:")
rotulo1.grid(row=0, column=0)

campo1=Entry(janela)
campo1.grid(row=0, column=1)

rotulo2=Label(janela, text="Valor 2:")
rotulo2.grid(row=1, column=0)

campo2=Entry(janela)
campo2.grid(row=1, column=1)

rotulo3=Label(janela, text="Resultado =")
rotulo3.grid(row=3, column=0)

campo3=Entry(janela, state="readonly") 
campo3.grid(row=3, column=1)

def somar():
    v1=float(campo1.get())
    v2=float(campo2.get())
    resultado= v1 + v2
    atualizar_resultado(resultado)

def subtrair():
    v1= float(campo1.get())
    v2= float(campo2.get())
    resultado= v1 - v2
    atualizar_resultado(resultado)

def multiplicar():
    v1=float(campo1.get())
    v2=float(campo2.get())
    resultado= v1 * v2
    atualizar_resultado(resultado)

def dividir():
    v1=float(campo1.get())
    v2=float(campo2.get())
    if v2 != 0:
        resultado= v1 / v2
    else:
        resultado= "Erro: Div/0"  
    atualizar_resultado(resultado)

def atualizar_resultado(resultado):
    campo3.config(state="normal") 
    campo3.delete(0, END)
    campo3.insert(0, resultado)
    campo3.config(state="readonly") 

botao_somar=Button(janela, text="Somar", command=somar, width=10)
botao_somar.grid(row=2, column=0)

botao_subtrair=Button(janela, text="Subtrair", command=subtrair, width=10)
botao_subtrair.grid(row=2, column=1)

botao_multiplicar=Button(janela, text="Multiplicar", command=multiplicar, width=10)
botao_multiplicar.grid(row=4, column=0)

botao_dividir=Button(janela, text="Dividir", command=dividir, width=10)
botao_dividir.grid(row=4, column=1)

janela.mainloop()