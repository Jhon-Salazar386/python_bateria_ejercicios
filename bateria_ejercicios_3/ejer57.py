trabajadores = int(input("Ingresa la cantidad de trabajadores: "))
precio_hora = int(input("Ingresa el sueldo por hora: "))

total_empresa = 0

for i in range(trabajadores):

    dias = int(input(f"¿Cuántos días trabajó el trabajador {i + 1}? "))

    horas_totales = 0

    for dia in range(dias):
        horas = int(input(f"Horas trabajadas el día {dia + 1}: "))
        horas_totales += horas

    sueldo = horas_totales * precio_hora

    print("Sueldo semanal:", sueldo)

    total_empresa += sueldo

print("Total pagado por la empresa:", total_empresa)
