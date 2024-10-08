# Un servicio de integración se ejecuta periódicamente para recuperar los IDs de clientes que están
# asociados a cuatro o más empresas registradas en una casa matriz. El proceso realiza consultas
# individualmente para cada empresa, accediendo a diversas bases de datos que utilizan distintas
# tecnologías de persistencia. Como resultado, se genera un array de datos que contiene los IDs de
# los clientes, sin verificar ni eliminar posibles duplicados.

def eliminar_duplicados(array):
    result = []
    for i in range(0, len(array)):          # O(n)
        duplicate = False                   # O(1)
        for j in range(i + 1, len(array)):  # O(nx(n-i-1))
            if array[i] == array[j]:        # O(nxn)
                duplicate = True            # O(nxn)
                break                       # O(nxn)

        if duplicate is False:              # O(n)
            result.append(array[i])         # O(n)

    return result                           # O(1)


def eliminar_duplicados_optimizado(array2):
    result2 = set()
    for item in array2:  # O(n)
        if (item in result2) is False:  # O(n)
            result2.add(item)  # O(n)
    return result2  # O(1)


array = [1, 2, 3, 3, 4, 5, 8, 7, 9, 12, 10, 10, 14, 25, 4, 58]
print(array)
result = eliminar_duplicados(array)
print(result)
# result2 = eliminar_duplicados_optimizado(array)
# print(result2)
