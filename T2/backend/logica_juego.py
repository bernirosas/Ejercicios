from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtMultimedia
import parametros as p
from backend.guisantes import GuisanteHielo, Guisante
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QMutex
from random import randint
from aparicion_zombies import intervalo_aparicion
from backend.zombies import Zombie
from time import sleep


class LogicaJuego(QObject):
    resultado_planta = pyqtSignal(bool, str)
    senal_jardin = pyqtSignal(str)
    senal_salida = pyqtSignal(str)
    senal_cambiar_label = pyqtSignal(QLabel)
    senal_cambiar_label2 = pyqtSignal(QLabel)
    senal_agregar_sol = pyqtSignal(int, int, int, int)
    senal_actualizar_datos = pyqtSignal(QLabel, str)
    senal_planta_verde = pyqtSignal(QLabel, str)
    senal_guisante_verde = pyqtSignal(int, int)
    senal_actualizar_guis = pyqtSignal(QLabel, tuple)
    senal_terminado = pyqtSignal(int)  # misma para ambos guisantes
    senal_inicial = pyqtSignal(tuple)
    senal_inicial_hielo = pyqtSignal(tuple)
    senal_guisante_hielo = pyqtSignal(int, int)
    senal_papa = pyqtSignal(QLabel, str)
    senal_zombie = pyqtSignal(QLabel, str)
    senal_mover_zombie = pyqtSignal(QLabel, tuple)
    senal_inicial_zombie = pyqtSignal(tuple, tuple)
    senal_morir_zombie = pyqtSignal(int)
    senal_ganaron_zombies = pyqtSignal()
    senal_termino_ronda = pyqtSignal(bool, bool)
    senal_ventana_post_ronda = pyqtSignal(bool, int, int, int, int, int)
    senal_pop_up = pyqtSignal(str)

    def __init__(self, ventana_jardin) -> None:
        super().__init__()
        self.escenario = ventana_jardin
        self._soles = p.SOLES_INICIALES
        self._ronda = 1
        self.puntaje = 0
        self.puntaje_ronda = 0
        self._zombies_destruidos = 0
        self.plantas = []
        self.lock_plantas = QMutex()
        self.noche = False
        self.instanciar_timers()
        self.senal_guisante_verde.connect(self.crear_guisante)
        self.senal_terminado.connect(self.borrar_guis)
        self.senal_guisante_hielo.connect(self.crear_guisante_hielo)
        self.senal_morir_zombie.connect(self.borrar_zombie)
        self.nro_soles = 0
        self.soles_labels = {}
        self.lock_soles = QMutex()
        self.guisantes = {}
        self.nro_guisantes = 0
        self.zombies = {}
        self.lock_zombies = QMutex()
        self.lock_guisantes = QMutex()
        self._zombies_restantes = p.N_ZOMBIES*2  # al ser dos carriles
        self.zombies_iniciales = p.N_ZOMBIES*2
        self.nro_zombies = 0
        self.senal_ganaron_zombies.connect(self.ganaron_zombies)
        self.perdio = False
        self.avanza = False

    def instanciar_timers(self):
        self.timer_soles = QTimer()
        self.timer_soles.setInterval(p.INTERVALO_APARICION_SOLES)
        self.timer_soles.timeout.connect(self.aparecer_soles)
        self.timer_revisar_colisión_zombie = QTimer()
        self.timer_revisar_colisión_zombie.setInterval(30)
        self.timer_revisar_colisión_zombie.timeout.connect(self.
                                                           revisar_colision)
        self.timer_abrir_ventana_post_ronda = QTimer()
        (self.timer_abrir_ventana_post_ronda.timeout.
         connect(self.abrir_ventana_post))
        self.timer_abrir_ventana_post_ronda.setInterval(5000)

    def abrir_ventana_post(self):
        self.timer_abrir_ventana_post_ronda.stop()
        self.senal_ventana_post_ronda.emit(self.perdio, self.ronda, self.soles,
                                           self.zombies_destruidos,
                                           self.puntaje_ronda,
                                           self.puntaje)
        self.senal_termino_ronda.emit(self.perdio, False)

    def pasar_ronda(self):
        self.ronda += 1

    def ganaron_zombies(self):
        self.timer_abrir_ventana_post_ronda.start()
        self.perdio = True
        self.senal_termino_ronda.emit(self.perdio, True)
        self.parar_ronda()
        self.guardar_puntaje()

    def avanzar(self):
        if self.soles >= p.COSTO_AVANZAR:
            self.soles -= p.COSTO_AVANZAR
            self.avanza = True
            self.gano_jugador_ronda()

    def guardar_puntaje(self):
        with open("puntajes.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{str(self.usuario)},{str(self.puntaje)}")
            archivo.write("\n")

    def gano_jugador_ronda(self):
        self.timer_abrir_ventana_post_ronda.start()
        self.parar_ronda()
        if not self.avanza:
            self.calcular_puntaje_extra()
        self.senal_termino_ronda.emit(self.perdio, True)

    def calcular_puntaje_extra(self):
        puntaje_extra = round(self.puntaje_ronda * self.dificultad)
        self.puntaje_ronda += puntaje_extra
        self.puntaje += puntaje_extra

    def parar_ronda(self):
        self.funciones_2.parar_ronda()

    def resetear_ronda(self):
        self.funciones_2.resetear_ronda()

    def cheatcode_sun(self):
        self.soles += p.SOLES_EXTRA

    def cheatcode_kil(self):
        self.funciones_2.cheatcode_kil()

    def revisar_colision(self):
        self.funciones_2.revisar_colision()

    def aparecer_soles(self):
        #  queremos que el sol se cree en una casilla random
        nro = randint(1, 20)
        casilla = self.escenario.casillas[nro]
        ancho = 40
        valor_random = randint(-10, 10)  # variabilidad
        y = int((casilla.y1 + casilla.y2)/2 - 10) + valor_random
        valor_random = randint(-10, 10)
        x = casilla.x1 + 65 + valor_random
        self.senal_agregar_sol.emit(x, y, ancho, ancho)

    def pausar(self):
        sleep(10)

    def recibir_sol(self, sol):
        self.lock_soles.lock()
        self.nro_soles += 1
        sol.id = self.nro_soles
        self.soles_labels[sol.id] = sol
        self.lock_soles.unlock()

    def borrar_zombie(self, id):
        if not self.perdio:
            nro = randint(1, 6)
            if nro == 1:
                QtMultimedia.QSound.play(p.ruta_sonido_1)
            if nro == 2:
                QtMultimedia.QSound.play(p.ruta_sonido_2)
            if nro == 3:
                QtMultimedia.QSound.play(p.ruta_sonido_3)
            if nro == 4:
                QtMultimedia.QSound.play(p.ruta_sonido_4)
            if nro == 5:
                QtMultimedia.QSound.play(p.ruta_sonido_5)
            if nro == 6:
                QtMultimedia.QSound.play(p.ruta_sonido_6)
        self.lock_zombies.lock()
        self.zombies.pop(id)
        self.zombies_destruidos += 1
        self.zombies_restantes -= 1
        self.lock_zombies.unlock()

    def borrar_sol(self, sol):
        self.lock_soles.lock()
        self.soles_labels.pop(sol.id)
        self.lock_soles.unlock()
        sol.hide()

    def crear_guisante(self, x, y):
        x = x + 45
        ancho = 31
        alto = 41
        pos_guis = (x, y, ancho, alto)
        self.senal_inicial.emit(pos_guis)

    def recibir_label(self, pos_guis, label):
        # recibe label de guisante para instanciarlo
        self.lock_guisantes.lock()
        self.nro_guisantes += 1
        id = self.nro_guisantes
        guis = Guisante(pos_guis, id, self.senal_terminado,
                        self.senal_actualizar_guis, label,
                        self.senal_planta_verde)
        guis.iniciar_timers()
        self.guisantes[id] = guis
        self.lock_guisantes.unlock()

    def crear_guisante_hielo(self, x, y):
        x = x + 45
        ancho = 31
        alto = 41
        pos_guis = (x, y, ancho, alto)
        self.senal_inicial_hielo.emit(pos_guis)

    def recibir_label_hielo(self, pos_guis, label):
        self.lock_guisantes.lock()
        self.nro_guisantes += 1
        id = self.nro_guisantes
        guis = GuisanteHielo(pos_guis, id, self.senal_terminado,
                             self.senal_actualizar_guis, label,
                             self.senal_planta_verde)
        guis.iniciar_timers()
        self.guisantes[id] = guis
        self.lock_guisantes.unlock()

    def borrar_guis(self, id):
        self.lock_guisantes.lock()
        self.guisantes[id].timer_guis.stop()
        self.guisantes.pop(id)
        self.lock_guisantes.unlock()

    @property
    def ronda(self):
        return self._ronda

    @ronda.setter
    def ronda(self, valor):
        self._ronda = valor
        self.senal_actualizar_datos.emit(self.escenario.label_nivel,
                                         str(valor))
        self.cambiar_puntaje(round(self.puntaje))
        intervalo_zombies = intervalo_aparicion(self.ronda, self.dificultad)
        intervalo_zombies = round(intervalo_zombies*8000)
        self.timer_zombies = QTimer()
        self.timer_zombies.setInterval(intervalo_zombies)
        self.timer_zombies.timeout.connect(self.crear_labels_zombies)
        self.resetear_ronda()

    def cambiar_puntaje(self, puntaje):
        #  esta función la llama lógica SOLO al pasar de ronda
        self.senal_actualizar_datos.emit(self.escenario.label_puntaje,
                                         str(puntaje))

    @property
    def soles(self):
        return self._soles

    @soles.setter
    def soles(self, valor):
        #  el proceso de comprobación de que haya suficientes soles
        #  se da en cada caso
        self._soles = valor
        self.senal_actualizar_datos.emit(self.escenario.label_soles,
                                         str(self.soles))

    @property
    def zombies_restantes(self):
        return self._zombies_restantes

    @zombies_restantes.setter
    def zombies_restantes(self, valor):
        if not self.perdio and not self.avanza:
            if valor <= 0:
                self.gano_jugador_ronda()
            self._zombies_restantes = valor
            self.senal_actualizar_datos.emit(self.escenario.label_restantes,
                                             str(valor))

    @property
    def zombies_destruidos(self):
        return self._zombies_destruidos

    @zombies_destruidos.setter
    def zombies_destruidos(self, valor):
        if not self.perdio and not self.avanza:
            self._zombies_destruidos = valor
            if not self.noche:
                self.puntaje += p.PUNTAJE_ZOMBIE_DIURNO
                self.puntaje_ronda += p.PUNTAJE_ZOMBIE_DIURNO
            elif self.noche:
                self.puntaje += p.PUNTAJE_ZOMBIE_NOCTURNO
                self.puntaje_ronda += p.PUNTAJE_ZOMBIE_NOCTURNO
            self.senal_actualizar_datos.emit(self.escenario.label_destruidos,
                                             str(valor))

    def escenificar(self, usuario, escenario):
        self.usuario = usuario
        self.senal_actualizar_datos.emit(self.escenario.label_soles,
                                         str(self.soles))
        self.dificultad = p.PONDERADOR_DIURNO
        if escenario == "salida_nocturna":
            self.escenario.label_escenario.setPixmap(QPixmap(p.ruta_noche))
            self.noche = True
            self.dificultad = p.PONDERADOR_NOCTURNO
        self.senal_jardin.emit(usuario)
        self.funciones.otorgar_posiciones()
        intervalo_zombies = intervalo_aparicion(self.ronda, self.dificultad)
        intervalo_zombies = round(intervalo_zombies*8000)
        self.timer_zombies = QTimer()
        self.timer_zombies.setInterval(intervalo_zombies)
        self.timer_zombies.timeout.connect(self.crear_labels_zombies)
        self.senal_actualizar_datos.emit(self.escenario.label_restantes,
                                         str(self._zombies_restantes))

    def crear_labels_zombies(self):
        #  uno para cada carril
        if self.nro_zombies < self.zombies_iniciales:
            x = p.LIM_DERECHO
            y1 = 160
            y2 = 240
            ancho = 55
            alto = 80
            pos_zombie_1 = (x, y1, ancho, alto)
            pos_zombie_2 = (x, y2, ancho, alto)
            self.senal_inicial_zombie.emit(pos_zombie_1, pos_zombie_2)

    def crear_zombie(self, label_1, label_2):
        #  uno para cada carril
        self.lock_zombies.lock()
        zombie = Zombie(self.senal_zombie, label_1, self.senal_mover_zombie,
                        self.senal_morir_zombie, self.senal_ganaron_zombies)
        self.nro_zombies += 1
        zombie.id = self.nro_zombies
        self.zombies[zombie.id] = zombie
        zombie.iniciar_timers()
        zombie = Zombie(self.senal_zombie, label_2, self.senal_mover_zombie,
                        self.senal_morir_zombie, self.senal_ganaron_zombies)
        self.nro_zombies += 1
        zombie.id = self.nro_zombies
        self.zombies[zombie.id] = zombie
        zombie.iniciar_timers()
        self.lock_zombies.unlock()

    def jugar(self):
        for planta in self.plantas:
            planta.start()
            planta.iniciar_timers()
        if not self.noche:
            self.timer_soles.start()
        self.timer_zombies.start()
        self.timer_revisar_colisión_zombie.start()

    def recoger_sol(self, x, y):
        self.lock_soles.lock()
        recoger = False
        for sol in self.soles_labels.values():
            if ((sol.x <= x <= (sol.x + sol.ancho))
               and (sol.y <= y <= (sol.y + sol.ancho))):
                sol_elegido = sol
                recoger = True
        self.lock_soles.unlock()
        if recoger:
            if self.noche:
                self.soles += p.SOLES_POR_RECOLECCION
            else:
                self.soles += 2*p.SOLES_POR_RECOLECCION
            self.borrar_sol(sol_elegido)

    def validar_lugar_y_crear_planta(self, bool, casilla):
        self.funciones.validar_lugar_y_crear_planta(bool, casilla)

    def checkear_posicion_planta(self, x, y):
        self.funciones.checkear_posicion_planta(x, y)

    def checkear_posicion_lugar(self, x, y):
        self.funciones.checkear_posicion_lugar(x, y)
