from PyQt5.QtCore import QThread, QTimer
import parametros as p
from random import randint


class Girasol(QThread):

    def __init__(self, casilla, senal_cambiar_label, senal_cambiar_label2,
                 senal_agregar_sol):
        super().__init__()
        self.senal_cambiar_label = senal_cambiar_label
        self.senal_cambiar_label2 = senal_cambiar_label2
        self.senal_agregar_sol = senal_agregar_sol
        self.intervalo_sol = p.INTERVALO_SOLES_GIRASOL
        self.vida = p.VIDA_PLANTA
        self.soles_a_generar = p.CANTIDAD_SOLES
        self.casilla = casilla
        self.casilla.show()
        self.casilla.setScaledContents(True)
        self.senal_cambiar_label2.emit(self.casilla)
        self.instanciar_timers()
        self.viva = True

    def instanciar_timers(self):
        self.timer_cambiar_1 = QTimer()
        self.timer_cambiar_1.setInterval(800)
        self.timer_cambiar_1.timeout.connect(self.cambiar_label_1)
        self.timer_cambiar_2 = QTimer()
        self.timer_cambiar_2.setInterval(800)
        self.timer_cambiar_2.timeout.connect(self.cambiar_label_2)
        self.timer_soles = QTimer()
        self.timer_soles.setInterval(self.intervalo_sol)
        self.timer_soles.timeout.connect(self.generar_sol)

    def parar_timers(self):
        self.timer_cambiar_1.stop()
        self.timer_cambiar_2.stop()
        self.timer_soles.stop()

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.casilla.hide()
            self.casilla.ocupada = False
            self.quit()
            self.timer_cambiar_1.stop()
            self.timer_cambiar_2.stop()
            self.timer_soles.stop()
            self.viva = False
        else:
            self._vida = valor

    def iniciar_timers(self):
        self.timer_cambiar_1.start()
        self.timer_soles.start()

    def generar_sol(self):
        for i in range(self.soles_a_generar):
            casilla = self.casilla
            ancho = 40
            valor_random = randint(-10, 10)  # variabilidad
            y = int((casilla.y1 + casilla.y2)/2 - 10) + valor_random
            valor_random = randint(-10, 10)
            x = casilla.x1 + 65 + valor_random
            self.senal_agregar_sol.emit(x, y, ancho, ancho)

    def cambiar_label_1(self):
        self.senal_cambiar_label.emit(self.casilla)
        self.timer_cambiar_1.stop()
        self.timer_cambiar_2.start()

    def cambiar_label_2(self):
        self.senal_cambiar_label2.emit(self.casilla)
        self.timer_cambiar_1.start()
        self.timer_cambiar_2.stop()

    def run(self):
        pass


class PlantaVerde(QThread):
    def __init__(self, casilla, senal_planta_verde, senal_guisante_verde):
        super().__init__()
        self.casilla = casilla
        self.casilla.show()
        self.senal_planta_verde = senal_planta_verde
        self.senal_guisante_verde = senal_guisante_verde
        self.vida = p.VIDA_PLANTA
        self.casilla.setScaledContents(True)
        self.senal_planta_verde.emit(self.casilla, p.ruta_planta_verde1)
        self.instanciar_timers()
        self.viva = True

    def instanciar_timers(self):
        self.timer_label_1 = QTimer()
        self.timer_label_1.setInterval(650)
        self.timer_label_1.timeout.connect(self.cambiar_label_1)
        self.timer_label_2 = QTimer()
        self.timer_label_2.setInterval(650)
        self.timer_label_2.timeout.connect(self.cambiar_label_2)
        self.timer_disparo = QTimer()
        self.timer_disparo.setInterval(p.INTERVALO_DISPARO)
        self.timer_disparo.timeout.connect(self.disparar)

    def parar_timers(self):
        self.timer_label_1.stop()
        self.timer_label_2.stop()
        self.timer_disparo.stop()

    def iniciar_timers(self):
        self.timer_label_1.start()
        self.timer_disparo.start()

    def disparar(self):
        x = self.casilla.x1
        y = self.casilla.y1
        self.senal_guisante_verde.emit(x, y)
        self.cambiar_label_3()

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.casilla.hide()
            self.casilla.ocupada = False
            self.quit()
            self.timer_label_1.stop()
            self.timer_label_2.stop()
            self.timer_disparo.stop()
            self.viva = False
        else:
            self._vida = valor

    def cambiar_label_1(self):
        self.senal_planta_verde.emit(self.casilla, p.ruta_planta_verde1)
        self.timer_label_1.stop()
        self.timer_label_2.start()

    def cambiar_label_2(self):
        self.senal_planta_verde.emit(self.casilla, p.ruta_planta_verde2)
        self.timer_label_2.stop()

    def cambiar_label_3(self):
        self.senal_planta_verde.emit(self.casilla, p.ruta_planta_verde3)
        self.timer_label_1.start()

    def run(self):
        pass


