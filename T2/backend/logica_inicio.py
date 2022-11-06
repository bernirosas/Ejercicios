from PyQt5.QtCore import QObject, pyqtSignal
#  QTimer, QEventLoop
import parametros


class Logica_inicio(QObject):
    senal_resultado_log_in = pyqtSignal(bool, list)

    def __init__(self) -> None:
        super().__init__()

    def revisar_log_in(self, usuario):
        usuario = str(usuario)
        lista = []
        if not usuario != "":
            lista.append("Nombre de usuario debe tener carácteres "
                         "distintos de vacío.")
        if not (len(usuario) >= parametros.MIN_CARACTERES and
                len(usuario) <= parametros.MAX_CARACTERES):
            lista.append("Nombre de usuario debe tener entre "
                         f"{parametros.MIN_CARACTERES} "
                         f"y {parametros.MAX_CARACTERES} carácteres")
        if not usuario.isalnum():
            lista.append("Nombre de usuario debe contener solo"
                         " carácteres alfanuméricos")

        self.senal_resultado_log_in.emit(len(lista) == 0, lista)
