from Parte2.campus import Lugar
from collections import deque


def comprobar_chismoso(lugar: Lugar):
    # NO MODIFICAR
    for ayudante in lugar.ayudantes:
        if "Croak" in ayudante.frase:
            return True
    return False


def bfs_iterativo(inicio: Lugar, final: Lugar):
    visitados = set()
    cola = deque([inicio])
    while len(cola) > 0:
        # Elegimos el siguiente nodo a visitar de la cola
        vertice = cola.popleft()
        if vertice == final:
            return True
        # Detalle clave: si ya visitamos el nodo, no hacemos nada!
        visitados.add(vertice)
        # Agregamos los vecinos a la cola si es que no han sido visitados.
        for vecino in vertice.vecinos:
            if vecino not in visitados:
                lugar = vecino
                chismoso = comprobar_chismoso(lugar)
                if not chismoso:
                    cola.append(lugar)
    return False


def dfs_iterativo(inicio: Lugar, final: Lugar):
    pass
    # Vamos a mantener un set con los nodos visitados.
#    visitados = set()

    # El stack de siempre, comienza desde el nodo inicio.
 #   stack = [inicio]

#    while len(stack) > 0:
#        vertice = stack.pop()
#        # Detalle clave: si ya visitamos el nodo, ¡no hacemos nada!
#        if vertice == final:
#            return True

        # Lo visitamos
#        visitados.add(vertice)

#        # Agregamos los vecinos al stack si es que no han sido visitados.
#        for vecino in vertice.vecinos:
#            if vecino not in visitados:
#                lugar = vecino
#                chismoso = comprobar_chismoso(lugar)
#                if not chismoso:
#                    stack.append(lugar)

#    return False


def bfs_iterativo_largo(inicio: Lugar, final: Lugar):
    visitados = set()
    cola = deque([inicio, 0])
    while len(cola) > 0:
        # Elegimos el siguiente nodo a visitar de la cola
        vertice, largo = cola.popleft()
        if vertice == final:
            return largo
        # Detalle clave: si ya visitamos el nodo, no hacemos nada!
        visitados.add(vertice)
        # Agregamos los vecinos a la cola si es que no han sido visitados.
        for vecino in vertice.vecinos:
            if vecino not in visitados:
                lugar = vecino
                chismoso = comprobar_chismoso(lugar)
                if not chismoso:
                    cola.append((lugar, largo + 1))
    return -1


def dfs_iterativo_largo(inicio: Lugar, final: Lugar):
    # Completar
    pass


def bfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino. 
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos) 
    # y el valor el nodo en cuestion
    padres = dict()
    padres[inicio] = None

    # Completar
    pass
    

def dfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino. 
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos) 
    # y el valor el nodo en cuestion
    padres = dict()
    padres = dict()
    padres[inicio] = None

    # Completar
    pass
    
    
def creador_camino(diccionario_padres, final):
    # NO MODIFICAR
    camino = []
    camino.append(final)
    while diccionario_padres[final] is not None:
        camino.append(diccionario_padres[final])
        final = diccionario_padres[final]
    camino.reverse()
    return camino


def imprimir_camino(camino):
    # NO MODIFICAR
    recorrido = ""
    largo = len(camino)
    contador = 1
    for lugar in camino:
        if contador < largo:
            recorrido = recorrido + f"[{lugar.nombre}] -> "
        else:
            recorrido = recorrido + f"[{lugar.nombre}]."
        contador += 1
    print(recorrido)

if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)
