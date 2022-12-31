from dic_parametros import info_json
import threading
from cartas import get_penguins
from time import sleep


class Logica:
    def __init__(self, parent):
        # Esto permite ejecutar funciones de la clase Servidor
        self.parent = parent
        self.usuarios = {}
        self.partida_iniciada = False
        self.comenzado = False
        self.lock_login = threading.Lock()
        self.lock_carta = threading.Lock()

    def validar_login(self, nombre):
        with self.lock_login:
            if len(self.usuarios.values()) <= 1:
                if nombre.lower() not in self.usuarios.values():
                    if 1 <= len(nombre) <= 10 and nombre.isalnum():
                        self.usuarios[self.parent.id_cliente - 1] = (nombre.
                                                                     lower())
                        self.parent.log("Jugador ingresa nombre de manera "
                                        "correcta a la sala de espera que no "
                                        "se encuentra llena.")
                        return {
                            "comando": "respuesta_validacion_login",
                            "estado": "aceptado",
                            "nombre_usuario": nombre,
                            "usuarios": ",".join(self.usuarios.values()),
                        }
                    else:
                        error = ("Nombre no tiene entre 1 y 10 " +
                                 "carácteres y/o es alfanumérico.")
                else:
                    error = "Nombre ya registrado"
            else:
                error = "servidor a máxima capacidad"
            self.parent.log("Usuario no puede entrar a sala de espera ya que ")
            self.parent.log(error)
            return {
                "comando": "respuesta_validacion_login",
                "estado": "rechazado",
                "error": error,
                    }

    def procesar_mensaje(self, mensaje, socket_cliente, id_cliente):
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}
        respuesta = None
        if comando == "validar_login":
            respuesta = self.validar_login(
                mensaje["nombre usuario"],
            )
        if comando == "volver":
            self.eliminar_nombre(id_cliente)
        if comando == "carta_seleccionada":
            usuario = mensaje["usuario"]
            usuarioss = list(self.usuarios.values())
            if usuario == usuarioss[0]:
                self.carta_enviada_0 = mensaje["carta_selec"]
                elemento = self.carta_enviada_0["elemento"]
                self.parent.log(f"Usuario {usuario} envío carta "
                                f"de tipo {elemento}")
            if len(usuarioss) >= 2:
                if usuario == usuarioss[1]:
                    self.carta_enviada_1 = mensaje["carta_selec"]
                    elemento = self.carta_enviada_1["elemento"]
                    self.parent.log(f"Usuario {usuario} envío carta "
                                    f"de tipo {elemento}")
            for i in range(0, len(self.parent.sockets.values())):
                mensajee = {"comando": "otro_usuario_envio_carta",
                            "usuario_que_mando": usuario,
                            "carta_opositora": mensaje["carta_selec"]}
                self.parent.enviar_mensaje(mensajee, self.parent.sockets[i])
            if self.carta_enviada_0 and self.carta_enviada_1:
                self.revisar_resultado(self.carta_enviada_0,
                                       self.carta_enviada_1)
        if comando == "reportar_ganador":
            self.ganador = mensaje["ganador"]
            for i in range(0, len(self.parent.sockets.values())):
                if i != id_cliente:
                    mensajee = {"comando": "otro_usuario_gano",
                                "usuario_que_gano": self.ganador}
                    self.parent.enviar_mensaje(mensajee, self.parent.sockets[i])
        return respuesta

    def eliminar_nombre(self, id):
        usuar = self.usuarios.pop(id, None)
        return usuar

    def revisar_resultado(self, carta_enviada_0, carta_enviada_1):
        if not self.ronda_terminada:
            self.parent.log("Revisando resultados")
            self.ronda_terminada = True
            carta_ganadora = None
            usuario_ganador = None
            if carta_enviada_0["elemento"] == carta_enviada_1["elemento"]:
                if int(carta_enviada_0["puntos"]) < int(carta_enviada_1["puntos"]):
                    carta_ganadora = carta_enviada_1
                    usuario_ganador = list(self.usuarios.values())[1]
                if int(carta_enviada_0["puntos"]) > int(carta_enviada_1["puntos"]):
                    carta_ganadora = carta_enviada_0
                    usuario_ganador = list(self.usuarios.values())[0]
            else:
                if ((carta_enviada_0["elemento"] == "agua" and
                    carta_enviada_1["elemento"] == "fuego") or
                    (carta_enviada_0["elemento"] == "nieve" and
                    carta_enviada_1["elemento"] == "agua") or
                    (carta_enviada_0["elemento"] == "fuego" and
                   carta_enviada_1["elemento"] == "nieve")):
                    carta_ganadora = carta_enviada_0
                    usuario_ganador = list(self.usuarios.values())[0]
                else:
                    carta_ganadora = carta_enviada_1
                    usuario_ganador = list(self.usuarios.values())[1]
            if not carta_ganadora:
                self.parent.log("Termina ronda, ocurrió un empate.")
                for sock in self.parent.sockets.keys():
                    self.parent.enviar_mensaje({
                        "comando": "actualizar_ronda",
                        "usuario_ganador": "empate"},
                        self.parent.sockets[sock])
            else:
                self.parent.log("Termina ronda, gana usuario"
                                f" {usuario_ganador}")
                for sock in self.parent.sockets.keys():
                    self.parent.enviar_mensaje({
                        "comando": "actualizar_ronda",
                        "usuario_ganador": usuario_ganador},
                        self.parent.sockets[sock])

    def iniciar_juego(self):
        usuarioss = list(self.usuarios.values())
        self.ganador = None
        self.instanciar_timer_inicial()
        self.mini_timer.start()
        self.contador = 0
        tiempo = info_json("CUENTA_REGRESIVA_INICIO")
        while self.contador < tiempo:
            # el parámetro está en segundos.
            pass
        usuarios_y = " y ".join(usuarioss)
        self.parent.log("Se inicia una partida entre "
                        f"{usuarios_y}")
        self.partida_iniciada = True
        mazo_1 = get_penguins()
        mazo_1["usuario"] = str(usuarioss[0])
        mazo_1["comando"] = "iniciar_juego"
        mazo_1["usuarios"] = ",".join(usuarioss)
        mazo_2 = get_penguins()
        mazo_2["usuario"] = str(usuarioss[1])
        mazo_2["comando"] = "iniciar_juego"
        mazo_2["usuarios"] = ",".join(usuarioss)
        for sock in self.parent.sockets.keys():
            self.parent.enviar_mensaje(mazo_1, self.parent.sockets[sock])
            self.parent.enviar_mensaje(mazo_2, self.parent.sockets[sock])
        self.ronda_terminada = False
        self.iniciar_ronda()
        while not self.ganador:
            if self.ronda_terminada:
                self.ronda_terminada = False
                self.timer_ronda.cancel()
                self.parent.log("Iniciando nueva ronda")
                self.iniciar_ronda()
        self.timer_ronda.cancel()
        self.contador_ronda = 0
        self.parent.log(f"Partida terminada, gana el jugador {self.ganador}")

    def iniciar_ronda(self):
        self.contador_ronda = 0
        self.carta_enviada_0 = None  # la del usuario[0]
        self.carta_enviada_1 = None
        self.timer_ronda = threading.Timer(1, self.actualizar_tiempo_ronda)
        self.timer_ronda.cancel()
        self.timer_ronda = threading.Timer(1, self.actualizar_tiempo_ronda)
        tiempo = info_json("CUENTA_REGRESIVA_RONDA")
        for sock in self.parent.sockets:
            self.parent.enviar_mensaje({
                "comando": "actualizar_ventana_timer_juego",
                "tiempo_restante": tiempo
            }, self.parent.sockets[sock])
        self.timer_ronda.start()

    def actualizar_tiempo_ronda(self):
        if not self.ronda_terminada and not self.ganador:
            if (self.contador_ronda < info_json("CUENTA_REGRESIVA_RONDA")
               and not self.ronda_terminada and not self.ganador):
                self.contador_ronda += 1
                self.timer_ronda = threading.Timer(1, self.
                                                   actualizar_tiempo_ronda)
                self.timer_ronda.start()
                tiempo = (info_json("CUENTA_REGRESIVA_RONDA")
                          - self.contador_ronda)
                for sock in self.parent.sockets:
                    self.parent.enviar_mensaje({
                        "comando": "actualizar_ventana_timer_juego",
                        "tiempo_restante": tiempo
                    }, self.parent.sockets[sock])
            else:
                if not self.ronda_terminada and not self.ganador:
                    self.parent.log("Se acabo el tiempo "
                                    "y se lanza carta al azar")
                    self.timer_ronda.cancel()
                    keys = list(self.usuarios.keys())
                    if not self.carta_enviada_0 and not self.ganador:
                        self.parent.enviar_mensaje({
                            "comando": "forzar_carta"
                        }, self.parent.sockets[keys[0]])
                    sleep(0.1)
                    if not self.carta_enviada_1 and not self.ganador:
                        self.parent.enviar_mensaje({
                            "comando": "forzar_carta"
                        }, self.parent.sockets[keys[1]])

    def instanciar_timer_inicial(self):
        self.mini_timer = threading.Timer(1, self.actualizar_tiempo)
        tiempo = info_json("CUENTA_REGRESIVA_INICIO")
        for sock in self.parent.sockets:
            self.parent.enviar_mensaje({
                "comando": "actualizar_ventana_espera",
                "tiempo_restante": tiempo,
                "usuarios": ",".join(self.usuarios.values())
            }, self.parent.sockets[sock])

    def actualizar_tiempo(self):
        if len(self.usuarios.values()) == 2:
            self.contador += 1
            if self.contador < info_json("CUENTA_REGRESIVA_INICIO"):
                self.mini_timer = threading.Timer(1, self.actualizar_tiempo)
                self.mini_timer.start()
            tiempo_restante = (info_json("CUENTA_REGRESIVA_INICIO")
                               - self.contador)
            if len(self.usuarios.values()) == 2:
                for sock in self.parent.sockets:
                    self.parent.enviar_mensaje({
                        "comando": "actualizar_ventana_espera",
                        "tiempo_restante": tiempo_restante,
                        "usuarios": ",".join(self.usuarios.values())
                    }, self.parent.sockets[sock])
