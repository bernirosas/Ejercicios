from PyQt5.QtCore import QObject
import parametros as p
from PyQt5.QtWidgets import QLabel
from backend.plantas import (Girasol, PlantaVerde, PlantaHielo, Papa)


class FuncionesVarias(QObject):
    def __init__(self, logica) -> None:
        super().__init__()
        self.logica = logica

    def validar_lugar_y_crear_planta(self, bool, casilla):
        costeado = False
        self.logica.escenario.click_lugar = False
        self.logica.escenario.click_planta = True
        if bool:
            if self.planta != "pala":
                if self.logica.planta == "girasol":
                    if self.logica.soles >= 50:
                        planta = Girasol(casilla,
                                         self.logica.senal_cambiar_label,
                                         self.logica.senal_cambiar_label2,
                                         self.logica.senal_agregar_sol)
                        self.logica.soles -= 50
                        costeado = True
                if self.logica.planta == "planta_verde":
                    if self.logica.soles >= 100:
                        planta = PlantaVerde(casilla,
                                             self.logica.senal_planta_verde,
                                             self.logica.senal_guisante_verde)
                        self.logica.soles -= 100
                        costeado = True
                if self.logica.planta == "planta_azul":
                    if self.logica.soles >= 150:
                        planta = PlantaHielo(casilla,
                                             self.logica.senal_planta_verde,
                                             self.logica.senal_guisante_hielo)
                        self.logica.soles -= 150
                        costeado = True
                if self.logica.planta == "papa":
                    if self.logica.soles >= 75:
                        planta = Papa(casilla, self.logica.senal_papa)
                        self.logica.soles -= 75
                        costeado = True
                if costeado:
                    self.logica.lock_plantas.lock()
                    self.logica.plantas.append(planta)
                    self.logica.lock_plantas.unlock()
                if self.logica.escenario.iniciado and costeado:
                    # dado que queremos que inicie sin tener que esperar
                    planta.start()
                    planta.iniciar_timers()
                if not costeado:
                    casilla.ocupada = False
                    (self.logica.senal_pop_up.
                     emit("No tienes suficientes soles."))
            if self.planta == "pala":
                for planta in self.logica.plantas:
                    if casilla == planta.casilla:
                        planta.vida -= 1000

    def checkear_posicion_planta(self, x, y):
        #  revisar si corresponde a planta
        planta = False
        elegida = ""
        if (p.x1_girasol <= x <= p.x2_girasol
                and p.y1_girasol <= y <= p.y2_girasol):
            planta = True
            elegida = "girasol"
        if (p.x1_planta_azul <= x <= p.x2_planta_azul
                and p.y1_planta_azul <= y <= p.y2_planta_azul):
            planta = True
            elegida = "planta_azul"
        if (p.x1_planta_verde <= x <= p.x2_planta_verde
                and p.y1_planta_verde <= y <= p.y2_planta_verde):
            planta = True
            elegida = "planta_verde"
        if (p.x1_papa <= x <= p.x2_papa
                and p.y1_papa <= y <= p.y2_papa):
            planta = True
            elegida = "papa"
        if (p.x1_pala <= x <= p.x2_pala
                and p.y1_pala <= y <= p.y2_pala):
            planta = True
            elegida = "pala"
        self.planta = elegida
        self.logica.planta = elegida
        self.logica.resultado_planta.emit(planta, elegida)

    def checkear_posicion_lugar(self, x, y):
        posicion = False
        casilla = QLabel(self.logica.escenario)
        if (p.x1_A1 <= x <= p.x2_A1
                and p.y1_A1 <= y <= p.y2_A1):
            if (not self.logica.escenario.A1.ocupada):
                posicion = True
                casilla = self.logica.escenario.A1
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.A1.ocupada:
                posicion = True
                casilla = self.logica.escenario.A1
        if (p.x1_A2 <= x <= p.x2_A2
                and p.y1_A2 <= y <= p.y2_A2):
            if not (self.logica.escenario.A2.ocupada):
                posicion = True
                casilla = self.logica.escenario.A2
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.A2.ocupada:
                posicion = True
                casilla = self.logica.escenario.A2
        if (p.x1_A3 <= x <= p.x2_A3
                and p.y1_A3 <= y <= p.y2_A3):
            if not (self.logica.escenario.A3.ocupada):
                posicion = True
                casilla = self.logica.escenario.A3
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.A3.ocupada:
                posicion = True
                casilla = self.logica.escenario.A3
        if (p.x1_A4 <= x <= p.x2_A4
                and p.y1_A4 <= y <= p.y2_A4):
            if not (self.logica.escenario.A4.ocupada):
                posicion = True
                casilla = self.logica.escenario.A4
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.A4.ocupada:
                posicion = True
                casilla = self.logica.escenario.A4
        if (p.x1_A5 <= x <= p.x2_A5
                and p.y1_A5 <= y <= p.y2_A5):
            if not (self.logica.escenario.A5.ocupada):
                posicion = True
                casilla = self.logica.escenario.A5
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.A5.ocupada:
                posicion = True
                casilla = self.logica.escenario.A5
        if (p.x1_A6 <= x <= p.x2_A6
                and p.y1_A6 <= y <= p.y2_A6):
            if not (self.logica.escenario.A6.ocupada):
                posicion = True
                casilla = self.logica.escenario.A6
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.A6.ocupada:
                posicion = True
                casilla = self.logica.escenario.A6
        if (p.x1_A7 <= x <= p.x2_A7
                and p.y1_A7 <= y <= p.y2_A7):
            if not (self.logica.escenario.A7.ocupada):
                posicion = True
                casilla = self.logica.escenario.A7
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.A7.ocupada:
                posicion = True
                casilla = self.logica.escenario.A7
        if (p.x1_A8 <= x <= p.x2_A8
                and p.y1_A8 <= y <= p.y2_A8):
            if not (self.logica.escenario.A8.ocupada):
                posicion = True
                casilla = self.logica.escenario.A8
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.A8.ocupada:
                posicion = True
                casilla = self.logica.escenario.A8
        if (p.x1_A9 <= x <= p.x2_A9
                and p.y1_A9 <= y <= p.y2_A9):
            if not (self.logica.escenario.A9.ocupada):
                posicion = True
                casilla = self.logica.escenario.A9
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.A9.ocupada:
                posicion = True
                casilla = self.logica.escenario.A9
        if (p.x1_A10 <= x <= p.x2_A10
                and p.y1_A10 <= y <= p.y2_A10):
            if not (self.logica.escenario.A10.ocupada):
                posicion = True
                casilla = self.logica.escenario.A10
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.A10.ocupada:
                posicion = True
                casilla = self.logica.escenario.A10
        if (p.x1_B1 <= x <= p.x2_B1
                and p.y1_B1 <= y <= p.y2_B1):
            if not (self.logica.escenario.B1.ocupada):
                posicion = True
                casilla = self.logica.escenario.B1
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.B1.ocupada:
                posicion = True
                casilla = self.logica.escenario.B1
        if (p.x1_B2 <= x <= p.x2_B2
                and p.y1_B2 <= y <= p.y2_B2):
            if not (self.logica.escenario.B2.ocupada):
                posicion = True
                casilla = self.logica.escenario.B2
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.B2.ocupada:
                posicion = True
                casilla = self.logica.escenario.B2
        if (p.x1_B3 <= x <= p.x2_B3
                and p.y1_B3 <= y <= p.y2_B3):
            if not self.logica.escenario.B3.ocupada:
                posicion = True
                casilla = self.logica.escenario.B3
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.B3.ocupada:
                posicion = True
                casilla = self.logica.escenario.B3
        if (p.x1_B4 <= x <= p.x2_B4
                and p.y1_B4 <= y <= p.y2_B4):
            if not self.logica.escenario.B4.ocupada:
                posicion = True
                casilla = self.logica.escenario.B4
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.B4.ocupada:
                posicion = True
                casilla = self.logica.escenario.B4
        if (p.x1_B5 <= x <= p.x2_B5
                and p.y1_B5 <= y <= p.y2_B5):
            if not self.logica.escenario.B5.ocupada:
                posicion = True
                casilla = self.logica.escenario.B5
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.B5.ocupada:
                posicion = True
                casilla = self.logica.escenario.B5
        if (p.x1_B6 <= x <= p.x2_B6
                and p.y1_B6 <= y <= p.y2_B6):
            if not self.logica.escenario.B6.ocupada:
                posicion = True
                casilla = self.logica.escenario.B6
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.B6.ocupada:
                posicion = True
                casilla = self.logica.escenario.B6
        if (p.x1_B7 <= x <= p.x2_B7
                and p.y1_B7 <= y <= p.y2_B7):
            if not self.logica.escenario.B7.ocupada:
                posicion = True
                casilla = self.logica.escenario.B7
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.B7.ocupada:
                posicion = True
                casilla = self.logica.escenario.B7
        if (p.x1_B8 <= x <= p.x2_B8
                and p.y1_B8 <= y <= p.y2_B8):
            if not self.logica.escenario.B8.ocupada:
                posicion = True
                casilla = self.logica.escenario.B8
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.B8.ocupada:
                posicion = True
                casilla = self.logica.escenario.B8
        if (p.x1_B9 <= x <= p.x2_B9
                and p.y1_B9 <= y <= p.y2_B9):
            if not self.logica.escenario.B9.ocupada:
                posicion = True
                casilla = self.logica.escenario.B9
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.B9.ocupada:
                posicion = True
                casilla = self.logica.escenario.B9
        if (p.x1_B10 <= x <= p.x2_B10
                and p.y1_B10 <= y <= p.y2_B10):
            if not self.logica.escenario.B10.ocupada:
                posicion = True
                casilla = self.logica.escenario.B10
                casilla.ocupada = True
            if self.planta == "pala" and self.logica.escenario.B10.ocupada:
                posicion = True
                casilla = self.logica.escenario.B10
        if not posicion:
            self.logica.senal_pop_up.emit("Casilla no válida")
        self.logica.validar_lugar_y_crear_planta(posicion, casilla)

    def otorgar_posiciones(self):
        #  otorga x1, x2, y1 e y2 a cada celda
        casilla = self.logica.escenario.A1
        casilla.x1 = p.x1_A1
        casilla.x2 = p.x2_A1
        casilla.y1 = p.y1_A1
        casilla.y2 = p.y2_A1
        casilla.ocupada = False
        casilla = self.logica.escenario.A2
        casilla.x1 = p.x1_A2
        casilla.x2 = p.x2_A2
        casilla.y1 = p.y1_A2
        casilla.y2 = p.y2_A2
        casilla.ocupada = False
        casilla = self.logica.escenario.A3
        casilla.x1 = p.x1_A3
        casilla.x2 = p.x2_A3
        casilla.y1 = p.y1_A3
        casilla.y2 = p.y2_A3
        casilla.ocupada = False
        casilla = self.logica.escenario.A4
        casilla.x1 = p.x1_A4
        casilla.x2 = p.x2_A4
        casilla.y1 = p.y1_A4
        casilla.y2 = p.y2_A4
        casilla.ocupada = False
        casilla = self.logica.escenario.A5
        casilla.x1 = p.x1_A5
        casilla.x2 = p.x2_A5
        casilla.y1 = p.y1_A5
        casilla.y2 = p.y2_A5
        casilla.ocupada = False
        casilla = self.logica.escenario.A6
        casilla.x1 = p.x1_A6
        casilla.x2 = p.x2_A6
        casilla.y1 = p.y1_A6
        casilla.y2 = p.y2_A6
        casilla.ocupada = False
        casilla = self.logica.escenario.A7
        casilla.x1 = p.x1_A7
        casilla.x2 = p.x2_A7
        casilla.y1 = p.y1_A7
        casilla.y2 = p.y2_A7
        casilla.ocupada = False
        casilla = self.logica.escenario.A8
        casilla.x1 = p.x1_A8
        casilla.x2 = p.x2_A8
        casilla.y1 = p.y1_A8
        casilla.y2 = p.y2_A8
        casilla.ocupada = False
        casilla = self.logica.escenario.A9
        casilla.x1 = p.x1_A9
        casilla.x2 = p.x2_A9
        casilla.y1 = p.y1_A9
        casilla.y2 = p.y2_A9
        casilla.ocupada = False
        casilla = self.logica.escenario.A10
        casilla.x1 = p.x1_A10
        casilla.x2 = p.x2_A10
        casilla.y1 = p.y1_A10
        casilla.y2 = p.y2_A10
        casilla.ocupada = False
        casilla = self.logica.escenario.B1
        casilla.x1 = p.x1_B1
        casilla.x2 = p.x2_B1
        casilla.y1 = p.y1_B1
        casilla.y2 = p.y2_B1
        casilla.ocupada = False
        casilla = self.logica.escenario.B2
        casilla.x1 = p.x1_B2
        casilla.x2 = p.x2_B2
        casilla.y1 = p.y1_B2
        casilla.y2 = p.y2_B2
        casilla.ocupada = False
        casilla = self.logica.escenario.B3
        casilla.x1 = p.x1_B3
        casilla.x2 = p.x2_B3
        casilla.y1 = p.y1_B3
        casilla.y2 = p.y2_B3
        casilla.ocupada = False
        casilla = self.logica.escenario.B4
        casilla.x1 = p.x1_B4
        casilla.x2 = p.x2_B4
        casilla.y1 = p.y1_B4
        casilla.y2 = p.y2_B4
        casilla.ocupada = False
        casilla = self.logica.escenario.B5
        casilla.x1 = p.x1_B5
        casilla.x2 = p.x2_B5
        casilla.y1 = p.y1_B5
        casilla.y2 = p.y2_B5
        casilla.ocupada = False
        casilla = self.logica.escenario.B6
        casilla.x1 = p.x1_B6
        casilla.x2 = p.x2_B6
        casilla.y1 = p.y1_B6
        casilla.y2 = p.y2_B6
        casilla.ocupada = False
        casilla = self.logica.escenario.B7
        casilla.x1 = p.x1_B7
        casilla.x2 = p.x2_B7
        casilla.y1 = p.y1_B7
        casilla.y2 = p.y2_B7
        casilla.ocupada = False
        casilla = self.logica.escenario.B8
        casilla.x1 = p.x1_B8
        casilla.x2 = p.x2_B8
        casilla.y1 = p.y1_B8
        casilla.y2 = p.y2_B8
        casilla.ocupada = False
        casilla = self.logica.escenario.B9
        casilla.x1 = p.x1_B9
        casilla.x2 = p.x2_B9
        casilla.y1 = p.y1_B9
        casilla.y2 = p.y2_B9
        casilla.ocupada = False
        casilla = self.logica.escenario.B10
        casilla.x1 = p.x1_B10
        casilla.x2 = p.x2_B10
        casilla.y1 = p.y1_B10
        casilla.y2 = p.y2_B10
        casilla.ocupada = False
