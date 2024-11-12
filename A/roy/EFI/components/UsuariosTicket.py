import reflex as rx
from ..backend.db_usuarios import TablaUser

def usr(users: list):
    return rx.table.row(
            rx.table.cell(users[0], color="#FFF"),
            rx.table.cell(users[1], color="#FFF"),#aca los mismo muestro los datos del usuarios
            rx.table.cell(users[2], color="#FFF"),
            rx.table.cell(users[3], color="#FFF"),
            border_bottom="1px solid #2e3133",
            
        )




def usuariosContent():
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
                    ),
                ),
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("clipboard-list", color="#46A758"),
                        "Email",
                        spacing="2",
                        align="center",
                        color="#FFF"
                    )
                ),
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("clipboard-list", color="#46A758"),
                        "Contraseña",
                        spacing="2",
                        align="center",
                        color="#FFF"
                    )
                ),
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("circle-help", color="#46A758"),
                        "Tipo",
                        spacing="2",
                        align="center",
                        color="#FFF"
                    ),
                ),
            border_bottom="1px solid #2e3133",  
            ),
        ),
        rx.table.body(
            rx.foreach(
               TablaUser.users, usr #aca hago el foreach apra mostrar todo los datos
           ),
        ),
        width="100%",
    )




