from collections import namedtuple
from programon import Programon_agua, Programon_fuego, Programon_planta
from objetos import caramelo, baya, pocion


def cargar_programon_requerido(ruta, nombre_programon):
    # función crea instancias del programon a partir de los nombre
    # Cumple el bonus
    with open(ruta, "r", encoding="utf-8") as archivo_2:
        lineas_sucias = archivo_2.readlines()
    contador = 0
    for linea_sucia in lineas_sucias:
        linea = linea_sucia.strip().split(",")
        if contador == 0:
            datos = namedtuple("programon", [linea[0], linea[1], linea[2],
                                             linea[3], linea[4], linea[5],
                                             linea[6]])
        else:
            instancia = datos(linea[0], linea[1], linea[2], linea[3],
                              linea[4], linea[5], linea[6])
            if instancia.nombre == nombre_programon:
                if instancia.tipo == "agua":
                    programon = Programon_agua(instancia.nombre,
                                               instancia.tipo,
                                               instancia.nivel,
                                               instancia.vida,
                                               instancia.ataque,
                                               instancia.defensa,
                                               instancia.velocidad)
                elif instancia.tipo == "planta":
                    programon = Programon_planta(instancia.nombre,
                                                 instancia.tipo,
                                                 instancia.nivel,
                                                 instancia.vida,
                                                 instancia.ataque,
                                                 instancia.defensa,
                                                 instancia.velocidad)
                elif instancia.tipo == "fuego":
                    programon = Programon_fuego(instancia.nombre,
                                                instancia.tipo,
                                                instancia.nivel,
                                                instancia.vida,
                                                instancia.ataque,
                                                instancia.defensa,
                                                instancia.velocidad)
                return programon
        contador += 1


def cargar_objeto(ruta, nombre_objeto):
    # función crea instancias del objeto a partir de los nombre
    # Cumple el bonus
    with open(ruta, "r", encoding="utf-8") as archivo_3:
        lineas_sucias = archivo_3.readlines()
    contador = 0
    for linea_sucia in lineas_sucias:
        linea = linea_sucia.strip().split(",")
        if contador == 0:
            datos = namedtuple("objeto", [linea[0], linea[1]])
        else:
            instancia = datos(linea[0], linea[1])
            if instancia.nombre == nombre_objeto:
                if instancia.tipo == "caramelo":
                    objeto = caramelo(instancia.nombre,
                                      instancia.tipo)
                elif instancia.tipo == "pocion":
                    objeto = pocion(instancia.nombre,
                                    instancia.tipo)
                elif instancia.tipo == "baya":
                    objeto = baya(instancia.nombre,
                                  instancia.tipo)
                return objeto
        contador += 1


def cargar_objetos_tipo(ruta, tipo_objeto):
    # función crea instancias de todos los objetos de
    # cierto tipo y retorna una lista con estos
    # aplica bonus
    with open(ruta, "r", encoding="utf-8") as archivo_3:
        lineas_sucias = archivo_3.readlines()
    contador = 0
    lista = []
    for linea_sucia in lineas_sucias:
        linea = linea_sucia.strip().split(",")
        if contador == 0:
            datos = namedtuple("objeto", [linea[0], linea[1]])
        else:
            instancia = datos(linea[0], linea[1])
            if instancia.tipo == tipo_objeto:
                if instancia.tipo == "caramelo":
                    objeto = caramelo(instancia.nombre,
                                      instancia.tipo)
                elif instancia.tipo == "pocion":
                    objeto = pocion(instancia.nombre,
                                    instancia.tipo)
                elif instancia.tipo == "baya":
                    objeto = baya(instancia.nombre,
                                  instancia.tipo)
                lista.append(objeto)
        contador += 1
    return lista
