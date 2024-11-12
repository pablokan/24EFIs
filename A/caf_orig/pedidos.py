import reflex as rx
import sqlite3

# Data de los pedidos
class Data(rx.State):
    pedidos: list[list] = []  # Lista para almacenar todos los pedidos
    ultimos_pedidos: list[list] = []  # Lista para almacenar los últimos 5 pedidos

    def ObtenerPedidos(self):
        # Conectamos a la base de datos y obtenemos todos los pedidos
        conn = sqlite3.connect('pedidos.db')  # Establecemos la conexión con la base de datos
        cursor = conn.cursor()  # Creamos un cursor para ejecutar consultas
        cursor.execute("SELECT * FROM pedidos")  # Consulta para obtener todos los pedidos
        self.pedidos = cursor.fetchall()  # Guardamos los resultados en la lista 'pedidos'
        conn.close()  # Cerramos la conexión a la base de datos

    def ObtenerUltimosPedidos(self):
    
        conn = sqlite3.connect('pedidos.db')  
        cursor = conn.cursor()  
        cursor.execute("SELECT * FROM pedidos ORDER BY fecha DESC LIMIT 5")
        self.ultimos_pedidos = cursor.fetchall()  # Guardamos los resultados en 'ultimos_pedidos'
        conn.close()

# Función para mostrar una fila de la tabla de pedidos
# Función para mostrar una fila de la tabla de pedidos
def show_person(person: list):
    page = rx.table.row(
        rx.table.cell(person[0], padding="12px", border="1px solid #ddd", color="blue"),  # ID
        rx.table.cell(person[1], padding="12px", border="1px solid #ddd", color="blue"),  # Fecha
        rx.table.cell(person[2], padding="12px", border="1px solid #ddd", color="blue"),  # Mesas
        rx.table.cell(person[3], padding="12px", border="1px solid #ddd", color="blue"),  # Personas
        rx.table.cell(person[4], padding="12px", border="1px solid #ddd", color="blue"),  # Producto
        rx.table.cell(person[5], padding="12px", border="1px solid #ddd", color="blue")   # Total
    )
    return page

# Tabla para mostrar todos los pedidos
def tablaPedidos():
    tabla = rx.box(
        rx.text("Todos los Pedidos", font_size="24px", font_weight="bold", margin_bottom="20px", color="#333"),
        rx.box(
            rx.button(
                'Cargar Pedidos',
                on_click=Data.ObtenerPedidos,
                background_color="#555",
                color="white",
                padding="10px 20px",
                font_weight="bold",
                border_radius="5px",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.2)",
            ),
            display="flex",
            justify_content="flex-end",
            margin_bottom="20px",
            padding_right="20px"
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("ID", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                    rx.table.column_header_cell("FECHA", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                    rx.table.column_header_cell("MESAS", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                    rx.table.column_header_cell("PERSONAS", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                    rx.table.column_header_cell("PRODUCTO", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                    rx.table.column_header_cell("TOTAL", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    Data.pedidos, show_person
                )
            ),
            width="100%",
            border="1px solid #ddd",
            border_collapse="collapse",
            border_radius="8px"
        ),
        padding="20px",
        box_shadow="0px 4px 8px rgba(0, 0, 0, 0.1)",
        border_radius="8px"
    )
    return tabla

# Tabla para mostrar los últimos 5 pedidos
def tablaUltimosPedidos():
    ultimos = rx.box(
        rx.text("Últimos 5 Pedidos", font_size="24px", font_weight="bold", margin_bottom="20px", color="#333"),
        rx.box(
            rx.button(
                'Cargar Últimos 5 Pedidos',
                on_click=Data.ObtenerUltimosPedidos,
                background_color="#555",
                color="white",
                padding="10px 20px",
                font_weight="bold",
                border_radius="5px",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.2)",
            ),
            display="flex",
            justify_content="flex-end",
            margin_bottom="20px",
            padding_right="20px"
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("ID", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                    rx.table.column_header_cell("FECHA", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                    rx.table.column_header_cell("MESAS", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                    rx.table.column_header_cell("PERSONAS", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                    rx.table.column_header_cell("PRODUCTO", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                    rx.table.column_header_cell("TOTAL", padding="12px", background_color="#555", color="white", border="1px solid #ddd"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    Data.ultimos_pedidos, show_person
                )
            ),
            width="100%",
            border="1px solid #ddd",
            border_collapse="collapse",
            border_radius="8px"
        ),
        padding="20px",
        box_shadow="0px 4px 8px rgba(0, 0, 0, 0.1)",
        border_radius="8px"
    )
    return ultimos