"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

import sqlite3

class State(rx.State):
    opcionElegida: str
    elegirOpcion: str

# Conectar a la base de datos
conn = sqlite3.connect('ventas_y_stock.db')
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        precio_compra REAL,
        precio_venta REAL,
        fecha DATE,
        stock INTEGER
    );
''')

def obtener_total_un_producto(nombre_producto):
     # Consulta SQL para obtener el total del producto específico
    query = "SELECT SUM(stock) FROM productos WHERE nombre = ?"
    cursor.execute(query, (nombre_producto,))

    # Obtener el resultado
    total = cursor.fetchone()[0]

    return total if total is not None else 0

def agregarProducto(nombre, precio_compra, precio_venta, fecha, stock):
    cursor.execute("INSERT INTO productos (nombre, precio_compra, precio_venta, fecha, stock) VALUES (?, ?, ?, ?, ?)", 
                   (nombre, precio_compra, precio_venta, fecha, stock))
    conn.commit()

def realizar_venta(producto_id, cantidad):
    cursor.execute("UPDATE productos SET stock = stock - ? WHERE id = ?", (cantidad, producto_id))
    cursor.execute("INSERT INTO ventas (producto_id, cantidad, fecha) VALUES (?, ?, DATE('now'))", (producto_id, cantidad))
    conn.commit()

def consultar_stock():
    cursor.execute("SELECT id, nombre, precio_compra, precio_venta, fecha, stock FROM productos")
    for row in cursor.fetchall():
        id_producto, nombre, precio_compra, precio_venta, fecha, stock = row
        rx.print(f'Producto: {nombre}, Precio compra: {precio_compra}, Precio venta: {precio_venta}, Fecha: {fecha}, Stock: {stock}')

def balance(): 
    cursor.execute("SELECT SUM(cantidad) FROM ventas")
    total_ventas = cursor.fetchone()[0]
    print("Total Ventas:", total_ventas if total_ventas is not None else 0)

def menu(opcion):

    if opcion == "Agregar producto":
        producto = rx.input("Producto: ")
        precio_compra = rx.input("Precio compra: ")
        precio_venta = rx.input("Precio venta: ")
        stock = rx.input("Stock: ")
        agregarProducto(producto, precio_compra, precio_venta, stock)

    elif opcion == 'Ver historial':

        while True:

            rx.select("Total de un producto",
            "Historial total del stock",
            "Atras",on_change=State.set_elegirOpcion,)
        
            if  State.elegirOPcion == "Total de un producto":
                 nombre_producto = rx.input('Nombre del producto:')
                 cantida = obtener_total_un_producto(nombre_producto)
                 rx.text(f'la cantidad de {nombre_producto} es de {cantida}')

            elif State.elegirOpcion == "Historial total del stock":
                 consultar_stock()

            elif State.elegirOpcion == "Atras":
                break
            
    elif opcion == "Realizar venta":
        producto_id = int(rx.input("ID Producto: "))
        cantidad = int(rx.input("Cantidad: "))
        realizar_venta(producto_id, cantidad)
        
    elif opcion == "Consultar stock":
        consultar_stock()
        
    elif opcion == "Salir":
            return rx.text("Gracias por todo")


def index():
    page =rx.box(
        rx.vstack(
            rx.heading("Gestion de verduleria EFI 2024"),
            rx.image(
                src = "/imagen.jpeg",
                width = "2400px",
                height = "250px",
            ),
            rx.heading("Alumnos: Silva Nahuel, "),
            rx.text("Altamirano marcos,"),
            rx.text("Funes Marcos,"),
            rx.text("Panero Maximiliano."),
            rx.divider(),
            rx.text("Lista de opciones:"),
    ),  
        rx.hstack(
            rx.select(["Agregar Producto",
                         "Ver historial",
                         "Realizar Venta",
                         "Consultar Stock"],
                        default_value="",
                        on_change=State.set_opcionElegida,
            )),                
            rx.input(State.opcionElegida,
                rx.button("Buscar",
                   
                        ),
                    ),
                background="Green",
            )
            
    return page
conn.close()
app = rx.App()
app.add_page(index)
