import reflex as rx
import sqlite3

class PedidoState(rx.State):
    productos = [""]  # Inicializa productos como una lista con un producto vacío

    @staticmethod
    def agregar_producto():
        PedidoState.productos.append("")  # Agrega un nuevo campo de producto vacío

    @staticmethod
    def actualizar_producto(index, value):
        PedidoState.productos[index] = value  # Actualiza el valor de un producto en la lista


def crear_pedido(mesa, personas, productos, precio_total):
    conn = sqlite3.connect('pedidos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO pedidos (mesa, personas, productos, precio_total)
        VALUES (?, ?, ?, ?)
    ''', (mesa, personas, productos, precio_total))
    
    conn.commit()
    conn.close()

def modificar_pedido(id_pedido, mesa, personas, productos, precio_total):
    conn = sqlite3.connect('pedidos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE pedidos
        SET mesa = ?, personas = ?, productos = ?, precio_total = ?
        WHERE id = ?
    ''', (mesa, personas, productos, precio_total, id_pedido))
    
    conn.commit()
    conn.close()

def borrar_pedido(id_pedido):
    conn = sqlite3.connect('pedidos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        DELETE FROM pedidos
        WHERE id = ?
    ''', (id_pedido,))
    
    conn.commit()
    conn.close()


