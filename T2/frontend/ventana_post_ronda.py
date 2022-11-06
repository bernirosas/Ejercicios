from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
window_name, base_class = uic.loadUiType("ventana_post_ronda.ui")


class VentanaPostRonda(window_name, base_class):
    senal_salir = pyqtSignal()
    senal_pasar_ronda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_ronda.clicked.connect(self.pasar_ronda)

    def salir(self):
        self.senal_salir.emit()
        self.hide()

    def pasar_ronda(self):
        if not self.perdio:
            self.senal_pasar_ronda.emit()
            self.hide()

    def abrir(self, perdio, ronda, soles, zombies, ptje_total, ptje_ronda):
        self.show()
        self.perdio = perdio
        self.label_ronda.setText(str(ronda))
        self.label_soles.setText(str(soles))
        self.label_zombies.setText(str(zombies))
        self.label_ptje_total.setText(str(ptje_total))
        self.label_ptje_ronda.setText(str(ptje_ronda))
        if perdio:
            self.label_gano.hide()
        elif not perdio:
            self.label_perdio.hide()
