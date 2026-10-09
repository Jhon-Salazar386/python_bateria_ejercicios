meses = 12

dinero_ahorrado = 0

for i in range(meses):
    contador = i + 1
    dinero_mes = int(input(f"Ingresa dinero del mes {contador} "))
    dinero_ahorrado += dinero_mes
    print("Dinero ahorrado: ", dinero_ahorrado)