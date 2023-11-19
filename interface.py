import tkinter as tk

def exibir_texto():
    #maior_valor = float(maior.get()
    maior_valor = float(maior.get())
    menor_valor = float(menor.get())

    beta = float(valor_inteiro.get())
    alpha = float(distancia.get())

    aux1 = (beta - menor_valor) * alpha
    aux2 = (maior_valor - menor_valor)
    if aux1 > aux2:
        x = aux1 / aux2
    else:
        x = aux2 / aux1
    
    resultado_final = x
    label_resultado.config(text=resultado_final)
    
janela = tk.Tk()
janela.title("Calculo de Curva de Nivel")


label_maior = tk.Label(janela, text="Valor Maior:")
label_maior.grid(row=0,column=0,pady=5,padx=5,sticky=tk.W)

maior = tk.Entry(janela,width=10)
maior.grid(row=0,column=1,pady=5,padx=5)


label_menor = tk.Label(janela, text="Valor Menor:")
label_menor.grid(row=1,column=0,pady=5,padx=5,sticky=tk.W)

menor = tk.Entry(janela,width=10)
menor.grid(row=1,column=1,pady=5,padx=5)


label_valor_inteiro = tk.Label(janela, text="Valor Inteiro:")
label_valor_inteiro.grid(row=2,column=0,pady=5,padx=5,sticky=tk.W)

valor_inteiro = tk.Entry(janela,width=10)
valor_inteiro.grid(row=2,column=1,pady=5,padx=5)


label_distancia = tk.Label(janela, text="Distancia:")
label_distancia.grid(row=3,column=0,pady=5,padx=5,sticky=tk.W)

distancia = tk.Entry(janela,width=10)
distancia.grid(row=3,column=1,pady=5,padx=5)

botao_exibir = tk.Button(janela,text = "Calcular",
command=exibir_texto)

botao_exibir.grid(row=4,column=0,columnspan=2, pady=10)

label_resultado = tk.Label(janela,text="")
label_resultado.grid(row=6,column=0,columnspan=2)

janela.mainloop()