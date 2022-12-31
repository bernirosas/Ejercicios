from tablero import print_tablero
# idea de ejericicios propuestos
from validar import coordenada_valida, revisar_input_correcto, \
                    validar_bestias_cercanas, verificar_ganar, \
                    descubrimiento_de_casillas
from os import path
from manejo_partidas import guardar, calcular_y_guardar_puntaje, \
                            cargar_partida, crear_nuevo_tablero, \
                            terminado_func, ver_ranking
from os.path import isfile


def descubrir_sector(tablero_de_jugador, tablero_de_bestias,
                     nombre_usuario):
    print("Por favor ingrese una coordenada válida de la forma [Letra:Número] "
          "que desee descubrir:\nRecuerde que Letra corresponde a la columna "
          "y Número a la fila. Ej: A:2 \n"
          "Ingrese [0] para volver al menú de juego")
    # Se pide la coordenada de esta manera para facilitar el procesamiento
    # y hacer que sea más inmune a errores.
    coordenada = coordenada_valida(tablero_de_jugador)
    # función se asegura de tener una coordenada válida
    if coordenada == "menu":
        return menu_de_juego(nombre_usuario, tablero_de_jugador,
                             tablero_de_bestias)
    if coordenada == "sector":
        return descubrir_sector(tablero_de_jugador, tablero_de_bestias,
                                nombre_usuario)
    fila = coordenada[0]
    columna = coordenada[1]
    if tablero_de_bestias[fila][columna] == "N":  # se usa el tablero oculto
        print("La celda contiene a una bestia.\nPerdiste el juego :(\n"
              "Revelando posiciones de bestias...")
        print_tablero(tablero_de_bestias)
        calcular_y_guardar_puntaje(tablero_de_jugador,
                                   tablero_de_bestias,
                                   nombre_usuario)
        # se asegura de que al perder no se pueda seguir jugando la partida
        return menu_de_inicio(nombre_usuario,
                              tablero_de_jugador, tablero_de_bestias)
    elif tablero_de_jugador[fila][columna].isdigit() is True:
        # la fila elegida corresponde a un número lo que significa que ya
        # fue elegida. Vuelve a descubrir sector.
        print("Sector fue previamente descubierto.\n"
              "Porfavor elija otro sector.")
        return descubrir_sector(tablero_de_jugador, tablero_de_bestias,
                                nombre_usuario)
    else:
        print("Felicidades, no había ninguna bestia en la celda seleccionada")
        bestias_cercanas = validar_bestias_cercanas(tablero_de_jugador,
                                                    tablero_de_bestias, fila,
                                                    columna)
        tablero_de_jugador[fila][columna] = str(bestias_cercanas)
        print(f"Hay {bestias_cercanas} bestia(s) en las celdas contiguas")
        if bestias_cercanas == 0:  # Descubrir todas
            tablero_de_jugador = descubrimiento_de_casillas(tablero_de_jugador,
                                                            tablero_de_bestias,
                                                            fila, columna)
        ganar = verificar_ganar(tablero_de_jugador)
        if ganar:
            print("Felicidades, ¡ganaste!")
            calcular_y_guardar_puntaje(tablero_de_jugador,
                                       tablero_de_bestias,
                                       nombre_usuario)
            return menu_de_inicio(nombre_usuario,
                                  tablero_de_jugador, tablero_de_bestias)
    return menu_de_juego(nombre_usuario, tablero_de_jugador,
                         tablero_de_bestias)


def salir_del_juego(nombre_usuario="", tablero_de_bestias=[],
                    tablero_de_jugador=[]):
    print("¿Estás seguro de que deseas salir del juego? \n"
          "[1] SI \n[2] NO")
    opcion = revisar_input_correcto({"1", "2"})
    if opcion == 2:
        return menu_de_inicio(nombre_usuario,
                              tablero_de_jugador, tablero_de_bestias)
    elif opcion == 1:
        print("Lamentamos verte ir.\n"
              "¡Nos vemos pronto!")


