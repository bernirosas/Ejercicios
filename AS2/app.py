from random import randint
from time import sleep
from pedido import Pedido
from shopper import Shopper
from threading import Thread


class DCComidApp(Thread):

    def __init__(self, shoppers, tiendas, pedidos):
        # NO MODIFICAR
        super().__init__()
        self.shoppers = shoppers
        self.pedidos = pedidos
        self.tiendas = tiendas

    def obtener_shopper(self):
        for shopper in self.shoppers:
            if not shopper.ocupado:
                return shopper
        print("Todos los shoppers están ocupados")
        Shopper.evento_disponible.wait()
        print("Se desocupó un shopper :)")
        Shopper.evento_disponible.clear()
        return self.obtener_shopper()

    def run(self):
        while len(self.pedidos) >= 1:
            pedido = self.pedidos.pop(0)
            tienda_elegida = self.tiendas[pedido[1]]
            pedido = Pedido(*pedido)
            shopper = self.obtener_shopper()
            shopper.asignar_pedido(pedido)
            tienda_elegida.ingresar_pedido(pedido, shopper)
            num = randint(1, 5)
            sleep(num)





if __name__ == '__main__':
    pass
