count=0
suma=0
for n in range(10):
    base=int(input("Ingresar la base del triangulo"))
    altura=int(input("Ingresar la altura del triangulo"))
    superficie=(base*altura)/2
    print("La base del triangulo es: ", base, ", la altura del triangulo es: ", altura, " y la superficie del triangulo es: ", superficie)
    count +=1
    if superficie>12:
        suma=suma+1
print("La cantidad de triangulos cuya superficie es mayor a 12 es: ", suma)
    
