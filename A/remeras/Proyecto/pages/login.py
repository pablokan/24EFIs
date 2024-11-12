import reflex as rx
import sqlite3


class Data(rx.State):
    usuarios: list[list] = []

    def obtener_usuarios(self):
        conn = sqlite3.connect("datos.db")
        cursor= conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        self.usuarios = cursor.fetchall()
    
    def agregar(self, nombre, telefono, email,usuario,contra):
        conn = sqlite3.connect("datos.db")
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO clientes (nombre,telefono,email,usuario,contra) VALUES ('{nombre}', '{telefono}','{email}','{usuario}','{contra}')"
        )
        conn.commit()
        conn.close()    

class Login(rx.State):
    #variables de clientes
    nombre_usu:str
    tele_usu:str
    email_usu:str
    usu:str
    contra:str

    def limpiar(self):
        Login.nombre_usu=''
        Login.tele_usu=''
        Login.email_usu=''
        Login.usu=''
        Login.contra=''
    
    def home(self):
        return rx.redirect('/')

def logins():
    login=rx.center( 
                 rx.vstack( 
                        rx.vstack(
                            rx.heading(
                                'REGISTRARSE',
                                size='5',
                                weight='bold',
                            ),
                            rx.text(
                                'Ingrese sus datos debajo para crear su cuenta',
                                font_size= '12px',
                                weight='medium',
                                color_scheme='gray',
                            ),
                            width='100%',
                            spacing='1',
                            align='center',
                        ),
                        rx.input(
                            width='100%',
                            placeholder='Nombre',
                            on_blur=Login.set_nombre_usu,                    
                        ),
                        rx.input(
                            width='100%',
                            placeholder='Telefono',
                            on_blur=Login.set_tele_usu,                    
                        ),
                        rx.input(
                            width='100%',
                            placeholder='email ejemplo@ejemplo.com',
                            on_blur=Login.set_email_usu,                    
                        ),
                        rx.input(
                            width='100%',
                            placeholder='Usuario',
                            on_blur=Login.set_usu,                    
                        ),
                        rx.input(
                            width='100%',
                            placeholder='Contraseña',
                            on_blur=Login.set_contra,                    
                        ),                                                
                        rx.button(
                            rx.icon(tag='pencil-line',size=15),
                            'Crear',
                            width='100%',
                            cursor='pointer',
                            variant='surface',
                            color_scheme='grass',
                            on_click=Data.agregar(Login.nombre_usu,Login.tele_usu,Login.email_usu,Login.usu,Login.contra),
                            on_blur=Login.limpiar,            
                        ),
                        rx.hstack(
                            rx.divider(width='25%'),
                            rx.text(
                                'Si tiene cuenta ingrese',
                                font_size='10px',
                                weight='bold',
                                color_scheme='indigo',

                            ),
                            rx.divider(width='25%'),
                            width='100%',
                            align='center',
                            justify='center',
                            padding='5px 0px',
                        ),
                        rx.input(
                            width='100%',
                            placeholder='Usuario',                    
                        ),
                        rx.input(
                            width='100%',
                            placeholder='Contraseña',                    
                        ),                        
                        rx.button(
                            rx.icon(tag='door-open',size=15),
                            'Ingresar',
                            width='100%',
                            variant='surface',
                            cursor='pointer',
                            color_scheme='cyan',
                        ),
                        rx.text(
                            'Al hacer clic en Continuar, aceptas nuestros.',
                            font_size='11px',
                            color_scheme='gray',
                            text_align='center',
                            padding='5px 0px',
                        ),
                        rx.button('home',
                            on_click=Login.home),
                        bg=rx.color('blue', 2),
                        width='21em',
                        max_width='21em',
                        justify='center',align='center',
                        border_radius='15px 15px',
                        padding='10px',

                    ),       
    )
    return login
