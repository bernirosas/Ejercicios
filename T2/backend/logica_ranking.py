from PyQt5.QtCore import QObject, pyqtSignal
import os


class LogicaRanking(QObject):
    senal_actualizar_labels = pyqtSignal(list)

    def __init__(self) -> None:
        super().__init__()

    def sort_help(self, linea):
        return int(linea[1])

    def actualizar(self):
        ruta = os.path.join("puntajes.txt")
        partidas = []
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas_sucias = archivo.readlines()
        for linea_sucia in lineas_sucias:
            linea = linea_sucia.strip().split(",")
            partidas.append(linea)
        partidas.sort(key=self.sort_help, reverse=True)
        self.senal_actualizar_labels.emit(partidas)
