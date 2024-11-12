import sqlite3
import reflex as rx
from datetime import datetime

# Conectar a la base de datos
conn = sqlite3.connect('pedidos.db')
cursor = conn.cursor()

# Lista de productos con sus precios
productos = [
    ("Café chico", 9999),
    ("Café en jarra", 1800),
    ("Café doble", 2100),
    ("Café con leche", 2100),
    ("Té", 1700),
    ("Té con leche", 1900),
    ("Mate cocido", 1900),
    ("Submarino", 3000),
    ("Chocolate (frío o caliente)", 2600),
    ("Medialunas/Facturas", 750),
    ("Criollos", 600),
    ("Tostadas por unidad", 900),
    ("Mafalda", 1700)
]

class St(rx.State):
    personas: int = 0
    producto: str = ""
    precio_producto: int = 0
    cantidad: int = 0
    cantidad_Productos: list = []
    mesa_color: str = "green"  # Color inicial de la mesa
    mesa_actual: str = ""  # Almacena el nombre de la mesa seleccionada

    def agregar_pedido(self, personas, productos, precio_total):
        # Obtener la fecha y hora actuales
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Insertar el pedido en la tabla 'pedidos'
        cursor.execute('''
            INSERT INTO pedidos (fecha, mesa, personas, productos, precio_total)
            VALUES (?, ?, ?, ?, ?)
        ''', (fecha, self.mesa_actual, personas, productos, precio_total))
        # Guardar los cambios
        conn.commit()

    def abrir_mesa(self, mesa_nombre):
        self.mesa_color = "green"
        self.mesa_actual = mesa_nombre  # Guardar el nombre de la mesa seleccionada

    def cerrar_mesa(self):
        self.mesa_color = "red"

    def set_producto(self, producto):
        # Encuentra el precio del producto seleccionado
        for prod, precio in productos:
            if prod == producto:
                self.producto = producto
                self.precio_producto = precio
                break

    def set_cantidad(self, cantidad):
        try:
            self.cantidad = int(cantidad)
        except ValueError:
            self.cantidad = 0  # Valor predeterminado si no es un número válido

    def agregar_producto(self):
        if self.producto and self.cantidad > 0:
            # Calcula el precio total del producto multiplicando por la cantidad
            precio_total_producto = self.precio_producto * self.cantidad
            # Agregamos el producto, cantidad y precio total como un string a la lista
            self.cantidad_Productos.append(f"{self.producto} x {self.cantidad} - ${precio_total_producto}")

    def quitar_ultimo_producto(self):
        # Eliminamos el último producto de la lista, si existe
        if self.cantidad_Productos:
            self.cantidad_Productos.pop()

    def enviar(self):
        # Convertir lista de productos a un string
        productos = "; ".join(self.cantidad_Productos)
        # Calcular el precio total sumando los precios de cada producto en `cantidad_Productos`
        precio_total = sum(int(item.split("- $")[-1]) for item in self.cantidad_Productos)
        # Llamar a agregar_pedido para almacenar los datos en la base de datos
        self.agregar_pedido(self.personas, productos, precio_total)
        # Limpiar la lista de productos después de enviar
        self.cantidad_Productos.clear()

def mesa(nombre):
    # Definimos cada mesa con estilo y tamaño
    mesita = rx.dialog.root(
        rx.dialog.trigger(
            rx.box(
                rx.button(
                    nombre, 
                    color_scheme=St.mesa_color,  # Usa el color de la mesa del estado
                    height="150px",
                    width="150px",
                    border_radius="100px",
                    on_click=lambda: St.abrir_mesa(nombre)  # Guardar la mesa seleccionada al abrir
                ), 
                display="flex", 
                align_items="center", 
                justify_content="center"
            )
        ),
        rx.dialog.content(
            rx.vstack(
                rx.heading(nombre, font_size="24px", margin_bottom="10px", color_scheme="blue"),
                rx.hstack(
                    rx.button("Abrir Mesa", color_scheme="green", on_click=lambda: St.abrir_mesa(nombre)),
                    rx.button("Cerrar Mesa", color_scheme="red", on_click=St.cerrar_mesa),
                    spacing="10px"
                ),
                rx.text("Personas", color_scheme="blue"),
                rx.input(
                    width="100%",
                    on_blur=St.set_personas
                ),
                rx.text("Producto", color_scheme="blue"),
                # Menú desplegable para seleccionar productos
                rx.hstack(
                    rx.select([prod for prod, _ in productos], placeholder="Seleccionar producto", on_change=St.set_producto),
                    rx.input(
                        width="100%",
                        placeholder="Cantidad",
                        on_blur=lambda cantidad: St.set_cantidad(cantidad)
                    ),
                    spacing="10px"
                ),
                rx.hstack(
                    rx.button("BORRAR", color_scheme="red", on_click=St.quitar_ultimo_producto),
                    rx.button("OK", color_scheme="blue", on_click=St.agregar_producto),
                    spacing="10px"
                ),
                rx.text("Mi pedido:", color_scheme="blue"),
                
                # Usamos `rx.foreach` para mostrar cada pedido en `cantidad_Productos`
                rx.foreach(
                    St.cantidad_Productos, 
                    lambda pedido: rx.text(pedido, color_scheme="blue")
                ),

                rx.button("Enviar", color_scheme="green", on_click=St.enviar)
            ),
            padding="20px",
            background_color="white",
            border_radius="10px",
            box_shadow="lg",
            max_width="300px"
        )
    )
    return mesita

def mesas():
    # Centramos las mesas horizontalmente
    page = rx.center(
        rx.hstack(
            mesa("Mesa 1"),
            mesa("Mesa 2"),
            mesa("Mesa 3"),
            spacing="20px"  # Espaciado entre mesas
        ),
        background_color="lightyellow",
        padding="20px",
        min_height="100vh"  # Aseguramos que se centre verticalmente también
    )
    return page