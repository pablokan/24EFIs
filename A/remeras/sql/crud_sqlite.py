import sqlite3

class CrudSQLite:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def crear_tabla(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS clientes \
            (id INTEGER PRIMARY KEY, \
            nombre TEXT NOT NULL, \
            telefono TEXT NOT NULL,\
            email TEXT NOT NULL,\
            usuario TEXT NOT NULL,\
            contra TEXT NOT NULL)"
        )
        self.conn.commit()
        
    def agregar(self, nombre, telefono, email,usuario,contra):
        self.cursor.execute(
            f"INSERT INTO clientes (nombre,telefono,email,usuario,contra) VALUES ('{nombre}', '{telefono}','{email}','{usuario}','{contra}')"
        )
        self.conn.commit()
        
    def modificar(self, id, nombre, telefono, email,usuario,contra):
        self.cursor.execute(
            f"UPDATE clientes SET nombre = '{nombre}', telefono = '{telefono}',email= '{email}', usuario= '{usuario}', contra='{contra}' WHERE id = {id}" 
        )
        self.conn.commit()

    def listar(self):
        def kprint(lista_diccionarios):
            for diccionario in lista_diccionarios:
                linea = " - ".join(f"{clave}: {valor}" for clave, valor in diccionario.items())
                print(linea)

        self.cursor.execute("SELECT * FROM clientes")
        todo = self.cursor.fetchall()
        campos = ['id', 'nombre', 'telefono', 'email', 'usuario', 'contra']
        #lista_completa = [{'id': fila[0], 'nombre': fila[1], 'edad': fila[2]} for fila in todo]
        # Tiré esta magia siguiente para no tener que escribir fila[0] y fila[1] y fila[2]:
        lista_completa = [{k: v for k, v in zip(campos, fila)} for fila in todo]
        kprint(lista_completa)

    def eliminar(self,tabla ,id):
        self.cursor.execute(f"DELETE FROM {tabla} WHERE id = {id}")
        self.conn.commit()

    def cerrar_db(self):
        self.conn.close()






























