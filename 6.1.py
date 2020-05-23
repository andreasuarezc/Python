#Realizar un programa que solicite la carga de valores enteros por teclado y los sume. Finalizar la carga al ingresar el valor -1.
n=int(input("Ingresar un número entero"))
suma=0
while n !=-1:
    suma=suma+n
    n=int(input("Ingresar un número entero"))
print(suma)
