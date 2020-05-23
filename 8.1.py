lista=[200,14,289,65,437,28,53,701]
x=0
contador=0
while x<len(lista):
    if lista[x]>100:
        contador=contador+1
    x=x+1
print (contador, "valores de las lista son superior a 100")
