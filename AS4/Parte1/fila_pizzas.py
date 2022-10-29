class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

    def __str__(self):
        # NO MODIFICAR
        return self.nombre


class FilaPizza:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.largo = 0

    def llega_cliente(self, cliente: Cliente):
        if self.largo == 0:
            self.primero = cliente
            self.ultimo = cliente
        else:
            self.ultimo.siguiente = cliente
            self.ultimo = cliente
        self.largo += 1

    def alguien_se_cuela(self, cliente: Cliente, posicion: int):
        if self.largo <= 0:
            self.primero = cliente
            self.ultimo = cliente
        elif posicion >= self.largo:
            self.ultimo.siguiente = cliente
            self.ultimo = cliente
        elif posicion == 0:
            cliente.siguiente = self.primero
            self.primero = cliente
        elif 0 < posicion < self.largo:
            cliente_actual = self.primero
            for _ in range(0, posicion - 1):
                cliente_actual = cliente_actual.siguiente
            cliente.siguiente = cliente_actual.siguiente
            cliente_actual.siguiente = cliente
        self.largo += 1

    def cliente_atendido(self):
        nodo = self.primero
        if nodo is not None:
            self.primero = nodo.siguiente
            self.largo -= 1
            if self.primero is None:
                self.ultimo = None
        return nodo

    def __str__(self):
        cliente = self.primero
        str = "Cola actual: "
        while cliente is not None:
            str += cliente.nombre + " "
            cliente = cliente.siguiente
        return str


if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise (ModuleNotFoundError)
