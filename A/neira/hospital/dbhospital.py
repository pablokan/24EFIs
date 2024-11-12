import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('dbHospital.db')

# Crear la tabla datosp con los nuevos campos
conn.execute('''
CREATE TABLE IF NOT EXISTS datosp (
    DNI INTEGER PRIMARY KEY,
    nombre VARCHAR(50),
    correo VARCHAR(100),
    telefono VARCHAR(15),
    fecha_nacimiento DATE
);
''')

# Cerrar la conexión
conn.close()
