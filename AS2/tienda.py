from threading import Thread, Lock
from time import sleep
from random import randint


class Tienda(Thread):
    def __init__(self, nombre):
        # NO MODIFICAR
        super().__init__()
        self.nombre = nombre
        self.cola_pedidos = []
        self.abierta = True
        self.candado = Lock()
        # COMPLETAR DESDE AQUI

    def ingresar_pedido(self, pedido, shopper):
        with self.candado:
            self.cola_pedidos.append((pedido, shopper))

    def preparar_pedido(self, pedido):
        num = randint(1, 10)
        print(f"El pedido {pedido.id_} se demorara {num}")
        sleep(num)
        print(f"Pedido {pedido.id_} preparado con éxito")

    def run(self):
        while self.abierta:
            if len(self.cola_pedidos) >= 1:
                with self.candado:
                    seleccionado = self.cola_pedidos.pop(0)
                self.preparar_pedido(seleccionado[0])
                seleccionado[0].evento_pedido_listo.set()
                seleccionado[0].evento_llego_repartidor.wait()
                print("Pedido retirado")
            else:
                print("No hay pedidos")
                num = randint(1, 5)
                sleep(num)
