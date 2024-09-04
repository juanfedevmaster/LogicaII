import random


def buscar_elemento(array, elemento):
    for i in range(len(array)):
        if array[i] == elemento:
            return i
    return -1


array = [37, 93, 71, 90, 85, 55, 13, 82, 22, 3, 26, 4, 11, 54, 71, 12, 6, 53, 62, 24]
resultado = buscar_elemento(array, 37)

if resultado >= 0:
    print(f"El elemento se encontro en la posición: {resultado}")

resultado = buscar_elemento(array, 24)
if resultado >= 0:
    print(f"El elemento se encontro en la posición: {resultado}")