def menu_de_inicio(nombre_usuario="", tablero_de_jugador=[],
                   tablero_de_bestias=[]):
    print("Bienvenido joven Programawan, fui informado que usted "
          "nos visita desde un lugar lejano y es mi deber acompañarlo "
          "en su práctica para derrotar al Gran Maestro.\n"
          "Por favor seleccione alguna de las siguientes opciones"
          " para comenzar Star Advanced "
          "para comenzar su viaje: \n"
          "[1] Comenzar una partida nueva.\n"
          "[2] Cargar una partida.\n"
          "[3] Ver rankings de puntajes.\n"
          "[0] Salir del juego.")
    nombre_usuario = ""
    opcion = revisar_input_correcto({"0", "1", "2", "3"})
    if opcion == 0:
        return salir_del_juego(nombre_usuario, tablero_de_bestias,
                               tablero_de_jugador)
    if opcion == 1:
        print("Ha seleccionado comenzar una nueva partida.")
        nombre_usuario = input("Por favor ingrese su nombre de usuario: ")
        nombre_usuario = nombre_usuario.strip()
        # solo acepta números y letras para evitar errores
        if not nombre_usuario.isalnum():
            print("Nombre inválido, debe contener solo números y/o letras.")
            return menu_de_inicio(nombre_usuario, tablero_de_bestias,
                                  tablero_de_jugador)
        ruta_guardar = path.join("partidas", f"{nombre_usuario}.txt")
        existe = isfile(ruta_guardar)
        terminado = False
        if existe:
            terminado = terminado_func(ruta_guardar)  # revisa si se terminó
        # partida anterior partida anterior de jugador si esta existe
        if existe and not terminado:
            print("¿Está seguro de que desea comenzar una nueva partida?\n"
                  "Se perderá el progreso guardado.")
            print("[1] Omitir mensaje.\n[0] Volver al menú.")
            opcion = revisar_input_correcto({"0", "1"})
            if opcion == 0:
                return menu_de_inicio()
            elif opcion == 1:
                pass
        tableros = crear_nuevo_tablero()
        tablero_de_bestias = tableros[0]
        tablero_de_jugador = tableros[1]
        guardar(nombre_usuario, tablero_de_jugador, tablero_de_bestias)
        return menu_de_juego(nombre_usuario, tablero_de_jugador,
                             tablero_de_bestias)
    elif opcion == 2:
        print("Ha seleccionado cargar una partida.")
        nombre_usuario = str(input("Por favor ingrese el nombre de usuario "
                               "que registró previamente: "))
        ruta_guardar = path.join("partidas", f"{str(nombre_usuario)}.txt")
        if not nombre_usuario.isalnum():
            print("Nombre inválido, debe contener solo números y/o letras.")
            return menu_de_inicio(nombre_usuario, tablero_de_bestias,
                                  tablero_de_jugador)
        print("Cargando partida...")
        cargar = cargar_partida(nombre_usuario)
        if cargar is False:  # revisa si existe partida a cargar.
            return menu_de_inicio(nombre_usuario, tablero_de_bestias,
                                  tablero_de_jugador)
        terminado = terminado_func(ruta_guardar)
        if terminado is True:  # revisa si partida anterior terminó
            return menu_de_inicio()
        tablero_de_bestias = cargar[0]
        tablero_de_jugador = cargar[1]
        return menu_de_juego(nombre_usuario, tablero_de_jugador,
                             tablero_de_bestias)
    elif opcion == 3:
        ruta = path.join("puntajes.txt")
        ver_ranking(ruta)
        print("Por favor seleccione una de las siguientes opciones: \n"
              "[1] Volver al menú principal. \n"
              "[0] Salir del juego.\n")
        opcion_ranking = revisar_input_correcto({"0", "1"})
        if opcion_ranking == 0:
            return salir_del_juego(nombre_usuario,
                                   tablero_de_bestias,
                                   tablero_de_jugador)
        elif opcion_ranking == 1:
            return menu_de_inicio(nombre_usuario,
                                  tablero_de_jugador, tablero_de_bestias)


def menu_de_juego(nombre_usuario, tablero_de_jugador, tablero_de_bestias):
    print("Tablero actual:\n")
    print_tablero(tablero_de_jugador)
    print("Por favor seleccione alguna de las siguientes opciones"
          " para continuar: \n"
          "[1] Descubrir un sector.\n"
          "[2] Guardar la partida.\n"
          "[0] Salir de la partida y volver al menú principal.")
    opcion_juego = revisar_input_correcto({"0", "1", "2"})
    if opcion_juego == 0:
        print("¿Desea guardar la partida?")
        print(" [1] SI \n [2] NO \n [0] Volver al menú de juego")
        input_guardar = revisar_input_correcto({"0", "1", "2"})
        if input_guardar == 1:
            guardar(nombre_usuario, tablero_de_jugador, tablero_de_bestias)
        if input_guardar == 0:
            return menu_de_juego(nombre_usuario, tablero_de_jugador,
                                 tablero_de_bestias)
        return menu_de_inicio(nombre_usuario, tablero_de_jugador,
                              tablero_de_bestias)

    elif opcion_juego == 1:   # Descubrir un sector
        descubrir_sector(tablero_de_jugador, tablero_de_bestias,
                         nombre_usuario)
        return menu_de_juego(nombre_usuario, tablero_de_jugador,
                             tablero_de_bestias)

    elif opcion_juego == 2:
        guardar(nombre_usuario, tablero_de_jugador, tablero_de_bestias)
        return menu_de_juego(nombre_usuario, tablero_de_jugador,
                             tablero_de_bestias)


menu_de_inicio()
