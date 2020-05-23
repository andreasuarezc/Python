count=0
suma1=0
suma2=0
while count<15:
    valor1=int(input("Ingresar un valor a la lista1"))
    suma1=suma1+valor1

    valor2=int(input("Ingresar un valor a la lista2"))
    suma2=suma2+valor2

    count+=1
    
if suma1==suma2:
    print("Las listas son iguales")
else:
    if suma1>suma2:
        print("Lista 1 mayor")
    else:
        print("Lista 2 mayor")
