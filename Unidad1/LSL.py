class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __del__(self):
        print(f"{self.valor} ha sido recolectado.")


class LSL:
    def __init__(self):
        self.inicio = None

    def insertar_valor(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.inicio is None:
            self.inicio = nuevo_nodo
        else:
            nodo_actual = self.inicio
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

    def eliminar_elemento_lista(self, valor_buscado):
        nodo_actual = self.inicio
        if nodo_actual is None:
            return
        if nodo_actual.siguiente is None and nodo_actual.valor is valor_buscado:
            nodo_actual = None

        else:
            nodo_anterior = None
            while nodo_actual.valor is not valor_buscado:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente

            nodo_anterior.siguiente = nodo_actual.siguiente


lista = LSL()

lista.insertar_valor(5)
lista.insertar_valor(10)
lista.insertar_valor(15)
lista.insertar_valor(20)
lista.imprimir_lista()
print('===========================')
lista.eliminar_elemento_lista(15)
print('===========================')
lista.imprimir_lista()
print('===========================')
