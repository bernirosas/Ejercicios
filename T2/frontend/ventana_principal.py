from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox
window_name, base_class = uic.loadUiType("ventana_principal.ui")


class VentanaPrincipal(window_name, base_class):
    senal_abrir_juego = pyqtSignal(str, str)

    def __init__(self) -> None:
        super().__init__()
        self.config()

    def config(self):
        self.setupUi(self)
        self.jugar.clicked.connect(self.asignar_escenario)

    def asignar_escenario(self):
        error = ""
        if self.JardinAbuela.isChecked() and self.SalidaNocturna.isChecked():
            error = "Solo se debe checkear una casilla"
        elif not (self.JardinAbuela.isChecked() or
                  self.SalidaNocturna.isChecked()):
            error = "Se debe checkear una casilla"
        elif self.JardinAbuela.isChecked():
            self.senal_abrir_juego.emit(self.usuario, "jardin_abuela")
            self.hide()
        elif self.SalidaNocturna.isChecked():
            self.senal_abrir_juego.emit(self.usuario, "salida_nocturna")
            self.hide()
        if error != "":
            error_box = QMessageBox()
            error_box.setWindowTitle("Ventana de error")
            error_box.setText("Error")
            error_box.setInformativeText(error)
            error_box.setIcon(QMessageBox.Critical)
            error_box.setDefaultButton(QMessageBox.Ok)
            error_box.exec_()

    def mostrar_principal(self, usuario):
        self.show()
        self.usuario = usuario