class PlantaHielo(QThread):
    def __init__(self, casilla, senal_planta_hielo, senal_guisante_hielo):
        super().__init__()
        self.casilla = casilla
        self.senal_planta_hielo = senal_planta_hielo
        self.senal_guisante_hielo = senal_guisante_hielo
        self.vida = p.VIDA_PLANTA
        self.dano = p.DANO_PROYECTIL
        self.instanciar_timers()
        self.casilla = casilla
        self.casilla.show()
        self.casilla.setScaledContents(True)
        self.senal_planta_hielo.emit(self.casilla, p.ruta_planta_azul1)
        self.instanciar_timers()
        self.viva = True

    def instanciar_timers(self):
        self.timer_label_1 = QTimer()
        self.timer_label_1.setInterval(650)
        self.timer_label_1.timeout.connect(self.cambiar_label_1)
        self.timer_label_2 = QTimer()
        self.timer_label_2.setInterval(650)
        self.timer_label_2.timeout.connect(self.cambiar_label_2)
        self.timer_disparo = QTimer()
        self.timer_disparo.setInterval(p.INTERVALO_DISPARO)
        self.timer_disparo.timeout.connect(self.disparar)

    def iniciar_timers(self):
        self.timer_label_1.start()
        self.timer_disparo.start()

    def parar_timers(self):
        self.timer_label_1.stop()
        self.timer_label_2.stop()
        self.timer_disparo.stop()

    def disparar(self):
        x = self.casilla.x1
        y = self.casilla.y1
        self.senal_guisante_hielo.emit(x, y)
        self.cambiar_label_3()
        self.timer_label_1.start()

    def cambiar_label_1(self):
        self.senal_planta_hielo.emit(self.casilla, p.ruta_planta_azul1)
        self.timer_label_1.stop()
        self.timer_label_2.start()

    def cambiar_label_2(self):
        self.senal_planta_hielo.emit(self.casilla, p.ruta_planta_azul2)
        self.timer_label_2.stop()

    def cambiar_label_3(self):
        self.senal_planta_hielo.emit(self.casilla, p.ruta_planta_azul3)
        self.timer_label_1.start()

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.casilla.hide()
            self.casilla.ocupada = False
            self.timer_label_1.stop()
            self.timer_label_2.stop()
            self.timer_disparo.stop()
            self.viva = False
            self.quit()
        else:
            self._vida = valor

    def run(self):
        pass


class Papa(QThread):
    def __init__(self, casilla, senal_papa):
        super().__init__()
        self.casilla = casilla
        self.senal_papa = senal_papa
        self._vida = 2*p.VIDA_PLANTA
        self.vida_media = p.VIDA_PLANTA
        self.vida_cuarto = p.VIDA_PLANTA/2
        self.casilla.setScaledContents(True)
        self.casilla.show()
        self.cambiar_label_1()
        self.viva = True

    def iniciar_timers(self):
        pass

    @property
    def vida(self):
        return self._vida

    def parar_timers(self):
        pass

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.casilla.hide()
            self.casilla.ocupada = False
            self.quit()
            self.viva = False
        elif valor <= self.vida_media:
            self.cambiar_label_2()
            self._vida = valor
        elif valor <= self.vida_cuarto:
            self.cambiar_label_3()
            self._vida = valor
        else:
            self._vida = valor

    def cambiar_label_1(self):
        self.senal_papa.emit(self.casilla, p.ruta_papa1)

    def cambiar_label_2(self):
        self.senal_papa.emit(self.casilla, p.ruta_papa2)

    def cambiar_label_3(self):
        self.senal_papa.emit(self.casilla, p.ruta_papa3)

    def run(self):
        pass
