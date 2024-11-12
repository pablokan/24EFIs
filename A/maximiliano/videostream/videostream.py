import reflex as rx
from .backend import *
from .listado import *
from .altas import *
from .bajas import *

@rx.page(on_load=Plataforma.obtenerDatos)
def index() -> rx.Component:
    page = rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Bienvenidos a VIDEOSTREAM!", size="9"),
            rx.text("Proyecto de Programacion 1", size="5"),
            rx.container(
            rx.vstack(
            rx.heading("Menú Principal", size="7"),
            rx.link(
                rx.button("ALTAS"),
                href="/altas" 
            ),
            rx.link(
                rx.button("BAJAS"),
                href="/bajas" 
            ),
            rx.link(
                rx.button("LSITADO - MODIFICACIONES"),
                href="/listado", 
            ),
           
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
    )
    )
    return page



app = rx.App()
app.add_page(index)
app.add_page(altas, "/altas")
app.add_page(listado, "/listado")
app.add_page(bajas, "/bajas")
