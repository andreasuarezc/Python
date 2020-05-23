sueldo=[]
x=0
suma=0
while x<5:
    valor=float(input("Ingresar el sueldo del operario"))
    sueldo.append(valor)
    suma=suma+valor
    x=x+1
promedio=suma/5
print("La lista de sueldo ingresada es")
print(sueldo)
print("El promedio de sueldo es")
print(promedio)
