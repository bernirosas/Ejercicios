from parametros import MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO,\
                       MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA,\
                       AUMENTAR_VIDA_PLANTA, AUMENTAR_ATAQUE_FUEGO,\
                       AUMENTAR_VELOCIDAD_AGUA

from random import randint
from abc import ABC, abstractmethod


class Programon(ABC):
    def __init__(self, nombre, tipo, nivel, vida, ataque, defensa, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.__nivel = int(nivel)
        self.__vida = int(vida)
        self.__ataque = int(ataque)
        self.__defensa = int(defensa)
        self.__velocidad = int(velocidad)
        self.__experiencia = 0

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, nuevo_valor):
        if nuevo_valor >= 1 and nuevo_valor <= 255:
            self.__vida = nuevo_valor
        elif nuevo_valor < 1:
            self.__vida = 1
        elif nuevo_valor > 255:
            print("Vida del programon llegó al máximo")
            self.__vida = 255

    @property
    def ataque(self):
        return self.__ataque

    @ataque.setter
    def ataque(self, nuevo_valor):
        if nuevo_valor >= 5 and nuevo_valor <= 190:
            self.__ataque = nuevo_valor
        elif nuevo_valor < 5:
            self.__ataque = 5
        elif nuevo_valor > 190:
            print("Ataque del programon llegó al máximo")
            self.__ataque = 190

    @property
    def defensa(self):
        return self.__defensa

    @defensa.setter
    def defensa(self, nuevo_valor):
        if nuevo_valor >= 5 and nuevo_valor <= 250:
            self.__defensa = nuevo_valor
        elif nuevo_valor < 5:
            self.__defensa = 5
        elif nuevo_valor > 250:
            print("Defensa del programon llegó al máximo")
            self.__defensa = 250

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, nuevo_valor):
        if nuevo_valor >= 5 and nuevo_valor <= 200:
            self.__velocidad = nuevo_valor
        elif nuevo_valor < 5:
            self.__velocidad = 5
        elif nuevo_valor > 200:
            self.__velocidad = 200

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, nuevo_valor):
        if nuevo_valor >= 0 and nuevo_valor < 100:
            self.__experiencia = nuevo_valor
        elif nuevo_valor < 0:
            self.__experiencia = 0
        elif nuevo_valor >= 100:
            self.nivel += 1
            self.__experiencia = nuevo_valor - 100

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nuevo_valor):
        if nuevo_valor >= 100:
            print("Entrenamiento ya no hace efecto")
            print("Nivel máximo alcanzado")
            self.__nivel = 100
            self.__experiencia = 0
            print("La experiencia de tu programon quedó en 0")
        elif nuevo_valor >= 1:
            self.experiencia -= 100
            self.__nivel = nuevo_valor
            nro_a_subir = randint(MIN_AUMENTO_ENTRENAMIENTO,
                                  MAX_AUMENTO_ENTRENAMIENTO)
            self.vida += nro_a_subir
            print(f"Por subir de nivel, la vida de tu programon quedó"
                  f" en {self.vida}")
            nro_a_subir = randint(MIN_AUMENTO_ENTRENAMIENTO,
                                  MAX_AUMENTO_ENTRENAMIENTO)
            self.ataque += nro_a_subir
            print(f"El ataque de tu programon quedó en {self.ataque}")
            nro_a_subir = randint(MIN_AUMENTO_ENTRENAMIENTO,
                                  MAX_AUMENTO_ENTRENAMIENTO)
            self.defensa += nro_a_subir
            print(f"El defensa de tu programon quedó en {self.defensa}")
            nro_a_subir = randint(MIN_AUMENTO_ENTRENAMIENTO,
                                  MAX_AUMENTO_ENTRENAMIENTO)
            self.velocidad += nro_a_subir
            print(f"La velocidad de tu programon quedó en {self.velocidad}")
            print(f"Nuevo nivel: {self.__nivel}")

    def entrenamiento(self):
        nro_aumentar = randint(MIN_AUMENTO_EXPERIENCIA,
                               MAX_AUMENTO_EXPERIENCIA)
        self.experiencia += nro_aumentar

    @abstractmethod
    def luchar(self):
        pass

    @abstractmethod
    def aumenta_al_ganar_batalla(self):
        pass


