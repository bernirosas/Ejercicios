import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
import os


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        # COMPLETAR
        self.label_logo = QLabel(self)
        ruta = os.path.join("frontend", "assets", "logo.png")

        pixeles = QPixmap(ruta)
        self.label_logo.setPixmap(pixeles)
        self.label_logo.setScaledContents(True)

        self.label_usuario = QLabel("Ingrese su nombre: ", self)
        self.respuesta_usuario = QLineEdit("", self)

        self.label_contraseña = QLabel("Ingrese su contraseña: ", self)
        self.respuesta_contraseña = QLineEdit("", self)
        self.respuesta_contraseña.setEchoMode(QLineEdit.Password)

        self.boton_login = QPushButton("Ingresar", self)
        self.boton_login.clicked.connect(self.enviar_login)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox1.addWidget(self.label_usuario)
        hbox1.addWidget(self.respuesta_usuario)

        hbox2.addWidget(self.label_contraseña)
        hbox2.addWidget(self.respuesta_contraseña)

        vbox.addWidget(self.label_logo)
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.boton_login)
        vbox.addStretch(2)

        self.setLayout(vbox)

    def enviar_login(self):
        self.senal_enviar_login.emit((self.respuesta_usuario.text(), self.respuesta_contraseña.text()))

    def recibir_validacion(self, valid, errores):
        if valid:
            self.hide()
        if "Usuario" in errores:
            self.respuesta_usuario.setText("")
            self.respuesta_usuario.setPlaceholderText("Usuario no válido")
        elif "Contraseña" in errores:
            self.respuesta_contraseña.setText("")
            self.respuesta_contraseña.setPlaceholderText("Contraseña no válida")



if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.show()
    sys.exit(app.exec_())
