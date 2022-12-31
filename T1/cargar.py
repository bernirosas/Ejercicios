from collections import namedtuple
from entrenador import Entrenador


def cargar_entrenadores(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo_1:
        lineas_sucias = archivo_1.readlines()
    contador = 0
    lista_de_entrenadores = []
    for linea_sucia in lineas_sucias:
        linea = linea_sucia.strip().split(",")
        if contador == 0:
            # se implementa el bonus a través de named tuples
            datos = namedtuple("Entrenador", [linea[0], linea[1], linea[2],
                                              linea[3]])
        else:
            instancia = datos(linea[0], linea[1], linea[2], linea[3])
            # Crear entrenador [nombre, programones, energia, objetos]
            entrenador = Entrenador(instancia.nombre, instancia.programones,
                                    instancia.energia, instancia.objetos)
            lista_de_entrenadores.append(entrenador)
        contador += 1
    return lista_de_entrenadores