class Programon_agua(Programon):
    def __init__(self, *args):
        super().__init__(*args)
        self.tipo_compite = ""  # cuando este en competencia es != ""

    @property
    def des_o_ventaja_contra(self):
        if self.tipo_compite == "agua":
            return 0
        elif self.tipo_compite == "planta":
            return -1
        elif self.tipo_compite == "fuego":
            return 1

    @property
    def puntaje_lucha(self):
        return max(0, (float(self.vida)*0.2 + float(self.nivel)*0.3
                       + float(self.ataque)*0.15
                       + float(self.defensa)*0.15 + float(self.velocidad)*0.2 +
                       float(self.des_o_ventaja_contra)*40))

    def luchar(self, otro_programon):
        self.tipo_compite = otro_programon.tipo
        otro_programon.tipo_compite = self.tipo
        if self.puntaje_lucha > otro_programon.puntaje_lucha:
            self.aumenta_al_ganar_batalla()
            return "gano"
        elif self.puntaje_lucha < otro_programon.puntaje_lucha:
            otro_programon.aumenta_al_ganar_batalla()
            return "pierdo"
        else:
            # se elige al azar
            opcion = randint(1, 2)
            if opcion == 1:
                self.aumenta_al_ganar_batalla()
                return "gano"
            else:
                otro_programon.aumenta_al_ganar_batalla()
                return "pierdo"

    def aumenta_al_ganar_batalla(self):
        anterior = self.velocidad
        self.velocidad += AUMENTAR_VELOCIDAD_AGUA
        print(f"Por ganar la batalla, la velocidad del programon "
              f"{self.nombre} aumenta"
              f" desde {anterior} hasta {self.velocidad}")


class Programon_planta(Programon):
    def __init__(self, *args):
        super().__init__(*args)
        self.tipo_compite = ""

    @property
    def des_o_ventaja_contra(self):
        if self.tipo_compite == "planta":
            return 0
        elif self.tipo_compite == "fuego":
            return -1
        elif self.tipo_compite == "agua":
            return 1

    @property
    def puntaje_lucha(self):
        return max(0, (float(self.vida)*0.2 + float(self.nivel)*0.3
                       + float(self.ataque)*0.15
                       + float(self.defensa)*0.15 + float(self.velocidad)*0.2 +
                       float(self.des_o_ventaja_contra)*40))

    def luchar(self, otro_programon):
        self.tipo_compite = otro_programon.tipo
        otro_programon.tipo_compite = self.tipo
        if self.puntaje_lucha > otro_programon.puntaje_lucha:
            self.aumenta_al_ganar_batalla()
            return "gano"
        elif self.puntaje_lucha < otro_programon.puntaje_lucha:
            otro_programon.aumenta_al_ganar_batalla()
            return "pierdo"
        else:
            # se elige al azar
            opcion = randint(1, 2)
            if opcion == 1:
                self.aumenta_al_ganar_batalla()
                return "gano"
            else:
                otro_programon.aumenta_al_ganar_batalla()
                return "pierdo"

    def aumenta_al_ganar_batalla(self):
        anterior = self.vida
        self.vida += AUMENTAR_VIDA_PLANTA
        print(f"Por ganar la batalla, la vida del programon "
              f"{self.nombre} aumenta"
              f" desde {anterior} hasta {self.vida}")


class Programon_fuego(Programon):
    def __init__(self, *args):
        super().__init__(*args)
        self.tipo_compite = ""

    @property
    def des_o_ventaja_contra(self):
        if self.tipo_compite == "fuego":
            return 0
        elif self.tipo_compite == "agua":
            return -1
        elif self.tipo_compite == "planta":
            return 1

    @property
    def puntaje_lucha(self):
        return max(0, (float(self.vida)*0.2 + float(self.nivel)*0.3
                       + float(self.ataque)*0.15
                       + float(self.defensa)*0.15 + float(self.velocidad)*0.2 +
                       float(self.des_o_ventaja_contra)*40))

    def luchar(self, otro_programon):
        self.tipo_compite = otro_programon.tipo
        otro_programon.tipo_compite = self.tipo
        if self.puntaje_lucha > otro_programon.puntaje_lucha:
            self.aumenta_al_ganar_batalla()
            return "gano"
        elif self.puntaje_lucha < otro_programon.puntaje_lucha:
            otro_programon.aumenta_al_ganar_batalla()
            return "pierdo"
        else:
            # se elige al azar
            opcion = randint(1, 2)
            if opcion == 1:
                self.aumenta_al_ganar_batalla()
                return "gano"
            else:
                otro_programon.aumenta_al_ganar_batalla()
                return "pierdo"

    def aumenta_al_ganar_batalla(self):
        anterior = self.ataque
        self.ataque += AUMENTAR_ATAQUE_FUEGO
        print(f"Por ganar la batalla, el ataque del programon "
              f"{self.nombre} aumenta"
              f" desde {anterior} hasta {self.ataque}")
