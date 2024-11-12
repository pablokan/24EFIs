from facciones import *
# Clase Carta que representa cada carta jugable
class Carta:
    def __init__(self, personaje):
        self.personaje = personaje

    def accion(self, jugadorActual, jugadorRival):
        # Si es un Soldado o Apoyo, hace daño al objetivo
        if isinstance(self.personaje, Soldado) or isinstance(self.personaje, Apoyo):
            self.personaje.atacar(jugadorRival)
        
        # Si es un Medico o Apoyo, cura al objetivo
        if isinstance(self.personaje, Medico) or isinstance(self.personaje, Apoyo):
            self.personaje.curar(jugadorActual)

# Clase Jugador
class Jugador:
    def __init__(self, nombre, faccion):
        self.nombre = nombre
        self.faccion = faccion
        self.cartas = [Carta(s) for s in faccion.listaSoldados]  # Cartas a partir de los soldados de la facción
        self.salud = faccion.salud
        self.saludMaxima = faccion.saludMaxima

    def eliminarCarta(self, carta):
        """Elimina una carta de la mano del jugador."""
        self.cartas.remove(carta)