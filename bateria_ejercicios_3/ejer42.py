print("ADIVINA EL NUMERO")

intentos = 10
intentos_fallido = 0

num_secret = 25

print(num_secret)

while intentos > 0:

    numero = int(input("Intenta adivinar el numero: "))

    if(numero == num_secret):
        print(f"Has adivinado, era {num_secret}")
        print(f"numero de intentos fallidos = {intentos_fallido}")
        break
    else:
        print("Es incorrecto")
        intentos -= 1
        intentos_fallido += 1

if(intentos == 0):
    print(f"Has fallado, el numero era {num_secret}")
