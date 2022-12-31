from funciones_utiles import revisar_input_correcto, salir_del_juego
from random import randint, choice


class Liga_programon:
    def __init__(self, lista_de_entrenadores, entrenador_elegido):
        self.lista_de_entrenadores = lista_de_entrenadores
        self.ronda_actual = 1
        self.campeon = ""
        self.siguen = lista_de_entrenadores[:]
        self.entrenador_elegido = entrenador_elegido
        self.perdedores = []
        # Acordar de bajarla cuando no sigan

    def resumen_campeonato(self):
        siguen_nombres = []
        for entrenador in self.siguen:
            siguen_nombres.append(entrenador.nombre)
        siguen = ", ".join(siguen_nombres)
        participantes = []
        for entrenador in self.lista_de_entrenadores:
            participantes.append(entrenador.nombre)
        participantes = ", ".join(participantes)
        print("                             Resumen Campeonato     "
              "                         \n"
              "-------------------------------------------------------"
              "---------------------\n"
              f"Participantes: {participantes}\n"
              f"Ronda actual: {self.ronda_actual}\n"
              f"Entrenadores que siguen en la competencia: {siguen}\n")

    def simular_ronda(self):
        print("    *** Elige tu luchador ***   \n"
              "--------------------------------")
        contador = 1
        for programon in self.entrenador_elegido.programones:
            uwu = str(contador) + "]"
            print(f"[{uwu: <4s}{programon.nombre}")
            contador += 1
        uwu = str(contador) + "]"
        print(f"[{uwu: <4s}Volver")
        # se centra para que se vea bien, si hay 100 o más entrenadores
        # tan solo se corre y desalinea
        uwu = str(contador + 1) + "]"
        print(f"[{uwu: <4s}Salir")
        opcion = revisar_input_correcto({str(i + 1)
                                        for i in range(contador + 1)})
        if opcion == "menu":  # input incorrecto, avisa en consola
            return self.simular_ronda()
        elif opcion == contador:
            return "menu_entrenador"
        elif opcion == contador + 1:
            print("¿Estás segur@ de que quieres salir del juego?\n"
                  "[1] Si\n[2] No")
            opcion = revisar_input_correcto({"1", "2"})
            if opcion == "menu" or opcion == 2:
                # si introduce algo no válido se vuelve al menú
                return self.simular_ronda()
            return salir_del_juego()
        else:
            programon_elegido = self.entrenador_elegido.\
                                programones[opcion - 1]
            print(f"Has elegido a {programon_elegido.nombre}!")
            print("Armando parejas para competir...")
            nro_entrenadores = len(self.siguen)
            armar = self.siguen[:]
            parejas = []
            for i in range(int(nro_entrenadores/2)):
                nro_random = randint(1, len(armar) - 1)
                poppear = armar.pop(nro_random)
                pareja = [armar[0], poppear]
                parejas.append(pareja)
                armar.pop(0)
            print("                                  Ronda "
                  f"{self.ronda_actual}                                   \n"
                  "-----------------------------------------------------------"
                  "-----------------")
            for pareja in parejas:
                if pareja[0].nombre == self.entrenador_elegido.nombre:
                    programon_lucha_1 = programon_elegido
                else:
                    programon_lucha_1 = choice(pareja[0].programones)
                if pareja[1].nombre == self.entrenador_elegido.nombre:
                    programon_lucha_2 = programon_elegido
                else:
                    programon_lucha_2 = choice(pareja[1].programones)
                print(f"{pareja[0].nombre} usando al "
                      f"programón {programon_lucha_1.nombre}"
                      f", se enfrenta a {pareja[1].nombre} usando el programon"
                      f" {programon_lucha_2.nombre}")
                resultado_1 = programon_lucha_1.luchar(programon_lucha_2)
                if resultado_1 == "gano":
                    print(f"{pareja[0].nombre} ha ganado la batalla.")
                    self.siguen.remove(pareja[1])
                    pareja[1].perdedor = True
                    self.perdedores.append(pareja[1])
                elif resultado_1 == "pierdo":
                    print(f"{pareja[1].nombre} ha ganado la batalla.")
                    self.siguen.remove(pareja[0])
                    pareja[0].perdedor = True
                    self.perdedores.append(pareja[0])

            for entrenador in self.siguen:
                entrenador.energia = 100
            self.ronda_actual += 1
            if len(self.siguen) == 1:
                self.campeon = self.siguen[0].nombre
                print("El ganador es ...")
                print(f"{self.campeon}!")
                if self.entrenador_elegido.perdedor is True:
                    print("Has perdido el juego! Mejor suerte para la "
                          "próxima.\n")
                else:
                    print("Felicidades! Has ganado el juego.")
                return "menu_inicio"
            if self.entrenador_elegido.perdedor is True:
                print("Has perdido el juego! Mejor suerte para la próxima.\n")
                return "menu_inicio"
            else:
                print("Has ganado la batalla!")
                return "menu_entrenador"
