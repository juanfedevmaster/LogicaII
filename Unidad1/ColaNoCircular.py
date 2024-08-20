class ColaNoCircular:
    def __init__(self, m):
        self.capacidad = m  # Capacidad de la cola
        self.V = []

    def cola_vacia(self):
        return len(self.V) == 0

    def cola_llena(self):
        return len(self.V) == self.capacidad

    def encolar_no_circular(self, valor):
        if self.cola_llena():
            print(" Cola llena ")
            return
        else:
            self.V.append(valor)

    def desencolar_no_circular(self):
        if self.cola_vacia():
            print(" Cola vacia ")
            return None
        else:
            return self.V.pop(0)  # remueve el elemento en posicion 0

    def imprimir_no_circular(self):
        if self.cola_vacia():
            print(" Cola vacia ")
        else:
            Vector = []
            print(" Cola No circular :")
            for valor in self.V:
                Vector.append(valor)
            print(Vector)


cola = ColaNoCircular(7)

cola.encolar_no_circular(1)
cola.encolar_no_circular(2)
cola.encolar_no_circular(3)
cola.encolar_no_circular(4)
cola.encolar_no_circular(5)
cola.encolar_no_circular(6)
cola.encolar_no_circular(7)
cola.encolar_no_circular(8)

cola.imprimir_no_circular()
cola.desencolar_no_circular()
cola.desencolar_no_circular()
cola.desencolar_no_circular()
cola.imprimir_no_circular()
