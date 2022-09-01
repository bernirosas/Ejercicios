from parametros import PROBABILIDAD_EVENTO, PUBLICO_EXITO, PUBLICO_INICIAL, \
                       PUBLICO_TERREMOTO, AFINIDAD_OLA_CALOR, \
                       AFINIDAD_LLUVIA, PUBLICO_OLA_CALOR
from random import random, choice, randint


class DCCPalooza:

    def __init__(self):
        self.artista_actual = ''
        self.__dia = 1
        self.line_up = []
        self.cant_publico = PUBLICO_INICIAL
        self.artistas = []
        self.prob_evento = PROBABILIDAD_EVENTO
        self.suministros = []

    @property
    def dia(self):
        return self.__dia
    

    @property
    def funcionando(self):
        return self.exito_del_concierto and self.dia <= 3

    @property
    def exito_del_concierto(self):
        return self.cant_publico >= PUBLICO_EXITO

    def imprimir_estado(self):
        print(f"Día: {self.__dia}\nCantidad de Personas: "
              f"{self.cant_publico}\nArtistas:")
        for artista in self.line_up:
            print(f"- {artista.nombre}")

    def ingresar_artista(self, artista):
        self.line_up.append(artista)
        print(f'Se ha ingresado un nuevo artista!!!\n{artista}')

    def asignar_lineup(self):
        self.line_up = []
        for artista in self.artistas:
            if self.dia == artista.dia_presentacion:
                self.ingresar_artista(artista)

    def nuevo_dia(self):
        pasar = self.exito_del_concierto
        if pasar:
            self.__dia += 1
        if self.__dia <= 3:
            print("Comienza un nuevo día")

    def ejecutar_evento(self):
        num = randint(1, 100)
        if num <= self.prob_evento*100:
            if 1 <= num and num <= 10:
                self.artista_actual.afinidad_con_publico -= AFINIDAD_LLUVIA
                print(f"Está lloviendo! Que mal para el público de {self.artista_actual.nombre}")
            elif 11 <= num and num <= 20:
                self.cant_publico -= PUBLICO_TERREMOTO
                print("TERREMOTOOO")
            elif 21 <= num and num <= 30:
                self.artista_actual.afinidad_con_publico -= AFINIDAD_OLA_CALOR
                self.cant_publico -= PUBLICO_OLA_CALOR
                print("Se informa que las temperaturas actuales llegan a los 60°C")
