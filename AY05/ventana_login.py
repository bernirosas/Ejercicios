import os
import re
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QHBoxLayout, QVBoxLayout, QLineEdit)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class VentanaLogin(QWidget):

    #Señales

    senal_respuesta = pyqtSignal(bool)
    senal_enviar_login = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.init_gui()

        
    def init_gui(self):

        #Ventana

        self.setWindowTitle('AvanzadaAPP')
        self.setGeometry(600, 400, 500, 500)
        self.ventana = QWidget(self)

        #Imagen

        self.logo = QLabel(self)
        self.logo.setGeometry(100, 100, 100, 100)
        logo = os.path.join('img', 'logo.png')
        pixeles = QPixmap(logo)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)

        #Usuario

        self.label_user = QLabel('Ingrese su nombre de usuario: ', self)
        self.edit_user = QLineEdit()

        #Contraseña

        self.label_contra = QLabel('Ingrese su contraseña: ', self)
        self.edit_contra = QLineEdit(self)
        self.edit_contra.setEchoMode(2)

        #Boton
        
        self.boton = QPushButton('Iniciar sesión', self)
        self.boton.clicked.connect(self.enviar_login)

        #Layouts

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()


        hbox1.addWidget(self.label_user)
        hbox1.addWidget(self.edit_user)

        hbox2.addWidget(self.label_contra)
        hbox2.addWidget(self.edit_contra)

        vbox.addWidget(self.logo)
        vbox.addStretch()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.boton)
        vbox.addStretch()

        self.setLayout(vbox)

        #Conexiones

        

    def enviar_login(self):
        #Enviar señal para validar login
        usuario = self.edit_user.text()
        contra = self.edit_contra.text()

        
        self.senal_enviar_login.emit(usuario, contra)

    def recibir_login(self, valido):
        #Abrir ventana principal si es correcto el login
        if valido:
            self.hide()
            respuesta = True
            return respuesta

        else:  
            respuesta = False
            return respuesta


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaLogin()
    ventana.show()
    sys.exit(app.exec_())