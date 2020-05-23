mañana=[]
tarde=[]
for x in range (4):
    valor1=float(input("Ingresar el salario de un empleado del turno de la mañana"))
    mañana.append(valor1)
    valor2=float(input("Ingresar el salario de un empleado del turno de la tarde"))
    tarde.append(valor2)
print("La lista de sueldos de los empleados del turno de la mañana es: ")
print(mañana)
print("La lista de sueldos de los empleados del turno de la tarde es: ")
print(tarde)
