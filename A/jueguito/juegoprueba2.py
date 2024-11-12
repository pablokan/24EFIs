import random
from soldados import *
from facciones import *
from clasesdejuego import *

# Clase para manejar la partida
class Partida:
    def __init__(self, jugador, computadora):
        self.jugador = jugador
        self.computadora = computadora
        self.turnoJugador = True  # El jugador empieza

    def turno(self, jugadorActual, jugadorRival):
        # Mostrar las cartas disponibles para el jugador actual
        if jugadorActual.cartas:  # Solo se muestra y se permite jugar si hay cartas disponibles
            print(f"{jugadorActual.nombre} - Turno de {jugadorActual.nombre}")
            print("Cartas disponibles:")
            for i, carta in enumerate(jugadorActual.cartas):
                print(f"{i + 1}. {carta.personaje.nombre}")

            # Seleccionar una carta
            if jugadorActual.nombre == 'Jugador':  # Turno del jugador
                seleccion = int(input("Selecciona una carta para jugar: ")) - 1
                cartaJugada = jugadorActual.cartas[seleccion]
                jugadorActual.eliminarCarta(cartaJugada)  # Eliminar la carta después de usarla
            else:  # Turno de la computadora
                cartaJugada = random.choice(jugadorActual.cartas)
                print(f"{jugadorActual.nombre} elige la carta: {cartaJugada.personaje.nombre}")
                jugadorActual.eliminarCarta(cartaJugada)  # Eliminar la carta después de usarla

            # Aplicar la acción de la carta al rival
            cartaJugada.accion(jugadorActual, jugadorRival)

        # Cambiar de turno
        self.turnoJugador = not self.turnoJugador

    def jugar(self):
        while (self.jugador.salud > 0 or self.computadora.salud > 0):
            if self.turnoJugador:
                self.turno(self.jugador, self.computadora)
            else:
                self.turno(self.computadora, self.jugador)

            # Mostrar salud de ambos jugadores
            print(f"Salud de {self.jugador.nombre}: {self.jugador.salud}")
            print(f"Salud de {self.computadora.nombre}: {self.computadora.salud}")

            # Verificar si ambos jugadores se han quedado sin cartas
            if not self.jugador.cartas and not self.computadora.cartas:
                print("Ambos jugadores se han quedado sin cartas. ¡El juego ha terminado!")
                # Determinar el ganador según la salud
                if self.jugador.salud > self.computadora.salud:
                    print(f"¡{self.jugador.nombre} gana con más salud restante!")
                    print(f'{self.jugador.nombre} = {self.jugador.salud}')
                    print(f'{self.computadora.nombre} = {self.computadora.salud}')
                elif self.jugador.salud < self.computadora.salud:
                    print(f"¡{self.computadora.nombre} gana con más salud restante!")
                    print(f'{self.jugador.nombre} = {self.jugador.salud}')
                    print(f'{self.computadora.nombre} = {self.computadora.salud}')
                else:
                    print("¡Es un empate!")
                break

            # Revisar si la salud de alguno de los jugadores ha llegado a 0
            if self.jugador.salud <= 0:
                print(f"{self.jugador.nombre} ha sido derrotado. ¡La computadora gana!")
                break
            elif self.computadora.salud <= 0:
                print(f"{self.computadora.nombre} ha sido derrotado. ¡{self.jugador.nombre} gana!")
                break

# Crear las facciones
griego = Vikingo()
romano = Romano()

# Crear los jugadores
jugador = Jugador("Jugador", griego)
computadora = Jugador("Computadora", romano)

# Crear la partida y jugar
partida = Partida(jugador, computadora)
partida.jugar()
