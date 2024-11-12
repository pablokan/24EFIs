import reflex as rx
from ..backend.backend import ColorsState
from ..backend.login import Login
from ..backend.db_ticket import TablaTicket
from ..backend.comentarios import Comentarios


def ticketBtn():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("copy-plus", size=30),
                rx.text("Nuevo Ticket", font_size="1.5rem"),
                background_color="#3DD88D",
                padding="1.5rem 2rem",
                cursor="pointer",
            ),
        ),
        rx.dialog.content(
            rx.center(
                rx.flex(
                    rx.icon("ticket", color="#46A758", size=150, stroke_width=1),
                    rx.flex(
                        rx.dialog.title("Generar ticket", font_size="3rem", color="#FFF"),
                        rx.dialog.description(
                            "Rellena el formulario", font_size="1.3rem", color="#FFF", 
                        ),
                        direction="column",
                        spacing="2",
                    ),
                    align="center",
                    justify="center",
                    spacing="4",
                ),
                margin_bottom="1rem",
            ),
            rx.form(
                rx.center(
                    rx.flex(
                        rx.input(
                            placeholder="Solicitante",
                            width="30rem",
                            name="solicitante",
                            border="1px solid #484e54",
                            background="transparent",
                            style={
                                "outline-color": "#46A758",
                                "height": "3em",
                                "& input::placeholder": {
                                    "color": "#484e54", 
                                },
                                "& input": {
                                    "color": "#fff",  
                                },
                            },
                        ),
                        rx.input(
                            placeholder="Asunto",
                            width="30rem",
                            name="asunto",
                            border="1px solid #484e54",
                            background="transparent",
                            style={
                                "outline-color": "#46A758",
                                "height": "3em",
                                "& input::placeholder": {
                                    "color": "#484e54", 
                                },
                                "& input": {
                                    "color": "#fff",  
                                },
                            },
                        ),
                        rx.input(
                            placeholder="Contacto",
                            width="30rem",
                            name="contacto",
                            border="1px solid #484e54",
                            background="transparent",
                            style={
                                "outline-color": "#46A758",
                                "height": "3em",
                                "& input::placeholder": {
                                    "color": "#484e54", 
                                },
                                "& input": {
                                    "color": "#fff",  
                                },
                            },
                        ),
                        rx.text_area(
                            placeholder="Detalla tu consulta aqui!",
                            name="mensaje",
                            background="transparent",
                            border="1px solid #484e54",
                            style={
                                "height": "7em",
                                "outline-color": "#46A758",
                                "& textarea::placeholder": {
                                    "color": "#484e54", 
                                },
                                "& textarea": {
                                    "color": "#fff",  
                                },
                            },
                        ),
                        direction="column",
                        spacing="4",
                    ),
                ),
                rx.flex(
                    rx.dialog.close(
                        rx.button("Cancelar", background_color="#272826", cursor="pointer"),
                    ),
                    rx.dialog.close(
                        rx.flex(
                          rx.button("Confirmar", type="submit", background_color="#46A758", cursor="pointer"),  
                        ),
                    ),
                    spacing="5",
                    margin_top="2rem",
                    justify="end",
                ),
                on_submit=TablaTicket.agregarTicket, #accion para agregar ticker en la base de datos
                reset_on_submit=True, #resetea el formulario al enviar los datos
            ),
        background_color="#111210",
        ),
    )


        
