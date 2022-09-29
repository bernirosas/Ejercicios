from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel
from parametros import PUNTAJE_INICIAL, TECLA_ABAJO, TECLA_ARRIBA, TECLA_DERECHA, TECLA_IZQUIERDA, TIEMPO_JUEGO
import parametros as p
from PyQt5 import uic

# Recuerda que estamos usando QT Designer :eyes:
# CARGAR ARCHIVO AQUÍ
window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)
# COMPLETAR:
class VentanaJuego(window_name, base_class):  # pylint: disable=E0602

    senal_iniciar_juego = pyqtSignal()
    senal_tecla = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def mostrar_ventana(self, usuario):
        self.casilla_nombre = QLabel(f"{usuario}", self)
        self.casilla_puntaje = QLabel(str(PUNTAJE_INICIAL), self)
        self.casilla_tiempo = QLabel(str(TIEMPO_JUEGO), self)
        self.show()
        self.senal_iniciar_juego.emit()

    def keyPressEvent(self, event):
        if event.key() == TECLA_ABAJO:
            self.senal_tecla.emit("D")
        elif event.key() == TECLA_ARRIBA:
            self.senal_tecla.emit("U")
        elif event.key() == TECLA_DERECHA:
            self.senal_tecla.emit("R")
        elif event.key() == TECLA_IZQUIERDA:
            self.senal_tecla.emit("L")

    def init_gui(self):
        self.setWindowTitle("Ventana de Juego")
        self.boton_salir.clicked.connect(self.salir)

    def actualizar_topos(self, topos):
        for topo in topos:
            topo.topo_label.setParent(self)
            topo.topo_label.setVisible(True)
            topo.topo_label.move(topo.pos_topo.x(), topo.pos_topo.y())

    def mover_martillo(self, martillo):
        martillo.martillo_label.setParent(self)
        martillo.martillo_label.setVisible(True)
        martillo.martillo_label.move(martillo.pos_martillo.x(),
                                     martillo.pos_martillo.y())

    def actualizar_datos(self, tiempo, puntaje):
        self.casilla_tiempo.setText(tiempo)
        self.casilla_tiempo.repaint()

        self.casilla_puntaje.setText(puntaje)
        self.casilla_puntaje.repaint()

    def salir(self):
        self.close()
