cantidad=int(input("Cuántas coordenadas vas a ingresar"))
primero=0
segundo=0
tercero=0
cuarto=0
for x in range (cantidad):
    coordenadax=float(input("Ingresar coordenada x"))
    coordenaday=float(input("Ingresar coordenada y"))
    if coordenadax>0 and coordenaday>0:
        primero=primero+1
    else:
        if coordenadax<0 and coordenaday>0:
            segundo=segundo+1
        else:
            if coordenadax<0 and coordenaday<0:
                tercero=tercero+1
            else:
                if coordenadax>0 and coordenaday<0:
                    cuarto=cuarto+1
print("Se ingresaron ", primero, " puntos en el plano en el primer cuadrante ,", segundo, " puntos en el segundo cuadrante ,", tercero, " puntos en el tercer cuadrante y ", cuarto, " puntos en el cuarto cuadrante")

