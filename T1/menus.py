from cargar import cargar_entrenadores
from parametros import ENERGIA_ENTRENAMIENTO, MIN_AUMENTO_EXPERIENCIA,\
                       MAX_AUMENTO_EXPERIENCIA
from random import randint
from liga_programon import Liga_programon
from funciones_utiles import revisar_input_correcto, salir_del_juego


def menu_inicio():
    print("Felicidades! Lograste Proteger el templo de maestros ayudantes del"
          " malvado canciller, quién decidió escapar a una dimensión paralela")
    print("donde te desafía (tu yo de la otra dimensión) a un DCCampeonato.\n"
          "Practica a continuación.")
    lista_de_entrenadores = cargar_entrenadores("entrenadores.csv")
    print("              *** Menu de inicio ***              \n"
          "--------------------------------------------------\n"
          "Por favor elige un entrenador:")
    contador = 0
    for entrenador in lista_de_entrenadores:
        lista_nombres = []
        for programon in entrenador.programones:
            lista_nombres.append(programon.nombre)
        programones = ", ".join(lista_nombres)
        uwu = str(contador + 1) + "]"
        print(f"[{uwu: <4s} {entrenador.nombre}: {programones}")
        contador += 1
    uwu = str(contador + 1) + "]"
    print(f"[{uwu: <4s} Salir")
    opcion = revisar_input_correcto({str(i + 1) for i in range(contador + 1)})
    if opcion == "menu":  # si el input está mal retorna eso
        return menu_inicio()
    if opcion == contador + 1:
        print("¿Estás segur@ de que quieres salir del juego?\n"
              "[1] Si\n[2] No")
        opcion = revisar_input_correcto({"1", "2"})
        if opcion == "menu" or opcion == 2:
            # si introduce algo no válido se vuelve al menú
            return menu_inicio()
        return salir_del_juego()
    entrenador_elegido = lista_de_entrenadores[opcion - 1]
    liga_programon = Liga_programon(lista_de_entrenadores, entrenador_elegido)
    return menu_entrenador(liga_programon)


def menu_entrenador(liga_programon):
    print(f"Menú de {liga_programon.entrenador_elegido.nombre}!")
    print("  *** Menú Entrenador ***  \n"
          "---------------------------\n"
          "[1] Entrenamiento\n"
          "[2] Simular ronda\n"
          "[3] Resumen campeonato\n"
          "[4] Crear objetos\n"
          "[5] Utilizar objeto\n"
          "[6] Estado entrenador\n"
          "[7] Volver\n"
          "[8] Salir")
    opcion = revisar_input_correcto({str(i + 1) for i in range(8)})
    if opcion == "menu":
        return menu_entrenador(liga_programon)
    if opcion == 1:
        return menu_entrenamiento(liga_programon)
    if opcion == 2:
        resultado = liga_programon.simular_ronda()
        if resultado == "menu_entrenador":
            return menu_entrenador(liga_programon)
        elif resultado == "menu_inicio":  # el jugador gano o perdió
            print("Se terminó el juego!\n"
                  "[1] Jugar de nuevo\n[2] Salir")
            opcion = revisar_input_correcto({"1", "2"})
            if opcion == "menu":  # si el input está mal retorna eso
                return menu_entrenador(liga_programon)
            if opcion == 1:
                return menu_inicio()
            elif opcion == 2:
                return salir_del_juego()
    if opcion == 3:
        liga_programon.resumen_campeonato()
        return menu_entrenador(liga_programon)
    if opcion == 4:
        op = liga_programon.entrenador_elegido.crear_objetos()
        if op == "volver":
            return menu_entrenador(liga_programon)
        elif op == "salir":
            print("¿Estás segur@ de que quieres salir del juego?\n"
                  "[1] Si\n[2] No")
            opcion = revisar_input_correcto({"1", "2"})
            if opcion == "menu" or opcion == 2:
                # si introduce algo no válido se vuelve al menú
                return menu_entrenamiento(liga_programon)
            return salir_del_juego()
    if opcion == 5:
        op = menu_usar_objeto(liga_programon)
        if op == "salir":
            print("¿Estás segur@ de que quieres salir del juego?\n"
                  "[1] Si\n[2] No")
            opcion = revisar_input_correcto({"1", "2"})
            if opcion == "menu" or opcion == 2:
                # si introduce algo no válido se vuelve al menú
                return menu_entrenador(liga_programon)
            return salir_del_juego()
        elif op == "volver":
            return menu_entrenador(liga_programon)
    if opcion == 6:
        op = liga_programon.entrenador_elegido.estado_entrenador()
        if op == "salir":
            print("¿Estás segur@ de que quieres salir del juego?\n"
                  "[1] Si\n[2] No")
            opcion = revisar_input_correcto({"1", "2"})
            if opcion == "menu" or opcion == 2:
                # si introduce algo no válido se vuelve al menú
                return menu_entrenador(liga_programon)
            return salir_del_juego()
        elif op == "volver":
            return menu_entrenador(liga_programon)
    if opcion == 7:
        print("¿Estás segur@ de que quieres ir al menú de inicio?\n"
              "Cualquier proceso será perdido.\n"
              "[1] Si\n[2] No")
        opcion = revisar_input_correcto({"1", "2"})
        if opcion == "menu" or opcion == 2:
            # si introduce algo no válido se vuelve al menú
            return menu_entrenador(liga_programon)
        return menu_inicio()
    if opcion == 8:
        print("¿Estás segur@ de que quieres salir del juego?\n"
              "[1] Si\n[2] No")
        opcion = revisar_input_correcto({"1", "2"})
        if opcion == "menu" or opcion == 2:
            # si introduce algo no válido se vuelve al menú
            return menu_entrenador(liga_programon)
        return salir_del_juego()


