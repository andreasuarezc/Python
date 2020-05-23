x=1
gastospersonal=0
suma1=0
suma2=0
while x>=1:
    sueldo=int(input("Ingresar el sueldo del empleado"))
    if sueldo>300:
        suma1=suma1+1
    else:
        suma2=suma2+1
    gastospersonal=gastospersonal+sueldo
    print(suma2, " empleados cobran entre $100 y $300. Y ", suma1, " empleados cobran más de $300")
    print("En total la empresa gasta ", gastospersonal, " en sueldos al personal")
