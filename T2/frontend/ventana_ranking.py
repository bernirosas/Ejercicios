from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
window_name, base_class = uic.loadUiType("ventana_ranking.ui")


class VentanaRanking(window_name, base_class):
    senal_volver = pyqtSignal()
    senal_actualizar_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.config()

    def config(self):
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver_a_inicio)

    def abrir(self):
        self.senal_actualizar_ranking.emit()
        self.show()

    def actualizar_labels(self, lista):
        if len(lista) >= 1:
            self.ranking_1.setText(f"{lista[0][0]: <14s}"
                                   f"{lista[0][1]} puntos")
        if len(lista) >= 2:
            self.ranking_2.setText(f"{lista[1][0]: <14s}"
                                   f"{lista[1][1]} puntos")
        if len(lista) >= 3:
            self.ranking_3.setText(f"{lista[2][0]: <14s}"
                                   f"{lista[2][1]} puntos")
        if len(lista) >= 4:
            self.ranking_4.setText(f"{lista[3][0]: <14s}"
                                   f"{lista[3][1]} puntos")
        if len(lista) >= 5:
            self.ranking_5.setText(f"{lista[4][0]: <14s}"
                                   f"{lista[4][1]} puntos")

    def volver_a_inicio(self):
        self.hide()
        self.senal_volver.emit()
