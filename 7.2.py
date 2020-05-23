oracion=input("Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas")
oracion=oracion.lower()
print(oracion)
x=0
cantidad=0
while x<len(oracion):
    if oracion[x]=="a" or oracion[x]=="u" or oracion[x]=="e" or oracion[x]=="i" or oracion[x]=="o" or oracion[x]=="á" or oracion[x]=="é" or oracion[x]=="í" or oracion[x]=="ó" or oracion[x]=="ú":
        cantidad=cantidad+1
    x=x+1
print("La oración tiene ", cantidad, "vocales")
