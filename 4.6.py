sueldo=int(input("Ingresar el sueldo del operario"))
antiguedad=int(input("Ingresar los años de antiguedad del operario"))
aumento1=sueldo+(sueldo*0.2)
aumento2=sueldo+(sueldo*0.05)
if sueldo<500 and antiguedad >= 10:
    print("Se debe otorgar un aumento salarial del 20% al operario. Así que su nuevo salario será de: ", aumento1)
else:
    if sueldo<500 and antiguedad<10:
        print("Se debe otorgar un aumento salarial del 5% al operario. Así que su nuevo salario será de: ", aumento2)
    else:
        if sueldo>=500:
            print("El sueldo del operario es: ", sueldo)
