from parametros import VIDA_PEKKA, RECUPERACION_VIDA_PEKKA, ORO_INICIAL, \
    PONDERADOR_BARBAROS
from threading import Lock


class CentroUrbano:

    def __init__(self) -> None:
        self.oro = ORO_INICIAL
        self.chozas = 0
        self.candado_oro = Lock()
        self.candado_choza = Lock()

    @property
    def barbaros(self) -> int:
        return int(self.chozas * PONDERADOR_BARBAROS)
