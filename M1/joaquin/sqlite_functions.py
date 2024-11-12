import sqlite3

# Funcion para crear la base de datos
def createDB():
    conn = sqlite3.connect("turnero.db") #nos conectamos a la base de datos
    conn.commit()
    conn.close()

    print('Base de datos creada')

# Funcion para crear una tabla
def createTable():
    conn = sqlite3.connect("turnero.db")
    cursor = conn.cursor() #creamos un cursor para ejecutar sentencias y consultas SQL
    cursor.execute(
        """CREATE TABLE reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cancha TEXT,
        fecha TEXT,
        hora TEXT,
        precio REAL,
        nombre TEXT,
        telefono TEXT,
        pagado BOOL
        )"""
    )
    conn.commit() #confirmamos la transaccion
    conn.close() #cerramos la conexion

    print('Tabla creada')

# Funcion de carga de datos
def insertRow(cancha: str, fecha: str, hora: str, precio: float, nombre: str, telefono: str, pagado: bool):
    conn = sqlite3.connect("turnero.db")
    cursor = conn.cursor()
    instruccion = f"""INSERT INTO reservas (cancha, fecha, hora, precio, nombre, telefono, pagado)
    VALUES ('{cancha}', '{fecha}', '{hora}', {precio}, '{nombre}', '{telefono}', {pagado})"""
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

    print('Fila añadida correctamente')

# Funcion de lectura de datos
def readRows():
    conn = sqlite3.connect("turnero.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM reservas" # El * toma todos los campos
    cursor.execute(instruccion)
    datos = cursor.fetchall() # Devuelve todos lo datos
    conn.commit()
    conn.close()
    return datos

# Funcion de carga de lista de datos
def insertRows(reservasList):
    conn = sqlite3.connect("turnero.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO reservas (cancha, fecha, hora, precio, nombre, telefono, pagado) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.executemany(instruccion, reservasList)
    conn.commit()
    conn.close()

    print('Filas añadida correctamente')

# Funcion para buscar un turno
def search(idReserva: int):
    conn = sqlite3.connect("turnero.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM reservas WHERE id={idReserva}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

# Funcion para actualizar datos
def updateFields(cancha: str, fecha: str, hora: str, precio: float, nombre: str, telefono: str, pagado: bool, idReserva: int):
    conn = sqlite3.connect("turnero.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE reservas SET cancha='{cancha}', fecha='{fecha}', hora='{hora}', precio={precio}, nombre='{nombre}', telefono='{telefono}', pagado={pagado} WHERE id={idReserva}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

    print('Fila actualizada correctamente')

# Funcion para borrar todas las filas
def deleteRows():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM reservas" # tomo todo los campos
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

# Funcion para eliminar un turno
def deleteRow(idReserva: int):
    conn = sqlite3.connect("turnero.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM reservas WHERE id={idReserva}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

    print('Fila borrada correctamente')

# Funcion para buscar el ID de una fila recien ingresada
def searchLastID():
    conn = sqlite3.connect("turnero.db")
    cursor = conn.cursor()
    instruccion = f"SELECT id FROM reservas ORDER BY id DESC LIMIT 1"
    cursor.execute(instruccion)
    datos = cursor.fetchone()
    conn.commit()
    conn.close()
    return datos[0]

# Testing que no queremos que se ejecute en el programa principal
if __name__ == '__main__':
    # createDB()
    # createTable()
    # deleteTable()
    # insertRow('Adentro 1', 'Juan', '2024-08-13', '9:30', 10.5)
    # insertRow('Adentro 2', 'Pedro', '2024-08-13', '8:00', 12.5)
    # insertRow('Afuera 1', 'Carla', '2024-08-13', '15:30', 9.5)
    # readRows()
    reservas = [
        ('Adentro 2', 'Juan', '2024-08-13', '17:00', 12.5),
        ('Afuera 1', 'Juan', '2024-08-13', '12:30', 9.5),
        ('Afuera 2', 'Juan', '2024-08-13', '11:00', 8.5)
    ]
    # insertRows(reservas)
    # readOrdered('hora')
    # search()
    # updateFields()
    # deleteRow()
    # print(searchLastID())
