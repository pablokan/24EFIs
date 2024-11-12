# Clases de personajes
class Personaje:
    def __init__(self, nom):
        self.nombre = nom

class Soldado(Personaje):
    def __init__(self, nom, fuerza=0):
        super().__init__(nom)
        self.fuerza = fuerza
        
    def atacar(self, rival):
        rival.salud -= self.fuerza
        if rival.salud < 0:
            rival.salud = 0

class Medico(Personaje):
    def __init__(self, nom, curacion=0):
        super().__init__(nom)
        self.curacion = curacion

    def curar(self, faccion):
        faccion.salud += self.curacion
        if faccion.salud > faccion.saludMaxima:
            faccion.salud = faccion.saludMaxima

class Apoyo(Personaje):
    def __init__(self, nom, fuerza=0, curacion=0):
        super().__init__(nom)
        self.fuerza = fuerza
        self.curacion = curacion

    def atacar(self, rival):
        rival.salud -= self.fuerza
        if rival.salud < 0:
            rival.salud = 0

    def curar(self, faccion):
        faccion.salud += self.curacion
        if faccion.salud > faccion.saludMaxima:
            faccion.salud = faccion.saludMaxima