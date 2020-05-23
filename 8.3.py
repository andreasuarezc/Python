lista=["andrea","viviana","jorge","blanca","luis"]
x=0
contador=0
while x<len(lista):
    if len (lista[x])>=5:
        contador=contador+1
    x=x+1
print(contador, " de los nombres almacenados en la lista tienen 5 o más caracteres")
