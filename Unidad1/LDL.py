class Nodo:
    def __init__(self, valor):
        self.siguiente = None
        self.anterior = None
        self.valor = valor


class LDL:
    def __init__(self):
        self.cabecera = None
        self.cola = None

    def insertar_al_inicio_ldl(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cabecera is None:
            self.cabecera = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabecera
            self.cabecera.anterior = nuevo_nodo
            self.cabecera = nuevo_nodo

    def insertar_al_final_ldl(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cola is None:
            self.cabecera = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def insertar_por_posicion_ldl(self, valor, pos):
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
            self.cola = nuevo_nodo
        elif pos <= 1:
            nuevo_nodo.siguiente = self.cabecera
            self.cabecera.anterior = nuevo_nodo
            self.cabecera = nuevo_nodo
        else:
            nodo_actual = self.cabecera
            i = 1
            while (nodo_actual is not None) and (i < pos):
                nodo_actual = nodo_actual.siguiente
                i = i + 1
            if i == pos and nodo_actual is None:  # Como no encontro la posición deseada se inserta al final.
                self.cola.siguiente = nuevo_nodo
                nuevo_nodo.anterior = self.cola
                self.cola = nuevo_nodo
            elif nodo_actual is None:
                print("No puede insertar un valor en una posición mayor al tamaño de la lista")
            elif i == pos and nodo_actual is not None:
                nodo_anterior = nodo_actual.anterior
                nodo_anterior.siguiente = nuevo_nodo
                nuevo_nodo.anterior = nodo_anterior
                nuevo_nodo.siguiente = nodo_actual
                nodo_actual.anterior = nuevo_nodo

    def imprimir_lista(self):
        if self.cabecera is None:
            print("La lista esta vacia")
        else:
            nodo_actual = self.cabecera

            while True:
                if nodo_actual is None:
                    break
                else:
                    print(f"Valor nodo: {nodo_actual.valor}")
                    nodo_actual = nodo_actual.siguiente

    def eliminar_nodo_ldl(self, valor):
        if self.cabecera is None:
            print("La lista esta vacia")
        else:
            nodo_actual = self.cabecera
            while nodo_actual is not None:
                if nodo_actual.valor == valor:
                    break
                nodo_actual = nodo_actual.siguiente

            if nodo_actual is None:
                print("No se encontro el valor en la lista")
                return

            if nodo_actual == self.cabecera:
                self.cabecera = self.cabecera.siguiente
                self.cabecera.anterior = None
                nodo_actual.siguiente = None
            elif nodo_actual == self.cola:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
                nodo_actual.anterior = None
            else:
                nodo_anterior = nodo_actual.anterior
                nodo_siguiente = nodo_actual.siguiente

                nodo_anterior.siguiente = nodo_siguiente
                nodo_siguiente.anterior = nodo_anterior


lista = LDL()

lista.insertar_al_final_ldl(1)
lista.insertar_al_final_ldl(2)
lista.insertar_al_final_ldl(3)
lista.insertar_al_final_ldl(4)

lista.insertar_por_posicion_ldl(10, 5)
lista.imprimir_lista()
print("=======================")
lista.eliminar_nodo_ldl(10)
lista.imprimir_lista()