def menu_entrenamiento(liga_programon):
    print("  *** Menú de entrenamiento***  \n"
          "--------------------------------\n"
          "Elija un programon para entrenar:")
    contador = 1
    for programon in liga_programon.entrenador_elegido.programones:
        uwu = str(contador) + "]"
        print(f"[{uwu: <4s}{programon.nombre}")
        contador += 1
    uwu = str(contador) + "]"
    print(f"[{uwu: <4s}Volver")
    uwu = str(contador + 1) + "]"
    print(f"[{uwu: <4s}Salir")
    opcion = revisar_input_correcto({str(i + 1) for i in range(contador + 1)})
    if opcion == "menu":  # input incorrecto
        return menu_entrenamiento(liga_programon)
    elif opcion == contador:
        return menu_entrenador(liga_programon)
    elif opcion == contador + 1:
        print("¿Estás segur@ de que quieres salir del juego?\n"
              "[1] Si\n[2] No")
        opcion = revisar_input_correcto({"1", "2"})
        if opcion == "menu" or opcion == 2:
            # si introduce algo no válido se vuelve al menú
            return menu_entrenamiento(liga_programon)
        return salir_del_juego()
    else:
        # no se cobra energía si no hay suficiente
        if liga_programon.entrenador_elegido.energia >= ENERGIA_ENTRENAMIENTO:
            energia_anterior = liga_programon.entrenador_elegido.energia
            liga_programon.entrenador_elegido.energia -= ENERGIA_ENTRENAMIENTO
            programon_elegido = liga_programon.\
                entrenador_elegido.programones[opcion - 1]
            experiencia_anterior = programon_elegido.experiencia
            print(f"Has elegido a {programon_elegido.nombre}.")
            experiencia_sumada = randint(MIN_AUMENTO_EXPERIENCIA,
                                         MAX_AUMENTO_EXPERIENCIA)
            programon_elegido.experiencia += experiencia_sumada
            print(f"La energía de {liga_programon.entrenador_elegido.nombre}"
                  f" disminuyó"
                  f" de {energia_anterior} hasta "
                  f"{liga_programon.entrenador_elegido.energia}."
                  f" La experiencia de {programon_elegido.nombre} pasó de "
                  f"{experiencia_anterior} hasta "
                  f"{programon_elegido.experiencia}")
            return menu_entrenador(liga_programon)
        else:
            print("No hay suficiente energía para realizar la acción.")
            return menu_entrenador(liga_programon)


