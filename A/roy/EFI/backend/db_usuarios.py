import reflex as rx
import sqlite3

#ACA VAMOS A HACER LA CONEXION CON LA BASE DE DATOS SOBRE LA TABLA USUARIOS 

class TablaUser(rx.State):
    users: list[list[str]] = []

    def obtenerUsuarios(self): #Imprime los los datos de la tabla usuarios
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * from USUARIOS') #Selecciona a los usuarios de la tabla usuarios
        self.users = cursor.fetchall() #traigo todos los usuarios 
        conn.close()
        
        
  