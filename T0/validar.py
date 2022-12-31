from string import ascii_lowercase as letras
from math import ceil
from parametros import PROB_BESTIA


def funcion_miscelanea(tablero_de_jugador, tablero_de_bestias, fila, columna):
    if tablero_de_jugador[fila][columna] not in "0123456789":
        # cheackear si la celda fue revisada para no caer en loop
        bestias_cercanas = validar_bestias_cercanas(tablero_de_jugador,
                                                    tablero_de_bestias,
                                                    fila, columna)
        tablero_de_jugador[fila][columna] = str(bestias_cercanas)
        # revisar si esta es cero, en cuyo caso se llama de nuevo
        if bestias_cercanas == 0:
            tablero_de_jugador = descubrimiento_de_casillas(tablero_de_jugador,
                                                            tablero_de_bestias,
                                                            fila, columna)
    return tablero_de_jugador


def revisar_input_correcto(opciones_correctas: set):
    # Esta función se asegura de que el usuario ingresó una opción válida
    # Se basó en función de la actividad AF1
    input_jugador = input()
    if input_jugador in opciones_correctas:
        return int(input_jugador)
    else:
        print("Opción no válida, vuelva a intentarlo.")
        return revisar_input_correcto(opciones_correctas)


def coordenada_valida(tablero_de_jugador):
    largo = len(tablero_de_jugador)
    ancho = len(tablero_de_jugador[0])
    diccionario_comprension = {letras[i].upper(): i
                               for i in range(len(letras))}
    input_jugador = input()
    if input_jugador == "0":
        return "menu"
    if ":" not in input_jugador:
        print("No olvidar "":"" para ingresar coordenada válida.")
        return "sector"
    input_jugador = input_jugador.strip().split(":")
    columna = input_jugador[0]  # checkear si es una letra
    if columna.isalpha() and len(columna) == 1:
        columna = columna.upper()
    else:
        print("Columna ingresada no válida. Debe ser una letra.")
        return "sector"
    fila = input_jugador[1]  # checkear que sea un dígito
    if fila.isdigit() and "." not in fila:
        fila = int(fila)  # Checkear que sea un entero
    else:
        print("Fila ingresada no válida. Deber ser un número entero.")
        return "sector"
    numero_columna = diccionario_comprension[columna]
    if numero_columna >= 0 and numero_columna < ancho and \
       fila < largo and fila >= 0:
        return fila, numero_columna
    else:
        print("Coordenada fuera de rango")
        return "sector"


def validar_bestias_cercanas(tablero_de_jugador, tablero_de_bestias,
                             fila, columna):
    largo = len(tablero_de_jugador)  # Largo = 8 ancho = 5
    ancho = len(tablero_de_jugador[0])
    cantidad_bestias = 0
    # checkae arriba, abajo, izquierda, derecha
    if fila <= (largo - 2) and fila >= 0:  # cheackear abajo
        if tablero_de_bestias[fila + 1][columna] == "N":
            cantidad_bestias += 1
    if fila > 0:  # checkeamos arriba
        if tablero_de_bestias[fila - 1][columna] == "N":
            cantidad_bestias += 1
    if columna > 0:  # checkear izquierda
        if tablero_de_bestias[fila][columna - 1] == "N":
            cantidad_bestias += 1
    if columna <= (ancho - 2) and columna >= 0:  # checkear derecha
        if tablero_de_bestias[fila][columna + 1] == "N":
            cantidad_bestias += 1
    if fila <= (largo - 2) and fila >= 0 and columna > 0:
        # cheackear abajo e izquierda
        if tablero_de_bestias[fila + 1][columna - 1] == "N":
            cantidad_bestias += 1
    if fila > 0 and columna <= (ancho - 2) and columna >= 0:
        # checkeamos arriba y derecha
        if tablero_de_bestias[fila - 1][columna + 1] == "N":
            cantidad_bestias += 1
    if columna > 0 and fila > 0:  # checkear izquierda y arriba
        if tablero_de_bestias[fila - 1][columna - 1] == "N":
            cantidad_bestias += 1
    if columna <= (ancho - 2) and fila <= (largo - 2) and fila >= 0:
        # checkear derecha y abajo
        if tablero_de_bestias[fila + 1][columna + 1] == "N":
            cantidad_bestias += 1
    return cantidad_bestias


def verificar_ganar(tablero_de_jugador):
    ancho_largo = (len(tablero_de_jugador))*(len(tablero_de_jugador[0]))
    cantidad_bestias = ceil(ancho_largo*PROB_BESTIA)
    contador_de_desbloqueos = 0
    for fila in tablero_de_jugador:
        for columna in fila:
            if columna in "0123456789":
                contador_de_desbloqueos += 1
    if contador_de_desbloqueos == (ancho_largo - cantidad_bestias):
        return True
    else:
        return False


def descubrimiento_de_casillas(tablero_de_jugador, tablero_de_bestias,
                               fila, columna):
    print("Cero bestias detectadas, se procederá a "
          "despejar celdas contiguas...")
    largo = len(tablero_de_jugador)  # Largo = 8 ancho = 5
    ancho = len(tablero_de_jugador[0])
    if fila <= (largo - 2) and fila >= 0:  # checkear abajo
        tablero_de_jugador = funcion_miscelanea(tablero_de_jugador,
                                                tablero_de_bestias,
                                                fila + 1, columna)
        # funcion miscelanea realiza varias acciones para
        # asegurar el revelamiento de forma ordenada sin loop
    if fila > 0:  # checkear arriba
        tablero_de_jugador = funcion_miscelanea(tablero_de_jugador,
                                                tablero_de_bestias,
                                                fila - 1, columna)
    if columna > 0:
        tablero_de_jugador = funcion_miscelanea(tablero_de_jugador,
                                                tablero_de_bestias,
                                                fila, columna - 1)
        # checkear izquierda
    if columna <= (ancho - 2) and columna >= 0:
        tablero_de_jugador = funcion_miscelanea(tablero_de_jugador,
                                                tablero_de_bestias,
                                                fila, columna + 1)
        # checkear derecha
    if fila <= (largo - 2) and fila >= 0 and columna > 0:
        tablero_de_jugador = funcion_miscelanea(tablero_de_jugador,
                                                tablero_de_bestias,
                                                fila + 1, columna - 1)
        # checkear abajo e izquierda
    if fila > 0 and columna <= (ancho - 2) and columna >= 0:
        tablero_de_jugador = funcion_miscelanea(tablero_de_jugador,
                                                tablero_de_bestias,
                                                fila - 1, columna + 1)
        # checkeamos arriba y derecha
    if columna > 0 and fila > 0:
        tablero_de_jugador = funcion_miscelanea(tablero_de_jugador,
                                                tablero_de_bestias,
                                                fila - 1, columna - 1)
        # arriba e izquierda
    if columna <= (ancho - 2) and fila <= (largo - 2) and fila >= 0:
        # checkear derecha y abajo
        tablero_de_jugador = funcion_miscelanea(tablero_de_jugador,
                                                tablero_de_bestias,
                                                fila + 1, columna + 1)
    return tablero_de_jugador
