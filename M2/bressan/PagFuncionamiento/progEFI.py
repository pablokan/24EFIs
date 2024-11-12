import os # uso import os porque tuve un problema a la hora de buscar el archivo de la base de datos, busque en internet y con esta libreria se puede resolver
import reflex as rx
import sqlite3

db_path = os.path.join(os.path.dirname(__file__), 'database/basededatos.db') #obtener ruta absoluta de la base de datos

#backend
class Carrito(rx.State):
    items: list[int] = []
    total: int = 0

    def agregar_precio_componente(self, comp):
        self.items.append(comp)
        self.calcular_total() 

    def calcular_total(self):
        self.total = sum(self.items)

    def vaciar_carrito(self):
        self.items = []
        self.total = 0

def obtener_componentes(tipo):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventario WHERE tipo = ?', (tipo,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def crear_pagina_componentes(tipo, titulo):
    componentes = obtener_componentes(tipo)
    return rx.container(
        rx.heading(titulo),
        *[
            rx.container(
                rx.text(f'{componente[5]} - Precio ${componente[6]}'),
                rx.button('Agregar componente', on_click=Carrito.agregar_precio_componente(componente[6]))
            ) for componente in componentes
        ],
        rx.link(
            rx.button('Atras'),
            href='/'
        ),
    )

def micro(): # obtener de cada componente la descripcion y el precio
    return crear_pagina_componentes('CPU', 'Microprocesador')

def mother():
    return crear_pagina_componentes('Motherboard', 'Motherboard')

def ram():
    return crear_pagina_componentes('RAM', 'Memorias RAM')

def almacenamiento():
    return crear_pagina_componentes('Almacenamiento', 'Almacenamiento')

def fuente():
    return crear_pagina_componentes('Fuente', 'Fuente de poder')

def gabinete():
    return crear_pagina_componentes('Gabinete', 'Gabinete')

def grafica():
    return crear_pagina_componentes('GPU', 'Tajeta grafica')

def carrito(): # por separado, la pagina del carrito
    return rx.container(
        rx.heading('Carrito de Compras'),
        rx.text(
            f'Total: ${Carrito.total}'
        ),
        rx.button(
            'Vaciar carrito', on_click=Carrito.vaciar_carrito()
        ),
        rx.link(
            rx.button('Atras'),
            href='/'
        ),
    )

#frontend
def index():
    return rx.container(
        rx.heading('ITEC Store'),
        rx.divider(),
        rx.text('En esta pagina le damos la oportunidad al usuario de armar su propia PC de escritorio'),
        rx.link(
            rx.button('MOTHERBOARD'), # armar el boton que te lleva a la pagina de cada componente
            href='/mother'
        ),
        rx.link(
            rx.button('MICROPROCESADOR'),
            href='/micro',
        ),
        rx.link(
            rx.button('RAM'),
            href='/ram'
        ),
        rx.link(
            rx.button('ALMACENAMIENTO'),
            href='/almacenamiento'
        ),
        rx.link(
            rx.button('FUENTE DE PODER'),
            href='/fuente',
        ),
        rx.link(
            rx.button('GABINETES'),
            href='/gabinete'
        ),
        rx.link(
            rx.button('TARJETA GRAFICA'),
            href='/grafica',
        ),
        rx.link(
            rx.button('VER CARRITO'), # boton que te lleva a la pagina para ver el carrito
            href='/carrito',
        ),
        ),


app = rx.App() # inicializamos la pagina
app.add_page(index)
app.add_page(micro)
app.add_page(mother)
app.add_page(ram)
app.add_page(almacenamiento)
app.add_page(fuente)
app.add_page(gabinete)
app.add_page(grafica)
app.add_page(carrito)