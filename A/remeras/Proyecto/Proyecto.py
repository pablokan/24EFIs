#EFI Istituto Tecnico Rio Cuarto
#Este Trabajo fue realizado con el framework Reflex
#Integrantes :
            # Ambrogio Francisco
            # Arballo Federico
            # Cepeda Emanuel
            # Rodriguez Joaquin
#-->
import reflex as rx
from .pages.dialog import dialog
from .pages.login import logins
from .pages.modificar import modificar
import sqlite3

#BackEnd
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

    def delete_user(self, user_id):
        conn = sqlite3.connect("datos.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM clientes WHERE id = {user_id}")
        conn.commit()
        conn.close()
        self.obtener_usuarios()      
    
    def delete_user(self, user_id):
        conn = sqlite3.connect("datos.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM clientes WHERE id = {user_id}")
        conn.commit()
        conn.close()
        self.obtener_usuarios()  

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

    def obtener_usuario_por_id(self, user_id):
            conn = sqlite3.connect("datos.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = {user_id}")
            usuario = cursor.fetchone()
            conn.close()
            if usuario:
                self.usuario_editar = {
                    "id": usuario[0],
                    "nombre": usuario[1],
                    "telefono": usuario[2],
                    "email": usuario[3],
                    "usuario": usuario[4],
                    "contra": usuario[5]
                }

class Validar(rx.State):
    clave:str 
    verif= False

    def change(self):
        if self.clave == '1234BE':
            self.verif =True
        else:
            self.verif = False

class State(rx.State):
    ropa: list[list] = [['remera1.png','remera','azul','$2300'],['remera2.png','remera','azul','$2300'],['remera3.png','remera','azul','$2300']]

    lista=['remera1.png', 'remera2.png', 'remera3.png','remera4.png','remera5.png','remera6.png','remera7.png','remera8.png','remera9.png','remera10.png','remera11.png','remera12.png']
    producto=['remera','remera','remera','remera','remera','remera','remera','remera','remera','remera','remera','remera']
    color=['azul','balco','verde','azul','balco','verde','azul','balco','verde','azul','balco','verde',]
    precio=['$2300','$1200','$4500','$2300','$1200','$4500','$2300','$1200','$4500','$2300','$1200','$4500',]
    cant=len(lista)

#Variables de clientes
    nombre_usu:str
    tele_usu:str
    email_usu:str
    usu:str
    contra:str

    def limpiar(self):
        self.nombre_usu=''
        self.tele_usu=''
        self.email_usu=''
        self.usu=''
        self.contra=''

    def carrito(self, lista):
        total = 0
        for producto in lista:
            precio = float(producto[3].replace("$", ""))
            total += precio
        return total
    
    def validar_contraseña(self, contraseña):
        mayuscula = False
        minuscula = False
        numero = False
        simbolo = False

        for c in contraseña:
            if c.isupper():
               mayuscula = True
            elif c.islower():
                minuscula = True
            elif c.isdigit():
                numero = True
            elif not c.isalnum():
                simbolo = True
            if mayuscula and minuscula and numero and simbolo:
                return True

        return False

    def valid_email(self):
        pass

#REDIRECCIONES DE PAGINAS
    def home(self):
        return rx.redirect('/')
    
    def pago(self):
        return rx.redirect('/pago')

    def clicked(self):
        return rx.redirect('/cuenta')
    
    def base_clientes(self):
        return rx.redirect('/base_clientes') 
    


#FrontEnd
@rx.page('/','Home page compras')
@rx.page(on_load=Data.obtener_usuarios)


