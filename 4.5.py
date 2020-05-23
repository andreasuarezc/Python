coordenada1=float(input("Ingresar la coordenada x"))
coordenada2=float(input("Ingresar la coordenada y"))
if coordenada1>0 and coordenada2>0:
    print("El punto se ubica en el primer cuadrante")
else:
    if coordenada1<0 and coordenada2>0:
        print("El punto se ubica en el segundo cuadrante")
    else:
        if coordenada1<0 and coordenada2<0:
            print("El punto se ubica en el tercer cuadrante")
        else:
            if coordenada1>0 and coordenada2<0:
                print("El punto se ubica en el cuarto cuadrante")
