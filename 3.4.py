preguntas=int(input("Ingresar el total de preguntas realizadas"))
correctas=int(input("Ingresar el total de respuestas correctas"))
porcentaje=correctas/preguntas
if porcentaje>=0.9:
    print("El postulante obtuvo el nivel máximo")
else:
    if porcentaje>=0.75:
        print("El postulante obtuvo el nivel medio")
    else:
        if porcentaje>=0.5:
            print("El postulante obtuvo el nivel regular")
        else:
            print("El postulante está fuera de nivel")
    
