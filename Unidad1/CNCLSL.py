class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class CNCLSL:
    def __init__(self):
        self.primero = None
        self.final = None

    def encolar_CNCLSL(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar_CNCLSL(self):
        if self.primero is None:
            return None

        nodo_desencolar = self.primero
        self.primero = nodo_desencolar.siguiente
        if self.primero is None:
            self.final = None
        return nodo_desencolar.valor

    def imprimir_CNCLSL(self):
        nodo_actual = self.primero
        while nodo_actual:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print(" None ")


cola = CNCLSL()

cola.encolar_CNCLSL(1)
cola.encolar_CNCLSL(2)
cola.encolar_CNCLSL(3)
cola.encolar_CNCLSL(4)
cola.encolar_CNCLSL(5)

cola.imprimir_CNCLSL()
cola.desencolar_CNCLSL()
cola.imprimir_CNCLSL()
