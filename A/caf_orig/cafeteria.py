import reflex as rx
from .components.navbar import *
from .components.mesas import *
from .Carta import carta
from .components.pedidos import tablaPedidos
from .components.pedidos import tablaUltimosPedidos
from rxconfig import config


def mostrador() -> rx.Component:

    mostra = rx.box(
        # Encabezado del mostrador con botÃ³n
        rx.heading(
            "MOSTRADOR",
            size="lg",
            weight="bold",
            color="white",
            padding='15px'
            ),
    padding="0",
    margin="0",
    width="100%",
    background='#cccccc'
    )
    return mostra

def pedi() -> rx.Component:

    pedid = rx.box(
        navbar(),
        mostrador(),
        tablaPedidos(),
        tablaUltimosPedidos(),
        width="100%",
        min_height="100vh",
        background="lightyellow",
        padding="0",   
        margin="0",    
        overflow_x="hidden", 
    )
    return pedid

def main() -> rx.Component:
    page = rx.box(
        navbar(),
        mesas(),
        width = "100%",
        height = "100vh",
        background = "lightyellow",
        padding = "0",
        margin = "0"
    )
    return page


app = rx.App()
app.add_page(main)
app.add_page(carta)
app.add_page(pedi , route ="/fjf")
