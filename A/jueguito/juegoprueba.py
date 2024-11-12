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
        print(f"{jugadorActual.nombre} - Turno de {jugadorActual.nombre}")
        print("Cartas disponibles:")
        for i, carta in enumerate(jugadorActual.cartas):
            print(f"{i + 1}. {carta.personaje.nombre}")  # Aquí accedemos a los nombres de los personajes

        # El jugador selecciona una carta
        if jugadorActual.nombre == 'Jugador':  # Si es el turno del jugador
            seleccion = int(input("Selecciona una carta para jugar: ")) - 1
            cartaJugada = jugadorActual.cartas[seleccion]
            jugadorActual.eliminarCarta(cartaJugada)  # Eliminar la carta después de usarla
        else:  # Si es el turno de la computadora, elige una carta aleatoria
            cartaJugada = random.choice(jugadorActual.cartas)
            print(f"{jugadorActual.nombre} elige la carta: {cartaJugada.personaje.nombre}")
            jugadorActual.eliminarCarta(cartaJugada)  # Eliminar la carta después de usarla

        cartaJugada.accion(jugadorActual, jugadorRival)  # El efecto de la carta se aplica al rival

        # Después de que el jugador o la computadora juega su carta, el turno cambia
        if self.turnoJugador:  # Si el turno era del jugador, pasa a la computadora
            self.turnoJugador = False
        else:  # Si el turno era de la computadora, pasa al jugador
            self.turnoJugador = True

    def jugar(self):
        while self.jugador.salud > 0 and self.computadora.salud > 0:
            if self.turnoJugador:
                self.turno(self.jugador, self.computadora)
            else:
                self.turno(self.computadora, self.jugador)

            # Mostrar el estado actual de las salud de ambas facciones
            print(f"Salud de {self.jugador.nombre}: {self.jugador.salud}")
            print(f"Salud de {self.computadora.nombre}: {self.computadora.salud}")

            # Revisamos si alguien ha ganado
            if self.jugador.salud <= 0:
                print(f"{self.jugador.nombre} ha sido derrotado. ¡La computadora gana!")
                
            elif self.computadora.salud <= 0:
                print(f"{self.computadora.nombre} ha sido derrotado. ¡{self.jugador.nombre} gana!")
            
            elif self.jugador.salud > self.computadora.salud:
                print(f'{self.jugador.nombre} ha ganado por tener mas salud que el rival.')
                print(f'{self.jugador.nombre} = {self.jugador.salud}')
                print(f'{self.computadora.nombre} = {self.computadora.salud}')

            elif self.computadora.salud > self.jugador.salud:
                print(f'{self.computadora.nombre} ha ganado por tener mas salud que el rival.')
                print(f'{self.jugador.nombre} = {self.jugador.salud}')
                print(f'{self.computadora.nombre} = {self.computadora.salud}')

            elif self.computadora.salud == self.jugador.salud:
                print(f'Empate! Ambas facciones terminaron con la misma vida.')
                

# Crear las facciones
vikingo = Vikingo()
romano = Romano()

# Crear los jugadores
jugador = Jugador("Jugador", vikingo)
computadora = Jugador("Computadora", romano)

# Crear la partida y jugar
partida = Partida(jugador, computadora)
partida.jugar()
