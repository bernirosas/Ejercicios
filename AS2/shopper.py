from threading import Thread, Event
from time import sleep
from random import randint


class Shopper(Thread):

    evento_disponible = Event()

    def __init__(self, nombre, velocidad):
        # No Modificar
        super().__init__()
        self.posicion = 0
        self.distancia_tienda = 0
        self.distancia_destino = 0
        self.pedido_actual = None
        self.termino_jornada = False
        # COMPLETAR DESDE AQUI
        self.nombre = nombre
        self.velocidad = velocidad

    @property
    def ocupado(self):
        # No Modificar
        if self.pedido_actual:
            return True
        return False

    def asignar_pedido(self, pedido):
        # No Modificar
        print(f"Asignando pedido {pedido.id_} a {self.nombre}...")
        self.distancia_tienda = randint(1, 10)
        self.distancia_destino = self.distancia_tienda +\
            pedido.distancia_destino
        self.pedido_actual = pedido
        self.posicion = 0
        print(f"El pedido {pedido.id_} fue asignado a {self.nombre}")

    def avanzar(self):
        self.posicion += 1
        sleep(1/self.velocidad)
        print(f"{self.nombre} avanzó una posición hasta {self.posicion}")

    def run(self):
        while self.termino_jornada is False:
            while self.pedido_actual:
                self.avanzar()
                if self.posicion == self.distancia_tienda:
                    print("Se llego a la tienda")
                    self.pedido_actual.evento_llego_repartidor.set()
                    print(f"Esperando pedido...{self.pedido_actual.id_}")
                    self.pedido_actual.evento_pedido_listo.wait()
                    print("Pedido listo.")
                if self.posicion == self.distancia_destino:
                    print(f"{self.nombre} ha entregado el pedido")
                    self.pedido_actual.entregado = True
                    Shopper.evento_disponible.set()
                    self.posicion = 0
                    self.pedido_actual = None


if __name__ == "__main__":
    pass
