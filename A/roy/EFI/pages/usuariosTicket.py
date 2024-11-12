import reflex as rx
from ..components.Header import header
from ..components.UsuariosTicket import usuariosContent

def usuariosTicket():
    return rx.box(
        header(),
        rx.box(
            usuariosContent(),
            padding="0 4rem 0 4rem",
            margin_top="4rem",
            width="100%",
        ),
        background_color="#111210",
        height="100vh",
    )