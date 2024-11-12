import sqlite3

def registrarPaciente(dni, nombre, correo, telefono, fNacimiento):
    conn = sqlite3.connect('dbHospital.db')
    try:
        conn.execute('INSERT INTO datosp (DNI, nombre, correo, telefono, fecha_nacimiento) VALUES (?, ?, ?, ?, ?)', 
                     (dni, nombre, correo, telefono, fNacimiento))
        conn.commit()
        return "Paciente registrado"
    except sqlite3.IntegrityError:
        return "Los datos del paciente ya existen"
    finally:
        conn.close()

def realizarConsulta(dni):
    conn = sqlite3.connect('dbHospital.db')
    try:
        cursor = conn.execute('''SELECT datosp.nombre, consultas.consulta, consultas.peso, consultas.altura, consultas.fecha, ROUND(peso / (altura * altura), 2) AS IMC
                                 FROM datosp 
                                 JOIN consultas ON datosp.DNI = consultas.DNI 
                                 WHERE datosp.DNI = ?''', (dni,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al realizar la consulta: {e}")
        return []
    finally:
        conn.close()

def registrarConsulta(dni, consulta, peso, altura, fecha):
    conn = sqlite3.connect('dbHospital.db')
    try:
        conn.execute('INSERT INTO consultas (DNI, consulta, peso, altura, fecha) VALUES (?, ?, ?, ?, ?)', 
                     (dni, consulta, peso, altura, fecha))
        conn.commit()
        return "Consulta registrada"
    except sqlite3.IntegrityError:
        return "Error al registrar la consulta"
    finally:
        conn.close()

def editarPaciente(dni, nombre, correo, telefono, fNacimiento):
    conn = sqlite3.connect('dbHospital.db')
    try:
        conn.execute('''UPDATE datosp 
                        SET nombre = ?, correo = ?, telefono = ?, fecha_nacimiento = ? 
                        WHERE DNI = ?''', (nombre, correo, telefono, fNacimiento, dni))
        conn.commit()
        return "Paciente actualizado"
    except Exception as e:
        print(f"Error al actualizar el paciente: {e}")
        return "Error al actualizar el paciente"
    finally:
        conn.close()
