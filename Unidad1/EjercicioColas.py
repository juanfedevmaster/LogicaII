from ColaNoCircular import ColaNoCircular


class Cafeteria:
    def __init__(self):
        # Cola de máximo 100 pedidos.
        self.cola = ColaNoCircular(100)

    def imprimir_menu(self):
        while True:
            print(f"++++++++++++++++++++++++++++")
            print(f"1. Cafe expresso.")
            print(f"2. Cafe Late.")
            print(f"3. Cafe Americano.")
            print(f"4. Procesar Pedido")
            print(f"5. Salir")
            print(f"++++++++++++++++++++++++++++")

            opcion = input("ingrese la opcion deseada: ")

            if opcion == '1':
                self.cola.encolar_no_circular("Cafe Expresso")
            elif opcion == '2':
                self.cola.encolar_no_circular("Cafe Late")
            elif opcion == '3':
                self.cola.encolar_no_circular("Cafe Americano")
            elif opcion == '4':
                pedido = self.cola.desencolar_no_circular()
                if pedido is not None:
                    print(f"Pedido procesado: {pedido}")
            else:
                print("Gracias por la visita")
                return


cafeteria = Cafeteria()
cafeteria.imprimir_menu()

