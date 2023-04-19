numeros = [2, 5, 7, 10, 8, 6, 11, 15]
pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("La lista tiene", pares, "números pares y", impares, "números impares")
