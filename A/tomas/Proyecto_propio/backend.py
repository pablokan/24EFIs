import reflex as rx
import sqlite3

class Base_datos(rx.State):
    organos_disponibles : list
    tipos_sangre : list
    #Salida del menu pacientes
    mensaje_salida_carga_paciente : str
    mensaje_salida_eliminacion_paciente : str
    mensaje_salida_busqueda_paciente : list[str]
    mensaje_salida_ver_pacientes:list[list]
    
    #Salida del menu donantes
    mensaje_salida_carga_donantes : str
    mensaje_salida_eliminacion_donante : str
    mensaje_salida_busqueda_donante : list[str]
    mensaje_salida_ver_donantes:list[list]
    
    nombre : str
    apellido : str
    telefono : str
    organo : str
    sangre : str
    id : int

    organos_disponibles = ["corazon", "pulmon", "riñon", "higado", "tejido", "cornea", "pancreas", "instestino"]
    tipos_sangre = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
#--------------------------------------------------------------------------------------------------------------------------
    #Funcion para cargar pacientes y donantes en las tablas
    def cargar_pacientes(self, nombre, apellido, telefono,sangre, organo):
        conexion = sqlite3.connect('base_datos.db')
        if (sangre in self.tipos_sangre) and (organo in self.organos_disponibles):
            query = f"INSERT INTO Pacientes(Nombre, Apellido, Telefono, Grupo_Sanguineo, Busqueda) VALUES(?,?,?,?,?);"
            conexion.execute(query,(nombre, apellido,telefono,sangre,organo)),
            self.mensaje_salida_carga_paciente = f"¡Carga del paciente realizada con exito!"
            conexion.commit()
        else:
                self.mensaje_salida_carga_paciente = f"ERROR: Datos de paciente no validos"
    
    def cargar_donantes(self, nombre, apellido, telefono,sangre, organo):
        conexion = sqlite3.connect('base_datos.db')
        if (sangre in self.tipos_sangre) and (organo in self.organos_disponibles):
            query = f"INSERT INTO Donantes(Nombre, Apellido, Telefono, Grupo_Sanguineo, Donacion) VALUES(?,?,?,?,?);"
            conexion.execute(query,(nombre, apellido,telefono,sangre,organo)),
            self.mensaje_salida_carga_donante = f"¡Carga del donante realizada con exito!"
            conexion.commit()
        else:
            self.mensaje_salida_carga_donante = f"ERROR: Datos del donante no validos"
      
#--------------------------------------------------------------------------------------------------------------------------
    #Funcion para eliminar pacientes de las tablas
    def eliminar_paciente(self,id):
        self.mensaje_salida_eliminacion_paciente = ""
        conexion = sqlite3.connect('base_datos.db')
        query = f"DELETE FROM Pacientes WHERE id=?;"
        cursor = conexion.execute(query,(id,))
        conexion.commit()
        if cursor.rowcount > 0: 
            self.mensaje_salida_eliminacion_paciente = f"¡Eliminacion del paciente realizada con exito!"
        else:
            self.mensaje_salida_eliminacion_paciente = f"ID del paciente no registrado"
    
    def eliminar_donante(self,id):
        conexion = sqlite3.connect('base_datos.db')
        query = f"DELETE FROM Donantes WHERE id=?;"
        cursor = conexion.execute(query,(id,))
        conexion.commit()
        if cursor.rowcount > 0: 
            self.mensaje_salida_eliminacion_donante = f"¡Eliminacion del Donante realizada con exito!"
        else:
            self.mensaje_salida_eliminacion_donante = f"ID del Donante no registrado"                
#--------------------------------------------------------------------------------------------------------------------------
    #Funcion para mostrar las tablas
    def mostrar_tabla_pacientes(self):
        self.mensaje_salida_ver_pacientes = []
        conexion = sqlite3.connect('base_datos.db')
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM Pacientes")
        encontrados = cursor.fetchall()
        if encontrados:
            for encontrado in encontrados:
                registro = [encontrado[0],encontrado[1],encontrado[2],encontrado[3],encontrado[4],encontrado[5]]
                self.mensaje_salida_ver_pacientes.append(registro)
    
    def mostrar_tabla_donantes(self):
        self.mensaje_salida_ver_donantes = []
        conexion = sqlite3.connect('base_datos.db')
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM Donantes")
        encontrados = cursor.fetchall()
        if encontrados:
            for encontrado in encontrados:
                registro = [encontrado[0],encontrado[1],encontrado[2],encontrado[3],encontrado[4],encontrado[5]]
                self.mensaje_salida_ver_donantes.append(registro)
    
    
#-------------------------------------------------------------------------------------------------------------------------- 
    
    #Funcion para buscar pacientes o donantes con cirtos criterios
    def buscar_paciente(self,organo,sangre):
        self.mensaje_salida_busqueda_paciente = []
        conexion = sqlite3.connect('base_datos.db')
        if (sangre in self.tipos_sangre) and (organo in self.organos_disponibles):
            query = "SELECT * FROM Pacientes WHERE Busqueda = ? AND Grupo_Sanguineo= ?;"
            cursor = conexion.execute(query,(organo,sangre))
            encontrados = cursor.fetchall()
            if encontrados:
                for encontrado in encontrados:
                    registro = [encontrado[1],encontrado[2],encontrado[3],encontrado[4],encontrado[5]]
                    self.mensaje_salida_busqueda_paciente.append(registro)
    
    def buscar_donante(self,organo,sangre):
        self.mensaje_salida_busqueda_donante = []
        conexion = sqlite3.connect('base_datos.db')
        if (sangre in self.tipos_sangre) and (organo in self.organos_disponibles):
            query = "SELECT * FROM Donantes WHERE Donacion = ? AND Grupo_Sanguineo= ?;"
            cursor = conexion.execute(query,(organo,sangre))
            encontrados = cursor.fetchall()
            if encontrados:
                for encontrado in encontrados:
                    registro = [encontrado[1],encontrado[2],encontrado[3],encontrado[4],encontrado[5]]
                    self.mensaje_salida_busqueda_donante.append(registro)
            
        
#--------------------------------------------------------------------------------------------------------------------------
    #Cerrar la conexion de la base de datos
    def cerrar_conexion(self):
        conexion = sqlite3.connect('base_datos.db')
        conexion.close