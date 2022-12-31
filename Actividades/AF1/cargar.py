from collections import namedtuple


def cargar_platos(ruta_archivo: str) -> list:
    with open(ruta_archivo, "rt") as archivo:
        lineas_sucias = archivo.readlines()
    lista = []
    for linea_sucia in lineas_sucias:
        linea = linea_sucia.strip().split(",")
        caracteristicas = namedtuple(
            "platos",
            ["nombre", "categoria",
             "tiempo_preparacion", "precio",
             "ingredientes"])
        lista_ingredientes = linea[4].split(";")
        set_ingredientes = set(lista_ingredientes)
        instancia = caracteristicas(str(linea[0]), str(linea[1]),
                                    int(linea[2]), int(linea[3]),
                                    set_ingredientes)
        lista.append(instancia)
    lista.pop(0)
    return lista


def cargar_ingredientes(ruta_archivo: str) -> dict:
    with open(ruta_archivo) as archivo:
        lineas_sucias = archivo.readlines()
    ingredientes = dict()
    for linea_sucia in lineas_sucias:
        ingrediente = linea_sucia.strip().split(",")
        ingredientes[ingrediente[0]] = int(ingrediente[1])
    return ingredientes
