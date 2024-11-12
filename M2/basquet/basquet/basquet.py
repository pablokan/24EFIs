import reflex as rx
from rxconfig import config
import sqlite3




# Back-end: Clase para manejar el estado de los jugadores
class TableForEachState(rx.State):
    # Lista de jugadores
    jugadores: list[list] = []




    # Variables para los datos del jugador
    nombre_jugador: str = ""
    dorsal: str = ""
    minutos: str = ""
    puntos: str = ""
    faltas: str = ""




    # Función para agregar un jugador a la lista
    def agregar_jugador(self):
        nuevo_jugador = [
            self.nombre_jugador,
            self.dorsal,
            self.minutos,
            self.puntos,
            self.faltas,
        ]
        self.jugadores.append(nuevo_jugador)  # Agregar a la lista de jugadores
        # Insertar el jugador en la base de datos
        conn = sqlite3.connect('jugadores.db')
        cursor = conn.cursor()


        cursor.execute('''
        INSERT INTO jugadores (nombre, dorsal, minutos, puntos, faltas)
        VALUES (?, ?, ?, ?, ?)
    ''', (self.nombre_jugador, self.dorsal, self.minutos, self.puntos, self.faltas))#Los valores que se insertan son los atributos del objeto


        conn.commit() #guardando los cambios en la base de datos
        conn.close()  #cierra la conexión con la base de datos




        # Limpiar los campos de entrada
        self.nombre_jugador = ""
        self.dorsal = ""
        self.minutos = ""
        self.puntos = ""
        self.faltas = ""




    # Función para eliminar un jugador de la lista
    def eliminar_jugador(self, index: int):
        if 0 <= index < len(self.jugadores):
            del self.jugadores[index]  # Eliminar el jugador en el índice especificado




# Función para mostrar cada jugador en una fila de la tabla
def mostrar_jugadores(jugador: list, index: int):#'jugador' es una lista que contiene los datos de los jugadores index' es el índice del jugador dentro de la lista
    return rx.table.row(
        rx.table.cell(jugador[0]),  # Nombre del Jugador
        rx.table.cell(jugador[1]),  # Dorsal
        rx.table.cell(jugador[2]),  # Minutos jugados
        rx.table.cell(jugador[3]),  # Puntos
        rx.table.cell(jugador[4]),  # Faltas
        rx.table.cell(
            rx.button("Eliminar",
                      on_click=lambda: #llama a la función de eliminar 
                    TableForEachState.eliminar_jugador(index))  # Elimina al jugador
        ),
    )




# Función para crear la tabla con los jugadores
def foreach_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre del Jugador"),
                rx.table.column_header_cell("Dorsal"),
                rx.table.column_header_cell("Minutos Jugados"),
                rx.table.column_header_cell("Puntos"),
                rx.table.column_header_cell("Faltas cometidas"),
                rx.table.column_header_cell("Acciones"),  # Columna para el botón de eliminar
            ),
        ),
        rx.table.body(
            rx.foreach(
                TableForEachState.jugadores, mostrar_jugadores  # Mostrar los jugadores
            )
        ),
        width="100%",
    )




# Clase para manejar el puntaje
class State(rx.State):
    puntos_equipo_a: int = 0
    puntos_equipo_b: int = 0




    def sumar_puntos_equipo_a(self, puntos):
        self.puntos_equipo_a += puntos




    def restar_puntos_equipo_a(self, puntos):
        if self.puntos_equipo_a > 0:
            self.puntos_equipo_a -= puntos




    def sumar_puntos_equipo_b(self, puntos):
        self.puntos_equipo_b += puntos




    def restar_puntos_equipo_b(self, puntos):
        if self.puntos_equipo_b > 0:
            self.puntos_equipo_b -= puntos




# Front-end: Función principal que crea la interfaz
def index():
    page = rx.box(
        rx.heading('Mesa de Control De Basquet'),  # Título principal
        rx.vstack(
            # Sección de puntaje del equipo local y visitante
            rx.flex(
                # Puntaje Local
                rx.box(
                    rx.icon("dribbble", color="green", font_size="48px"),
                    rx.text("Puntaje Local", font_size="18px", color="green", font_weight="bold"),
                    rx.text(f"{State.puntos_equipo_a}", font_size="28px", color="green"),
                    rx.hstack(
                        rx.button("Suma 1 al Local", on_click=lambda: State.sumar_puntos_equipo_a(1)),
                        rx.button("Restar 1 al Local", on_click=lambda: State.restar_puntos_equipo_a(1)),
                        spacing="10px"
                    ),
                    padding="20px", border="1px solid #ccc", border_radius="5px",
                    align="center", spacing="10px", width="45%", margin="10px"
                ),
                # Puntaje Visitante
                rx.box(
                    rx.icon("dribbble", color="red", font_size="48px"),
                    rx.text("Puntaje Visitante", font_size="18px", color="red", font_weight="bold"),
                    rx.text(f"{State.puntos_equipo_b}", font_size="28px", color="red"),
                    rx.hstack(
                        rx.button("Suma 1 al Visitante", on_click=lambda: State.sumar_puntos_equipo_b(1)),
                        rx.button("Restar 1 al Visitante", on_click=lambda: State.restar_puntos_equipo_b(1)),
                        spacing="10px"
                    ),
                    padding="20px", border="1px solid #ccc", border_radius="5px",
                    align="center", spacing="10px", width="45%", margin="10px"
                ),
                justify_content="space-around", width="80%", padding="15px 0"
            ),
           
            # Título de estadísticas del jugador
            rx.text("Estadísticas del jugador en el partido", font_size="16px", padding="15px 20px",
                    border="3px solid #4CAF50", border_radius="8px", margin="20px 0"),
           
            # Formulario de datos del jugador
            rx.hstack(
                rx.text("Nombre del Jugador", font_size="16px"),
                rx.input(value=TableForEachState.nombre_jugador, placeholder="Juancito",
                         border_radius="5px", width="100px", on_change=lambda e: TableForEachState.set_nombre_jugador(e)),
                rx.text("Dorsal", font_size="16px"),
                rx.input(type="number", value=TableForEachState.dorsal, placeholder="5",
                         border_radius="5px", width="100px", on_change=lambda e: TableForEachState.set_dorsal(e)),
                rx.text("Minutos Jugados", font_size="16px"),
                rx.input(type="number", value=TableForEachState.minutos, placeholder="0-40",
                         border_radius="5px", width="100px", on_change=lambda e: TableForEachState.set_minutos(e)),
                rx.text("Puntos", font_size="16px"),
                rx.input(type="number", value=TableForEachState.puntos, placeholder="Puntos",
                         border_radius="5px", width="100px", on_change=lambda e: TableForEachState.set_puntos(e)),
                rx.text("Faltas Cometidas", font_size="16px"),
                rx.input(type="number", value=TableForEachState.faltas, placeholder="0-5",
                         border_radius="5px", width="100px", on_change=lambda e: TableForEachState.set_faltas(e)),
                spacing="10px"
            ),
           
            # Botón para agregar el jugador
            rx.button("Agregar Jugador", font_weight="bold", border_radius="8px",
                      padding="10px 20px", border="none", margin="20px 0",
                      on_click=TableForEachState.agregar_jugador),
           
            # Mostrar la tabla de jugadores
            rx.flex(
                foreach_table_example(),
                justify_content="center",  # Centra la tabla en el contenedor
                width="100%", padding="25px 0"
            ),
        ),
        background_color="#f0f8ff",  # Color de fondo para toda la interfaz
        padding="20px",
    )
    return page


app = rx.App()
app.add_page(index)  # Añadir la página principal