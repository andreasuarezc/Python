n=float(input("Ingresar un número entero positivo de hasta tres cifras"))
division=n/10
if division>=100:
    print("Eror. El número ingresado tiene más de tres cifras.")
else:
    if division>=10:
        print("El número ingresado tiene tres cifras")
    else:
        if division>=1:
            print("El número ingresado tiene dos cifras")
        else:
            print("El número ingresado tiene una cifra")