def actualizarTicket(tic: list): #pasamos el parametro para poder obtener los datos del ticket qiue se selecciona asi se actualzia

    return rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.icon("pencil", size=25),
                    background_color="transparent",
                    cursor="pointer",
                    _hover={"color": "#3DD88D"},
                    on_click=lambda: TablaTicket.obtener_ticket(tic)
                ),
            ),
            rx.dialog.content(
                rx.center(
                    rx.flex(
                        rx.icon("ticket", color="#46A758", size=150, stroke_width=1),
                        rx.flex(
                            rx.dialog.title("Editar ticket", font_size="3rem", color="#FFF"),
                            rx.dialog.description(
                                "Edita el formulario", font_size="1.3rem", color="#FFF",
                            ),
                            direction="column",
                            spacing="2",
                        ),
                        align="center",
                        justify="center",
                        spacing="4",
                    ),
                    margin_bottom="1rem",
                ),
                rx.form(  # Agregado el componente form
                    rx.center(
                        rx.flex(
                            rx.input(
                                placeholder="Solicitante",
                                width="30rem",
                                background="transparent",
                                border="1px solid #484e54",
                                name="solicitante",  # Agregado name
                                style={
                                    "outline-color": "#46A758",
                                    "height": "3em",
                                    "& input::placeholder": {
                                        "color": "#484e54", 
                                    },
                                    "& input": {
                                        "color": "#fff",  
                                    },
                                },
                                default_value=tic[2],  # Carga el valor del diccionario,
                            ),
                            rx.input(
                                placeholder="Asunto",
                                width="30rem",
                                background="transparent",
                                border="1px solid #484e54",
                                name="asunto",  # Agregado name
                                style={
                                    "outline-color": "#46A758",
                                    "height": "3em",
                                    "& input::placeholder": {
                                        "color": "#484e54", 
                                    },
                                    "& input": {
                                        "color": "#fff",  
                                    },
                                },
                                default_value=tic[1],  # Carga el valor del diccionario,
                            ),
                            rx.input(
                                placeholder="Contacto",
                                width="30rem",
                                background="transparent",
                                border="1px solid #484e54",
                                name="contacto",  # Agregado name
                                style={
                                    "outline-color": "#46A758",
                                    "height": "3em",
                                    "& input::placeholder": {
                                        "color": "#484e54", 
                                    },
                                    "& input": {
                                        "color": "#fff",  
                                    },
                                },
                                default_value=tic[5],  # Carga el valor del diccionario,
                            ),
                            rx.input(
                                placeholder="Detalla tu consulta aqui!",
                                background="transparent",
                                border="1px solid #484e54",
                                name="mensaje",  # Agregado name
                                style={
                                    "height": "7em",
                                    "outline-color": "#46A758",
                                    "& input::placeholder": {
                                        "color": "#484e54", 
                                    },
                                    "& input": {
                                        "color": "#fff",  
                                    },
                                },
                                default_value=tic[6],  # Carga el valor del diccionario,
                            ),
                            direction="column",
                            spacing="4",
                        ),
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancelar", 
                                background_color="#272826", 
                                cursor="pointer"
                            ),
                        ),
                        rx.dialog.close(
                            rx.flex(
                                rx.button(
                                    "Confirmar", 
                                    type="submit",  # Agregado type="submit"
                                    background_color="#46A758", 
                                    cursor="pointer"
                                ),
                            ),
                        ),
                        spacing="5",
                        margin_top="2rem",
                        justify="end",
                    ),
                    on_submit=TablaTicket.editarTicket,  # Agregado on_submit
                    reset_on_submit=True,  # Agregado reset_on_submit
                ),
            background_color="#111210",
            ),
        )
    


def eliminarTicket(tic): #paso aprametro para lo mismo seleccionar el ticket actual
    return rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.icon("trash-2", size=25),
                    background_color="transparent",
                    cursor="pointer",
                    _hover={
                        "color": "red",
                    },
                ),
            ),
            rx.dialog.content(
                rx.center(
                    rx.flex(
                        rx.icon("trash-2", color="#46A758", size=130, stroke_width=1),
                        rx.flex(
                            rx.dialog.title(
                                "¿Desea eliminar el ticket?",
                                font_size="2rem",
                                color="#FFF",
                            ),
                            rx.flex(
                                rx.dialog.close(
                                    rx.button(
                                        "Cancelar",
                                        background_color="#272826",
                                        cursor="pointer",
                                    ),
                                ),
                            rx.dialog.close(
                                rx.flex(
                                    rx.button(
                                        "Confirmar",
                                        background_color="#46A758",
                                        cursor="pointer",
                                        on_click=TablaTicket.eliminarUsuario(tic[0]) #aca selecciono el ticket para borrarlo
                                    ),
                                ),
                            ),
                                spacing="5",
                                justify="center",
                            ),
                            direction="column",
                            spacing="2",
                        ),
                        align="center",
                        justify="center",
                        spacing="4",
                    ),
                    margin_bottom="1rem",
                ),
            background_color="#111210",
            ),
        )



