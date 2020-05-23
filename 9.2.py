altura=[]
suma=0
for x in range(5):
    valor=(float(input("Ingresar la altura de cada persona")))
    altura.append(valor)
    suma=suma+valor
promedio=suma/5
print("El promedio de estatura es de: ")
print(promedio)
suma1=0
suma2=0
for x in range(5):
    if altura[x]>promedio:
        suma1=suma1+1
    else:
        if altura[x]<promedio:
            suma2=suma2+1
print("La cantidad de personas que son más altas que el promedio es de: ")
print(suma1)
print("La cantidad de personas que son más bajas que el promedio es de: ")
print(suma2)
           
