def platos_por_categoria(lista_platos: list) -> dict:
    diccionario_categorias = dict()
    for plato in lista_platos:
        if plato[1] not in diccionario_categorias.keys():
            diccionario_categorias[plato[1]] = [plato]
        else:
            diccionario_categorias[plato[1]].append(plato)
    return diccionario_categorias


def descartar_platos(ingredientes_descartados: set,
                     lista_platos: list) -> list:
    contador = 0
    for plato in lista_platos:
        devolver = False
        for ingrediente in plato.ingredientes:
            if ingrediente in ingredientes_descartados:
                devolver = True
        if devolver:
            lista_platos.pop(contador)
        contador += 1
    return lista_platos


# --- EXPLICACION --- #
# Si el plato necesita un ingrediente que no tiene cantidad suficiente,
# entonces retorna False
#
# En caso que tenga todo lo necesario, resta uno a cada cantidad y retorna True
# NO MODIFICAR
def preparar_plato(plato, ingredientes: dict) -> bool:
    for ingrediente_plato in plato.ingredientes:
        if ingredientes[ingrediente_plato] <= 0:
            return False

    for ingrediente_plato in plato.ingredientes:
        ingredientes[ingrediente_plato] -= 1

    return True


def resumen_orden(lista_platos: list) -> dict:
    diccionario_orden = dict()
    for plato in lista_platos:
        if diccionario_orden == {}:
            diccionario_orden["precio total"] = int(plato[3])
            diccionario_orden["tiempo total"] = int(plato[2])
            diccionario_orden["cantidad de platos"] = 1
            diccionario_orden["platos"] = [plato[0]]
        else:
            diccionario_orden["precio total"] += int(plato[3])
            diccionario_orden["tiempo total"] += int(plato[2])
            diccionario_orden["cantidad de platos"] += 1
            diccionario_orden["platos"].append(plato[0])
    return diccionario_orden
