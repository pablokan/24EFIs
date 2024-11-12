"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...
import reflex as rx
from rxconfig import config
import sqlite3

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


# Funciones

#agregado por pomo (23/10/2024):
def obtener_total_un_producto(nombre_producto):
     # Consulta SQL para obtener el total del producto específico
    query = "SELECT SUM(stock) FROM productos WHERE nombre = ?"
    cursor.execute(query, (nombre_producto,))

    # Obtener el resultado
    total = cursor.fetchone()[0]

    return total if total is not None else 0
#modificar
def agregar_producto(nombre, precio_compra, precio_venta, fecha, stock):
    cursor.execute("INSERT INTO productos (nombre, precio_compra, precio_venta, fecha, stock) VALUES (?, ?, ?, ?, ?)", 
                   (nombre, precio_compra, precio_venta, fecha, stock))
    conn.commit()

def realizar_venta(producto_id, cantidad):
    cursor.execute("UPDATE productos SET stock = stock - ? WHERE id = ?", (cantidad, producto_id))
    cursor.execute("INSERT INTO ventas (producto_id, cantidad, fecha) VALUES (?, ?, DATE('now'))", (producto_id, cantidad))
    conn.commit()

#modificado por pomo:
def consultar_stock():
    cursor.execute("SELECT id, nombre, precio_compra, precio_venta, fecha, stock FROM productos")
    for row in cursor.fetchall():
        id_producto, nombre, precio_compra, precio_venta, fecha, stock = row
        print(f'Producto: {nombre}, Precio compra: {precio_compra}, Precio venta: {precio_venta}, Fecha: {fecha}, Stock: {stock}')

def balance(): 
    cursor.execute("SELECT SUM(cantidad) FROM ventas")
    total_ventas = cursor.fetchone()[0]
    print("Total Ventas:", total_ventas if total_ventas is not None else 0)


# Menú
while True:

    print("1. Agregar producto")
    print("2. Ver historial")
    print("3. Realizar venta")
    print("4. Consultar stock")
    print("5. Salir")
    opcion = input("Ingrese opción: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        precio_compra = float(input("Precio compra: "))
        precio_venta = float(input("Precio venta: "))
        stock = int(input("Stock: "))
        agregar_producto(nombre, precio_compra, precio_venta, stock)

#agregado por pomo (23/10/2024):
    elif opcion == '2':

        while True:

            print("1.Total de un producto")
            print("2.Historial total del stock")
            print('3.Atras')
            option = input('Ingrese opcion: ')

            if option == '1':
                 nombre_producto = input('Nombre del producto:')
                 cantida = obtener_total_un_producto(nombre_producto)
                 print(f'la cantidad de {nombre_producto} es de {cantida}')

            elif option == '2':
                 consultar_stock()

            elif option =='3':
                break

    elif opcion == "3":
        producto_id = int(input("ID Producto: "))
        cantidad = int(input("Cantidad: "))
        realizar_venta(producto_id, cantidad)
        
    elif opcion == "4":
        consultar_stock()
        
    elif opcion == "6":
        break

conn.close()

