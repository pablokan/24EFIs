import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('base_datos.db')

#Crear la tabla Donantes
#conn.execute(" CREATE TABLE Donantes (id INTEGER PRIMARY KEY, Nombre TEXT, Apellido TEXT, Telefono TEXT, Grupo_Sanguineo TEXT, Donacion TEXT );")

# Crear la tabla Pacientes
#conn.execute(" CREATE TABLE Pacientes ( id INTEGER PRIMARY KEY, Nombre TEXT, Apellido TEXT, Telefono TEXT, Grupo_Sanguineo TEXT, Busqueda TEXT);")

#Eliminar tabla
#conn.execute("DROP TABLE Pacientes;")
#conn.execute("DROP TABLE Donantes;")

# Datos ficticios
donantes = [
    ("Juan", "Perez", "1234567890", "B+", "riñon"),
    ("Maria", "Gomez", "2345678901", "AB-", "higado"),
    ("Luis", "Martinez", "3456789012", "B+", "corazon"),
    ("Ana", "Lopez", "4567890123", "AB-", "pulmon"),
    ("Carlos", "Sanchez", "5678901234", "AB-", "pancreas"),
    ("Laura", "Ramirez", "6789012345", "A+", "cornea"),
    ("Diego", "Torres", "7890123456", "O-", "intestino"),
    ("Lucia", "Hernandez", "8901234567", "AB+", "tejido"),
    ("Javier", "Garcia", "9012345678", "A+", "riñon"),
    ("Sofia", "Diaz", "0123456789", "A-", "higado"),
    ("Pablo", "Cruz", "1234567891", "AB+", "corazon"),
    ("Claudia", "Vega", "2345678902", "AB+", "pulmon"),
    ("Ricardo", "Morales", "3456789013", "A-", "pancreas"),
    ("Teresa", "Rios", "4567890124", "O+", "cornea"),
    ("Andres", "Castillo", "5678901235", "A-", "intestino"),
    ("Carmen", "Jimenez", "6789012346", "B+", "tejido"),
    ("Fernando", "Salas", "7890123457", "B-", "riñon"),
    ("Isabel", "Moreno", "8901234568", "AB-", "higado"),
    ("Antonio", "Mendoza", "9012345679", "AB+", "corazon"),
    ("Paola", "Cordova", "0123456790", "O-", "pulmon"),
    ("Martin", "Paniagua", "1234567892", "O+", "pancreas"),
    ("Nadia", "Almeida", "2345678903", "A-", "cornea"),
    ("Jorge", "Gonzalez", "3456789014", "B+", "intestino"),
    ("Veronica", "Alonso", "4567890125", "O+", "tejido"),
    ("Diego", "Castro", "5678901236", "A+", "riñon"),
    ("Gloria", "Valdez", "6789012347", "B-", "higado"),
    ("Felipe", "Rojas", "7890123459", "AB-", "corazon"),
    ("Rosa", "Sierra", "8901234569", "A+", "pulmon"),
    ("Emilio", "Bermudez", "9012345680", "B-", "pancreas"),
    ("Laura", "Santiago", "0123456791", "AB+", "cornea"),
    ("Cristian", "Nunez", "1234567893", "A+", "intestino"),
    ("Fabiola", "Perez", "2345678904", "B+", "tejido"),
    ("Alberto", "Guerrero", "3456789015", "O+", "riñon"),
    ("Patricia", "Caceres", "4567890126", "B-", "higado"),
    ("Eduardo", "Mora", "5678901237", "A+", "corazon"),
    ("Santiago", "Paz", "6789012348", "O+", "pulmon"),
    ("Gabriela", "Maldonado", "7890123450", "O+", "pancreas"),
    ("Samuel", "Salcedo", "8901234570", "AB+", "cornea"),
    ("Nicolas", "Ramirez", "9012345681", "B+", "intestino"),
    ("Daniela", "Bravo", "0123456792", "B-", "tejido"),
    ("Leonardo", "Paredes", "1234567894", "O-", "riñon"),
    ("Silvia", "Ocampo", "2345678905", "A+", "higado"),
    ("Hector", "Jimenez", "3456789016", "AB+", "corazon"),
    ("Alma", "Escobar", "4567890127", "AB+", "pulmon"),
    ("Patricio", "Mendoza", "5678901238", "A+", "pancreas"),
    ("Carla", "Mendez", "6789012349", "B-", "cornea"),
    ("Cristina", "Silva", "7890123451", "AB+", "intestino"),
    ("Roberto", "Ortega", "8901234560", "B-", "tejido"),
    ("Marisol", "Gomez", "9012345672", "A+", "riñon"),
    ("Leonor", "Soto", "0123456783", "O+", "higado")
]

