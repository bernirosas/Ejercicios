from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, set)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario, contrasena):
        set_errores = set()
        if not usuario.isalnum(): #si no es alfanumérico
            set_errores.add("usuario")
        if contrasena in p.CONTRASENAS_PROHIBIDAS:
            set_errores.add("contraseña")
        if len(set_errores) == 0:
            self.senal_abrir_juego.emit(usuario)
        self.senal_respuesta_validacion.emit(len(set_errores) == 0, set_errores)
