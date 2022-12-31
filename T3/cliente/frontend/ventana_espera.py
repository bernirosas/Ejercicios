from PyQt5 import uic
import os
ruta = os.path.join("ventana_espera.ui")
window_name, base_class = uic.loadUiType(ruta)


class VentanaEspera(window_name, base_class):
    def __init__(self, senal_volver):
        super().__init__()
        self.config()
        self.senal_volver = senal_volver

    def config(self):
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)

    def volver(self):
        diccionario = {
            "comando": "volver",
            "nombre usuario": self.nombre}
        self.senal_volver.emit(diccionario)

    def preparar(self, usuarios: list):
        if len(usuarios) >= 1:
            self.jugador_1.setText(usuarios[0])
            self.jugador_1.repaint()
        if len(usuarios) >= 2:
            self.jugador_2.setText(usuarios[1])
            self.jugador_2.repaint()
        else:
            self.jugador_2.setText("Esperando...")
            self.jugador_2.repaint()

    def actualizar_interface(self, tiempo):
        self.label_numero.setText(str(tiempo))
        self.label_numero.repaint()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
