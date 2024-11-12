import reflex as rx 
import sqlite3

class Login(rx.State):
    email: str = ""
    contraseña: str = ""
    tipo: str = ""
    usr: list[list[str]]  #lista para obtener todos los usuarios de la base de datos
    form_data: dict = {} #obtengo los datos del formulario login
    esValido: bool = True #para validar si el user existe o no en la base de datos
    tipoUsuario: str = ""

    
    print("Entre a la clase login")
    
        
    def obtener_dato_login(self, form_data: dict):
        self.form_data = form_data #guardamos los datos aca
        self.email = self.form_data["email"] #aca sacamos los datos email y contraseña parra guardarlkos en esa variable 
        self.contraseña = self.form_data["contraseña"]
        self.obtenerDatos_database() #llamo al metodo para obtener los usuarios registrados en la base de datros
        if self.validarUsuario():
            return rx.redirect("/ticket") #aca valido si existe o no ese usuarioi
        print("dato obtenido del login usuario:", self.email)
        print("dato obtenido del login contraseña:", self.contraseña)
        
    
    def obtenerDatos_database(self):
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        cursor.execute('SELECT EMAIL, CONTRASEÑA, TIPO FROM USUARIOS')  # Selecciono solo los atri butos que necesito
        self.usr = cursor.fetchall()
        print("registros de la base de datos", self.usr)
        conn.close()
        print("Obtuve datos de la base de datos")

  
    def iniciarSesion(self, tipo):
        # pongo el tipo de usuario para la sesión actual
        self.tipoUsuario = tipo
        print(f"Sesión iniciada para usuario tipo: {self.tipoUsuario}")
  
    def validarUsuario(self):
        # itero sobre todos los usuarios para verificar si alguno coincide con los datos ique ingreso el usuario
        for email, password, tipo in self.usr:
            if email == self.email and password == self.contraseña:
                self.tipo = tipo
                self.iniciarSesion(tipo) #aca guardo el tipo de cuenta que tiene el usuario la uso para validar despues y filtrar botones
                print(f"Usuario validado como {self.tipo}")
                return True

        # Si no encontró coincidencias
        print("Usuario no validado")
        self.esValido = not self.esValido #aca cambio el estado para mostrar los usuarios si estan valdiados o no 
        return False
    
    def cerrarSesion(self): #aca lo que hago es sacarle el tipo de usuario a la variable para que se limpie asi cuando ingresa otro se guarda bien el dato
        self.tipo = None
        self.esValido = True
        print(f"le sacamoos el tipo al usuario {self.tipo}")
        print("Sesión cerrada")
        return rx.redirect("/login")
    
