import reflex as rx
import sqlite3


class Data(rx.State):
    usuarios: list[list] = []
    
    def modificar_usuario(self, user_id, nuevo_nombre, nuevo_telefono,
        nuevo_email, nuevo_usuario, nueva_contra):
        conn = sqlite3.connect("datos.db")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE clientes SET nombre = ?, telefono = ?, email = ?, usuario = ?, contra = ? WHERE id = {user_id}",
        (nuevo_nombre, nuevo_telefono, nuevo_email, nuevo_usuario, nueva_contra, user_id))
        conn.commit()
        conn.close()
        self.mostrar_formulario = False
        self.obtener_usuarios()
   
class State(rx.State):
    #variables de clientes
    nombre_usu:str
    tele_usu:str
    email_usu:str
    usu:str
    contra:str


def modificar():
    login=rx.box( 
            
                rx.center(  
                  
                        rx.vstack(
                        rx.input(
                            width='100%',
                            placeholder='Nombre',
                            on_blur=State.set_nombre_usu,                    
                        ),
                        rx.input(
                            width='100%',
                            placeholder='Telefono',
                            on_blur=State.set_tele_usu,                    
                        ),
                        rx.input(
                            width='100%',
                            placeholder='email ejemplo@ejemplo.com',
                            on_blur=State.set_email_usu,                    
                        ),
                        rx.input(
                            width='100%',
                            placeholder='Usuario',
                            on_blur=State.set_usu,                    
                        ),
                        rx.input(
                            width='100%',
                            placeholder='Contraseña',
                            on_blur=State.set_contra,                    
                        ),                                                
                        rx.button(
                            rx.icon(tag='pencil-line',size=15),
                            'Modificar',
                            width='100%',
                            cursor='pointer',
                            variant='surface',
                            color_scheme='grass',
                            on_click=Data.modificar_usuario(State.nombre_usu,State.tele_usu,State.email_usu,State.usu,State.contra),        
                        ),
                        bg=rx.color('blue', 2),
                        width='21em',
                        max_width='21em',
                        justify='center',align='center',
                        border_radius='15px 15px',
                        padding='10px',

                    ),
                    background='transparent',
                    border_radius='15px',
                ),

    )
    return login
