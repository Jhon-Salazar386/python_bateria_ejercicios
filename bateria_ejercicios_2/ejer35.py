alumnos = int(input("introduce el número de alumnos: "))

if alumnos >= 100:
    precio = 65
    total = alumnos * precio
elif alumnos >= 50:
    precio = 70
    total = alumnos * precio
elif alumnos >= 30:
    precio = 95
    total = alumnos * precio
else:
    total = 4000
    precio = total / alumnos

print("cada alumno debe pagar:", precio, "euros")
print("la compañía de autobuses debe recibir:", total, "euros")
