from PyQt5.QtCore import QObject, QTimer
import parametros as p


class FuncionesVarias2(QObject):
    def __init__(self, logica) -> None:
        super().__init__()
        self.logica = logica

    def parar_ronda(self):
        #  mata a todos los objetos y timers presentes
        #  en el caso de los zombies se revisa si el jugador gano
        #  o perdió para suma o no puntaje
        self.logica.timer_soles.stop()
        self.logica.timer_revisar_colisión_zombie.stop()
        self.logica.timer_zombies.stop()
        for planta in self.logica.plantas:
            planta.vida -= 1000
        copia_zombie = self.logica.zombies.copy()
        for zombie in copia_zombie.values():
            zombie.vida -= 1000
        copia_soles = self.logica.soles_labels.copy()
        for sol in copia_soles.values():
            self.logica.borrar_sol(sol)

    def resetear_ronda(self):
        for planta in self.logica.plantas:
            planta.vida -= 1000
        self.logica._soles = p.SOLES_INICIALES
        self.logica._zombies_destruidos = 0
        self.logica.plantas = []
        self.logica.nro_soles = 0
        self.logica.soles_labels = {}
        self.logica.escenario.iniciado = False
        self.logica.guisantes = {}
        self.logica.nro_guisantes = 0
        self.logica.zombies = {}
        self.logica._zombies_restantes = p.N_ZOMBIES*2  # al ser dos carriles
        self.logica.nro_zombies = 0
        self.logica.puntaje_ronda = 0
        self.logica.avanza = False
        self.logica.senal_actualizar_datos.emit(self.logica.escenario.
                                                label_soles,
                                                str(self.logica.soles))
        self.logica.senal_actualizar_datos.emit(self.logica.escenario.
                                                label_restantes,
                                                str(self.logica.
                                                    _zombies_restantes))
        self.logica.senal_actualizar_datos.emit(self.logica.escenario.
                                                label_destruidos,
                                                str(self.logica.
                                                    _zombies_destruidos))

    def cheatcode_kil(self):
        self.logica.timer_zombies.stop()
        copia_zombie = self.logica.zombies.copy()
        for zombie in copia_zombie.values():
            zombie.vida -= 1000
        if not self.logica.noche:
            self.logica.puntaje += (p.PUNTAJE_ZOMBIE_DIURNO *
                                    self.logica.zombies_restantes)
            self.logica.puntaje_ronda += (p.PUNTAJE_ZOMBIE_DIURNO *
                                          self.logica.zombies_restantes)
        elif self.logica.noche:
            self.logica.puntaje += (p.PUNTAJE_ZOMBIE_NOCTURNO *
                                    self.zombies_restantes)
            self.logica.puntaje_ronda += (p.PUNTAJE_ZOMBIE_NOCTURNO *
                                          self.logica.zombies_restantes)
        self.logica._zombies_restantes = 0
        self.logica._zombies_destruidos = p.N_ZOMBIES*2
        self.logica.senal_actualizar_datos.emit(self.logica.escenario.
                                                label_restantes,
                                                str(0))
        self.logica.senal_actualizar_datos.emit(self.logica.escenario.
                                                label_destruidos,
                                                str(p.N_ZOMBIES*2))
        self.logica.gano_jugador_ronda()

    def revisar_colision(self):
        # el primero de los zombies (menor x) de cada carril será el
        # que recibirá el impacto así que primero sabremos cual es este
        self.logica.timer_revisar_colisión_zombie.stop()
        # para asegurarnos de terminar de revisar todo
        self.logica.lock_guisantes.lock()
        self.logica.lock_zombies.lock()
        guisante_elegido = ""
        zombie_elegido = ""
        for guisante in self.logica.guisantes.values():
            for zombie_1 in self.logica.zombies.values():
                if zombie_1.y == guisante.y:
                    if ((guisante.x - 15) >= zombie_1.x and
                       (guisante.y == zombie_1.y) and
                       (guisante.x_inicial - 30 <= zombie_1.x)):
                        if guisante.hielo and not zombie_1.ralentizado:
                            zombie_1.ralentizar()
                        if guisante_elegido == "":
                            guisante_elegido = guisante
                        if zombie_elegido == "":
                            zombie_elegido = zombie_1
                if zombie_1.y == guisante.y:
                    if ((guisante.x - 10) >= zombie_1.x and
                       (guisante.y == zombie_1.y) and
                       (guisante.x_inicial - 30 <= zombie_1.x)):
                        if not guisante.hielo:
                            (guisante.senal_actualizar_interface.
                             emit(guisante.label,
                                  p.ruta_guisante2))
                        if guisante.hielo:
                            (guisante.senal_actualizar_interface.
                             emit(guisante.label,
                                  p.ruta_guisante_hielo2))
                    if ((guisante.x + 20) >= zombie_1.x and
                       (guisante.y == zombie_1.y) and
                       (guisante.x_inicial - 30 <= zombie_1.x)):
                        if not guisante.hielo:
                            (guisante.senal_actualizar_interface.
                             emit(guisante.label,
                                  p.ruta_guisante3))
                        if guisante.hielo:
                            (guisante.senal_actualizar_interface.
                             emit(guisante.label,
                                  p.ruta_guisante_hielo3))
        self.logica.lock_guisantes.unlock()
        self.logica.lock_zombies.unlock()
        if guisante_elegido != "":
            guisante_elegido.muerte = True
            guisante_elegido.eliminarse()
        if zombie_elegido != "":
            zombie_elegido.daño_guisante()
        self.logica.lock_zombies.lock()
        self.logica.lock_plantas.lock()
        for zombie in self.logica.zombies.values():
            if zombie.avanzar:
                for planta in self.logica.plantas:
                    if (((planta.casilla.x1 + planta.casilla.x2)/2) >= zombie.x
                       and (planta.casilla.y1 == zombie.y) and planta.viva
                       and zombie.x >= planta.casilla.x1):
                        zombie.empezar_a_comer(planta)
        self.logica.lock_plantas.unlock()
        self.logica.lock_zombies.unlock()
        self.logica.lock_plantas.lock()
        indice = ""
        for i in range(0, len(self.logica.plantas)):
            if not self.logica.plantas[i].viva:
                indice = i
        if indice != "":
            self.logica.plantas.pop(indice)
        self.logica.lock_plantas.unlock()
        self.logica.timer_revisar_colisión_zombie.start()

    def pausar(self):
        self.logica.tiempo_soles = self.logica.timer_soles.remainingTime()
        self.logica.timer_soles.stop()
        self.logica.tiempo_zombie = self.logica.timer_zombies.remainingTime()
        self.logica.timer_zombies.stop()

    def reanudar(self):
        if not self.logica.noche:
            if self.logica.pausado_reciente_sol:
                tiempo = self.logica.timer_temporal_sol.remainingTime()
                self.logica.timer_temporal_sol = QTimer()
                self.logica.timer_temporal_sol.setInterval(tiempo)
            else:
                self.logica.timer_temporal_sol = QTimer()
                self.logica.timer_temporal_sol.setInterval(self.logica.
                                                           tiempo_soles)
            self.logica.timer_temporal_sol.setSingleShot(True)
            self.logica.timer_temporal_sol.timeout.connect(self.logica.
                                                           reanudar_soles)
            self.logica.timer_temporal_sol.start()
            self.logica.pausado_reciente_sol = True
        if self.logica.pausado_reciente_zombie:
            tiempo_2 = self.logica.timer_temporal_zombie.remainingTime()
            self.logica.timer_temporal_zombie = QTimer()
            self.logica.timer_temporal_zombie.setInterval(tiempo_2)
        else:
            self.timer_temporal_zombie = QTimer()
            self.timer_temporal_zombie.setInterval(self.logica.tiempo_zombie)
        self.logica.timer_temporal_zombie.setSingleShot(True)
        self.logica.timer_temporal_zombie.timeout.connect(self.logica.
                                                          reanudar_zombies)
        self.logica.timer_temporal_zombie.start()
        self.logica.pausado_reciente_zombie = True

    def reanudar_zombies(self):
        self.logica.pausado_reciente_zombie = False
        self.logica.crear_labels_zombies()
        self.logica.timer_zombies.start()

    def reanudar_soles(self):
        self.logica.pausado_reciente_sol = False
        self.logica.aparecer_soles()
        self.logica.timer_soles.start()
