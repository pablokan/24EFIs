import sqlite3


# Clase que maneja la base de datos para almacenar información de jugadores
class JugadorDB:
    # Método inicializador de la clase
    def __init__(self, db_file='jugadores.db'):
        # Conecta a la base de datos SQLite especificada (o la crea si no existe)
        self.conn = sqlite3.connect(db_file)
        # Crea un cursor para ejecutar comandos SQL
        self.cursor = self.conn.cursor()
        # Llama al método para crear la tabla en la base de datos si no existe
        self.create_table()


    # Método para crear la tabla de jugadores si aún no existe en la base de datos
    def create_table(self):
        # Ejecuta el comando SQL para crear la tabla "jugadores" con las columnas especificadas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS jugadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,                         
                dorsal INTEGER,                      
                minutos INTEGER,                     
                puntos INTEGER,                      
                faltas INTEGER                       
            )
        ''')
        # Guarda los cambios en la base de datos
        self.conn.commit()


    # Método para agregar un jugador a la base de datos
    def agregar_jugador(self, nombre, dorsal, minutos, puntos, faltas):
        # Ejecuta el comando SQL para insertar un nuevo jugador con los datos dados
        self.cursor.execute('''
            INSERT INTO jugadores (nombre, dorsal, minutos, puntos, faltas)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, dorsal, minutos, puntos, faltas))
        # Guarda los cambios en la base de datos
        self.conn.commit()
        # Retorna el ID del jugador recién agregado
        return self.cursor.lastrowid


    # Método para eliminar un jugador de la base de datos dado su ID
    def eliminar_jugador(self, jugador_id):
        # Ejecuta el comando SQL para eliminar el jugador con el ID especificado
        self.cursor.execute('''
            DELETE FROM jugadores WHERE id=?
        ''', (jugador_id,))
        # Guarda los cambios en la base de datos
        self.conn.commit()


    # Método para obtener todos los jugadores almacenados en la base de datos
    def obtener_todos_jugadores(self):
        # Ejecuta el comando SQL para seleccionar todos los jugadores
        self.cursor.execute('SELECT * FROM jugadores')
        # Retorna una lista con todos los registros de jugadores como tuplas
        return self.cursor.fetchall()


    # Método para cerrar la conexión con la base de datos
    def cerrar_conexion(self):
        # Cierra la conexión con la base de datos para liberar recursos
        self.conn.close()


# Ejemplo de uso de la clase JugadorDB
db = JugadorDB()  # Crea una instancia de la clase JugadorDB


# Agrega un nuevo jugador a la base de datos
jugador_id = db.agregar_jugador("Juan Pérez", 10, 25, 15, 2)
print("Jugador agregado con ID:", jugador_id)  # Imprime el ID del jugador agregado


# Elimina al jugador recién agregado usando su ID
db.eliminar_jugador(jugador_id)


# Obtiene e imprime todos los jugadores almacenados en la base de datos
jugadores = db.obtener_todos_jugadores()
for jugador in jugadores:
    print(jugador)


# Cierra la conexión con la base de datos
db.cerrar_conexion()