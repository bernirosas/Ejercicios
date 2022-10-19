from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, list)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, tupla_respuesta):
        errores = []
        usuario, contraseña = tupla_respuesta
        if len(usuario) > p.MAX_CARACTERES or not usuario.isalnum():
            errores.append("Usuario")
        if contraseña != "Contraseña":
            errores.append("Contraseña")
        if len(errores) == 0:
            self.senal_abrir_juego.emit(usuario)
        self.senal_respuesta_validacion.emit(len(errores) == 0, errores)
