import reflex as rx
from ..components.Ticket import ticketTable
from ..components.Modales import ticketBtn
from ..components.Header import header
from ..backend.login import Login

def ticket():
    return rx.box(
        header(),
        rx.box(
            rx.box(
                rx.cond( #aca filtro si es admin no tiene que ver el boton de agregar tickert si es user si
                    Login.tipo == "admin",
                    rx.box(),
                    ticketBtn(),
                ),
            padding="2rem 2rem 2rem 0",
            ),
        rx.flex(
            ticketTable(),
            flex_direction="column",
            justify="center",
            align="center",
            ),
        padding="0 4rem 0 4rem",
        ),
        background_color="#111210",
        height="100vh",
    )
