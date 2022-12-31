from PyQt5 import uic
import os
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QMutex
from dic_parametros import info_json
from PyQt5.QtWidgets import QMessageBox
from time import sleep
ruta = os.path.join("ventana_juego.ui")
window_name, base_class = uic.loadUiType(ruta)


class VentanaJuego(window_name, base_class):
    def __init__(self, senal_enviar_carta, senal_ganar, senal_perder):
        super().__init__()
        self.config()
        self.fichas_ganadas = 0
        self.fichas_otro = 0
        self.data_carta_seleccionada = None
        self.senal_enviar_carta = senal_enviar_carta
        self.senal_ganar = senal_ganar
        self.senal_perder = senal_perder

    def config(self):
        self.setupUi(self)
        self.dic_fichas_jug = {1: self.ficha_1, 2: self.ficha_2,
                               3: self.ficha_3, 4: self.ficha_4,
                               5: self.ficha_5, 6: self.ficha_6,
                               7: self.ficha_7, 8: self.ficha_8,
                               9: self.ficha_9,
                               10: self.ficha_10, 11: self.ficha_11,
                               12: self.ficha_12, 13: self.ficha_13,
                               14: self.ficha_14, 15: self.ficha_15}
        self.dic_fichas_otro = {1: self.otro_1, 2: self.otro_2, 3: self.otro_3,
                                4: self.otro_4, 5: self.otro_5, 6: self.otro_6,
                                7: self.otro_7, 8: self.otro_8, 9: self.otro_9,
                                10: self.otro_10, 11: self.otro_11,
                                12: self.otro_12, 13: self.otro_13,
                                14: self.otro_14, 15: self.otro_15}
        self.cartas = {1: self.carta_1, 2: self.carta_2, 3: self.carta_3,
                       4: self.carta_4, 5: self.carta_5}
        for i in range(1, len(self.dic_fichas_jug) + 1):
            self.dic_fichas_jug[i].hide()
            self.dic_fichas_otro[i].hide()
        self.carta_seleccionada.hide()
        self.carta_oponente.hide()
        self.boton_seleccionar.clicked.connect(self.enviar_carta)

    def ganar(self):
        self.ocultar()
        self.senal_ganar.emit()

    def perder(self):
        self.ocultar()
        self.senal_perder.emit()

    def resultado(self, resolucion, carta_opositora, fichas_ganador,
                  nueva_carta):
        info_carta_opositora = carta_opositora
        ruta_carta_opositora = os.path.join("sprites", "cartas",
                                            (info_carta_opositora["color"] +
                                             "_" +
                                             info_carta_opositora["elemento"] +
                                             "_"
                                             + info_carta_opositora["puntos"]
                                             + ".png"))
        self.carta_oponente.setPixmap(QPixmap(ruta_carta_opositora))
        self.carta_oponente.repaint()
        if resolucion == "ronda_ganada":
            info_ficha = self.data_carta_seleccionada
            ruta_ficha = os.path.join("sprites", "elementos", "fichas",
                                      (info_ficha["elemento"] + "_" +
                                       info_ficha["color"] + ".png"))
            if self.fichas_ganadas <= 15:
                (self.dic_fichas_jug[fichas_ganador].
                 setPixmap(QPixmap(ruta_ficha)))
                self.dic_fichas_jug[fichas_ganador].repaint()
                self.dic_fichas_jug[fichas_ganador].show()
        if resolucion == "ronda_perdida":
            info_ficha = info_carta_opositora
            ruta_ficha = os.path.join("sprites", "elementos", "fichas",
                                      (info_ficha["elemento"] + "_" +
                                       info_ficha["color"] + ".png"))
            if self.fichas_otro <= 15:
                (self.dic_fichas_otro[fichas_ganador].
                 setPixmap(QPixmap(ruta_ficha)))
                self.dic_fichas_otro[fichas_ganador].repaint()
                self.dic_fichas_otro[fichas_ganador].show()
        ruta_carta_nueva = os.path.join("sprites", "cartas",
                                        (nueva_carta["color"] +
                                         "_" +
                                         nueva_carta["elemento"] +
                                         "_"
                                         + nueva_carta["puntos"]
                                         + ".png"))
        if self.data_carta_seleccionada == self.data_carta_1:
            self.data_carta_1 = nueva_carta
            self.cartas[1].setPixmap(QPixmap(ruta_carta_nueva))
            self.cartas[1].repaint()
            ruta_1 = (nueva_carta["color"] + "_" + nueva_carta["elemento"] +
                      "_" + nueva_carta["puntos"] + ".png")
            self.ruta_1 = os.path.join("sprites", "cartas", ruta_1)
        elif self.data_carta_seleccionada == self.data_carta_2:
            self.data_carta_2 = nueva_carta
            self.cartas[2].setPixmap(QPixmap(ruta_carta_nueva))
            self.cartas[2].repaint()
            ruta_2 = (nueva_carta["color"] + "_" + nueva_carta["elemento"]
                      + "_" + nueva_carta["puntos"] + ".png")
            self.ruta_2 = os.path.join("sprites", "cartas", ruta_2)
        elif self.data_carta_seleccionada == self.data_carta_3:
            self.data_carta_3 = nueva_carta
            self.cartas[3].setPixmap(QPixmap(ruta_carta_nueva))
            self.cartas[3].repaint()
            ruta_3 = (nueva_carta["color"] + "_" + nueva_carta["elemento"]
                      + "_" + nueva_carta["puntos"] + ".png")
            self.ruta_3 = os.path.join("sprites", "cartas", ruta_3)
        elif self.data_carta_seleccionada == self.data_carta_4:
            self.data_carta_4 = nueva_carta
            self.cartas[4].setPixmap(QPixmap(ruta_carta_nueva))
            self.cartas[4].repaint()
            ruta_4 = (nueva_carta["color"] + "_" + nueva_carta["elemento"]
                      + "_" + nueva_carta["puntos"] + ".png")
            self.ruta_4 = os.path.join("sprites", "cartas", ruta_4)
        elif self.data_carta_seleccionada == self.data_carta_5:
            self.data_carta_5 = nueva_carta
            self.cartas[5].setPixmap(QPixmap(ruta_carta_nueva))
            self.cartas[5].repaint()
            ruta_5 = (nueva_carta["color"] + "_" + nueva_carta["elemento"]
                      + "_" + nueva_carta["puntos"] + ".png")
            self.ruta_5 = os.path.join("sprites", "cartas", ruta_5)
        sleep(1)
        self.nueva_ronda()

    def enviar_carta(self):
        if self.data_carta_seleccionada:
            dict = {"comando": "carta_seleccionada", "usuario": self.nombre,
                    "carta_selec": self.data_carta_seleccionada}
            self.senal_enviar_carta.emit(dict)
        else:
            self.crear_pop_up("No se ha seleccionado una carta")

    def otro_usuario_carta(self):
        self.carta_oponente.show()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()

    def preparar(self, nombre, usuarios, carta_1, carta_2, carta_3, carta_4,
                 carta_5):
        self.nombre = nombre
        self.data_carta_1 = carta_1
        self.data_carta_2 = carta_2
        self.data_carta_3 = carta_3
        self.data_carta_4 = carta_4
        self.data_carta_5 = carta_5
        ruta_1 = (carta_1["color"] + "_" + carta_1["elemento"] +
                  "_" + carta_1["puntos"] + ".png")
        self.ruta_1 = os.path.join("sprites", "cartas", ruta_1)
        ruta_2 = (carta_2["color"] + "_" + carta_2["elemento"]
                  + "_" + carta_2["puntos"] + ".png")
        self.ruta_2 = os.path.join("sprites", "cartas", ruta_2)
        ruta_3 = (carta_3["color"] + "_" + carta_3["elemento"]
                  + "_" + carta_3["puntos"] + ".png")
        self.ruta_3 = os.path.join("sprites", "cartas", ruta_3)
        ruta_4 = (carta_4["color"] + "_" + carta_4["elemento"]
                  + "_" + carta_4["puntos"] + ".png")
        self.ruta_4 = os.path.join("sprites", "cartas", ruta_4)
        ruta_5 = (carta_5["color"] + "_" + carta_5["elemento"]
                  + "_" + carta_5["puntos"] + ".png")
        self.ruta_5 = os.path.join("sprites", "cartas", ruta_5)
        self.cartas[1].setPixmap(QPixmap(self.ruta_1))
        self.cartas[2].setPixmap(QPixmap(self.ruta_2))
        self.cartas[3].setPixmap(QPixmap(self.ruta_3))
        self.cartas[4].setPixmap(QPixmap(self.ruta_4))
        self.cartas[5].setPixmap(QPixmap(self.ruta_5))
        baraja = info_json("BARAJA_PANTALLA")
        for i in range(1, baraja + 1):
            self.cartas[i].repaint()
        for usuario in usuarios:
            if usuario != nombre:
                contrincante = usuario
        self.label_contrincante.setText(contrincante)
        self.label_contrincante.repaint()
        self.label_jugador.setText(nombre)
        self.label_jugador.repaint()

    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        if (110 <= x <= (110 + 71)) and 390 <= y <= (390 + 111):
            self.data_carta_seleccionada = self.data_carta_1
            self.carta_seleccionada.setPixmap(QPixmap(self.ruta_1))
            self.carta_seleccionada.repaint()
            self.carta_seleccionada.show()
        if (200 <= x <= (200 + 71)) and 390 <= y <= (390 + 111):
            self.data_carta_seleccionada = self.data_carta_2
            self.carta_seleccionada.setPixmap(QPixmap(self.ruta_2))
            self.carta_seleccionada.repaint()
            self.carta_seleccionada.show()
        if (290 <= x <= (290 + 71)) and 390 <= y <= (390 + 111):
            self.data_carta_seleccionada = self.data_carta_3
            self.carta_seleccionada.setPixmap(QPixmap(self.ruta_3))
            self.carta_seleccionada.repaint()
            self.carta_seleccionada.show()
        if (380 <= x <= (380 + 71)) and 390 <= y <= (390 + 111):
            self.data_carta_seleccionada = self.data_carta_4
            self.carta_seleccionada.setPixmap(QPixmap(self.ruta_4))
            self.carta_seleccionada.repaint()
            self.carta_seleccionada.show()
        if (470 <= x <= (470 + 71)) and 390 <= y <= (390 + 111):
            self.data_carta_seleccionada = self.data_carta_5
            self.carta_seleccionada.setPixmap(QPixmap(self.ruta_5))
            self.carta_seleccionada.repaint()
            self.carta_seleccionada.show()

    def se_acabo_tiempo(self, num):
        if num == 1:
            self.data_carta_seleccionada = self.data_carta_1
            self.carta_seleccionada.setPixmap(QPixmap(self.ruta_1))
        if num == 2:
            self.data_carta_seleccionada = self.data_carta_2
            self.carta_seleccionada.setPixmap(QPixmap(self.ruta_2))
        if num == 3:
            self.data_carta_seleccionada = self.data_carta_3
            self.carta_seleccionada.setPixmap(QPixmap(self.ruta_3))
        if num == 4:
            self.data_carta_seleccionada = self.data_carta_4
            self.carta_seleccionada.setPixmap(QPixmap(self.ruta_4))
        if num == 5:
            self.data_carta_seleccionada = self.data_carta_5
            self.carta_seleccionada.setPixmap(QPixmap(self.ruta_5))
        self.carta_seleccionada.repaint()
        self.carta_seleccionada.show()
        self.enviar_carta()

    def nueva_ronda(self):
        self.carta_seleccionada.hide()
        self.data_carta_seleccionada = None
        ruta = os.path.join("sprites", "cartas", "back.png")
        self.carta_oponente.setPixmap(QPixmap(ruta))
        self.carta_oponente.repaint()
        self.carta_oponente.hide()

    def actualizar_interface(self, tiempo):
        self.label_timer.setText(str(tiempo))
        self.label_timer.repaint()

    def crear_pop_up(self, mensaje):
        error = QMessageBox()
        error.setWindowTitle("Ventana de error")
        error.setText("Error")
        error.setInformativeText(mensaje)
        error.setIcon(QMessageBox.Critical)
        error.setDefaultButton(QMessageBox.Ok)
        error.exec_()
