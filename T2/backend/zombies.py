from PyQt5.QtCore import QThread
from parametros import (DANO_MORDIDA, INTERVALO_TIEMPO_MORDIDA,
                        RALENTIZAR_ZOMBIE,
                        VELOCIDAD_ZOMBIE, VIDA_ZOMBIE)
from PyQt5.QtCore import QTimer
import parametros as p


class Zombie(QThread):
    def __init__(self, senal_zombie, label, senal_mover_zombie,
                 senal_morir, senal_ganaron_zombies):
        self.senal_ganaron_zombies = senal_ganaron_zombies
        self.senal_morir = senal_morir
        self.senal_mover_zombie = senal_mover_zombie
        self.senal_actualizar_zombie = senal_zombie
        super().__init__()
        self.label = label
        self.walker = self.label.walker
        self.id = id
        self._x = label.x
        self.y = label.y
        if self.y == 160:
            self.carril = 1
        elif self.y == 240:
            self.carril = 2
        self.ancho = label.ancho
        self.alto = label.alto
        self._vida = VIDA_ZOMBIE
        if self.walker:
            self.velocidad = VELOCIDAD_ZOMBIE
        else:
            self.velocidad = int(1.5*VELOCIDAD_ZOMBIE)
        self.intervalo_mordida = INTERVALO_TIEMPO_MORDIDA
        self.dano = DANO_MORDIDA
        self.instanciar_timer()
        self.vivo = True
        self.ralentizado = False
        self.avanzar = True  # es falso si se encuentra con una planta

    def instanciar_timer(self):
        self.timer_label_1 = QTimer()
        self.timer_label_1.setInterval(150)
        self.timer_label_1.timeout.connect(self.actualizar_label_1)
        self.timer_label_2 = QTimer()
        self.timer_label_2.setInterval(150)
        self.timer_label_2.timeout.connect(self.actualizar_label_2)
        self.timer_comer_1 = QTimer()
        self.timer_comer_1.setInterval(100)
        self.timer_comer_1.timeout.connect(self.comer_1)
        self.timer_comer_2 = QTimer()
        self.timer_comer_2.setInterval(100)
        self.timer_comer_2.timeout.connect(self.comer_2)
        self.timer_comer_3 = QTimer()
        self.timer_comer_3.setInterval(100)
        self.timer_comer_3.timeout.connect(self.comer_3)
        self.timer_comer = QTimer()
        self.timer_comer.setInterval(self.intervalo_mordida)
        self.timer_comer.timeout.connect(self.comer)

    def actualizar_label_1(self):
        if self.walker and self.avanzar:
            self.senal_actualizar_zombie.emit(self.label,
                                              p.ruta_zombie_walker_1)
        elif self.avanzar:
            self.senal_actualizar_zombie.emit(self.label,
                                              p.ruta_zombie_runner_2)
        self.timer_label_1.stop()
        if self.vivo:
            self.timer_label_2.start()

    def actualizar_label_2(self):
        if self.walker and self.avanzar:
            self.senal_actualizar_zombie.emit(self.label,
                                              p.ruta_zombie_walker_2)
        elif self.avanzar:
            self.senal_actualizar_zombie.emit(self.label,
                                              p.ruta_zombie_runner_1)
        self.timer_label_2.stop()
        if self.vivo:
            self.timer_label_1.start()
            if self.avanzar:
                self.actualizar_pos()

    def empezar_a_comer(self, planta):
        self.avanzar = False
        self.planta = planta

    def comer(self):
        if not self.avanzar:
            self.planta.vida -= self.dano
            if not self.planta.viva:
                self.avanzar = True

    def comer_1(self):
        if self.walker and not self.avanzar:
            if not self.planta.viva:
                self.avanzar = True
            self.senal_actualizar_zombie.emit(self.label,
                                              p.ruta_walker_comiendo_1)
        elif not self.avanzar:
            if not self.planta.viva:
                self.avanzar = True
            self.senal_actualizar_zombie.emit(self.label,
                                              p.ruta_runner_comiendo_1)
        self.timer_comer_1.stop()
        if self.vivo:
            self.timer_comer_2.start()

    def comer_2(self):
        if self.walker and not self.avanzar:
            if not self.planta.viva:
                self.avanzar = True
            self.senal_actualizar_zombie.emit(self.label,
                                              p.ruta_walker_comiendo_2)
        elif not self.avanzar:
            if not self.planta.viva:
                self.avanzar = True
            self.senal_actualizar_zombie.emit(self.label,
                                              p.ruta_runner_comiendo_2)
        self.timer_comer_2.stop()
        if self.vivo:
            self.timer_comer_3.start()

    def comer_3(self):
        if self.walker and not self.avanzar:
            if not self.planta.viva:
                self.avanzar = True
            self.senal_actualizar_zombie.emit(self.label,
                                              p.ruta_walker_comiendo_3)
        elif not self.avanzar:
            if not self.planta.viva:
                self.avanzar = True
            self.senal_actualizar_zombie.emit(self.label,
                                              p.ruta_runner_comiendo_3)
        self.timer_comer_3.stop()
        if self.vivo:
            self.timer_comer_1.start()

    def ralentizar(self):
        self.velocidad -= self.velocidad*RALENTIZAR_ZOMBIE
        self.ralentizado = True

    def daño_guisante(self):
        self.vida -= p.DANO_PROYECTIL

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor <= 0:
            self._vida = 0
            self.label.hide()
            self.vivo = False
            self.timer_label_1.stop()
            self.timer_label_2.stop()
            self.senal_morir.emit(self.id)
            self.quit()
        else:
            self._vida = valor

    def actualizar_pos(self):
        pos = self.mover()
        self.senal_mover_zombie.emit(self.label, pos)

    def iniciar_timers(self):
        self.timer_label_1.start()
        self.timer_comer.start()
        self.timer_comer_1.start()

    def mover(self):
        self.x -= self.velocidad
        return (self.x, self.y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if valor <= p.LIM_IZQUIERDO:
            self.senal_ganaron_zombies.emit()
            self.quit()
            self.label.hide()
            self.timer_label_1.stop()
            self.timer_label_2.stop()
        else:
            self._x = int(valor)

    def run(self):
        pass
