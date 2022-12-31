from os import path
from os.path import isfile
from parametros import PROB_BESTIA, POND_PUNT
from math import ceil
from random import randint
from validar import revisar_input_correcto


def sort_help(linea):
    return int(linea[1])


def ver_ranking(ruta):
    print("Ha seleccionado ver ranking de puntajes.")
    ranking_puntajes = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas_sucias = archivo.readlines()
    for linea_sucia in lineas_sucias:
        linea = linea_sucia.strip().split(":")
        ranking_puntajes.append(linea)
    ranking_puntajes.sort(key=sort_help, reverse=True)
    # ordenamos el ranking de la lisra
    if ranking_puntajes != []:
        print("Los 10 mejores puntajes registrados son:")
        if len(ranking_puntajes) <= 10:
            maximo = len(ranking_puntajes)
        else:
            maximo = 10
        for i in range(maximo):
            print(": ".join(ranking_puntajes[i]))
    else:
        print("No existen registros previos, "
              "juegue una partida para crear registro.")


def posicion_random_func(lista, numero_maximo) -> int:
    numero_random = randint(0, numero_maximo)
    # asegura un número al azar nuevo para una lista
    if numero_random not in lista:
        return numero_random
    else:
        return posicion_random_func(lista, numero_maximo)


def guardar(nombre_usuario, tablero_de_jugador, tablero_de_bestias):
    ruta_guardar = path.join("partidas", f"{nombre_usuario}.txt")
    # Recordar describir en read me
    with open(ruta_guardar, "w", encoding="utf-8") as archivo:
        escribir = "Tablero actual jugador:\n"
        escribir += f"Ancho:\n{len(tablero_de_jugador[0])}\n"
        escribir += f"Largo:\n{len(tablero_de_jugador)}\n"
        for fila in tablero_de_jugador:
            escribir += "-".join(fila) + "\n"
        escribir += "Tablero oculto de bestias: \n"
        for fila in tablero_de_bestias:
            escribir += "-".join(fila) + "\n"
        archivo.write(escribir)
    print("Partida guardada")
    return


def calcular_y_guardar_puntaje(tablero_de_jugador, tablero_de_bestias,
                               nombre_usuario) -> int:
    guardar(nombre_usuario, tablero_de_jugador, tablero_de_bestias)
    ancho_largo = (len(tablero_de_bestias))*(len(tablero_de_bestias[0]))
    cantidad_bestias = ceil(ancho_largo*PROB_BESTIA)
    encontradas = 0
    for fila in tablero_de_jugador:
        for columna in fila:
            if str(columna) in "0123456789":
                encontradas += 1
    puntaje_final = POND_PUNT*encontradas*cantidad_bestias
    print(f"El puntaje final de {nombre_usuario} es {puntaje_final} "
          "puntos.")
    ruta = "puntajes.txt"
    ruta_archivo_jugador = path.join("partidas", f"{nombre_usuario}.txt")
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    with open(ruta, "w", encoding="utf-8") as archivo:
        lineas += f"{nombre_usuario}:{puntaje_final}\n"
        for linea in lineas:
            archivo.write(linea)
    with open(ruta_archivo_jugador, "r", encoding="utf-8") as archivo_1:
        # Para establecer partida como terminada y jugador no haga "trampa"
        lineas = archivo_1.readlines()
    with open(ruta_archivo_jugador, "w", encoding="utf-8") as archivo_1:
        for linea in lineas:
            archivo_1.write(linea)
        archivo_1.write("Partida terminada\n")
    return puntaje_final


def cargar_partida(nombre_usuario):
    ruta_guardar = path.join("partidas", f"{nombre_usuario}.txt")
    existe = isfile(ruta_guardar)
    if existe is False:
        print("No existen registros previos del jugador.")
        return False
    with open(ruta_guardar, "r", encoding="utf-8") as archivo:
        lineas_sucias = archivo.readlines()
    largo_tablero = int(lineas_sucias[4].strip())
    tablero_de_jugador = []
    tablero_de_bestias = []
    for i in range(5, 5 + largo_tablero):
        fila = lineas_sucias[i].strip("\n").split("-")
        tablero_de_jugador.append(fila)
    for j in range(6 + largo_tablero, 6 + 2*largo_tablero):
        fila = lineas_sucias[j].strip("\n").split("-")
        tablero_de_bestias.append(fila)
    return tablero_de_bestias, tablero_de_jugador


def crear_nuevo_tablero():
    opciones_correctas = {str(i) for i in range(3, 16)}
    print("Por favor ingrese un ancho de tablero entre 3 y 15: ")
    ancho_tablero = revisar_input_correcto(opciones_correctas)
    print("Por favor ingrese un largo de tablero entre 3 y 15: ")
    largo_tablero = revisar_input_correcto(opciones_correctas)
    print("Creando nuevo tablero...")
    cantidad_bestias = ceil(ancho_tablero*largo_tablero*PROB_BESTIA)
    print(f"El tablero tiene {cantidad_bestias} bestias.\n"
          "Para ganar debe evitar elegir una coordenada que contenga "
          "una bestia.")
    tablero_de_bestias = []
    tablero_de_jugador = []
    # Creamos un tablero accesible al jugador y otro para que el
    # programa conozca si hay o no una bestia
    lista_posiciones_bestias = []
    numero_maximo = (ancho_tablero*largo_tablero)-1
    for i in range(cantidad_bestias):
        posicion_random = posicion_random_func(lista_posiciones_bestias,
                                               numero_maximo)
        lista_posiciones_bestias.append(posicion_random)
        #  obtiene posicion random que no haya salido antes para asegurar
        #  posiciones distintas, y la pone en una lista
        #  que permite luego asignar al tablero oculto de bestias
    contador = 0
    for fila_n in range(largo_tablero):
        fila_bestias = []
        fila_jugador = []
        for columna_n in range(ancho_tablero):
            if contador in lista_posiciones_bestias:
                fila_bestias.append("N")
            else:
                fila_bestias.append(" ")
            fila_jugador.append(" ")
            contador += 1
        tablero_de_bestias.append(fila_bestias)
        tablero_de_jugador.append(fila_jugador)
    return tablero_de_bestias, tablero_de_jugador


def terminado_func(ruta_guardar):
    # Ve si partida está terminada o no
    with open(ruta_guardar, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    if lineas[-1].strip() == "Partida terminada":
        print("Partida anterior terminada.\n"
              "Comience una nueva partida.")
        return True
    else:
        return False
