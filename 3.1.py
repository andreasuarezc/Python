num1=float(input("Ingresar el primer número"))
num2=float(input("Ingresar el segundo número"))
num3=float(input("Ingresar el tercer número"))
if num1>num2 and num1>num3:
    print(num1, " es el número mayor")
else:
    if num2>num1 and num2>num3:
        print(num2, " es el número mayor")
    else:
        print(num3, " es el número mayor")
