from servidor import Servidor
import sys
from dic_parametros import info_json


#  estructura sacada de AF3
if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    host = info_json("HOST")
    port = info_json("PORT")
    servidor = Servidor(host, port)

    try:
        while True:
            input("[Presione Ctrl+C para cerrar]".center(82, "+") + "\n")
    except KeyboardInterrupt:
        print("Cerrando servidor...")
        servidor.socket_servidor.close()
        sys.exit()
