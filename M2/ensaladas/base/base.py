import reflex as rx
from typing import List, Dict

class State(rx.State):
    
    nombre_producto: str = ""
    precio_producto: float = 0.0
    codigo_barra: str = ""
    stock: int = 0
    descripcion_producto: str = ""
    mensaje: str = ""
    productos: List[Dict[str, str]] = []  

    def set_nombre_producto(self, nombre):
        self.nombre_producto = nombre

    def set_precio_producto(self, precio):
        self.precio_producto = float(precio)

    def set_codigo_barra(self, codigo):
        self.codigo_barra = codigo

    def set_stock(self, stock):
        self.stock = int(stock)

    def set_descripcion_producto(self, descripcion):
        self.descripcion_producto = descripcion

    def agregar_producto(self):
        nuevo_producto = {
            "nombre_producto": self.nombre_producto,
            "codigo_barra": self.codigo_barra,
            "precio_producto": self.precio_producto,
            "stock": self.stock,
            "descripcion": self.descripcion_producto
        }
        self.productos.append(nuevo_producto)
        self.mensaje = "Producto agregado exitosamente."
        
        #self.nombre_producto = ""
       # self.codigo_barra = ""
       # self.precio_producto = 0.0
       # self.stock = 0
        #self.descripcion_producto = ""

def crear_fila_producto(producto):
    return rx.table.row(
        rx.table.cell(producto["nombre_producto"]),  
        rx.table.cell(producto["codigo_barra"]),   
        rx.table.cell(producto["precio_producto"]),  
        rx.table.cell(producto["stock"]),            
        rx.table.cell(producto["descripcion"]),      
        rx.button("Editar"),                          
        rx.button("Eliminar", color_scheme='red')  
    )

def index():

    return rx.box(
        rx.hstack(
            rx.box(
                rx.heading("Agregar Producto", color="#4A90E2", size="md"),
                rx.input(placeholder="Nombre del producto", on_blur=State.set_nombre_producto),
                rx.input(placeholder="Código de barra", on_blur=State.set_codigo_barra),
                rx.input(placeholder="Precio", type="number", on_blur=State.set_precio_producto),
                rx.input(placeholder="Stock", type="number", on_blur=State.set_stock),
                rx.input(placeholder="Descripción", on_blur=State.set_descripcion_producto),
                rx.button("Agregar Producto", on_click=State.agregar_producto, bg="#4A90E2", color="white"),
                rx.text(State.mensaje, color="gray"),
                bg="lightblue",
                border="1px solid #D9D9D9",
                border_radius="8px",
                padding="20px",
                margin="10px",
                width="300px",
            ),
            rx.box(
                rx.heading("Lista de Productos", color="#F39C12", size="md"),
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Nombre"),
                            rx.table.column_header_cell("Código"),
                            rx.table.column_header_cell("Precio"),
                            rx.table.column_header_cell("Stock"),
                            rx.table.column_header_cell("Descripción"),
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(State.productos, crear_fila_producto)
                    ),
                    width="100%",
                ),
                border="1px solid #D9D9D9",
                border_radius="8px",
                padding="20px",
                margin="10px",
                width="100%",
            ),
        )
    )

app = rx.App()
app.add_page(index, title="ENSALADAS")
