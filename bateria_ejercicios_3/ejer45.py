VOCALES = ["a", "e", "i", "o", "u",]

while True:

    letra = input("Ingresa una letra(Dejar en blanco para terminar): ")
    
    if(letra == ""):
        print("Saliendo")
        break
    elif(letra.lower() in VOCALES):
        print("VOCAL")
    else:
        print("NO VOCAL")