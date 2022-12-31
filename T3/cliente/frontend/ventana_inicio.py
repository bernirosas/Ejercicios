from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
ruta = "ventana_inicio.ui"
window_name, base_class = uic.loadUiType(ruta)


class VentanaInicio(window_name, base_class):

    def __init__(self, senal_log_in):
        super().__init__()
        self.config()
        self.senal_log_in = senal_log_in

    def config(self):
        self.setupUi(self)
        self.boton_enviar.clicked.connect(self.enviar)
        self.mostrar()

    def enviar(self):
        diccionario = {
            "comando": "validar_login",
            "nombre usuario": self.nombre.text()}
        self.senal_log_in.emit(diccionario)

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()

    def crear_pop_up(self, mensaje):
        error = QMessageBox()
        error.setWindowTitle("Ventana de error")
        error.setText("Error")
        error.setInformativeText(mensaje)
        error.setIcon(QMessageBox.Critical)
        error.setDefaultButton(QMessageBox.Ok)
        error.exec_()
