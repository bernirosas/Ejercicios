from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
window_name, base_class = uic.loadUiType("ventana_inicio.ui")


class VentanaInicio(window_name, base_class):
    senal_log_in = pyqtSignal(str)
    senal_salir = pyqtSignal()
    senal_abir_principal = pyqtSignal(str)
    senal_abrir_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.config()
        self.show()

    def config(self):
        self.setupUi(self)
        self.jugar.clicked.connect(self.enviar)
        self.salir.clicked.connect(self.salir_app)
        self.ranking.clicked.connect(self.ver_ranking)

    def enviar(self):
        self.senal_log_in.emit(self.usuario.text())

    def salir_app(self):
        self.hide()
        self.senal_salir.emit()

    def abrir(self):
        self.show()

    def ver_ranking(self):
        self.hide()
        self.senal_abrir_ranking.emit()

    def log_in(self, resultado, lista_error):
        if resultado is True:
            self.hide()
            us = str(self.usuario.text())
            self.senal_abir_principal.emit(us)
        elif resultado is False:
            #  código pop up de:
            #  https://www.techwithtim.net/tutorials/pyqt5-tutorial/messageboxes/
            texto_error = "\n".join(lista_error)
            error = QMessageBox()
            error.setWindowTitle("Ventana de error")
            error.setText("Error")
            error.setInformativeText(texto_error)
            error.setIcon(QMessageBox.Critical)
            error.setDefaultButton(QMessageBox.Ok)
            error.exec_()