def index():
    principal=rx.vstack(       
            rx.hstack(
                rx.heading('6 cuotas sin interes unicamente cuentas bancarizadas',size='2', color='black'),
                width='100%',height='15px',align='center',justify='center',margin_top='5px',
            ),
            rx.hstack(
                rx.hstack(
                    rx.image(src='/store.png', width='80px', height='auto', border_radius='100%'),
                    rx.heading('[BE].', size='7', color='white'),
                    align='center',
                ),
                rx.hstack(
                    rx.input(placeholder='¿Que estas buscando?',style={"& input::placeholder": {"color": "black"}},width='90%',radius='full',background_color='white',color='blue'),
                    rx.button(rx.icon('search', color='black'),size='1',background_color='white', radius='full'),
                    width='400px',height='30px',justify='center',align='center',border_radius='15px',background='White',
                ),
                rx.hstack(
                    rx.button(rx.icon('shopping-cart'),variant='ghost', color='white',on_click=State.pago),
                    dialog(validacion,'Usuarios','users'),
                    dialog(logins,'Registrarse/Logearse','clipboard-pen'),
                    margin_right='30px',
                    spacing='6',
                ),
                width='100%',height='100px',align='center',justify='between',position='sticky',z_index='999',top='0',background='#22282e',border_bottom='0.5px solid white',
            ),
        rx.hstack(
            rx.hover_card.root(
                rx.hover_card.trigger(
                    rx.link(
                        "Acerca de Nosotros",
                        color_scheme="gray",
                    ),
                ),
                rx.hover_card.content(
                    rx.hstack(
                        rx.image(src='/store.png',width='250px',height='auto'),
                        rx.vstack(
                            rx.heading('somos un grupo de estudiantes de ITEC Rio Cuarto', size='6',color='Black'),
                            rx.heading('Integrantes:', size='4',color='Black'),
                            rx.vstack(
                                rx.text('- Ambrogio Francisco',color='Black'),
                                rx.text('- Arballo Federico',color='Black'),
                                rx.text('- Cepeda Emanuel',color='Black'),
                                rx.text('- Rodriguez Joaquin',color='Black'),
                                spacing='1',
                            ),
                        ),
                    ),
                    background='white',margin='0',
                ),
            ),
            width='100%',height='50px',background='#22282e',justify='center',align='center',spacing='9',margin_top='-12px',position='sticky',z_index='998',top='98px',
        ),
        rx.hstack(
            rx.heading('[BE]. THE BEST >>>', size='8', color='#323232'),
            rx.image(src='/favicon.ico', width='100px', heigth='auto', border_radius='100%'),
            background_image='url(/futbol.png)',height='420px',width='100%',justify='between',align='end',padding='30px',
        ),
        rx.hstack(
            rx.grid(
                    rx.foreach(
                        rx.Var.range(State.cant),
                         lambda i:  rx.vstack(
                                        rx.image(src=f'/remeras/{State.lista[i]}', width='100%',height='300px',),
                                        rx.vstack(
                                            rx.hstack(
                                                rx.text(f'{State.precio[i]}', color='Black'),
                                                rx.button(rx.icon('heart'),variant='ghost', color='#ff6e61'),
                                                width='100%',justify='between',padding_x='10px',
                                            ),
                                            rx.divider(),
                                                rx.vstack(
                                                    rx.text(f'Producto: {State.producto[i]}', color='Black'),
                                                    rx.text(f'Color: {State.color[i]}', color='Black'),
                                                    spacing='1',background='#e8e8ef',padding='5px',width='100%',border_radius='2px',
                                                ),                         
                                            width='100%',
                                        ),
                                        width='100%',background='#dcdcdc',box_shadow=' 1.2px 1.5px 2.2px -0.8px #989898',
                                    ),  
                    ),
                    columns="4",spacing="6",margin_x='15%',margin_top='30px',width="100%",justify='center',align='center',
                ),
                width='100%',
        ),
        rx.hstack(
            rx.hstack(
                rx.image(src='/store.png', width='100px', height='auto', border_radius='100%'),
                rx.heading('[BE].', size='7', color='white'),
                align='center',
            ),
            rx.vstack(
            rx.text('Diseñado con:'),
            rx.heading('REFLEX', size='6'),
            rx.text('2024 proyecto de programacion ITEC Rio Cuarto'),
            margin='20px',
            ),
            width='100%',height='auto',align='center',justify='between',background='#323232',
        ),
        justify='center',align='center',width='100%',height='100%',background='#e8e8e8',
    )
    return principal

