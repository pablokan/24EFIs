import reflex as rx
from .Modales import configuracion
from ..backend.backend import ColorsState
from ..backend.login import Login


def seccionAdmin():
    return rx.flex(
            rx.text(
                "Tickets",
                font_size="1.6rem",
                cursor="pointer",
                color="#FFF",
                _hover={
                    "text_decoration": "underline",
                    "text_decoration_color": "#3DD88D",
                },
                on_click=rx.redirect("/ticket"),
            ),
            rx.text(
                    "Estados",
                    font_size="1.6rem",
                    cursor="pointer",
                    color="#FFF",
                    _hover={
                        "text_decoration": "underline",
                        "text_decoration_color": "#3DD88D",
                    },
                    on_click=rx.redirect("/estadosTicket"),
                ),
                rx.text(
                    "Usuarios",
                    font_size="1.6rem",
                    cursor="pointer",
                    color="#FFF",
                    _hover={
                        "text_decoration": "underline",
                        "text_decoration_color": "#3DD88D",
                    },
                    on_click=rx.redirect("/usuariosTicket"),
                ),
                justify="between",
                align="center",
                spacing="5",
            )
    
def seccionUser():
    return rx.box(
        rx.text(
                "Tickets",
                font_size="1.6rem",
                cursor="pointer",
                color="#FFF",
                _hover={
                    "text_decoration": "underline",
                    "text_decoration_color": "#3DD88D",
                },
                on_click=rx.redirect("/ticket"),
            ),
        )

def header():
    return rx.flex(
        rx.image(src="/logo.png", width="80px", height="auto"),
        rx.flex(
            rx.cond( #aca uso esto para fultrar entre los usuarios y los amdins
                Login.tipo == "admin",
                seccionAdmin(),
                seccionUser(),
            ),
            configuracion(),
            justify="between",
            align="center",
            spacing="5",
        ),
        background_color=ColorsState.colorElegido,  # backend, pongo el color del header, usando la clase ColorsState
        justify="between",
        align="center",
        width="100%",
        padding_x="1rem",
        border_bottom="1px solid white",
    )
