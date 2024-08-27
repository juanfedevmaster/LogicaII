class Pila:
    def __init__(self, tam):
        self.V = []
        self.cima = 0
        self.tam = tam

    def pila_vacia(self):
        if self.cima == 0:
            return True
        else:
            return False

    def pila_llena(self):
        if self.cima == self.tam - 1:
            return True
        else:
            return False

    def cima(self):
        if self.pila_llena() is True:
            print("La pila esta llena")
            return None
        return self.V[self.cima]

    def apilar(self, valor):
        if self.pila_llena() is True:
            print("La pila esta llena")
            return
        self.cima = self.cima + 1
        self.V.append(valor)

    def desapilar(self):
        if self.pila_vacia() is True:
            print("La pila esta Vacia")
            return None

        self.cima = self.cima - 1
        valor_eliminar = self.V[self.cima]
        self.V.pop(self.cima)

        return valor_eliminar

# pila = Pila(10)
# pila.apilar(1)
# pila.apilar(2)
# pila.apilar(3)
# pila.apilar(4)
# pila.apilar(5)
# pila.apilar(6)
# pila.apilar(7)
# pila.apilar(8)
# pila.apilar(9)
# pila.apilar(10)

# print(f"Desapilando: {pila.desapilar()}")
# print(f"Desapilando: {pila.desapilar()}")
# print(f"Desapilando: {pila.desapilar()}")

# print(pila.V)
