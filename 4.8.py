x=1
mayor=0
menor=0
while x<=10:
    nota= float(input("Ingresar la nota"))
    if nota>=7:
        mayor=mayor+1
    else:
        menor=menor+1
    x=x+1
print(mayor, " alumnos tienen notas mayores o iguales a 7 y ", menor, " alumnos tienen notas menores a 7.")
