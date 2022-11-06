from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
import parametros as p
from PyQt5.QtWidgets import QMessageBox
from random import randint
window_name, base_class = uic.loadUiType("ventana_juego_jardin.ui")


class VentanaJuegoJardin(window_name, base_class):
    senal_click_pantalla = pyqtSignal(int, int)
    senal_click_lugar = pyqtSignal(int, int)
    senal_boton_iniciar = pyqtSignal()
    senal_salir = pyqtSignal()
    senal_recoger_sol = pyqtSignal(int, int)
    senal_label_guis = pyqtSignal(tuple, QLabel)
    senal_label_hielo = pyqtSignal(tuple, QLabel)
    senal_label_zombies = pyqtSignal(QLabel, QLabel)
    senal_sol_colocado = pyqtSignal(QLabel)
    senal_pausa = pyqtSignal()
    senal_resume = pyqtSignal()
    senal_avanzar = pyqtSignal()
    senal_cheatcode_sun = pyqtSignal()
    senal_cheatcode_kil = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.config()
        self.click_planta = True
        self.click_lugar = False
        self.iniciado = False
        self.casillas = {1: self.A1, 2: self.A2, 3: self.A3, 4: self.A4,
                         5: self.A5, 6: self.A6, 7: self.A7, 8: self.A8,
                         9: self.A9, 10: self.A10, 11: self.B1, 12: self.B2,
                         13: self.B3, 14: self.B4, 15: self.B5, 16: self.B6,
                         17: self.B7, 18: self.B8, 19: self.B9, 20: self.B10}
        self.label_me_ha_salvado.hide()
        self.label_me_comieron.hide()
        self.zombies_ate_you_brains.hide()
        self.crazy_gigante.hide()
        self.pausado = False
        self.s = False
        self.u = False
        self.k = False
        self.i = False

    def actualizar_interfaz_post_ronda(self, bool, antes):
        if antes:
            if bool:  # perdio jugador
                self.zombies_ate_you_brains.show()
                self.label_me_comieron.show()
            if not bool:
                self.crazy_gigante.show()
                self.label_me_ha_salvado.show()
                self.crazy.hide()
        if not antes:
            self.label_me_ha_salvado.hide()
            self.zombies_ate_you_brains.hide()
            self.crazy_gigante.hide()
            self.crazy.show()
            self.label_me_comieron.hide()

    def config(self):
        self.setupUi(self)
        self.boton_iniciar.clicked.connect(self.iniciar_juego)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_pausa.clicked.connect(self.pausar)
        self.boton_avanzar.clicked.connect(self.avanzar)

    def avanzar(self):
        self.senal_avanzar.emit()

    def pausar(self):
        if not self.pausado:
            self.senal_pausa.emit()

    def crear_label_guis(self, pos):
        label = QLabel(self)
        label.setGeometry(pos[0], pos[1], pos[2], pos[3])
        label.setScaledContents(True)
        label.setPixmap(QPixmap(p.ruta_guisante1))
        label.show()
        self.senal_label_guis.emit(pos, label)

    def crear_label_hielo(self, pos):
        label = QLabel(self)
        label.setGeometry(pos[0], pos[1], pos[2] + 10, pos[3] - 10)
        label.setScaledContents(True)
        label.setPixmap(QPixmap(p.ruta_guisante_hielo1))
        label.show()
        self.senal_label_hielo.emit(pos, label)

    def salir(self):
        self.senal_salir.emit()

    def senal_inicial_zombie(self, pos_1, pos_2):
        label_1 = QLabel(self)
        label_1.setGeometry(pos_1[0], pos_1[1], pos_1[2], pos_1[3])
        label_1.setScaledContents(True)
        random = randint(1, 2)  # para que sea walker o runner aleatorio
        if random == 1:
            label_1.setPixmap(QPixmap(p.ruta_zombie_walker_1))
            label_1.walker = True
        elif random == 2:
            label_1.setPixmap(QPixmap(p.ruta_zombie_runner_2))
            label_1.walker = False
        label_1.show()
        label_1.x = pos_1[0]
        label_1.y = pos_1[1]
        label_1.ancho = pos_1[2]
        label_1.alto = pos_1[3]
        label_2 = QLabel(self)
        label_2.setGeometry(pos_2[0], pos_2[1], pos_2[2], pos_2[3])
        label_2.setScaledContents(True)
        random = randint(1, 2)  # para que sea walker o runner aleatorio
        if random == 1:
            label_2.setPixmap(QPixmap(p.ruta_zombie_walker_1))
            label_2.walker = True
        elif random == 2:
            label_2.setPixmap(QPixmap(p.ruta_zombie_runner_2))
            label_2.walker = False
        label_2.x = pos_2[0]
        label_2.y = pos_2[1]
        label_2.ancho = pos_2[2]
        label_2.alto = pos_2[3]
        label_2.show()
        self.senal_label_zombies.emit(label_1, label_2)

    def iniciar_juego(self):
        self.senal_boton_iniciar.emit()
        self.iniciado = True

    def abrir(self, usuario):
        self.show()
        self.usuario = usuario

    def actualizar_guisante(self, label, pos):
        label.move(pos[0], pos[1])

    def actualizar_posicion_zombie(self, label, pos):
        label.move(pos[0], pos[1])

    def actualizar_zombie(self, casilla, ruta):
        casilla.setPixmap(QPixmap(ruta))
        casilla.repaint()

    #  código de actividad en clases
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.click_planta:
            x = event.pos().x()
            y = event.pos().y()
            self.senal_click_pantalla.emit(x, y)
        elif event.button() == Qt.LeftButton and self.click_lugar:
            x = event.pos().x()
            y = event.pos().y()
            self.senal_click_lugar.emit(x, y)
        elif event.button() == Qt.RightButton:
            x = event.pos().x()
            y = event.pos().y()
            self.senal_recoger_sol.emit(x, y)

    def mouseMoveEvent(self, event):
        if self.click_lugar:
            if self.planta == "planta_verde":
                (self.copia_planta_verde.
                 move(event.pos().x() - 35, event.pos().y() - 40))
            if self.planta == "girasol":
                (self.copia_girasol.
                 move(event.pos().x() - 35, event.pos().y() - 40))
            if self.planta == "planta_azul":
                (self.copia_planta_azul.
                 move(event.pos().x() - 35, event.pos().y() - 40))
            if self.planta == "papa":
                (self.copia_papa.
                 move(event.pos().x() - 35, event.pos().y() - 40))
            if self.planta == "pala":
                (self.copia_pala.
                 move(event.pos().x() - 35, event.pos().y() - 30))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.click_lugar:
            if self.planta == "planta_verde":
                (self.copia_planta_verde.
                 move(20, 140))
            if self.planta == "girasol":
                (self.copia_girasol.
                 move(20, 20))
            if self.planta == "planta_azul":
                (self.copia_planta_azul.
                 move(20, 260))
            if self.planta == "papa":
                (self.copia_papa.
                 move(20, 380))
            if self.planta == "pala":
                (self.copia_pala.
                 move(20, 510))
            x = event.pos().x()
            y = event.pos().y()
            self.senal_click_lugar.emit(x, y)

    def keyPressEvent(self, event):
        if event.text() == "p":
            self.pausar()
        if event.text() == "s":
            self.s = True
        if event.text() == "u" and self.s:
            self.u = True
        if event.text() == "n" and self.u:
            self.senal_cheatcode_sun.emit()
            self.u = False
            self.s = False
        if event.text() != "u" and event.text() != "s":
            self.s = False
        if event.text() != "n" and event.text() != "u":
            self.u = False
        if event.text() == "k":
            self.k = True
        if event.text() == "i" and self.k:
            self.i = True
        if event.text() == "l" and self.i:
            self.senal_cheatcode_kil.emit()
            self.k = False
            self.i = False
        if event.text() != "i" and event.text() != "k":
            self.k = False
        if event.text() != "l" and event.text() != "i":
            self.i = False

    def actualizar_planta(self, casilla, ruta):
        casilla.setPixmap(QPixmap(ruta))
        casilla.repaint()

    def validar_planta_elegida(self, bool, planta):
        if bool:
            self.click_lugar = True
            self.click_planta = False
            self.planta = planta
        #  En el caso de que haya apretado una de las casillas
        #  No pasa nada

    def actualizar_datos(self, label, text):
        label.setText(text)
        label.repaint()
        label.resize(label.sizeHint())

    def colocar_sol(self, x, y, ancho, alto):
        sol = QLabel(self)
        sol.setGeometry(x, y, ancho, alto)
        sol.setScaledContents(True)
        sol.setPixmap(QPixmap(p.ruta_sol))
        sol.setAttribute(Qt.WA_TransparentForMouseEvents)
        sol.setMouseTracking(True)
        sol.x = x
        sol.y = y
        sol.ancho = ancho
        self.senal_sol_colocado.emit(sol)
        sol.show()

    def crear_pop_up(self, mensaje):
        error = QMessageBox()
        error.setWindowTitle("Ventana de error")
        error.setText("Error")
        error.setInformativeText(mensaje)
        error.setIcon(QMessageBox.Critical)
        error.setDefaultButton(QMessageBox.Ok)
        error.exec_()

    def actualizar_posicion_planta_1(self, casilla):
        casilla.setPixmap(QPixmap(p.ruta_girasol1))
        casilla.repaint()

    def actualizar_posicion_planta_2(self, casilla):
        casilla.setPixmap(QPixmap(p.ruta_girasol2))
        casilla.repaint()
