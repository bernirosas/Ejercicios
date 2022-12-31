from abc import ABC, abstractmethod
from parametros import AUMENTO_DEFENSA, GASTO_ENERGIA_BAYA,\
                       GASTO_ENERGIA_CARAMELO,\
                       GASTO_ENERGIA_POCION, PROB_EXITO_BAYA,\
                       PROB_EXITO_CARAMELO, PROB_EXITO_POCION
from random import randint


class objeto(ABC):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.prob_exito = 0  # para sobreecribir
        self.costo = 0  # para sobreescribir

    @abstractmethod
    def aplicar_objeto(self, programon):
        pass

    def __repr__(self):
        return (f"Nombre: {self.nombre}\n"
                f"objeto tipo {self.tipo} tiene probabilidad de exito de "
                f"{self.prob_exito}")


class baya(objeto):
    def __init__(self, *args):
        super().__init__(*args)
        self.prob_exito = PROB_EXITO_BAYA
        self.costo = GASTO_ENERGIA_BAYA

    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        aumento = randint(1, 10)
        programon.vida += aumento


class pocion(objeto):
    def __init__(self, *args):
        super().__init__(*args)
        self.prob_exito = PROB_EXITO_POCION
        self.costo = GASTO_ENERGIA_POCION

    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        aumento = randint(1, 7)
        programon.ataque += aumento


class caramelo(baya, pocion):
    def __init__(self, *args):
        super().__init__(*args)
        self.prob_exito = PROB_EXITO_CARAMELO
        self.costo = GASTO_ENERGIA_CARAMELO

    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        programon.defensa += AUMENTO_DEFENSA
