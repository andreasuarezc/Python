num1=float(input("Ingresar el primer número"))
num2=float(input("Ingresar el segundo número"))
num3=float(input("Ingresar el tercer número"))
if num1>num2 and num1>num3:
    print(num1, " es el número mayor")
    if num2>num3:
        print(num3, "es el número menor")
    else:
        if num3>=num2:
            print(num2, " es el número menor")
else:
    if num2>num1 and num2>num3:
        print(num2, " es el número mayor")
        if num1>num3:
            print(num3, " es el número menor")
        else:
            if num3>=num1:
                print(num1, " es el número menor")
    else:
        if num3>num1 and num3>num2:
            print(num3, " es el número mayor")
            if num1>num2:
                print(num2, " es el número menor")
            else:
                if num2>=num1:
                    print(num1, " es el número menor")
        else:
            if num1==num2 and num1==3:
                print("Todos los números son iguales, no hay mayor ni menor")
