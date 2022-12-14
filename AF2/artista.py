from parametros import (AFINIDAD_HIT, AFINIDAD_INICIAL, AFINIDAD_PUBLICO_POP,
                        AFINIDAD_STAFF_POP, AFINIDAD_PUBLICO_ROCK,
                        AFINIDAD_STAFF_ROCK, AFINIDAD_PUBLICO_TRAP_CHILENO ,
                        AFINIDAD_STAFF_TRAP_CHILENO , AFINIDAD_PUBLICO_REG,
                        AFINIDAD_STAFF_REG, AFINIDAD_ACCION_POP,
                        AFINIDAD_ACCION_ROCK, AFINIDAD_ACCION_TRAP_CHILENO ,
                        AFINIDAD_ACCION_REG, AFINIDAD_MIN, AFINIDAD_MAX)


class Artista:
    def __init__(self, nombre, genero, dia_presentacion,
                 hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL

    @property
    def afinidad_con_publico(self):
        return self._afinidad_con_publico

    @afinidad_con_publico.setter
    def afinidad_con_publico(self, valor):
        if valor > 100:
            self._afinidad_con_staff = 100
        elif valor < 0:
            self._afinidad_con_staff = 0
        else:
            self._afinidad_con_staff = valor
    
    @property
    def afinidad_con_staff(self):
        return self._afinidad_con_staff

    @afinidad_con_staff.setter
    def afinidad_con_staff(self, valor):
        if valor > 100:
            self._afinidad_con_staff = 100
        elif valor < 0:
            self._afinidad_con_staff = 0
        else:
            self._afinidad_con_staff = valor


    @property
    def animo(self):
        animo = self._afinidad_con_publico*0.5 + self._afinidad_con_staff*0.5
        return animo

    def recibir_suministros(self, suministro):  # atender artista
        if suministro.valor_de_satisfaccion < 0:
            print(f"{self.nombre} recibió {suministro.nombre} en malas condiciones.")
        elif suministro.valor_de_satisfaccion > 0:
            print(f"{self.nombre} recibió un {suministro.nombre} a tiempo!")
        self.afinidad_con_staff += suministro.valor_de_satisfaccion


    def cantar_hit(self):
        self._afinidad_con_publico += AFINIDAD_HIT
        print(f"{self.nombre} está tocando su hit: {self.hit_del_momento}!")

    def __str__(self):
        return f"Nombre: {self.nombre}\n Genero: {self.genero}\n Animo: {self.animo}"


class ArtistaPop(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.accion = "Cambio de vestuario"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_POP
        self._afinidad_con_staff = AFINIDAD_STAFF_POP
        

    def accion_especial(self):
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_POP

    @property
    def animo(self):
        valor_animo = super().animo
        if valor_animo < 10:
            print(f"ArtistaPop peligrando en el concierto. Animo: {valor_animo}")
        return valor_animo


class ArtistaRock(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.accion = "Solo de guitarra"
        self._afinidad_con_staff = AFINIDAD_STAFF_ROCK
        self._afinidad_con_publico = AFINIDAD_PUBLICO_ROCK


    def accion_especial(self):
        print(f"{self.nombre} hará un {self.accion}")
        self._afinidad_con_publico += AFINIDAD_ACCION_ROCK
    
    @property
    def animo(self):
        valor_animo = super().animo
        if valor_animo < 5:
            print(f"ArtistaRock peligrando en el concierto. Animo: {valor_animo}")
        return valor_animo


class ArtistaTrapChileno(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.accion = "Malianteo"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_TRAP_CHILENO
        self._afinidad_con_staff = AFINIDAD_STAFF_TRAP_CHILENO

    def accion_especial(self):
        print(f"{self.nombre} hará un {self.accion}")
        self._afinidad_con_publico += AFINIDAD_ACCION_TRAP_CHILENO
    
    @property
    def animo(self):
        valor_animo = super().animo
        if valor_animo < 20:
            print(f"ArtistaTrapChileno peligrando en el concierto. Animo: {valor_animo}")
        return valor_animo
        


class ArtistaReggaeton(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.accion = "Perrear"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_REG
        self._afinidad_con_staff = AFINIDAD_STAFF_REG

    def accion_especial(self):
        print(f"{self.nombre} hará un {self.accion}")
        self._afinidad_con_publico += AFINIDAD_ACCION_REG

    @property
    def animo(self):
        valor_animo = super().animo
        if valor_animo < 2:
            print(f"ArtistaReggaeton peligrando en el concierto. Animo: {valor_animo}")
        return valor_animo
