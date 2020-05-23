count=0
suma=0
for n in range (10):
    valor=int(input("Ingresar un número"))
    count +=1
    if count>5:
        suma=suma+valor
print("La suma de los últimos 5 valor ingresados es: ", suma)
    
