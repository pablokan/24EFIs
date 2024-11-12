import reflex as rx
from ..backend.db_estados import TablaEstados


def estados(estado: list):  # despues sacar esto o ver como se puede arreglar
    return rx.table.row(
        rx.table.cell(estado[0], color="#FFF"), #aca muestro los valores de la base de datos 
        rx.table.cell(estado[1], color="#FFF"),
        border_bottom="1px solid #2e3133",  
    )


def estadosContent():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("ticket", color="#46A758"),
                        "ID",
                        spacing="2",
                        align="center",
                        color="#FFF",
                    )
                ),
                rx.table.column_header_cell(
                    rx.flex(
                        rx.icon("clipboard-list", color="#46A758"),
                        "Nombre",
                        spacing="2",
                        align="center",
                        color="#FFF",
                    ),
                ),
            border_bottom="1px solid #2e3133",  
            ),
        ),
        rx.table.body(
            rx.foreach(TablaEstados.estados, estados), #le hago foreach para obtener los valores de la base de datos
        ),
        width="100%",
    )
