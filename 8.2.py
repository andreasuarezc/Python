lista=[4,9,6,8,12]
x=0
contador=0
while x<len(lista):
    if lista[x]>=7:
        contador=contador+1
    x=x+1
print(contador, " elementos de la lista son iguales o superiores a 7")
