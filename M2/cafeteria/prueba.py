import sqlite3
from datetime import datetime

# Conectar la base de datos
conexion = sqlite3.connect("pedidos.db")
cursor = conexion.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        mesa INTEGER NOT NULL,
        personas INTEGER NOT NULL,
        productos TEXT NOT NULL,
        precio_total REAL NOT NULL
    )
''')

""" 
# Función para borrar todos los pedidos de la base de datos
def borrar_todos_los_pedidos():
    cursor.execute("DELETE FROM pedidos")
    conexion.commit()
    print("Todos los pedidos han sido borrados.")

borrar_todos_los_pedidos()

 """
# Cerrar la conexión cuando ya no sea necesario
conexion.close()