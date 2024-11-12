import reflex as rx
from ..components.EstadosTicket import estadosContent
from ..components.Header import header

def estadosTicket():
    return rx.box(
        header(),
        rx.box(
            estadosContent(),
            padding="0 4rem 0 4rem",
            margin_top="4rem"
        ),
        background_color="#111210",
        height="100vh",
    )