def pago():
    pago= rx.box( 
                rx.hstack(
                    rx.hstack(
                        rx.heading(
                            'Tienda',
                            size='7',
                            margin_left='10px',
                            color='white',
                        ),          
                        width='200px',height='100px',justify='center',align='center',border_radius='10% 30% 50% 70%',background='SlateGray',
                    ),
                    rx.spacer(),
                    rx.button('home',
                            on_click=State.home),
                    width='100%',height='120px',align='center',background='DarkSlateGray',padding='10px',
                ), 
                rx.hstack(
                    rx.hstack(
                       rx.vstack(
                            rx.heading('CARRITO'),
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell(''),
                                        rx.table.column_header_cell('DESCRIPCION'),
                                        rx.table.column_header_cell('COLOR'),
                                        rx.table.column_header_cell('PRECIO'),
                                        rx.table.column_header_cell(''),
                                    ),
                                ),
                                rx.table.body(
                                    rx.foreach(
                                        State.ropa, mostrar_productos
                                    ),
                                ),
                            ),
                            background='black',border_radius='15px',padding='50px',width='80%',height='100%',margin_rigth='10px',
                        ),
                        rx.vstack(
                            rx.heading('MODO DE PAGO'),
                            rx.radio(['efectivo','tarjeta','QR']),
                            rx.spacer(),
                            rx.text('bases y condiciones en nuestra pagina web', size='1'),
                            rx.spacer(),
                            background='#595959',border_radius='15px',width='20%',height='100%',align='center',padding_top='20px',                          
                        ),
                        background='white',width='80%',height='80%',padding='20px',border_radius='15px',
                    ),
                    background='#e0e0e0',width='100%',height='100vh',justify='center',align='center',
                ),
    )
    return pago

def mostrar_productos(product: list):
    return rx.table.row(
        rx.table.cell(rx.box(rx.image(src=f'/remeras/{product[0]}', width='100px',height='auto',),),width='100%',height='auto'),
        rx.table.cell(product[1]),
        rx.table.cell(product[2]),
        rx.table.cell(product[3]),
        rx.table.cell(rx.spacer()),
        rx.table.cell(rx.hstack(rx.button('quitar'))),
    )

def validacion():
    return rx.center(
        rx.vstack(
            rx.input(placeholder='Intrduzca la contraseña', type='password',on_blur=Validar.set_clave),
            rx.text('la contraseña es "1234BE"'),
            rx.button("VALIDAR", on_click=Validar.change),
            rx.cond(
                Validar.verif,
                        clientes(),
                        rx.text(
                        f"La contraseña no es valida intente nuevamente",
                        color="red",
                    ),
            ),
        background='transparent',border_radius='15px',padding='50px',align='center',
        ),
    )

def clientes():
    page= rx.center(
            rx.flex(
                rx.button('volver', on_click= State.home),
                rx.hstack(
                rx.input(placeholder='Busqueda de usuario',width='70%'),
                rx.button('Realizar Busqueda'),
                margin='30px',
                justify='between'
                ),
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell('id'),
                            rx.table.column_header_cell('NOMBRE'),
                            rx.table.column_header_cell('TELEFONO'),
                            rx.table.column_header_cell('EMAIL'),
                            rx.table.column_header_cell('USUARIO'),
                            rx.table.column_header_cell('CONTRASEÑA'),
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(
                                Data.usuarios, mostrar_personas
                        ),
                    ),
                    align='center',
                ),
                direction='column',style={'width':'70vw', 'margin':'auto'},
            ),
            margin_y='70px',
    )
    return page

def mostrar_personas(person: list):
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
        rx.table.cell(person[3]),
        rx.table.cell(person[4]),
        rx.table.cell(person[5]),
        rx.table.cell(rx.spacer()),
        rx.table.cell(rx.hstack(dialog(modificar,'Modificar','pencil'),rx.button(rx.icon('trash-2'),on_click=Data.delete_user(person[0]))))
        )

app = rx.App()
app.add_page(index)
app.add_page(logins, route='/cuenta')
app.add_page(pago, route='/pago')
app.add_page(clientes, route='/base_clientes')
