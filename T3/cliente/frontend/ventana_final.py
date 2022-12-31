from PyQt5 import uic
import os
ruta = os.path.join("ventana_final.ui")
window_name, base_class = uic.loadUiType(ruta)


class VentanaFinal(window_name, base_class):
    def __init__(self, senal_volver_final):
        super().__init__()
        self.config()
        self.senal_volver_final = senal_volver_final

    def config(self):
        self.setupUi(self)
        self.label_ganaste.hide()
        self.label_perdiste.hide()
        self.boton_volver.clicked.connect(self.volver)

    def volver(self):
        self.senal_volver_final.emit()

    def ganar(self):
        self.label_ganaste.show()

    def perder(self):
        self.label_perdiste.show()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
