import sqlite3
class Base_datos():
    def __init__(self):
        self.conexion = sqlite3.connect('base_datos.db')
        self.organos_disponibles = ["corazon", "pulmon", "riñon", "higado", "tejido", "cornea", "pancreas", "instestino"]
        self.tipos_sangre = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
        
#--------------------------------------------------------------------------------------------------------------------------
    #Funcion para cargar en las tablas
    def cargar_en_tablas(self, tipo):
        if tipo == "pacientes":
            tabla = "Pacientes"
            columna_del_organo = "Busqueda"
            mensaje = "Busqueda"
        elif tipo =="donantes":
            tabla = "Donantes"
            columna_del_organo = "Donacion"
            mensaje="Donacion"
        nombre = input("-Nombre: ")
        apellido = input("-Apellido: ")
        telefono = input("-Telefono: ")
        volver = True
        while volver:
            grupo_sanguineo = input("-Grupo Sanguineo: ").upper()
            organo = input(f"-Organo en {mensaje}: ").lower()
            if (grupo_sanguineo in self.tipos_sangre) and (organo in self.organos_disponibles):
                query = f"INSERT INTO {tabla}(Nombre, Apellido, Telefono, Grupo_Sanguineo, {columna_del_organo}) VALUES(?,?,?,?,?);"
                self.conexion.execute(query,(nombre,apellido,telefono,grupo_sanguineo,organo)),
                print(f"""
            ¡Carga del {mensaje} realizada con exito!
        
                """)
                self.conexion.commit()
                break
            else:
                print(f"ERROR: Datos de {mensaje} no validos")
                volver = True
                
#--------------------------------------------------------------------------------------------------------------------------
    #Funcion para eliminar donantes o pacientes de las tablas
    def eliminar_de_tabla(self,tipo):
        if tipo == "donantes":
            tabla = "Donantes"
            mensaje = "Donante"
        elif tipo == "pacientes":
            tabla ="Pacientes"
            mensaje = "Paciente"
        print("")
        print(f"<---------| Eliminar {mensaje} |--------->")
        while True:
            try:
                id = int(input(f"Id del {mensaje} a eliminar de la lista: "))
                query = f"DELETE FROM {tabla} WHERE id=?;"
                cursor = self.conexion.execute(query,(id,))
                self.conexion.commit()
                if cursor.rowcount > 0: #Esto te dice cuántas filas fueron afectadas por la operación
                    print(f"""
                        ¡Eliminacion del {mensaje} realizada con exito!
            
                        """)
                    break
                else:
                    print(f"ID del {mensaje} no registrado")
            except:
                print(f"ERROR: ID del {mensaje} no valido")
                        
#--------------------------------------------------------------------------------------------------------------------------
    #Funcion para mostrar las tablas
    def mostrar_tabla(self, tipo):
        if tipo == 'donantes':
            tabla = 'Donantes'
            mensaje = "LISTA DE DONANTES"
        elif tipo == 'pacientes':
            tabla = 'Pacientes'
            mensaje = "LISTA DE PACIENTES"
        cursor = self.conexion.cursor()
        cursor.execute(f"SELECT * FROM {tabla}")
        encontrados = cursor.fetchall()
        print(f"<----------|{mensaje}|----------->")
        for encontrado in encontrados:
            print(f"ID: {encontrado[0]}, Nombre: {encontrado[1]}, Apellido: {encontrado[2]}, "
                f"Teléfono: {encontrado[3]}, Grupo Sanguíneo: {encontrado[4]}, Búsqueda: {encontrado[5]}")
        self.conexion.commit()
#-------------------------------------------------------------------------------------------------------------------------- 
    #Funcion para buscar pacientes o donantes con cirtos criterios
    def buscar_en_tabla(self, tipo):
        if tipo == "donantes":
            columna_del_organo = "Donacion"
            tabla = "Donantes"
            mensaje = "Organo en Donacion: "
        elif tipo == "pacientes":
            tabla = "Pacientes"
            columna_del_organo = "Busqueda"
            mensaje = "Organo en Requerimiento: "
        volver = True
        while volver:
            organo = input(f"-{mensaje}").lower()
            grupo_sanguineo = input("-Grupo Sanguieneo: ").upper()
            if (grupo_sanguineo in self.tipos_sangre) and (organo in self.organos_disponibles):
                query = f"SELECT * FROM {tabla} WHERE {columna_del_organo} = ? AND Grupo_Sanguineo= ?; "
                cursor = self.conexion.execute(query,(organo,grupo_sanguineo))
                encontrados = cursor.fetchall()
                if encontrados:
                    print(f"<------------| Posibles {tabla} |------------>")
                    for encontrado in encontrados:
                        print(f"Nombre: {encontrado[1]}, Apellido: {encontrado[2]}, Telefono: {encontrado[3]}, Grupo Sanguineo: {encontrado[4]}, Organo: {encontrado[5]}")
                else:
                    print(f"No se encontraron {tipo} con estos criterios.")
                volver = False
            else:
                print("ERROR: Datos no validos!")
                volver = True    
#--------------------------------------------------------------------------------------------------------------------------
    #Cerrar la conexion de la base de datos
    def cerrar_conexion(self):
        self.conexion.close