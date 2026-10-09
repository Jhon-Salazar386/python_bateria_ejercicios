dias_laborables = 6

sueldo_base = int(input("Ingresa sueldo base por horas del empleado "))

horas_trabajadas = 0

for i in range(dias_laborables):
    
    horas = int(input(f"Ingresa las horas trabajadas {i + 1} "))
    
    horas_trabajadas += horas


print("Horas trabajadas: ", horas_trabajadas)
print("Paga por la semana: ", (sueldo_base * horas_trabajadas))