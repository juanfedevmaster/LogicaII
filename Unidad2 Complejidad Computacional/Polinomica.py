def sumar_elementos(elementos):
    result = 0  # O(1)
    for i in range(0, len(elementos)):  # O(n)
        result = result + elementos[i]  # O(n)

    return result  # O(1)


def incremento_variables():
    n = 100  # O(1)
    m = 80  # O(1)
    i = 0  # O(1)
    j = 0  # O(1)

    while i <= n:  # O(n + 1)
        i = i + 1  # O(n)

    while j <= m:  # O(n + 1)
        j = j + 1  # O(n)


elementos = [12, 23, 43, 56, 23, 65, 14]
print(f"El resultado de la sumatoria de los elementos es: {sumar_elementos(elementos)}")
