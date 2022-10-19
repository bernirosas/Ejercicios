from PyQt5.QtCore import QObject, pyqtSignal


class LogicaLogin(QObject):

    # Señales
    senal_input = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.senal_bool = None
        self.senal_input.connect(self.comprobar_usuario)

    def comprobar_usuario(self, usuario, contrasena):
        # Validar si el usuario y la contraseña es correcta y enviar señal
        # emite un bool si es que el usario es aceptado o no
        usu = usuario == 'ADMIN'
        con = contrasena == 'IIC2233'
        if usu and con:
            self.senal_bool.emit(True)
        else:
            self.senal_bool.emit(False)
