dia = int(input("Ingresa el dia"))
mes = int(input("Ingresa el mes"))
anio = int(input("Ingresa el año"))

if(dia <= 31):
    if(mes <= 12 and mes != 2):
        print("la fecha es correcta ")
    elif(anio % 4 == 0 and mes == 2 and dia <= 29):
        print("La fecha es corresca, el año fue bisiesto")
    else:
        print("La fecha es incorrecta")
else:
    print("La fecha es incorrecta")