import reflex as rx
from .components.navbar import navbar
from .components.mostrador import mostrador
from .Carta import carta  
from .components.pedidos import tablaPedidos 
from .components.pedidos import tablaUltimosPedidos
from .cafeteria import main

def index() -> rx.Component:

    page = rx.box(
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
    return page


app = rx.App()
app.add_page(main, route="/")      
app.add_page(index, route="/fjf")      
app.add_page(carta, route="/carta")
app._compile()