pacientes = [
    ("Martin", "García", "9876543210", "A+", "riñon"),
    ("Claudia", "Fernandez", "8765432109", "B+", "higado"),
    ("Roberto", "Perez", "7654321098", "B-", "corazon"),
    ("Lucia", "Hernandez", "6543210987", "O+", "pulmon"),
    ("Diego", "Mendoza", "5432109876", "AB+", "pancreas"),
    ("Teresa", "Cruz", "4321098765", "O-", "cornea"),
    ("Fernando", "Lopez", "3210987654", "A-", "intestino"),
    ("Sofia", "Moreno", "2109876543", "B+", "tejido"),
    ("Javier", "Salas", "1098765432", "A+", "riñon"),
    ("Gabriela", "Soto", "0987654321", "O-", "higado"),
    ("Ricardo", "Nunez", "9876543211", "AB+", "corazon"),
    ("Patricia", "Rios", "8765432102", "AB+", "pulmon"),
    ("Samuel", "Salcedo", "7654321093", "A-", "pancreas"),
    ("Emilio", "Vega", "6543210984", "B+", "cornea"),
    ("Carlos", "Caceres", "5432109875", "B+", "intestino"),
    ("Ana", "Diaz", "4321098766", "AB-", "tejido"),
    ("Cristian", "Alonso", "3210987657", "A+", "riñon"),
    ("Isabel", "Morales", "2109876548", "O-", "higado"),
    ("Patricio", "Lara", "1098765439", "A+", "corazon"),
    ("Veronica", "Gonzalez", "0987654320", "AB+", "pulmon"),
    ("Fernando", "Cruz", "9876543213", "A-", "pancreas"),
    ("Maria", "Paniagua", "8765432104", "B+", "cornea"),
    ("Leonardo", "Salas", "7654321095", "B+", "intestino"),
    ("Santiago", "Valdez", "6543210986", "O+", "tejido"),
    ("Laura", "Sierra", "5432109877", "AB-", "riñon"),
    ("Alma", "Ramirez", "4321098768", "AB-", "higado"),
    ("Diego", "Maldonado", "3210987659", "AB+", "corazon"),
    ("Rosa", "Cortez", "2109876540", "B-", "pulmon"),
    ("Emilia", "Martin", "1098765431", "O+", "pancreas"),
    ("Cristina", "Hernandez", "0987654329", "A+", "cornea"),
    ("Pablo", "Garcia", "9876543214", "A-", "intestino"),
    ("Nadia", "Castillo", "8765432105", "B-", "tejido"),
    ("Antonio", "Moreno", "7654321096", "O-", "riñon"),
    ("Isabel", "Nunez", "6543210987", "A+", "higado"),
    ("Andres", "Torres", "5432109878", "AB+", "corazon"),
    ("Patricia", "Rios", "4321098769", "B-", "pulmon"),
    ("Gloria", "Cruz", "3210987650", "O+", "pancreas"),
    ("Fernando", "Silva", "2109876541", "A+", "cornea"),
    ("Carmen", "Perez", "1098765432", "B-", "intestino"),
    ("Laura", "Gonzalez", "0987654323", "AB-", "tejido"),
    ("Martin", "Soto", "9876543215", "O-", "riñon"),
    ("Ana", "Almeida", "8765432106", "A+", "higado"),
    ("Ricardo", "Vargas", "7654321097", "A+", "corazon"),
    ("Maria", "Caceres", "6543210988", "B-", "pulmon"),
    ("Esteban", "Cruz", "5432109879", "O+", "pancreas"),
    ("Silvia", "Lopez", "4321098760", "B+", "cornea"),
    ("Jorge", "Mendez", "3210987651", "A-", "intestino"),
    ("Claudia", "Mora", "2109876542", "AB-", "tejido"),
    ("Elena", "Santiago", "1098765433", "O-", "riñon"),
    ("Gabriel", "Valdez", "0987654324", "A+", "higado")
]


#conn.executemany(" INSERT INTO Donantes (Nombre, Apellido, Telefono, Grupo_Sanguineo, Donacion) VALUES ( ?, ?, ?, ?, ?);", donantes)

conn.executemany(" INSERT INTO Pacientes (Nombre, Apellido, Telefono, Grupo_Sanguineo, Busqueda) VALUES ( ?, ?, ?, ?, ?);", pacientes)

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
