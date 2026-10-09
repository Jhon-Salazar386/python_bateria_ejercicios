trabajadores = int(input("Ingresa la cantidad de trabajadores: "))
precio_hora = int(input("Ingresa el sueldo por hora: "))

total_empresa = 0

for i in range(trabajadores):

    horas = int(input(f"Ingresa las horas trabajadas por el trabajador {i + 1}: "))

    sueldo = horas * precio_hora

    print(f"Sueldo del trabajador {i + 1}: {sueldo}")

    total_empresa += sueldo

print("Total pagado por la empresa:", total_empresa)
