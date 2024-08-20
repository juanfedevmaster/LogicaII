class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.V = [None] * capacidad
        self.primero = self.final = -1

    def cola_vacia_circular(self):
        return self.primero == -1

    def cola_llena_circular(self):
        return self.primero == (self.final + 1) % self.capacidad

    def encolar_circular(self, valor):
        if self.cola_llena_circular():
            print(" Cola Llena ")
            return
        else:
            if self.cola_vacia_circular():
                self.primero = 0
            self.final = (self.final + 1) % self.capacidad
            self.V[self.final] = valor

    def desencolar_circular(self):
        if self.cola_vacia_circular():
            print(" Cola Vacia ")
            return None
        valor_a_eliminar = self.V[self.primero]
        if self.primero == self.final:
            self.primero = self.final = -1
        else:
            self.primero = (self.primero + 1) % self.capacidad
        return valor_a_eliminar

    def imprimir_circular(self):
        if self.cola_vacia_circular():
            print(" Cola vacia ")
        else:
            Vector = []
            print(" Cola Circular :")
            for valor in self.V:
                Vector.append(valor)
            print(Vector)

    def imprimir_cola_actualizada(self):
        if self.cola_vacia_circular():
            print(" Cola vacia ")
        else:
            vector = []
            print(" Cola Circular :")
            i = self.primero
            while True:
                vector.append(self.V[i])
                if i == self.final:
                    break
                i = (i + 1) % self.capacidad
        print(vector)


cola = ColaCircular(7)

cola.encolar_circular(1)
cola.encolar_circular(2)
cola.encolar_circular(3)
cola.encolar_circular(4)
cola.encolar_circular(5)
cola.encolar_circular(6)
cola.encolar_circular(7)
cola.encolar_circular(8)

cola.desencolar_circular()
cola.desencolar_circular()

cola.imprimir_cola_actualizada()
