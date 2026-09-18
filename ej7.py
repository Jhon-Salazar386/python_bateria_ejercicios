minutos = int(input("Escribe la cantidad de minutos que quieres transformar"))
horas = 0
paso = False

while not paso:
    if minutos >= 60:
        minutos -= 60
        horas += 1
    else:
        paso = True

print("Son: " + str(horas) + " hora y " + str(minutos) + " minutos")