def menu_usar_objeto(liga_programon):
    print("    *** Objetos disponibles ***    \n"
          "-----------------------------------")
    contador = 1
    for objeto in liga_programon.entrenador_elegido.objetos:
        uwu = str(contador) + "]"
        print(f"[{uwu: <4s}{objeto.nombre}")
        contador += 1
    uwu = str(contador) + "]"
    print(f"[{uwu: <4s}Volver")
    uwu = str(contador + 1) + "]"
    print(f"[{uwu: <4s}Salir")
    opcion = revisar_input_correcto({str(i + 1) for i in range(contador + 1)})
    if opcion == "menu":  # input incorrecto
        return menu_usar_objeto(liga_programon)
    elif opcion == contador:
        return "volver"
    elif opcion == contador + 1:
        return "salir"
    else:
        objeto_a_usar = liga_programon.entrenador_elegido.objetos[opcion - 1]
        print("  *** Menú de objetos***  \n"
              "--------------------------------\n"
              "Elija un programon para aplicarle el objeto:")
        contador = 1
        for programon in liga_programon.entrenador_elegido.programones:
            uwu = str(contador) + "]"
            print(f"[{uwu: <4s}{programon.nombre}")
            contador += 1
        uwu = str(contador) + "]"
        print(f"[{uwu: <4s}Volver")
        uwu = str(contador + 1) + "]"
        print(f"[{uwu: <4s}Salir")
        opcion = revisar_input_correcto({str(i + 1)
                                         for i in range(contador + 1)})
        if opcion == "menu":  # input incorrecto
            return menu_usar_objeto(liga_programon)
        elif opcion == contador:
            return menu_usar_objeto(liga_programon)
        elif opcion == contador + 1:
            print("¿Estás segur@ de que quieres salir del juego?\n"
                  "[1] Si\n[2] No")
            opcion = revisar_input_correcto({"1", "2"})
            if opcion == "menu" or opcion == 2:
                # si introduce algo no válido se vuelve al menú
                return menu_usar_objeto(liga_programon)
            return salir_del_juego()
        programon_a_aplicar = \
            liga_programon.entrenador_elegido.programones[opcion - 1]
        ataque_anterior = programon_a_aplicar.ataque
        defensa_anterior = programon_a_aplicar.defensa
        vida_anterior = programon_a_aplicar.vida
        objeto_a_usar.aplicar_objeto(programon_a_aplicar)
        liga_programon.entrenador_elegido.objetos.remove(objeto_a_usar)
        if objeto_a_usar.tipo == "baya":
            print(f"Programón beneficiado: {programon_a_aplicar.nombre}\n"
                  f"Objeto utilizado: {objeto_a_usar.nombre}"
                  f" (Tipo {objeto_a_usar.tipo})\n"
                  f"Aumento vida: {programon_a_aplicar.vida - vida_anterior}\n"
                  f"La vida subió de {vida_anterior} a"
                  f" {programon_a_aplicar.vida}\n")
        if objeto_a_usar.tipo == "pocion":
            print(f"Programón beneficiado: {programon_a_aplicar.nombre}\n"
                  f"Objeto utilizado: {objeto_a_usar.nombre}"
                  f" (Tipo {objeto_a_usar.tipo})\n"
                  f"Aumento ataque: "
                  f"{programon_a_aplicar.ataque - ataque_anterior}\n"
                  f"El ataque subió de {ataque_anterior} a "
                  f"{programon_a_aplicar.ataque}\n")
        if objeto_a_usar.tipo == "caramelo":
            print(f"Programón beneficiado: {programon_a_aplicar.nombre}\n"
                  f"Objeto utilizado: {objeto_a_usar.nombre}"
                  f" (Tipo {objeto_a_usar.tipo})\n"
                  f"Aumento vida: {programon_a_aplicar.vida - vida_anterior}\n"
                  f"La vida subió de {vida_anterior} a "
                  f"{programon_a_aplicar.vida}\n"
                  f"Aumento ataque: "
                  f"{programon_a_aplicar.ataque - ataque_anterior}\n"
                  f"El ataque subió de "
                  f"{ataque_anterior} a {programon_a_aplicar.ataque}\n"
                  f"Aumento defensa: "
                  f"{programon_a_aplicar.defensa - defensa_anterior}\n"
                  f"La defensa subió de {defensa_anterior} a "
                  f"{programon_a_aplicar.defensa}\n")
    return menu_usar_objeto(liga_programon)


menu_inicio()
