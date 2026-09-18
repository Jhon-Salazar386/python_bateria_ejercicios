hh = int(input("Ingrese la hora "))
mm = int(input("Ingrese los minutos "))
ss = int(input("Ingrese los segundos "))

t = int(input("Ingresa el tiempo de viaje en segundos "))

segundos_salida = hh * 3600 + mm * 60 + ss

segundos_llegada = segundos_salida + t

hora = (segundos_llegada // 3600) % 24
minutos = (segundos_llegada % 3600) // 60
segundos = segundos_llegada % 60

print("La hora de llegada es = HH =", hora, " MM=", minutos, " SS=", segundos)