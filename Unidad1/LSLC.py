class Nodo:
    def __init__(self, parametro):
        self.valor = parametro
        self.siguiete = None

    def __del__(self):
        print(f"{self.valor} eliminado por el GC")


class LSLC:
    def __init__(self):
        self.cabecera = None

    def __del__(self):
        print(f"La lista se elimino correctamente")

    def insertar_nuevo_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            nuevo_nodo.siguiete = nuevo_nodo
            self.cabecera = nuevo_nodo
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiete is not self.cabecera:
                nodo_actual = nodo_actual.siguiete

            nuevo_nodo.siguiete = self.cabecera
            nodo_actual.siguiete = nuevo_nodo

    def imprimir_lista(self):
        if self.cabecera is None:
            print("La lista esta vacia")
        else:
            nodo_actual = self.cabecera

            while True:
                print(f"Valor nodo: {nodo_actual.valor}")
                if nodo_actual.siguiete is self.cabecera:
                    break
                else:
                    nodo_actual = nodo_actual.siguiete

    def eliminar_primer_elemento(self):
        if self.cabecera is None:
            print("La lista esta vacia")
            return

        if self.cabecera.siguiete is self.cabecera:
            self.cabecera = None
            print("Se elimino el primer elemento de la lista")
            return

        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiete is not self.cabecera:
                nodo_actual = nodo_actual.siguiete

            self.cabecera = self.cabecera.siguiete
            nodo_actual.siguiete = self.cabecera


lista = LSLC()
lista.insertar_nuevo_nodo(5)
lista.insertar_nuevo_nodo(10)
lista.insertar_nuevo_nodo(25)

lista.imprimir_lista()
print("====================")
lista.eliminar_primer_elemento()
print("====================")

