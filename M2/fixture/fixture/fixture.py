import reflex as rx
import sqlite3

# Configuración de la base de datos SQLite
def connect_db():
    return sqlite3.connect("equipos.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insertEquipo(nombre):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO equipos (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

def obtenerEquipos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM equipos")
    equipos = [row[0] for row in cursor.fetchall()]
    conn.close()
    return equipos

# Backend
class State(rx.State):
    valorSelec: str = "4"
    numCampos: int = 0
    nombres: list[str] = []
    nombresAct: dict[str, str] = {}
    jornadas: list[list[tuple[str, str]]] = []

    def crearCampos(self):
        self.numCampos = int(self.valorSelec)
        self.nombres = []
        self.nombresAct = {}

    def agNombre(self, texto: str, campo_id: str):
        self.nombresAct[campo_id] = texto

    def guardarNom(self):
        self.nombres = list(self.nombresAct.values())
        for nombre in self.nombres:
            insertEquipo(nombre)

    def cargarNombres(self):
        self.nombres = obtenerEquipos()

    def generarFechas(self):
        equipos = self.nombres.copy()
        
        if len(equipos) % 2 != 0:
            equipos.append("Libre")
            
        n = len(equipos)
        jornadas = []
        for _ in range(n - 1):
            jornada = []
            for i in range(n // 2):
                if equipos[i] != "Libre" and equipos[n - 1 - i] != "Libre":
                    jornada.append((equipos[i], equipos[n - 1 - i]))
            jornadas.append(jornada)
            equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]
        self.jornadas = jornadas

# Frontend
def campoNombre(idx: int):
    campo_id = f"campo_{idx}"
    return rx.text_area(
        placeholder=f"Nombre {idx + 1}",
        on_change=lambda texto: State.agNombre(texto, campo_id),
        width="90%", 
        height="2em",  
        margin="0.5em",
        background="gray.300",
        border_radius="8px",
        padding="0.3em",
        color="white"
    )

# Página principal de la app
def index():
    # Llamamos a State.cargarNombres al inicializar para cargar los nombres desde la DB
    State.cargarNombres()

    # Barra superior
    top_bar = rx.box(
        rx.hstack(
            rx.image(src="/champ.png", width="24px", height="24px"),  
            rx.text("FutFixture", font_size="2xl", color="white", font_weight="bold", font_family="Arial, sans-serif"),
            spacing="1em"
        ),
        width="100%",
        padding="1em",
        background="linear-gradient(135deg, #1a202c, #2d3748)",
        display="flex",
        align_items="center",
        position="absolute",
        top="0",
        left="0",
        z_index="1",
    )

    # Encabezado de la página con imágenes y título
    header = rx.box(
        rx.hstack(
            rx.image(src="/10-Photoroom.png", width="32%", margin="0 auto"),
            rx.image(src="/jug2.png", width="16%", margin="0 auto"),
            rx.image(src="/iniesta.png", width="32%", margin="0 auto"),
            spacing="0.1em", 
            justify_content="center"
        ),
        rx.heading(
            "Gestor de Torneos de Fútbol", 
            size="4xl",  
            color="white",
            font_family="Poppins, sans-serif",  
            font_weight="bold",
            text_shadow="2px 2px 8px rgba(0, 0, 0, 0.8)", 
            margin_top="1em",
            padding="0.5em"
        ),
        rx.text(
            "La mejor app para gestionar torneos de fútbol", 
            font_size="xl",  
            color="gray.300",
            font_family="Roboto, sans-serif",  
            text_align="center",
            margin_top="0.5em",
            text_shadow="1px 1px 4px rgba(0, 0, 0, 0.6)"
        ),
        width="100%",
        height="100vh",
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",
        background="linear-gradient(135deg, #1a202c, #2d3748)",
        color="white",
        padding="2em",
        box_shadow="lg",
        position="relative",
    )

    # Componentes principáles de la pagina
    main_content = rx.box(
        rx.vstack(
            rx.select(
                ["4", "6", "8"],
                on_change=State.set_valorSelec,
                default_value="4",
                width="50%",  
                margin_bottom="1em",
                padding="0.5em",
                border_radius="8px",
                background="white",
                color="black"
            ),
            rx.button(
                "Enviar Cantidad de Equipos", 
                on_click=State.crearCampos,
                width="50%",
                margin_bottom="1em",
                padding="0.5em",
                background="teal",
                color="white",
                font_weight="bold",
                border_radius="8px",
                box_shadow="lg"
            ),
            rx.hstack(
                rx.box(
                    rx.foreach(
                        rx.Var.range(State.numCampos // 2),
                        lambda idx: campoNombre(idx)
                    ),
                    width="45%"
                ),
                rx.box(
                    rx.foreach(
                        rx.Var.range(State.numCampos // 2, State.numCampos),
                        lambda idx: campoNombre(idx)
                    ),
                    width="45%"
                ),
                spacing="5%",
            ),
            rx.button(
                "Guardar nombres",
                on_click=State.guardarNom,
                width="50%",
                margin_bottom="1em",
                padding="0.5em",
                background="teal",
                color="white",
                font_weight="bold",
                border_radius="8px",
                box_shadow="lg"
            ),
            rx.button(
                "Generar fechas",
                on_click=State.generarFechas,
                width="50%",
                margin_bottom="1em",
                padding="0.5em",
                background="teal",
                color="white",
                font_weight="bold",
                border_radius="8px",
                box_shadow="lg"
            ),
            rx.heading("Tabla de equipos", font_size="2xl", color="white", margin_top="2em"),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Nombres", color="white", font_weight="bold")
                    )
                ),
                rx.table.body(
                    rx.foreach(
                        State.nombres,
                        lambda nombre: rx.table.row(
                            rx.table.cell(nombre, color="white")
                        )
                    )
                ),
                margin_bottom="1em",
                background="rgba(0, 0, 0, 0.5)",
                border_radius="8px"
            ),
            rx.heading("Fechas", font_size="2xl", color="white", margin_top="2em"),
            rx.foreach(
                State.jornadas,
                lambda dia, idx: rx.box(
                    rx.vstack(
                        rx.heading(f"Fecha {idx + 1}", color="white"),
                        rx.foreach(
                            dia,
                            lambda partido: rx.text(f"{partido[0]} vs {partido[1]}", color="gray.300")
                        ),
                        border="1px solid #ccc",
                        padding="1em",
                        border_radius="8px",
                        margin="1em",
                        background="rgba(0, 0, 0, 0.7)",
                        box_shadow="lg",
                    )
                )
            ),
            align_items="center",
            spacing="1em",
            width="100%", 
        ),
        background="linear-gradient(135deg, #1a202c, #2d3748)", 
        padding="3em",
        width="100%",
        display="flex",
        justify_content="center",
        align_items="center",
    )

    # Estructura de la página principal
    return rx.fragment(
        top_bar,
        header,
        main_content
    )

# Crear la tabla en la base de datos al iniciar la aplicación
create_table()

# Crear la app de Reflex
app = rx.App()
app.add_page(index)
