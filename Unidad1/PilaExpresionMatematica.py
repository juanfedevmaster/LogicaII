class Pila:
    def __init__(self, tam):
        self.V = []
        self.cima = -1
        self.tam = tam

    def pila_vacia(self):
        if self.cima < 0:
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

        valor_eliminar = self.V.pop(self.cima)
        self.cima = self.cima - 1
        return valor_eliminar

    def expresion_balanceada(self, expresion):
        for caracter in expresion:
            if caracter == '(':
                self.apilar(caracter)
            elif caracter == ')':
                if self.pila_vacia():
                    return False
                self.desapilar()

        return self.pila_vacia()


expression1 = "(5 + 3) * (2 + 4)"
expression2 = "(5 + 3 * (2 + 4)"
expression3 = "((5 + 3) * 2) + 4)"
expression4 = "((5 + 3) * (2 + 4))"

pila = Pila(len(expression1))
print(f"'{expression1}' está balanceada: {pila.expresion_balanceada(expression1)}")

pila = Pila(len(expression2))
print(f"'{expression2}' está balanceada: {pila.expresion_balanceada(expression2)}")

pila = Pila(len(expression3))
print(f"'{expression3}' está balanceada: {pila.expresion_balanceada(expression3)}")

pila = Pila(len(expression4))
print(f"'{expression4}' está balanceada: {pila.expresion_balanceada(expression4)}")
