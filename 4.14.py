n=int(input("¿Cuántos números enteros vas a ingresar?"))
count=0
suma1=0
suma2=0
while count<n:
    valor=int(input("Ingresar un número entero"))
    if valor%2==0:
        suma1=suma1+1
    else:
        suma2=suma2+1
    count +=1
print(suma1, " valores fueron pares. Y ", suma2, " valores fueron impares")
