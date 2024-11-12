import sqlite3

#esta clase esta definida mas abajo, solo importar Crud.lafuncion 
class CrudSQLite:
    #conectar a la base de datos
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        print(f"Conectado a la base de datos '{db_name}'.")

    #crear tabla "inventario" Crud.crear_tabla()
    def crear_tabla(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS inventario \
            (id INTEGER PRIMARY KEY, \
            tipo TEXT NOT NULL, \
            nombre TEXT NOT NULL, \
            socket TEXT NOT NULL, \
            stock INTEGER NOT NULL, \
            descripcion TEXT, \
            precio INTEGER NOT NULL, \
            enlace TEXT)"
        )
        self.conn.commit()
        print("Tabla creada con éxito")
        
    #agregar info a la tabla Crud.agregar(tipo, nombre, compatibilidad_socket, stock, descripcion, precio, enlace)
    #definir  los parámetros de la función
    def agregar(self, tipo, nombre, socket, stock, descripcion, precio, enlace):
        self.cursor.execute(
            f"INSERT INTO inventario (tipo, nombre, socket, stock, descripcion, precio, enlace) VALUES ('{tipo}', '{nombre}', '{socket}', {stock}, '{descripcion}', {precio}, '{enlace}')"
        )
        self.conn.commit()
        print(f"Producto: {nombre}. Agregado con éxito al inventario")

    #modificar  info de la tabla Crud.modificar(id, tipo, nombre, socket, stock, descripcion, precio)
    #solo se pueden modificar todos  los campos de la tabla a la vez
    def modificar(self, id, tipo, nombre, socket, stock, descripcion, precio, enlace):
        self.cursor.execute(
            f"UPDATE inventario SET tipo = '{tipo}', nombre = '{nombre}', socket = '{socket}', stock = {stock}, descripcion = '{descripcion}', precio = {precio}, enlace = '{enlace}' WHERE id = {id}" 
        )
        self.conn.commit()
        print(f"Producto: {nombre}. Modificado con éxito en el inventario")

    #no usar, solo printea **ejemplo del profe** para recorrer la tabla facil
    def printlistar(self):
        def kprint(lista_diccionarios):
            for diccionario in lista_diccionarios:
                linea = " - ".join(f"{clave}: {valor}" for clave, valor in diccionario.items())
                print(linea)

        self.cursor.execute("SELECT * FROM inventario")
        todo = self.cursor.fetchall()
        campos = ['id', 'tipo', 'nombre', 'socket', 'stock', 'descripcion', 'precio', 'enlace']
        #lista_completa = [{'id': fila[0], 'nombre': fila[1], 'edad': fila[2]} for fila in todo]
        # Tiré esta magia siguiente para no tener que escribir fila[0] y fila[1] y fila[2]:
        lista_completa = [{k: v for k, v in zip(campos, fila)} for fila in todo]
        kprint(lista_completa)
    
    # devuelve una LISTA con  todos los elemntos de la tabla Crud.listar()
    def listar(self):
        self.cursor.execute("SELECT * FROM inventario")
        todo = self.cursor.fetchall()
        #campos = ['id', 'tipo', 'nombre', 'socket', 'stock', 'descripcion', 'precio', 'enlace']
        #lista_completa = [{k: v for k, v in zip(campos, fila)} for fila in todo]
        return todo


    # eliminar SOLO por id (toda la fila)  Crud.eliminar(id)
    def eliminar(self, id):
        self.cursor.execute(f"DELETE FROM inventario WHERE id = {id}")
        self.conn.commit()
        print(f"Producto con id {id} eliminado con éxito")

    # **USAR SIEMPRE** cierra la coneccion con la  base de datos
    def cerrar_db(self):
        self.conn.close()
        print(f"Conexión a la base de datos cerrada.")

    # busca elementos  en la tabla seleccionado un <campo> (id, tipo, nombre, etc) y
    # un <valor> que es una palabra **no exacta** como criterios de busqueda
    # Crud.serch_registros('nombre', 'rgb')
    def serch_registros(self, campo, valor):
        self.cursor.execute(f"SELECT * FROM inventario WHERE {campo} LIKE '%{valor}%'")  #probar para traer coincidencias
        todo = self.cursor.fetchall()
        campos = ['id', 'tipo', 'nombre', 'socket', 'stock', 'descripcion', 'precio', 'enlace']
        lista_completa = [{k: v for k, v in zip(campos, fila)} for fila in todo]   # probar si funciona
        return lista_completa
    
    #solo busca por campo (tipo, nombre,etc) y printea toda la columna Crud.get_registros('tipo')
    def get_registros (self, campo):
        self.cursor.execute(f"SELECT {campo} FROM inventario")
        todo = self.cursor.fetchall()
        lista_deseada =  []
        for fila in todo:
            lista_deseada.append(fila[0])
        return lista_deseada





    


#definir clase para tabla inventario, **CONTROLAR** que sea el mismo de la base de datos
Crud=CrudSQLite("basededatos.db")