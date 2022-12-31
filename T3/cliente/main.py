from dic_parametros import info_json
import sys
from backend.cliente import Cliente
from backend.interfaz import Interfaz
from PyQt5.QtWidgets import QApplication

#  estructura sacada de AF3
if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    try:
        app = QApplication(sys.argv)
        host = info_json("HOST")
        port = info_json("PORT")
        interfaz = Interfaz()
        cliente = Cliente(host, port)

        cliente.senal_mostrar_ventana_inicio.connect(interfaz.
                                                     mostrar_ventana_inicio)
        interfaz.senal_log_in.connect(cliente.enviar)
        cliente.senal_manejar_mensaje.connect(interfaz.manejar_mensaje)
        cliente.senal_servidor_desconectado.connect(interfaz.
                                                    servidor_desconectado)
        interfaz.senal_volver.connect(cliente.enviar)
        interfaz.senal_volver.connect(interfaz.volver)
        interfaz.senal_enviar_carta.connect(cliente.enviar)
        interfaz.senal_ganar.connect(interfaz.ganar)
        interfaz.senal_perder.connect(interfaz.perder)
        interfaz.senal_volver_final.connect(interfaz.volver_final)
        interfaz.senal_salir.connect(app.exit)
        interfaz.senal_ganador.connect(cliente.enviar)
        sys.exit(app.exec_())

    except ConnectionError as e:
        print("Ocurrió un error.", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente...")
        cliente.salir()
        app.exit()
        sys.exit()
