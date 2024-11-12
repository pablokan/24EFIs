import reflex as rx
from ..backend.db_ticket import TablaTicket
from ..backend.login import Login
from .Modales import actualizarTicket, eliminarTicket, devolverTicket
from .Badge import statuBadge

def tickets(tic: dict): #aca paso los aprametros para poder poner los valores
    
    return rx.table.row(
        rx.table.cell(tic[0], color="#FFF"),
        rx.table.cell(tic[1], color="#FFF"),#aca lo que hago es imprimir cada valor que hay en los tickets
        rx.table.cell(tic[2], color="#FFF"), 
        rx.table.cell(statuBadge(tic[4])), #aca muestro el estilo del badcge le estoy pasando el nombre por aprametro entonces va a llegar y si coicide con algo le pone el colro corresponciente si no le deja el estilo por default
        rx.table.cell(tic[5], color="#FFF"),
        rx.table.cell(
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        "Ver más",
                        cursor="pointer",
                        background_color="#3DD88D",
                    )
                ),
                rx.dialog.content(
                    rx.vstack(
                        rx.dialog.title("Mensaje Detallado", color="#FFF"),
                        rx.dialog.description(tic[6], margin_bottom="2rem", color="#FFF"),
                    ),
                    rx.dialog.close(
                        rx.button("Cerrar", background_color="#3DD88D", cursor="pointer"),
                    ),
                background_color="#18191b",
                ),
            )
        ),
        rx.table.cell(
            rx.cond(
                Login.tipo == "admin",
                accionAdmin(),
                accionUser(tic),
            ),
        ),
    border_bottom="1px solid #2e3133",  
    )
    


def ticketTable():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("ticket", color="#46A758"),
                        "ID",
                        spacing="2",
                        align="center",
                        color="#FFF"
                    )
                ),
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("clipboard-list", color="#46A758"),
                        "Asunto",
                        spacing="2",
                        align="center",
                        color="#FFF"
                    )
                ),
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("user", color="#46A758"),
                        "Solicitante",
                        spacing="2",
                        align="center",
                        color="#FFF"
                    )
                ),
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("route", color="#46A758"),
                        "Estado",
                        spacing="2",
                        align="center",
                        color="#FFF"
                    )
                ),  # Lo dejamos para despues
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("mails", color="#46A758"),
                        "Contacto",
                        spacing="2",
                        align="center",
                        color="#FFF"
                    )
                ),
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("search", color="#46A758"),
                        "Detalle",
                        spacing="2",
                        align="center",
                        color="#FFF"
                    )
                ),
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("activity", color="#46A758"),
                        "Acciones",
                        spacing="2",
                        align="center",
                        color="#FFF"
                    )
                ),
            ),
        border_bottom="1px solid #2e3133",  
        ),
        rx.table.body(
            rx.foreach(TablaTicket.ticket, tickets),  # Pasa la lista procesada de diccionarios a `tickets`.
        ),
        width="100%",
        on_mount=TablaTicket.obtenerTicket, #aca esto se ejecuta despue sde que el componente se renderiza en la pagina  es similar al onload para cargar los datos y que se puedan ver
    )


def accionAdmin():
    return rx.flex(
        rx.button(
            rx.icon("hand", size=25),
            background_color="transparent",
            cursor="pointer",
            _hover={"color": "#3DD88D"},
        ),
        devolverTicket(),
        rx.button(
            rx.icon("check-check", size=25),
            background_color="transparent",
            cursor="pointer",
            _hover={"color": "#3DD88D"},
        ),
        spacing="3",
    )


def accionUser(tic: list):#paso los aprametros para la fguncion actualizar ticket
    return rx.flex(actualizarTicket(tic), devolverTicket(), eliminarTicket(tic), spacing="3")
