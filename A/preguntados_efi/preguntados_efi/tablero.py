import reflex as rx
import sqlite3
import random
from rxconfig import config

def obtener_pregunta_y_respuestas(excluir_ids:list):
    conn = sqlite3.connect('preguntas.db') #conecta a la base de datos
    cursor = conn.cursor()
    #cursor.execute("SELECT id FROM preguntas ")
    #ids = cursor.fetchall() #selecciona todos los id de la tabla de la base de datos
    
    #fila_id = random.choice(ids)[0] #guarda un ID random entre todos los ID disponibles en la base de datos
    query = f"""
            SELECT * FROM preguntas 
            WHERE id NOT IN ({','.join('?' for _ in excluir_ids)})
            ORDER BY RANDOM()
            LIMIT 1;
            """
    cursor.execute(query, excluir_ids)
    # obtiene la pregunta y respuestas correspondientes al ID seleccionado
    # cursor.execute("SELECT pregunta, r1, r2, r3, rc FROM preguntas WHERE id = ?", (fila_id,))
    resultado = cursor.fetchone() #guarda la fila en una tupla
    conn.close()

    if resultado:
        id = resultado[0]
        pregunta = resultado[1] #guarda la pregunta
        #crea una lista de disccionario con las respuestas
        respuestas = [
            {"texto": resultado[2], "es_correcta": False},
            {"texto": resultado[3], "es_correcta": False},
            {"texto": resultado[4], "es_correcta": False},
            {"texto": resultado[5], "es_correcta": True}
        ]
        random.shuffle(respuestas)  #mezcla las respuestas para que el orden sea aleatorio
        return pregunta, respuestas, id
 

class Casilla(rx.Base): # Objeto Casilla para renderizar dinamicamente las casillas
    num: int = 0 # Numero de casilla
    esta: bool = False # Variable para controlar si aparece o no el icono del jugador ("ficha")

class Jugador(rx.Base): # Clase Jugador que gestiona el avance de cada jugador
    pregResp: int = 0 # Cantidad de preguntas respondidas
    renderizar: bool = True # Variable opcional para renderizas (sin uso)

    tablero: list[Casilla] = [ # Lista de objetos Casilla para renderizarlos con un foreach
        Casilla(num=0,esta=True),
        Casilla(num=1,esta=False),
        Casilla(num=2,esta=False),
        Casilla(num=3,esta=False),
        Casilla(num=4,esta=False),
        Casilla(num=5,esta=False),
    ]
    
    def resetear(self): # Metodo para resetear la cantidad de preguntas respondidas, tambien renderiza las casillas
        self.pregResp = 0
        for casilla in self.tablero:
            if casilla.num == self.pregResp:
                casilla.esta = True
            else:
                casilla.esta = False 
        

    def avanzarCasilla(self): # Metodo para hacer que el jugador avance una casilla, tambien renderiza las casillas
        self.pregResp += 1
        for casilla in self.tablero:
            if casilla.num == self.pregResp:
                casilla.esta = True
            else:
                casilla.esta = False

def renderizarCasilla(casilla: Casilla): # Funcion para renderizar dinamicamente las casillas
        return rx.cond( # rx.Cond
            casilla.esta,   # Si la variable esta de la clase Casilla() es true, muestra un icono
            rx.flex(
                rx.icon(
                    'user',
                    size=80,
                    align='center',
                ),
            width='10%',
            height='100%',
            bg='turquoise',
            border_radius='10%',
            align='center',
            justify='center',
            ),
            rx.box( # Si es False muestra solo la casilla
            width='10%',
            height='100%',
            border_radius='10%',
            bg='moccasin',
            align='center'
            ),
        )

class Tablero(rx.State): # Clase State que gestiona la conexion front y back
    jug1: Jugador = Jugador() # Jugador 1
    jug2: Jugador = Jugador() # Jugador 2
    jug1_nom = 'Jugador 1' # Variables para los nombres de los jugadores, el frontend no puede acceder correctamente al nombre si es un atributo
    jug2_nom = 'Jugador 2' # de la clase Jugador, de modo que al ser solo dos los almacenamos directamente en el State
    turno: bool = True # Variable para controlar el turno -> True = jug1 / False = jug2
    pregunta: str = ""
    respuestas: list[dict] = [] 
    eleccion: bool = False
    color_boton: str = 'blue'
    activar_botones: bool = True
    respuesta: str = '' # Variable de texto para mostrar si el jugador respondio bien o mal
    hayGanador: bool = False # Variable para renderizar el alert dialog cuando gana uno de los jugadores
    jugGanador: str = '' # Almacenara el nombre del jugador ganador
    idPreguntasUsadas: list = [] # Almacena las id de las preguntas que ya salieron en la partida

    def setearNombres(self):
        if self.jug1_nom == '':
            self.jug1_nom = 'Jugador 1'
        if self.jug2_nom == '':
            self.jug2_nom = 'Jugador 2'

    def respuestaCorrecta(self):    # Funcion para llamar cuando una respuesta sea correcta, llama a avanzar la casilla del jugador segun el turno que se este jugando
        if self.turno == True:
            self.jug1.avanzarCasilla()
        else:
            self.jug2.avanzarCasilla()
        return None
    
    
    def cambiarTurno(self): # Funcion para cambiar el turno (separada de la funcion de arriba para llamarla si respondieron mal) 
        self.turno = not(self.turno)
    
    def resetear(self): # Funcion para resetear a ambos jugadores
            self.jug1.resetear()
            self.jug2.resetear()
            self.turno = True #pone en True para que vuelva a jugar primero jugador 1
            self.hayGanador = False # Vuelve a False el ganador para el siguiente
            self.jugGanador = ''
            self.idPreguntasUsadas = []

    def calcularGanador(self):
        if (self.jug1.pregResp == 5):
            self.jugGanador = self.jug1_nom
            self.hayGanador = True
        elif (self.jug2.pregResp == 5):
            self.jugGanador = self.jug2_nom
            self.hayGanador = True

    def cargar_pregunta(self):
        #cargar una pregunta y respuestas aleatorias de la base de datos
        self.pregunta, self.respuestas, preg_usada = obtener_pregunta_y_respuestas(self.idPreguntasUsadas)
        self.eleccion = False
        self.color_boton = 'blue'
        self.activar_botones = True
        self.respuesta = ''
        self.idPreguntasUsadas.append(preg_usada)
 
    def verificar_respuesta(self, respuesta_texto):
      if self.activar_botones:  #solo entra si los botones estan activos
            for respuesta in self.respuestas:
                if respuesta["texto"] == respuesta_texto: #ve si el texto del boton es igual a alguna de las respuestas de la lista
                    if respuesta["es_correcta"]: #ve si es la correcta
                        self.respuestaCorrecta()
                        self.cambiarTurno()
                        self.eleccion = True
                        self.respuesta = 'Respuesta Correcta'
                    else:
                        self.cambiarTurno()
                        self.eleccion = False
                        self.respuesta = 'Respuesta Incorrecta'
                    break
            
            self.activar_botones = False  # Desactiva los botones después de una elección
            self.pintar_boton()

    def pintar_boton(self):
        #si la respuesta es correcta pinta a todos los botones de verde, sino de rojo
        self.color_boton = 'green' if self.eleccion else 'red'


