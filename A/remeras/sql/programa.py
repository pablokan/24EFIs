# Importar la clase
from crud_sqlite import CrudSQLite


# Crear un objeto de la clase
db = CrudSQLite("datos.db")

# Crear la tabla (si no existe)
db.crear_tabla()

nombre= input('Nombre:')
telefono= input('telefono:')
email= input('email')
usuario=input('usuario')
contra=input('contraseña')


db.agregar(nombre, telefono, email, usuario, contra)







db.listar()











