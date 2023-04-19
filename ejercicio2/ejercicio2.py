import random

numero_secreto = random.randint(1, 20)
intentos = 0

while intentos < 3:
    intento = int(input("Adivina el número (entre 1 y 20): "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Felicidades, adivinaste el número en", intentos, "intentos!")
        break
    else:
        print("Ese no es el número. Intenta de nuevo.")

if intentos == 3:
    print("Lo siento, has agotado tus intentos. El número secreto era", numero_secreto)