def devolverTicket():
    return rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.icon("corner-up-left", size=25),
                    background_color="transparent",
                    cursor="pointer",
                    _hover={"color": "#3DD88D"},
                ),
            ),
            rx.dialog.content(
                rx.center(
                    rx.flex(
                        rx.icon("ticket", color="#46A758", size=150, stroke_width=1),
                        rx.flex(
                            rx.dialog.title("Devolver ticket", font_size="3rem", color="#FFF"),
                            rx.dialog.description(
                                "Deja un comentario", font_size="1.3rem", color="#FFF"
                            ),
                            direction="column",
                            spacing="2",
                        ),
                        align="center",
                        justify="center",
                        spacing="4",
                    ),
                    margin_bottom="1rem",
                ),
                rx.center(
                    rx.flex(
                        rx.text("Historial: ", color="#FFF"),
                        rx.box(
                             rx.flex(
                                 rx.foreach( #aca hago el foreach para mostrar los datos que tengo guardados en la lista de los comentarios aca vemos la hora y todo
                                        Comentarios.listaDeComentarios, #aca le hago referencia a la lsita
                                        lambda item: rx.hstack( #aca tengo que llamar a iuna fiuncoon lambda para que me pueda traaer los datos almacenados en esa lista porque es una lsita que contiene tuplas y esas tuplas contienen cadenas en su interior
                                            rx.flex(
                                                rx.text(item[1], color="#FFF"),  # hora
                                                rx.text(item[0], color="#FFF"),  # comentario
                                                direction="column",
                                                ),
                                            margin_left="20px",
                                            margin_top="10px"
                                        )
                                    ),
                                direction="column",
                            ),
                            border="1px solid #46A758",
                            height="auto",
                            width="30rem",
                            border_radius="3px",
                            padding="0 1rem 1rem 1rem",
                        ),
                        rx.cond( #aca filtro para que solo el admin pueda mandar mensaje
                            Login.tipo == "admin",
                                rx.form(
                                    rx.text_area(
                                        placeholder="Mensaje",
                                        background_color="transparent",
                                        border="1px solid #484e54",
                                        width="30rem",
                                        style={
                                            "height": "7em",
                                            "outline-color": "#46A758",
                                            "& textarea::placeholder": {
                                                "color": "#484e54", 
                                            },
                                            "& textarea": {
                                                "color": "#fff",  
                                            },
                                        },
                                        
                                        name="comentario",
                                    ),
                                    rx.button("Enviar", type="submit", background_color="#46A758", margin_top="1rem"),
                                    on_submit=Comentarios.obtenerComentario, #aca mando el mensaje a la lista de la clase que hago referencia mas arriba
                                    reset_on_submit=True
                                ),
                            ),
                        direction="column",
                        spacing="4",
                    ),
                ),
                rx.flex(
                    rx.dialog.close(
                        rx.button(
                            "Cerrar", background_color="#272826", cursor="pointer"
                        ),
                    ),
                    spacing="5",
                    margin_top="2rem",
                    justify="end",
                ),
            background_color="#18191B",
            ),
        )
    

def configuracion():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon(
                    "settings",
                    size=30,
                    color="#757783",
                    cursor="pointer",
                    _hover={"color": "#3DD88D"},
                ),
                background_color="transparent",
                cursor="pointer",
                _hover={"color": "red"},
            ),
        ),
        rx.dialog.content(
            rx.center(
                rx.flex(
                    rx.icon("settings", color="#46A758", size=130, stroke_width=1),
                    rx.dialog.title("Configuracion y sesiòn", font_size="2rem", color="#FFF"),
                    align="center",
                    justify="center",
                    spacing="4",
                ),
                margin_bottom="1rem",
            ),
            rx.center(
                rx.flex(
                    rx.text("Cambiar color: ", color="#FFF"),
                    rx.box(
                        rx.table.root(
                            rx.table.body(
                                rx.table.row(
                                    rx.table.cell(
                                        rx.button(
                                            background_color="red",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido( #bueno aca sitve para elegur los colores del header 
                                                "red"
                                            ),
                                        ),
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="green",
                                            width="2rem",
                                            cursor="pointer",
                                            on_click=ColorsState.set_colorElegido(
                                                "green"
                                            ),
                                        ),
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="blue",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "blue"
                                            ),
                                        )
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="pink",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "pink"
                                            ),
                                        )
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="orange",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "orange"
                                            ),
                                        )
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="purple",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "purple"
                                            ),
                                        )
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="brown",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "brown"
                                            ),
                                        )
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.cell(
                                        rx.button(
                                            background_color="coral",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "coral"
                                            ),
                                        )
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="gold",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "gold"
                                            ),
                                        )
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="magenta",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "magenta"
                                            ),
                                        )
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="tan",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "tan"
                                            ),
                                        )
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="turquoise",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "turquoise"
                                            ),
                                        )
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="yellow",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "yellow"
                                            ),
                                        )
                                    ),
                                    rx.table.cell(
                                        rx.button(
                                            background_color="navy",
                                            cursor_="pointer",
                                            width="2rem",
                                            on_click=ColorsState.set_colorElegido(
                                                "navy"
                                            ),
                                        ),
                                    ),
                                
                                ),
                            ),
                            width="100%",
                        ),
                        height="auto",
                        width="30rem",
                        padding="1rem",
                    ),
                    rx.box(
                        rx.text(
                            'Color predeterminado:', color="#FFF",
                            margin_bottom="1rem",
                            ),
                            rx.button(
                                background_color="#111210",
                                cursor_="pointer",
                                width="2rem",
                                on_click=ColorsState.set_colorElegido("#111210"), #aca uso para ponerle el color por defecto
                            ),
                        ),
                    rx.text("Sesiòn", color="#FFF"),
                    rx.button(
                        "Cerrar Sesiòn",
                        background_color="#3DD88D",
                        cursor="pointer",
                        on_click=Login.cerrarSesion, #aca limpio el tipo de sesion
                    ),
                    direction="column",
                    spacing="4",
                ),
                
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cerrar",
                        background_color="#272826",
                        cursor="pointer",
                    ),
                ),
                spacing="5",
                margin_top="2rem",
                justify="end",
            ),
            background_color="#18191b",
        ),
    )


