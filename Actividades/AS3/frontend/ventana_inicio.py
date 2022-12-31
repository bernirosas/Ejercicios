from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
import os
import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        self.label_logo = QLabel(self)
        pixels = QPixmap(p.RUTA_LOGO)
        self.label_logo.setPixmap(pixels)
        self.label_logo.setScaledContents(True)

        self.label_usuario = QLabel("Ingresa tu nombre de usuario", self)
        self.respuesta_usuario = QLineEdit("", self)

        self.label_contraseña = QLabel("Ingresa tu contraseña", self)
        self.respuesta_contraseña = QLineEdit("", self)
        self.respuesta_contraseña.setEchoMode(QLineEdit.Password)

        self.boton_login = QPushButton("Empezar el juego!", self)
        self.boton_login.clicked.connect(self.enviar_login)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox1.addWidget(self.label_usuario)
        hbox1.addWidget(self.respuesta_usuario)

        hbox2.addWidget(self.label_contraseña)
        hbox2.addWidget(self.respuesta_contraseña)

        vbox.addWidget(self.label_logo)
        vbox.addStretch()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.boton_login)
        vbox.addStretch()

        self.setLayout(vbox)

    def enviar_login(self):
        self.senal_enviar_login.emit(self.respuesta_usuario.text(), self.respuesta_contraseña.text())

    def recibir_validacion(self, valid, errores):
        if valid:
            self.hide()
        if "usuario" in errores:
            self.respuesta_usuario.setText("")
            self.respuesta_usuario.setPlaceholderText("usuario inválido")
        if "contraseña" in errores:
            self.respuesta_contraseña.setText("")
            self.respuesta_contraseña.setPlaceholderText("contraseña inválida")
