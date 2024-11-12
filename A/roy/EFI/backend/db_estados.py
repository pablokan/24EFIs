import reflex as rx
import sqlite3

#ACA VAMOS A HACER LA CONEXION CON LA BASE DE DATOS SOBRE LA TABLA ESTADOS 

class TablaEstados(rx.State):
    estados: list[list[str]] = []

    def obtenerEstados(self): #Imprime los los datos de la tabla estados
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ESTADO') #Selecciona a los usuarios de la tabla ESTADOS
        self.estados = cursor.fetchall() #fechall trae todos los estados
        conn.close()
        
