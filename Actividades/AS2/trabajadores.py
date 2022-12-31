from time import sleep
from threading import Thread

from centro_urbano import CentroUrbano

from parametros import ENERGIA_RECOLECTOR, ORO_RECOLECTADO, \
    TIEMPO_RECOLECCION, TIEMPO_CONSTRUCCION, ORO_CHOZA


# Completar
class Recolector(Thread):

    def __init__(self, nombre: str, centro_urbano: CentroUrbano) -> None:
        super().__init__()
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        self.energia = ENERGIA_RECOLECTOR
        self.oro = 0
        self.daemon = True

    def run(self) -> None:
        self.trabajar()
        self.ingresar_oro()
        self.dormir()

    def log(self, mensage: str) -> None:
        print(f"El recolector {self.nombre}: {mensage}")

    def trabajar(self) -> None:
        self.log("Ha comenzado a trabajar")
        while self.energia > 0:
            self.oro += ORO_RECOLECTADO
            self.log(f"{self.nombre} recolectó {ORO_RECOLECTADO} de oro.")
            self.energia -= 1
            sleep(TIEMPO_RECOLECCION)

    def ingresar_oro(self) -> None:
        with self.centro_urbano.candado_oro:
            self.centro_urbano.oro += self.oro
            self.oro = 0
            self.log("Depositó el oro disponible")
            self.log(f"El oro total quedó en {self.centro_urbano.oro}.")

    def dormir(self) -> None:
        self.log("ha terminado su turno, procede a mimir")


# Completar
class Constructor(Thread):

    def __init__(self, nombre, centro_urbano: CentroUrbano) -> None:
        super().__init__()
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        self.daemon = True

    def run(self) -> None:
        while self.retirar_oro():
            self.log("está construyendo una choza de bárbaros")
            sleep(TIEMPO_CONSTRUCCION)
            self.construir_choza()
        self.log("terminó su trabajo por el día")

    def log(self, mensage: str) -> None:
        print(f"El constructor {self.nombre}: {mensage}")

    def retirar_oro(self) -> bool:
        with self.centro_urbano.candado_oro:
            if self.centro_urbano.oro >= ORO_CHOZA:
                self.centro_urbano.oro -= ORO_CHOZA
                self.log(f"Se construye una choza quedando {self.centro_urbano.oro} de oro en el centro urbano")
                return True
        self.log("No se encontró suficiente oro para construir una choza.")
        return False

    def construir_choza(self) -> None:
        with self.centro_urbano.candado_choza:
            self.centro_urbano.chozas += 1
            self.log(f"Se creó una choza. Las chozas totales son {self.centro_urbano.chozas}.")
