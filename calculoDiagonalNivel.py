import math

print("Calculo de Curva de Nivel \n")
maior = float(input("Maior: "))
menor = float(input("Menor: "))

beta = float(input("Valor inteiro: "))
alpha = float(input("Distancia do quadrado: "))

raiz = alpha * math.sqrt(2)

# raiz = (2 ** 1/2)

aux1 = (beta - menor) * (raiz) 
aux2 = (maior - menor)


if aux1 > aux2:
    x = aux1 / aux2
else:
    x = aux2 / aux1
    

print('Resultado ' + str(x))
    
#
# ( menor - maior ) = ( beta - menor )
#        alpha               X 
#     
