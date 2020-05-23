cantidad=int(input("Cuántos triángulos vas a calcular"))
suma1=0
suma2=0
suma3=0
for x in range(cantidad):
    lado1=int(input("Ingresar el primer lado del triángulo"))
    lado2=int(input("Ingresar el segundo lado del triándulo"))
    lado3=int(input("Ingresar el tercer lado del triándulo"))
    if lado1== lado2 and lado1==lado3:
        print("Es un triángulo equilatero")
        suma1=suma1+1
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("Es un triángulo isosceles")
            suma2=suma2+1
        else:
            print("Es un triángulo escaleno")
            suma3=suma3+1
print("La cantida de triángulos equilatero es: ", suma1, ", de triángulo isosceles es: ", suma2, " y de escaleno es: ", suma3)

    
    
