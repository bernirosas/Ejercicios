from abc import ABC, abstractmethod
import random


class Persona(ABC): # no olvidar poner ABC

    def __init__(self, nombre, edad, contagiado):
        # No modificar
        self.nombre = nombre
        self.edad = edad
        self.contagiado = contagiado

    @abstractmethod
    def saludar(self):
        pass


class Cliente(Persona):

    def __init__(self, nombre, edad, contagiado, nombre_local_favorito, dinero):
        super().__init__(nombre, edad, contagiado)
        self.nombre_local_favorito = nombre_local_favorito
        self.dinero = dinero
        self.saludar()

    def saludar(self):
        # No modificar
        print(f"Hola me llamo {self.nombre} y mi local favorito es {self.nombre_local_favorito}")


# Completar
class Trabajador(Persona):

    def __init__(self, nombre, edad, contagiado, sueldo, nombre_local):
        super().__init__(nombre, edad, contagiado)
        self.sueldo = sueldo
        self.contagiado = contagiado
        self.nombre_local = nombre_local
        self.saludar()

    def generar_posible_contagio(self):
        # No modificar
        # Si la probabilidad de contagio es menor a 0.1 se actualiza el atributo contagiado del
        # Trabajador a True.
        probabilidad_contagio = random.uniform(0, 1)
        if probabilidad_contagio < 0.1:
            self.contagiado = True

    def saludar(self):
        # No modificar
        print((
            f"Hola me llamo {self.nombre}, trabajo en {self.nombre_local}"
            f" y mi sueldo es {self.sueldo}"
        ))
