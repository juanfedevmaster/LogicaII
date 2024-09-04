def busqueda_binaria(lista, elemento):
    bajo = 0  # O(1)
    alto = len(lista) - 1  # O(1)

    while bajo <= alto:  # O(log n)
        medio = (bajo + alto) // 2  # O(log n)
        guess = lista[medio]  # O(log n)

        if guess == elemento:  # O(log n)
            return medio  # O(log n)
        if guess > elemento:  # O(log n)
            alto = medio - 1  # O(log n)
        else:
            bajo = medio + 1  # O(log n)

    return None  # O(1)


lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
elemento_a_buscar = 14

indice = busqueda_binaria(lista_ordenada, elemento_a_buscar)
if indice is not None:
    print(f"Elemento encontrado en el índice {indice} - valor: {lista_ordenada[6]}")
else:
    print("Elemento no encontrado")
