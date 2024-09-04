import math
import time

import numba


@numba.jit
def numero_primo_primero(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


@numba.jit
def numero_primo_segundo(n):
    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False
    return True


@numba.jit
def numero_primo_tercero(n):
    if n % 2:
        return False

    for i in range(3, int(n / 2), 2):
        if n % i == 0:
            return False
    return True


@numba.jit
def numero_primo_cuarto(n):
    n2 = math.sqrt(int(n / 2))

    if n % 2:
        return False

    for i in range(3, n2, 2):
        if n % i == 0:
            return False
    return True


inicio = time.time()
# resultado = numero_primo_primero(2147483647)
# resultado = numero_primo_segundo(2147483647)
# resultado = numero_primo_tercero(2147483647)
resultado = numero_primo_cuarto(2147483647)
fin = time.time()

if resultado is True:
    print(f"El número es primo")
else:
    print(f"El número no es primo")

print(f"Tiempo de ejecución: {fin - inicio}")
