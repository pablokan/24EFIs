import sqlite3

conn = sqlite3.connect('materiales.db')
print("Opened database successfully")

c = conn.cursor()

# Crear la tabla 'materiales'
c.execute('''
    CREATE TABLE IF NOT EXISTS materiales(
        cod INTEGER PRIMARY KEY,
        descripcion TEXT,
        precio REAL
    )
''')

# Lista de materiales
lista_materiales = [
    (1, 'Bolsa de Arena (15kg)', 2000),
    (2, 'Ladrillo', 170),
    (3, 'Bolsa de Yeso (30kg)', 10000),
    (4, 'Bolsa deCemento (50kg)', 11500),
    (5, 'Bolsa de Cal (25kg)', 4850),
]

# Usar executemany para insertar múltiples registros
c.executemany('INSERT INTO materiales (cod, descripcion, precio) VALUES (?, ?, ?)', lista_materiales)

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()