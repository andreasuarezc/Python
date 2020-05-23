suma1=0
suma2=0
suma3=0
for mañana in range (5):
    edad1=int(input("Ingresar edad de estudiante turno mañana"))
    suma1=suma1+edad1
for tarde in range (6):
    edad2=int(input("Ingresar edad de estudiante turno tarde"))
    suma2=suma2+edad2
for noche in range (11):
    edad3=int(input("Ingresar edad de estudiante turno noche"))
    suma3=suma3+edad3
promedio1=suma1/5
promedio2=suma2/6
promedio3=suma3/11
print("El promedio de edad de las estudiantes del turno mañana es: ", promedio1)
print("El promedio de edad de las estudiantes del turno tarde es: ", promedio2)
print("El promedio de edad de las estudiantes del turno noche es: ", promedio3)
if promedio1>promedio2 and promedio1>promedio3:
    print("El turno de la mañana tiene un promedio de edades mayor")
else:
    if promedio2>promedio1 and promedio2>promedio3:
        print("El turno de la tarde tiene un promedio de edades mayor")
    else:
        print("El turno de la noche tiene un promedio de edades mayor")
    
