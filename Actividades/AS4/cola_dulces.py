class TrickOrTreater:  # TrickOrTreater = tot

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.protagonista = False
        self.siguiente = None  # persona despues en la fila


class ColaDulces:
    """
    Clase que representa una lista ligada
    """

    def __init__(self):
        """
        Inicializa una lista ligada vacia, con una referencia nula a su cabeza y cola.
        """
        self.primero = None
        self.ultimo = None

    def tot_llega(self, nombre: str):
        """
        Agrega un nodo al final de la cola
        """
        nuevo = TrickOrTreater(nombre)

        if self.primero is None:
            self.primero = nuevo
            self.ultimo = self.primero
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = self.ultimo.siguiente

    def obtener_tot(self, posicion: int):
        """
        Recibe una posición como argumento y retorna
        el tot en esa posición de la cola
        """
        tot_actual = self.primero

        for _ in range(posicion):
            if tot_actual is not None:
                tot_actual = tot_actual.siguiente
            else:
                return None

        return tot_actual

    def obtener_posicion_protagonista(self):
        """
        Retorna la posición del tot protagoista en la cola.
        Si no se encuentra en la fila, retorna -1
        """
        actual = self.primero
        posicion = 0
        while actual is not None:
            if actual.protagonista:
                return posicion
            posicion += 1
            actual = actual.siguiente
        return -1

    def tot_se_cola(self, nombre: str, posicion: int): 
        """
        Crea una instancia de TrickOrTreater con el nombre recibido y
        lo inserta en la cola en la posición recibida.
        """
        colado = TrickOrTreater(nombre)
        if self.primero is None and self.ultimo is None:
            self.primero = colado
            self.ultimo = colado
            colado.siguiente = None
        elif posicion == 0:
            colado.siguiente = self.primero
            self.primero = colado
        else:
            actual = self.primero
            for _ in range(0, posicion):
                if actual.siguiente is not None:
                    actual = actual.siguiente
            if actual == self.ultimo:
                actual.siguiente = colado
                colado.siguiente = None
                self.ultimo = colado
            else:
                colado.siguiente = actual.siguiente
                actual.siguiente = colado

    def tot_se_va(self, posicion: int):
        """
        Elimina a la persona de la posición recibida de la cola.
        """
        if posicion == 0:
            tot_nuevo = self.primero.siguiente
            self.primero.siguiente = None
            self.primero = tot_nuevo

            if tot_nuevo.siguiente is None:
                self.ultimo = tot_nuevo

            return

        tot_actual = self.obtener(posicion-1)
        tot_fuera = tot_actual.siguiente
        tot_actual.siguiente = tot_fuera.siguiente
        tot_fuera.siguiente = None
        if tot_actual.siguiente is None:
            self.ultimo = tot_actual

    def atender_tot(self):
        """
        Elimina a la primera persona de la cola y la retorna.
        """
        eliminado = self.primero
        if eliminado is not None:
            self.primero = eliminado.siguiente
            if self.primero is None:
                self.ultimo = None
        return eliminado

    def obtener_largo(self):
        """
        Retorna el largo de la cola como int.
        """
        actual = self.primero
        largo = 1
        while actual is not self.ultimo:
            actual = actual.siguiente
            largo += 1
        return largo

    def __str__(self) -> str:
        """
        Retorna una representación de la fila con los nombres de
        cada uno de sus participantes.
        """
        string = "DULCES :) "
        tot_actual = self.primero
        while tot_actual:
            string += "<- "+tot_actual.nombre
            tot_actual = tot_actual.siguiente
        return string
