horas = 0
minutos = 0
segundos = 0

while (True) :

    while (segundos < 60):
        print(f"{horas:0>2}-{minutos:0>2}-{segundos:0>2}")
        segundos += 1

    segundos = 0
    minutos += 1

    if(minutos >= 60):
        minutos = 0
        horas += 1

    if(horas >= 24):
        horas = 0