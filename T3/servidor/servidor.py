from threading import Thread, Lock
import json
from cripto import encriptar, desencriptar
import socket
from logica import Logica
#  estructura principal de AF3


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.logica = Logica(self)
        self.id_cliente = 0
        self.log("".center(80, "-"))
        self.log("Inicializando servidor...")
        self.sockets = {}
        self.iniciar_servidor()
        self.lock_id = Lock()

    def iniciar_servidor(self):
        self.socket_servidor = socket.socket(socket.AF_INET,
                                             socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.log(f"Servidor escuchando en {self.host}: {self.port}")
        self.comenzar_a_aceptar()

    def comenzar_a_aceptar(self):
        thread = Thread(target=self.aceptar_clientes, daemon=True)
        thread.start()
        thread_revisar_condiciones = Thread(target=self.revisar_condiciones,
                                            daemon=True)
        thread_revisar_condiciones.start()

    def revisar_condiciones(self):
        while True:
            if (len(self.logica.usuarios.values()) == 2 and not
               self.logica.comenzado):
                self.logica.comenzado = True
                self.log("Hay dos usuarios, comenzando"
                         " cuenta regresiva...")
                self.logica.iniciar_juego()
            if (len(self.logica.usuarios.values()) < 2 and
               self.logica.comenzado and not self.logica.ganador):
                self.logica.partida_iniciada = False
                self.logica.comenzado = False
                self.log("Se detiene la jugada")
                self.logica.mini_timer.cancel()

    def aceptar_clientes(self):
        while True:
            try:
                socket_cliente, direccion = self.socket_servidor.accept()
                with self.lock_id:
                    self.log(f"Cliente con dirección {direccion} ha"
                             " sido aceptado")
                    thread_cliente = Thread(target=(self.escuchar_cliente),
                                            args=(self.id_cliente,
                                                  socket_cliente),
                                            daemon=True,
                                            )
                    thread_cliente.start()
                    self.sockets[self.id_cliente] = socket_cliente
                    self.id_cliente += 1

            except ConnectionError as error:
                self.log(f"Se ha producido un error de conexión: {error}")

    def escuchar_cliente(self, id_cliente, socket_cliente):
        self.log(f"Comenzando a escuchar al cliente {id_cliente}...")
        vinculado = True
        while vinculado:
            try:
                mensaje = self.recibir_mensaje(socket_cliente)
                if not mensaje:
                    vinculado = False
                    raise ConnectionResetError

                respuesta = self.logica.procesar_mensaje(mensaje,
                                                         socket_cliente,
                                                         id_cliente)
                if respuesta:
                    self.enviar_mensaje(respuesta, socket_cliente)
                    self.notificar_otros_usuarios(id_cliente, respuesta)
            except ConnectionError:
                self.log("Se ha producido un error de conexión al intentar"
                         " establecer conexión con el jugador.")
                id = 0
                self.logica.ganador = True
                for sock in self.sockets.values():
                    if sock == socket_cliente:
                        id_jugador = id
                    id += 1
                usuar = self.eliminar_cliente(id_jugador, socket_cliente)  
                # tiene usuario
                for usuario in list(self.logica.usuarios.values()):
                    if self.logica.partida_iniciada and usuar:
                        self.logica.ganador = usuario
                        for sock in self.sockets.keys():
                            self.enviar_mensaje({"comando": "ganar_por_omision",
                                                "usuario": usuario},
                                                self.sockets[sock])
                        self.log(f"El ganador es {self.logica.ganador}")

    def notificar_otros_usuarios(self, id_cliente_nuevo, respuesta):
        pass

    def recibir_mensaje(self, socket_jugador):
        if socket_jugador in self.sockets.values():
            tamano_chunk = 32
            largo_mensaje_bytes = socket_jugador.recv(4)
            largo_mensaje = int.from_bytes(largo_mensaje_bytes,
                                           byteorder="big")
            bytes_mensaje = bytearray()
            while len(bytes_mensaje) < largo_mensaje:
                nro_bloque_bytes = socket_jugador.recv(4)
                self.nro_bloque = int.from_bytes(nro_bloque_bytes,
                                                 byteorder="little")
                tamano_chunk = min(largo_mensaje - len(bytes_mensaje), 32)
                bytes_mensaje += socket_jugador.recv(tamano_chunk)
            ultimo = 32 - tamano_chunk
            socket_jugador.recv(ultimo)
            if not bytes_mensaje:
                return
            bytes_mensaje = desencriptar(bytes_mensaje)
            mensaje = self.decodificar_mensaje(bytes_mensaje)
            return mensaje

    def enviar_mensaje(self, mensaje, socket_jugador) -> None:
        try:
            if socket_jugador in self.sockets.values():
                bytes_mensaje = self.codificar_mensaje(mensaje)
                bytes_mensaje = encriptar(bytes_mensaje)
                largo_mensaje_bytes = (len(bytes_mensaje).
                                       to_bytes(4, byteorder="big"))
                nuevo_mensaje = bytearray()
                nuevo_mensaje += largo_mensaje_bytes
                nro_bloque = 1
                while len(bytes_mensaje) % 32 != 0:
                    bytes_mensaje += b'\x00'
                for i in range(0, len(bytes_mensaje), 32):
                    chunk = bytes_mensaje[i:i+32]
                    nro_bloque_bytes = (nro_bloque.
                                        to_bytes(4, byteorder="little"))
                    nuevo_mensaje += nro_bloque_bytes + chunk
                    nro_bloque += 1
                socket_jugador.sendall(nuevo_mensaje)
                return False
        except ConnectionResetError:
            self.log("Se ha producido un error de conexión al intentar"
                     " establecer conexión con el jugador.")
            id = 0
            self.logica.ganador = True
            for sock in self.sockets.values():
                if sock == socket_jugador:
                    id_jugador = id
                id += 1
            usuar = self.eliminar_cliente(id_jugador, socket_jugador)  
            # tiene usuario
            for usuario in list(self.logica.usuarios.values()):
                if self.logica.partida_iniciada and usuar:
                    self.logica.ganador = usuario
                    for sock in self.sockets.keys():
                        self.enviar_mensaje({"comando": "ganar_por_omision",
                                             "usuario": usuario},
                                            self.sockets[sock])
                    self.log(f"El ganador es {self.logica.ganador}")
            return True

    def eliminar_cliente(self, id_cliente, socket_cliente):
        try:
            self.log(f"Borrando socket del cliente {id_cliente}.")
            socket_cliente.close()
            self.sockets.pop(id_cliente, None)
            usuar = self.logica.eliminar_nombre(id_cliente)
            usuarios = ",".join(self.logica.usuarios.values())
            self.notificar_otros_usuarios(id_cliente, {"usuarios": usuarios})
            return usuar

        except KeyError as e:
            self.log(f"ERROR: {e}")

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode()
            return mensaje_bytes
        except json.JSONDecodeError:
            self.log("ERROR: No se pudo codificar el mensaje desde servidor")
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        try:
            mensaje = json.loads(mensaje_bytes)
            return mensaje
        except json.JSONDecodeError:
            self.log("ERROR: No se pudo decodificar mensaje desde servidor")
            return dict()

    def log(self, mensaje: str):
        print("|" + mensaje.center(90, " ") + "|")
