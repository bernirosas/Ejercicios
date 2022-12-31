from random import random
from random import choice
from cargar_objetos_y_programones import cargar_objetos_tipo,\
                                         cargar_programon_requerido,\
                                         cargar_objeto
from funciones_utiles import revisar_input_correcto


class Entrenador:
    def __init__(self, nombre, programones, energia, objetos) -> None:
        self.nombre = str(nombre)
        self.programones = programones.split(";")  # lista, crear instancias
        anexo = []
        for programon in self.programones:
            progra = cargar_programon_requerido("programones.csv", programon)
            # recibe nombre y crea instancia
            anexo.append(progra)
        self.programones = anexo[:]
        self.__energia = int(energia)  # int
        anexo_1 = []
        self.objetos = objetos.split(";")
        for objeto in self.objetos:
            obj = cargar_objeto("objetos.csv", objeto)
            # recibe nombre y crea instancia
            anexo_1.append(obj)
        self.objetos = anexo_1[:]
        self.perdedor = False
        self.ganador = False

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, nuevo_valor):
        if nuevo_valor < 0:
            print("No hay suficiente energía.")
        elif nuevo_valor > 100:
            self.__energia = 100
        else:
            self.__energia = nuevo_valor

    def estado_entrenador(self):
        string_objetos = []
        for objeto in self.objetos:
            string_objetos.append(objeto.nombre)
        string_objetos = ", ".join(string_objetos)
        print(f"           *** Estado entrenador ***           \n"
              f"-----------------------------------------------\n"
              f"Nombre: {self.nombre}\n"
              f"Energía: {self.energia}\n"
              f"Objetos: {string_objetos}\n"
              f"-----------------------------------------------\n"
              f"                  Programones                  \n"
              f"-----------------------------------------------\n"
              f"   Nombre   |   Tipo   |   Nivel   |   Vida    \n"
              f"-----------------------------------------------")
        for programon in self.programones:
            print(f" {programon.nombre: ^11s}|{programon.tipo: ^10s}|"
                  f"{programon.nivel: ^11d}|{programon.vida: ^11d}")
        print("[1] Volver\n"
              "[2] Salir")
        opcion = revisar_input_correcto({"1", "2"})
        if opcion == "menu":  # input no válido
            self.estado_entrenador()
        elif opcion == 1:
            return "volver"
        elif opcion == 2:
            return "salir"
    # Muestra en consola nombre, energía, objetos y programones del entrenador
    # junto a información importante de cada uno

    def crear_objetos(self):
        print("    *** Menú Objetos ***   \n"
              "---------------------------\n"
              "[1] Baya\n"
              "[2] Poción\n"
              "[3] Caramelo\n"
              "[4] Volver\n"
              "[5] Salir")
        opcion = revisar_input_correcto({str(i+1) for i in range(5)})
        if opcion == "menu":  # input no válido
            return self.crear_objetos()
        if opcion == 1:
            lista = cargar_objetos_tipo("objetos.csv", "baya")
            objeto = choice(lista)
        if opcion == 2:
            lista = cargar_objetos_tipo("objetos.csv", "pocion")
            objeto = choice(lista)
        if opcion == 3:
            lista = cargar_objetos_tipo("objetos.csv", "caramelo")
            objeto = choice(lista)
        if opcion == 1 or opcion == 2 or opcion == 3:
            print(f"El costo del objeto es {objeto.costo}")
            if self.energia < objeto.costo:
                print("No hay suficiente energía para tal acción")
                return self.crear_objetos()
            self.energia -= objeto.costo
            print("Costo realizado")
            # se cobra aunque no se logre crear el objeto
            prob = random()
            if prob <= objeto.prob_exito:
                # si objeto.prob_exito es 0.1. prob
                # será menor o igual que 0.1 el 10% de los casos
                self.objetos.append(objeto)
                print(f"Objeto {objeto.nombre} tipo {objeto.tipo}"
                      f" creado con éxito")
            else:
                print("Que mala suerte! No se ha podido crear el objeto")
            return self.crear_objetos()
        elif opcion == 4:
            return "volver"
        elif opcion == 5:
            return "salir"
