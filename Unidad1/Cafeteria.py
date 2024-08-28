from ColaNoCircular import ColaNoCircular


class Cafeteria:
    def __init__(self):
        self.cola = ColaNoCircular(100)

    def hacer_pedido(self, pedido):
        self.cola.encolar_no_circular(pedido)
        print(f"El pedido {pedido} esta en estado pendiente")

    def atender_pedido(self):
        pedido = self.cola.desencolar_no_circular()
        if pedido is not None:
            print(f"El pedido: {pedido} ya esta listo")
        else:
            print("No hay mas pedidos para atender.")

    def menu_cafeteria(self):
        print(f"++++++++++++++++++++++++++++++")
        print(f"+++++++++Cafeteria++++++++++++")
        print(f"++++++++++++++++++++++++++++++")
        print(f"1. Cafe Expresso")
        print(f"2. Cafe Americano")
        print(f"3. Cafe Late")
        print(f"4. Atender Pedido")
        print(f"5. Salir")

        opcion = input("Ingrese la opcion deseada: ")

        return opcion


cafeteria = Cafeteria()

while True:
    opcion = cafeteria.menu_cafeteria()

    match opcion:
        case "1":
            cafeteria.hacer_pedido("Cafe Expresso")
        case "2":
            cafeteria.hacer_pedido("Cafe Americano")
        case "3":
            cafeteria.hacer_pedido("Cafe Late")
        case "4":
            cafeteria.atender_pedido()
        case _:
            break
