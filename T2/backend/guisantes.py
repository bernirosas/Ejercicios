from PyQt5.QtCore import QThread, QTimer
import parametros as p


class Guisante(QThread):
    def __init__(self, pos_inicial, id, senal_terminado,
                 senal_actualizar_guis, label, senal_actualizar_interface):
        self.senal_actualizar_interface = senal_actualizar_interface
        self.label = label
        self.senal_actualizar_guis = senal_actualizar_guis
        super().__init__()
        self.id = id
        self.x_inicial = pos_inicial[0]
        self._x = pos_inicial[0]
        self.y = pos_inicial[1]
        self.ancho = pos_inicial[2]
        self.alto = pos_inicial[3]
        self.velocidad = 10
        self.senal_terminado = senal_terminado
        self.instanciar_timer()
        self.hielo = False
        self.activo = True

    def instanciar_timer(self):
        self.timer_guis = QTimer()
        self.timer_guis.setInterval(25)
        self.timer_guis.timeout.connect(self.actualizar_guisante)

    def actualizar_guisante(self):
        pos = self.mover()
        self.senal_actualizar_guis.emit(self.label, pos)

    def iniciar_timers(self):
        self.timer_guis.start()

    def mover(self):
        self.x += self.velocidad
        return (self.x, self.y)

    def eliminarse(self):
        self.label.hide()
        if self.activo:
            self.senal_terminado.emit(self.id)
        self.activo = False
        self.quit()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if valor > p.LIM_DERECHO:
            self.quit()
            self.label.hide()
            if self.activo:
                self.senal_terminado.emit(self.id)
            self.activo = False
        else:
            self._x = valor

    def run(self):
        pass


class GuisanteHielo(QThread):
    def __init__(self, pos_inicial, id, senal_terminado,
                 senal_act_hielo, label, senal_actualizar_interface):
        super().__init__()
        self.senal_actualizar_interface = senal_actualizar_interface
        self.label = label
        self.senal_act_hielo = senal_act_hielo
        self.id = id
        self.x_inicial = pos_inicial[0]
        self._x = pos_inicial[0]
        self.y = pos_inicial[1]
        self.ancho = pos_inicial[2]
        self.alto = pos_inicial[3]
        self.velocidad = 10
        self.senal_terminado = senal_terminado
        self.instanciar_timer()
        self.hielo = True
        self.activo = True

    def instanciar_timer(self):
        self.timer_guis = QTimer()
        self.timer_guis.setInterval(25)
        self.timer_guis.timeout.connect(self.actualizar_guisante)

    def actualizar_guisante(self):
        pos = self.mover()
        self.senal_act_hielo.emit(self.label, pos)

    def iniciar_timers(self):
        self.timer_guis.start()

    def mover(self):
        self.x += self.velocidad
        return (self.x, self.y)

    def eliminarse(self):
        self.senal_actualizar_interface.emit(self.label,
                                             p.ruta_guisante_hielo2)
        if self.activo:
            self.senal_terminado.emit(self.id)
        self.activo = False
        self.quit()
        self.label.hide()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if valor > p.LIM_DERECHO:
            self.quit()
            self.label.hide()
            if self.activo:
                self.senal_terminado.emit(self.id)
            self.activo = False
        else:
            self._x = valor

    def run(self):
        pass
