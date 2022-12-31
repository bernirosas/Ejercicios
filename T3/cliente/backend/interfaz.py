from PyQt5.QtCore import QObject
from frontend.ventana_espera import VentanaEspera
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_final import VentanaFinal
import random
from time import sleep
from PyQt5.QtCore import pyqtSignal


class Interfaz(QObject):
    senal_log_in = pyqtSignal(dict)
    senal_volver = pyqtSignal(dict)
    senal_enviar_carta = pyqtSignal(dict)
    senal_ganar = pyqtSignal()
    senal_perder = pyqtSignal()
    senal_volver_final = pyqtSignal()
    senal_salir = pyqtSignal()
    senal_ganador = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.ventana_inicio = VentanaInicio(self.senal_log_in)
        self.ventana_espera = VentanaEspera(self.senal_volver)
        self.ventana_juego = VentanaJuego(self.senal_enviar_carta,
                                          self.senal_ganar, self.senal_perder)
        self.ventana_final = VentanaFinal(self.senal_volver_final)
        self.nombre = None
        self.ventana_juego.nombre = None
        self.ventana_espera.nombre = None

    def mostrar_ventana_inicio(self):
        self.ventana_inicio.mostrar()

    def servidor_desconectado(self):
        #  da lo mismo que ventana cree el pop up al estar escondidas
        self.ventana_inicio.crear_pop_up("El servidor se"
                                         " ha desconectado repentinamente.")
        self.ventana_espera.hide()
        self.ventana_inicio.hide()
        self.ventana_final.hide()
        self.ventana_juego.hide()
        sleep(5)
        self.senal_salir.emit()

    def login_aceptado(self, usuarios, nombre):
        usuarios = usuarios.split(",")
        self.ventana_inicio.ocultar()
        self.ventana_espera.preparar(usuarios)
        self.usuarios = usuarios
        self.nombre = nombre
        self.ventana_juego.nombre = nombre
        self.ventana_espera.nombre = nombre
        self.ventana_espera.mostrar()
        self.cartas_ganadas_fuego = []
        self.cartas_ganadas_hielo = []
        self.cartas_ganadas_agua = []
        self.fichas_ganadas = 0
        self.fichas_otro = 0

    def volver(self, diccionario):
        self.ventana_espera.ocultar()
        self.ventana_inicio.mostrar()
        self.nombre = None

    def volver_final(self):
        self.ventana_final.ocultar()
        self.ventana_inicio.mostrar()

    def ganar(self):
        self.ventana_final.ganar()
        self.ventana_juego.ocultar()
        self.ventana_final.mostrar()

    def perder(self):
        self.ventana_final.perder()
        self.ventana_juego.ocultar()
        self.ventana_final.mostrar()

    def manejar_mensaje(self, mensaje: dict):
        if mensaje["comando"] == "respuesta_validacion_login":
            if mensaje["estado"] == "aceptado":
                self.login_aceptado(mensaje["usuarios"],
                                    mensaje["nombre_usuario"])
            elif mensaje["estado"] == "rechazado":
                self.ventana_inicio.crear_pop_up(mensaje["error"])
        if mensaje["comando"] == "actualizar_ventana_espera":
            usuarios = mensaje["usuarios"].split(",")
            self.ventana_espera.preparar(usuarios)
            (self.ventana_espera.actualizar_interface
             (mensaje["tiempo_restante"]))
        if mensaje["comando"] == "iniciar_juego":
            if mensaje["usuario"] == self.nombre:
                self.ventana_espera.ocultar()
                self.ventana_juego.mostrar()
                self.usuarios = mensaje["usuarios"].split(",")
                self.mazo = mensaje.copy()
                self.mazo.pop("comando")
                self.mazo.pop("usuario")
                self.mazo.pop("usuarios")
                numeros_elegidos = []
                self.lista_mazo = []
                # barajando cartas
                while len(numeros_elegidos) < 15:
                    num = random.randint(0, 14)
                    if num not in numeros_elegidos:
                        self.lista_mazo.append(self.mazo[str(num)])
                        numeros_elegidos.append(num)
                carta_1 = self.lista_mazo.pop(0)
                carta_2 = self.lista_mazo.pop(0)
                carta_3 = self.lista_mazo.pop(0)
                carta_4 = self.lista_mazo.pop(0)
                carta_5 = self.lista_mazo.pop(0)
                self.ventana_juego.preparar(self.nombre, self.usuarios,
                                            carta_1, carta_2, carta_3, carta_4,
                                            carta_5)
        if mensaje["comando"] == "otro_usuario_envio_carta":
            if self.nombre:
                if mensaje["usuario_que_mando"] == self.nombre:
                    self.carta_elegida = mensaje["carta_opositora"]
                else:
                    self.ventana_juego.otro_usuario_carta()
                    self.carta_opositora = mensaje["carta_opositora"]
                    self.ventana_juego.carta_opositora = self.carta_opositora

        if mensaje["comando"] == "actualizar_ventana_timer_juego":
            self.ventana_juego.actualizar_interface(mensaje["tiempo_restante"])

        if mensaje["comando"] == "ganar_por_omision":
            if mensaje["usuario"] == self.nombre:
                self.ventana_juego.ganar()

        if mensaje["comando"] == "actualizar_ronda":
            sleep(1)
            self.lista_mazo.append(self.carta_elegida)
            nueva_carta = self.lista_mazo.pop(0)
            if mensaje["usuario_ganador"] == self.nombre:
                self.fichas_ganadas += 1
                self.ventana_juego.resultado("ronda_ganada",
                                             self.carta_opositora,
                                             self.fichas_ganadas,
                                             nueva_carta)
                if self.carta_elegida["elemento"] == "fuego":
                    self.cartas_ganadas_fuego.append(self.
                                                     carta_elegida["color"])
                elif self.carta_elegida["elemento"] == "agua":
                    self.cartas_ganadas_agua.append(self.
                                                    carta_elegida["color"])
                elif self.carta_elegida["elemento"] == "nieve":
                    self.cartas_ganadas_hielo.append(self.
                                                     carta_elegida["color"])
                self.gano = False
                if (self.cartas_ganadas_fuego.count("azul") >= 1 and
                    self.cartas_ganadas_agua.count("rojo") >= 1 and
                   self.cartas_ganadas_hielo.count("verde") >= 1):
                    self.gano = True
                elif (self.cartas_ganadas_fuego.count("rojo") >= 1 and
                      self.cartas_ganadas_agua.count("azul") >= 1 and
                      self.cartas_ganadas_hielo.count("verde") >= 1):
                    self.gano = True
                elif (self.cartas_ganadas_fuego.count("verde") >= 1 and
                      self.cartas_ganadas_agua.count("azul") >= 1 and
                      self.cartas_ganadas_hielo.count("rojo") >= 1):
                    self.gano = True
                elif (self.cartas_ganadas_fuego.count("azul") >= 1 and
                      self.cartas_ganadas_agua.count("verde") >= 1 and
                      self.cartas_ganadas_hielo.count("rojo") >= 1):
                    self.gano = True
                elif (self.cartas_ganadas_fuego.count("rojo") >= 1 and
                      self.cartas_ganadas_agua.count("verde") >= 1 and
                      self.cartas_ganadas_hielo.count("azul") >= 1):
                    self.gano = True
                elif (self.cartas_ganadas_fuego.count("verde") >= 1 and
                      self.cartas_ganadas_agua.count("rojo") >= 1 and
                      self.cartas_ganadas_hielo.count("azul") >= 1):
                    self.gano = True
                elif (self.cartas_ganadas_fuego.count("verde") >= 1 and
                      self.cartas_ganadas_fuego.count("rojo") >= 1 and
                      self.cartas_ganadas_fuego.count("azul") >= 1):
                    self.gano = True
                elif (self.cartas_ganadas_hielo.count("verde") >= 1 and
                      self.cartas_ganadas_hielo.count("rojo") >= 1 and
                      self.cartas_ganadas_hielo.count("azul") >= 1):
                    self.gano = True
                elif (self.cartas_ganadas_agua.count("verde") >= 1 and
                      self.cartas_ganadas_agua.count("rojo") >= 1 and
                      self.cartas_ganadas_agua.count("azul") >= 1):
                    self.gano = True
                if self.gano:
                    dict = {"comando": "reportar_ganador", "ganador":
                            self.nombre}
                    self.senal_ganador.emit(dict)
                    self.ventana_juego.ganar()
            elif mensaje["usuario_ganador"] == "empate":
                self.ventana_juego.resultado("ronda_empatada",
                                             self.carta_opositora,
                                             0,
                                             nueva_carta)
            else:  # perdio
                self.fichas_otro += 1
                self.ventana_juego.resultado("ronda_perdida",
                                             self.carta_opositora,
                                             self.fichas_otro,
                                             nueva_carta)

        if mensaje["comando"] == "otro_usuario_gano":
            self.ventana_juego.perder()

        if mensaje["comando"] == "forzar_carta":
            num = random.randint(1, 5)
            self.ventana_juego.se_acabo_tiempo(num)
