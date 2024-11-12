import reflex as rx
import sqlite3

class ProductState(rx.State):
    
    products: list[dict] = []
    def load_entries(self):
        
        self.products = get_products()

    def add_product_to_db(self, form_data):
        
        insert_product(
            form_data["nombre"],
            form_data["descripcion"],
            float(form_data["precio"]),
            int(form_data["stock"])
        )
        self.load_entries()

    def delete_product_from_db(self, product_name):
        
        delete_product(product_name)
        self.load_entries()


def connect_db():
    
    return sqlite3.connect("productos.db")

def create_table():
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_product(nombre, descripcion, precio, stock):
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, precio, stock)
        VALUES (?, ?, ?, ?)
    """, (nombre, descripcion, precio, stock))
    conn.commit()
    conn.close()

def delete_product(nombre):
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre,))
    conn.commit()
    conn.close()

def get_products():
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, descripcion, precio, stock FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

@rx.page(on_load=ProductState.load_entries)
def index():
    
    return rx.center(
        rx.vstack(
            # Encabezado principal
            rx.heading("Control de Stock - Ricuras", font_size="3xl", color="pink.600", mb=6),

            # Formulario para agregar productos
            rx.box(
                rx.form.root(
                    rx.vstack(
                        rx.form.field(
                            rx.input(
                                placeholder="Nombre del producto",
                                name="nombre",
                                variant="soft",
                                bg="pink.50",
                                color="black",
                                borderColor="pink.300",
                                _hover={"borderColor": "pink.400"},
                            ),
                            label="Nombre",
                            width="100%",
                        ),
                        rx.form.field(
                            rx.input(
                                placeholder="Descripción",
                                name="descripcion",
                                variant="soft",
                                bg="pink.50",
                                color="black",
                                borderColor="pink.300",
                                _hover={"borderColor": "pink.400"},
                            ),
                            label="Descripción",
                            width="100%",
                        ),
                        rx.form.field(
                            rx.input(
                                placeholder="Precio",
                                name="precio",
                                type="number",
                                variant="soft",
                                bg="pink.50",
                                color="black",
                                borderColor="pink.300",
                                _hover={"borderColor": "pink.400"},
                            ),
                            label="Precio",
                            width="100%",
                        ),
                        rx.form.field(
                            rx.input(
                                placeholder="Stock",
                                name="stock",
                                type="number",
                                variant="soft",
                                bg="pink.50",
                                color="black",
                                borderColor="pink.300",
                                _hover={"borderColor": "pink.400"},
                            ),
                            label="Stock",
                            width="100%",
                        ),
                        rx.button(
                            "Agregar Producto",
                            bg="pink.400",
                            color="white",
                            width="100%",
                            mt=4,
                            _hover={"bg": "pink.500"},
                            type="submit",
                        ),
                    ),
                    on_submit=ProductState.add_product_to_db,
                ),
                width="400px",
                padding="20px",
                box_shadow="xl",
                border_radius="xl",
                border="1px solid",
                borderColor="pink.200",
                bg="white",
                mb=8,
            ),

            # Lista de productos
            rx.heading("Lista de Productos", font_size="2xl", color="purple.500", mb=4),
            rx.vstack(
                rx.foreach(
                    ProductState.products,
                    lambda product: rx.box(
                        rx.hstack(
                            rx.box(
                                rx.text(f"Producto: {product[0]}", font_weight="bold", color="black"),
                                rx.text(f"Descripción: {product[1]}",  color="black"),
                                rx.text(f"Precio: ${product[2]:.2f}", color="black"),
                                rx.text(f"Stock: {product[3]}", color="black"),
                                width="100%",
                                padding="10px",
                            ),
                            # Botón para eliminar producto
                            rx.button(
                                "Eliminar",
                                color="white",
                                bg="red",
                                on_click=lambda: ProductState.delete_product_from_db(product[0])
                            ),
                        ),
                        width="100%",
                        mb=2,
                        bg="white",
                    ),
                ),
                width="100%",
                max_width="800px",
                spacing="4",
            ),
        ),
        padding="20px",
        bg="yellow.50",
        min_height="100vh",
    )

# Configuración de la aplicación
create_table()
app = rx.App()
app.add_page(index)