# Un servicio de integración se ejecuta periódicamente para recuperar los IDs de clientes que están
# asociados a cuatro o más empresas registradas en una casa matriz. El proceso realiza consultas
# individualmente para cada empresa, accediendo a diversas bases de datos que utilizan distintas
# tecnologías de persistencia. Como resultado, se genera un array de datos que contiene los IDs de
# los clientes, sin verificar ni eliminar posibles duplicados.

def eliminar_duplicados(array):
    result = []
    for i in range(0, len(array)):
        duplicate = False
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                duplicate = True
                break

        if duplicate is False:
            result.append(array[i])

    return result


def eliminar_duplicados_optimizado(array2):
    result2 = set()
    for item in array2:
        if (item in result2) is False:
            result2.add(item)
    return result2


array = [1, 2, 3, 3, 4, 5, 8, 7, 9, 12, 10, 10, 14, 25, 4, 58]
print(array)
result = eliminar_duplicados(array)
print(result)
result2 = eliminar_duplicados_optimizado(array)
print(result2)
