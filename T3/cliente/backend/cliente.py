from PyQt5.QtCore import pyqtSignal, QObject
import socket
import json
from threading import Thread
from cripto import encriptar, desencriptar


class Cliente(QObject):
    senal_mostrar_ventana_inicio = pyqtSignal()
    senal_manejar_mensaje = pyqtSignal(dict)
    senal_servidor_desconectado = pyqtSignal()

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.iniciar_cliente()

    def iniciar_cliente(self):
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()
            self.senal_mostrar_ventana_inicio.emit()

        except ConnectionError as e:
            print(f"\n-ERROR: El servidor no está inicializado. {e}-")

    def comenzar_a_escuchar(self):
        thread = Thread(target=self.escuchar_servidor, daemon=True)
        thread.start()

    def escuchar_servidor(self):
        try:
            while self.conectado:
                mensaje = self.recibir()
                if mensaje:
                    self.senal_manejar_mensaje.emit(mensaje)

        except ConnectionError as e:
            self.senal_servidor_desconectado.emit()
            print("ERROR: el servidor se ha desconectado", e)

    def recibir(self):
        tamano_chunk = 32
        largo_mensaje_bytes = self.socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_mensaje_bytes, byteorder="big")
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            nro_bloque_bytes = self.socket_cliente.recv(4)
            self.nro_bloque = int.from_bytes(nro_bloque_bytes,
                                             byteorder="little")
            tamano_chunk = min(largo_mensaje - len(bytes_mensaje), 32)
            bytes_mensaje += self.socket_cliente.recv(tamano_chunk)
        if not bytes_mensaje:
            return
        ultimo = 32 - tamano_chunk
        self.socket_cliente.recv(ultimo)
        bytes_mensaje = desencriptar(bytes_mensaje)
        mensaje = self.decodificar_mensaje(bytes_mensaje)
        return mensaje

    def enviar(self, mensaje):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        bytes_mensaje = encriptar(bytes_mensaje)
        largo_mensaje_bytes = len(bytes_mensaje).to_bytes(4, byteorder="big")
        nuevo_mensaje = bytearray()
        nuevo_mensaje += largo_mensaje_bytes
        nro_bloque = 1
        while len(bytes_mensaje) % 32 != 0:
            bytes_mensaje += b'\x00'
        for i in range(0, len(bytes_mensaje), 32):
            chunk = bytes_mensaje[i:i+32]
            nro_bloque_bytes = nro_bloque.to_bytes(4, byteorder="little")
            nuevo_mensaje += nro_bloque_bytes + chunk
            nro_bloque += 1
        self.socket_cliente.sendall(nuevo_mensaje)

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode()
            return mensaje_bytes
        except json.JSONDecodeError:
            print("ERROR: No se pudo codificar el mensaje desde cliente")
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        try:
            mensaje = json.loads(mensaje_bytes)
            return mensaje
        except json.JSONDecodeError:
            print("ERROR: No se pudo decodificar el mensaje desde cliente")
            return {}
