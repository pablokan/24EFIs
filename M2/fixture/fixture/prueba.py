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

def insert_team(nombre):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO equipos (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

def get_teams():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM equipos")
    equipos = [row[0] for row in cursor.fetchall()]
    conn.close()
    return equipos

# Backend
class Estado(rx.State):
    valor_seleccionado: str = "4"
    numero_de_campos: int = 0
    nombres: list[str] = []
    nombres_actuales: dict[str, str] = {}
    jornadas: list[list[tuple[str, str]]] = []

    def crear_campos(self):
        self.numero_de_campos = int(self.valor_seleccionado)
        self.nombres = []
        self.nombres_actuales = {}

    def agregar_nombre(self, texto: str, campo_id: str):
        self.nombres_actuales[campo_id] = texto

    def guardar_nombres(self):
        # Guardar los nombres en la lista y en la base de datos
        self.nombres = list(self.nombres_actuales.values())
        for nombre in self.nombres:
            insert_team(nombre)

    def cargar_nombres(self):
        # Cargar los nombres desde la base de datos y actualizarlos en la lista
        self.nombres = get_teams()

    def generar_jornadas(self):
        equipos = self.nombres.copy()
        if len(equipos) % 2 != 0:
            equipos.append("BYE")
        n = len(equipos)
        jornadas = []
        for _ in range(n - 1):
            jornada = []
            for i in range(n // 2):
                if equipos[i] != "BYE" and equipos[n - 1 - i] != "BYE":
                    jornada.append((equipos[i], equipos[n - 1 - i]))
            jornadas.append(jornada)
            equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]
        self.jornadas = jornadas

# Frontend
def campo_nombre(idx: int):
    campo_id = f"campo_{idx}"
    return rx.text_area(
        placeholder=f"Nombre {idx + 1}",
        on_change=lambda texto: Estado.agregar_nombre(texto, campo_id),
        width="90%", 
        height="2em",  
        margin="0.5em",
        background="white",
        border_radius="8px",
        padding="0.3em",
        color="black"
    )

# Página principal de la app
def index():
    # Llamamos a Estado.cargar_nombres al inicializar para cargar los nombres desde la DB
    Estado.cargar_nombres()

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
                on_change=Estado.set_valor_seleccionado,
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
                on_click=Estado.crear_campos,
                width="50%",
                margin_bottom="1em",
                padding="0.5em",
                background="teal",
                color="white",
                font_weight="bold",
                border_radius="8px",
                box_shadow="lg"
            ),
            # Contenedor para dividir los campos de texto en dos columnas
            rx.hstack(
                rx.box(
                    rx.foreach(
                        rx.Var.range(Estado.numero_de_campos // 2),
                        lambda idx: campo_nombre(idx)
                    ),
                    width="45%"  # Ancho de la columna izquierda
                ),
                rx.box(
                    rx.foreach(
                        rx.Var.range(Estado.numero_de_campos // 2, Estado.numero_de_campos),
                        lambda idx: campo_nombre(idx)
                    ),
                    width="45%"  # Ancho de la columna derecha
                ),
                spacing="5%",  # Espacio entre las dos columnas
            ),
            rx.button(
                "Guardar nombres",
                on_click=Estado.guardar_nombres,
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
                on_click=Estado.generar_jornadas,
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
                        Estado.nombres,
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
                Estado.jornadas,
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
