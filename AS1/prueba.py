def f(a, b, *args, **kwargs):
    print(a)
    print(b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(f"{kwarg} → {kwargs[kwarg]}")

f(3, 4, [5,6,7], [8, 7], c=8)
# no sabía que si imprimías sin asrte

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def elegir_carrera(self, carrera):
        self.carrera = carrera
        print(f'{self.nombre} estudiará {self.carrera}')

estudiante = Estudiante("berni")
estudiante.elegir_carrera("ingeniería")
estudiante.div = "holo"
print(estudiante.div)
class Artista():

    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo_carrera = tiempo
    
    def presentacion(self):
        print(f"Hola! Me llamo {self.nombre} y llevo {self.tiempo_carrera} años de carrera como artista.")


class Cantante(Artista):

    def __init__(self, musica, numero_albumes, **kwargs):
        super().__init__(**kwargs)
        self.estilo_musica = musica
        self.albumes = numero_albumes
        
    def presentacion(self):
        super().presentacion()
        print(f'Soy cantante de {self.estilo_musica} y he grabado {self.albumes} albumes.')

class Bailarin(Artista):

    def __init__(self, estilo, **kwargs):
        super().__init__(**kwargs)
        self.estilo_baile = estilo
        self.horas_entrenamiento = 5
    
    def presentacion(self):
        super().presentacion()
        print(f'Soy bailarin de {self.estilo_baile} y entreno {self.horas_entrenamiento} horas al día.')

class Actor(Artista):

    def __init__(self, numero_peliculas, numero_series, **kwargs):
        super().__init__(**kwargs)
        self.peliculas = numero_peliculas
        self.series = numero_series
    
    def presentacion(self):
        super().presentacion()
        print(f'Soy actor, he salido en {self.peliculas} peliculas y {self.series} series.')


class Famoso(Cantante, Bailarin, Actor):

    def __init__(self, premios, **kwargs):
        # Solo un llamado, con todos los argumentos de las clases anteriores
        super().__init__(**kwargs)
        self.premios = premios

famoso = Famoso(
    17, nombre="Chayanne", tiempo=43, musica="pop latino", numero_albumes=22,
    estilo="pop", numero_peliculas=4, numero_series=10
    )


famoso.presentacion()