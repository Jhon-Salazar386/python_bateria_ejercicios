moneda2 = int(input("Cuantas monedas de 2 euros tienes "))
moneda1 = int(input("Cuantas monedas de 1 euro tienes "))

centimos50 = int(input("Cuantas monedas de 50 centimos tienes "))
centimos20 = int(input("Cuantas monedas de 20 centimos tienes"))
centimos10 = int(input("Cuantas monedas de 10 centimos tienes"))

centimos = (moneda2 * 200) + (moneda1 * 100) + (centimos50 * 50) + (centimos20 * 20) + (centimos10 * 10)

total_euros = centimos // 100

total_centimos = centimos % 100

print(" Total euros = ", total_euros, " Total centimos = ", total_centimos)


