import sqlite3
from datetime import datetime, timedelta


class Database:
    def __init__(self, dbName: str, tableName: str, *args) -> None:
        self.cone = sqlite3.connect(dbName + '.db')
        self.cursor = self.cone.cursor()
        self.tableName = tableName
        fields = list(args)

        if len(fields) != 0:
            self.fieldNames = ['id'] + [field.split()[0] for field in fields]
            strFieldsConTipo = ', '.join(fields)
            query = f"CREATE TABLE IF NOT EXISTS {self.tableName} (id INTEGER PRIMARY KEY AUTOINCREMENT, {strFieldsConTipo})"
            self.cursor.execute(query)
            self.cone.commit()
        else:
            self.cursor.execute(f"PRAGMA table_info({self.tableName})")
            dataColumnas = self.cursor.fetchall()
            self.fieldNames = [columna[1] for columna in dataColumnas]

    def get_all(self):
        self.cursor.execute(f"SELECT * FROM {self.tableName}")
        records = [list(t) for t in self.cursor.fetchall()]
        return records

    def upd(self, id, field, value):
        valueF = f"'{value}'" if isinstance(value, str) else str(value)
        query = f"UPDATE {self.tableName} SET {field} = {valueF} WHERE id = {id}"
        self.cursor.execute(query)
        self.cone.commit()

    def close(self):
        self.cursor.close()
        self.cone.close()
    
    def insert_usuario(self, nombre, dni, email, telefono, direccion):
        query = """
        INSERT INTO usuarios (nombre, dni, email, telefono, direccion)
        VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (nombre, dni, email, telefono, direccion))
        self.cone.commit()

    def insert_contenido(self, titulo, genero, ano, director, protagonista, tipo_contenido):
        query = """
        INSERT INTO contenido (titulo, genero, ano, director, protagonista, tipo_contenido)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (titulo, genero, ano, director, protagonista, tipo_contenido))
        self.cone.commit()

    def insert_alquiler(self, usuario_id, dni_usuario, contenido_id, fecha_alquiler, fecha_devolucion, importe, tipo_contenido, alquilado):
        query = """
        INSERT INTO alquileres (usuario_id, dni_usuario, contenido_id, fecha_alquiler, fecha_devolucion, importe, tipo_contenido, alquilado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (usuario_id, dni_usuario, contenido_id, fecha_alquiler, fecha_devolucion, importe, tipo_contenido, alquilado))
        self.cone.commit()


    def obtener_datos_usuario_por_dni(self, dni):
        self.cursor.execute("SELECT * FROM usuarios WHERE dni = ?", (dni,))
        resultado = [list(t) for t in self.cursor.fetchall()]
        return resultado if resultado else None

    
    def buscar_pelicula_por_titulo(self, titulo):
        self.cursor.execute("SELECT * FROM contenido WHERE titulo = ?", (titulo,))
        resultado = [list(t) for t in self.cursor.fetchall()]
        return resultado if resultado else None


    def obtener_alquileres_con_detalles(self):
        self.cursor.execute('''
            SELECT 
                alquileres.id, 
                usuarios.nombre AS nombre_usuario, 
                usuarios.dni,
                contenido.titulo AS titulo_contenido, 
                alquileres.fecha_alquiler, 
                alquileres.fecha_devolucion, 
                alquileres.importe, 
                alquileres.tipo_contenido,
                alquileres.alquilado
            FROM 
                alquileres
            JOIN 
                usuarios ON alquileres.usuario_id = usuarios.id
            JOIN 
                contenido ON alquileres.contenido_id = contenido.id
        ''')
        
        records = [list(t) for t in self.cursor.fetchall()]
        
        return records
    

    def eliminar_usuario(self, dni):
        self.cursor.execute("DELETE FROM usuarios WHERE dni = ?", (dni,))
        self.cone.commit()
    

    def eliminar_contenido(self, titulo):
        self.cursor.execute("DELETE FROM contenido WHERE titulo = ?", (titulo,))
        self.cone.commit()


  

