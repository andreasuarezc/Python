positivo=0
negativo=0
multiplo=0
acumulado=0
for n in range(10):
    valor=int(input("Ingresar un número entero"))
    if valor>0:
        positivo=positivo+1
    else:
        negativo=negativo+1
    if valor%15==0:
        multiplo=multiplo+1
    if valor%2==0:
        acumulado=acumulado+valor
print("La cantidad de valores ingresados negativos es: ", negativo)
print("La cantidad de valores ingresados positivos es: ", positivo)
print("La cantidad de múltiplos de 15 es: ", multiplo)
print("El valor acumulado de los números ingresados que son pares. ", acumulado)
