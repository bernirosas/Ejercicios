import json


def info_json(key):
    with open("parametros.json", "r", encoding="UTF-8") as archivo:
        diccionario_data = json.load(archivo)
    ret = diccionario_data[key]
    return ret
