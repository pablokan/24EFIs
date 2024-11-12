import sqlite3

# Establece la conexion con la base de datos
def conectar_db():
    # Conectar la base de datos (archivo .db)
    conn = sqlite3.connect('clientes.db')
    return conn

def crear_tabla():
    # Conectar a la base de datos 
    conn = conectar_db()
    cursor = conn.cursor()

    # Crear tabla Clientes si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT,
            telefono TEXT,
            direccion TEXT,
            fecha DATE,
            horario TEXT
        )
    """)
    # Guardas los cambios y cerrar la conexion 
    conn.commit()
    conn.close()

#  Recibe los atributos de un cliente y lo agrega a la tabla
def insertar_cliente(nombre, email, telefono, direccion,fecha,horario):
    # Conectar a la base de datos 
    conn = conectar_db()
    cursor = conn.cursor()

    # Crear cliente en la tabla 
    cursor.execute(
        """INSERT INTO clientes (nombre, email, telefono, direccion, fecha, horario) 
        VALUES (?, ?, ?, ?, ?, ?)""",
        (nombre, email, telefono, direccion, fecha, horario)
    )
    # Guardas cambios y cerrar la conexion 
    conn.commit()
    conn.close()

# Recibe la ID del cliente y devuelve los datos
def seleccionar_cliente(user_id):
    from .backend import Cliente
    # Conectar a la base de datos 
    conn = conectar_db()
    cursor = conn.cursor()
    
    # Buscar cliente segun ID
    cursor.execute("SELECT * FROM clientes WHERE id=?", (user_id,))
    row = cursor.fetchone()
    
    # Cerrar la conexion
    conn.close()

    return row

# Modifica cliente segun ID y recibe datos del formulario
def modificar_cliente(user_id,nombre,email,telefono,direccion):
    # Conectar a la base de datos 
    conn = conectar_db()
    cursor = conn.cursor()

    # Actualizar valores del cliente
    cursor.execute("""
        UPDATE INTO clientes (nombre, telefono, direccion, email) WHERE id=?, 
        VALUES (?,?,?,?)
    """, (nombre,telefono,direccion,email,user_id))

    # Guardar cambios y cerrar la conexion
    conn.commit()
    conn.close()

# Recibe la ID  del cliente y lo elimina de la tabla
def borrar_cliente(user_id):
    # Conectar a la base de datos 
    conn = conectar_db()
    cursor = conn.cursor()
    
    # Borrar cliente 
    cursor.execute("DELETE FROM clientes WHERE id=?", (user_id,))
    
    # Guardar cambios y cerrar la conexion
    conn.commit()
    conn.close()

# Selecciona todos los clientes y lo devuelve
def seleccionar_todos():
    # Importar clase Cliente
    from .backend import Cliente
    # Conectar a la base de datos 
    conn = conectar_db()
    cursor = conn.cursor() 

    # Traer todos los datos
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    # Cerrar la conexion
    conn.close()
    
    # Devolver lista con objetos Cliente
    tabla_clientes = [
                        Cliente(
                            id=row[0], 
                            nombre=row[1], 
                            email=row[2], 
                            telefono=row[3], 
                            direccion=row[4],
                            fecha=row[5],
                            horario=row[6]
                            ) for row in rows
                    ]
    return tabla_clientes
