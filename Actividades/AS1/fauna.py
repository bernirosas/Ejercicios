from random import randint
from parametros import INCREMENTO_FEROCIDAD, MAX_EX_CARNIVORO, MAX_EX_HERVIBORO, \
                        MIN_EX_CARNIVORO, MIN_EX_HERVIBORO, INCREMENTO_ADORABILIDAD, \
                        GAN_CARNIVORO, GAN_HERBIVORO
from abc import ABC, abstractmethod


# MODIFICAR
class Animal(ABC):

    # MODIFICAR
    def __init__(self, especie, **kwargs):
        self.especie = especie
        self.ganancia_actual = 0

    @abstractmethod
    def alimentarse(self):
        pass

    @abstractmethod
    def exhibicion(self):
        pass

    def __str__(self):
        return f"Animal de especie {self.especie}"


# MODIFICAR
class Carnivoro(Animal):

    # MODIFICAR
    def __init__(self, ferocidad, **kwargs):
        super().__init__(**kwargs) # revisar si funciona
        self.ferocidad = ferocidad
        self.ganancia_actual += GAN_CARNIVORO

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()
        self.ferocidad += INCREMENTO_FEROCIDAD
        print(f"Animal {self.especie} se come un kilogramo de Carne")

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()
        nro_al_azar = randint(MIN_EX_CARNIVORO, MAX_EX_CARNIVORO)
        incremento = self.ferocidad*nro_al_azar
        self.ganancia_actual += incremento


# MODIFICAR
class Herbivoro(Animal):

    # MODIFICAR
    def __init__(self, adorabilidad, **kwargs):
        super().__init__(**kwargs)  # revisar si funciona
        self.adorabilidad = adorabilidad
        self.ganancia_actual += GAN_HERBIVORO

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()
        self.adorabilidad += INCREMENTO_ADORABILIDAD
        print(f"Animal {self.especie} se come un kilogramo de vegetales")

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()
        nro_random = randint(MIN_EX_HERVIBORO, MAX_EX_HERVIBORO)
        incremento = self.adorabilidad*nro_random 
        self.ganancia_actual += incremento


# MODIFICAR
class Omnivoro(Carnivoro, Herbivoro):

    # MODIFICAR
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()
