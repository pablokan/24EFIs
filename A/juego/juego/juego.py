##main juego

import reflex as rx

from .wiki import ejercitos
from .front import navigation_bar
from .wiki import persa
from .wiki import romano
from .wiki import vikingo
from .wiki import griego
from .intro import intro
from .romanosjuego import romanosjuego
from .persasjuego import persasjuego
from .griegosjuego import griegosjuego
from .vikingosjuego import vikingosjuego





def index() -> rx.Component:
    # Welcome Page (Index)
    
    return rx.container(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                navigation_bar(),
                rx.heading("The Last Battle", size="12"),
                rx.video(
                    url="/intro.mp4",
                    width="auto",
                    height="auto",
                    playing=True,
                    loop=True,
                    controls=False,
                    style={"border-radius": "10px"},
                ),
                rx.text('Has en el boton jugar, luego selecciona tu ejercito y comienza la batalla', size="20", weight="bold"),
                

            ),
            rx.hstack(
                    rx.button(
                        rx.link("Jugar", href="/intro", size="400px", color="primary", style={"border-radius": "50px"}),
                    ),
                    rx.text('DEMO', size="20", weight="bold"),    
            ),    
            

            
        )
 

def quienessomos():
    return rx.container(
            navigation_bar(),
            rx.vstack(
                rx.heading('TRABAJO PRACTICO FINAL', size="40", weight="bold", align="center", high_contrast=True),
                rx.text.strong('Para la realizacion del presente trabajo, se ha utilizado, aparte de los conocimientos adquiridos en clase, la documentacion de Reflex y el uso de ejemplos de la misma.\n', size="20", weight="bold" ),
                rx.link("https://reflex.dev/docs/getting-started/introduction/", "Documentacion de Reflex", size="20", weight="bold"),
                rx.text("Quienes Somos", size="20", weight="bold"),
            ),
            rx.vstack(
                rx.table.root(
                    
                    rx.table.header(
                        
                        rx.table.row(
                            rx.table.column_header_cell("Nombre"),
                            rx.table.column_header_cell("Email"),
                            rx.table.column_header_cell("Group"),
                        ),
                    ),
                    rx.table.body(
 
                        rx.table.row(
                            rx.table.row_header_cell("Matias Pepe"),
                            rx.table.cell("matias@example.com"),
                            rx.table.cell("Developer"),
                        ),
                        rx.table.row(
                            rx.table.row_header_cell("Perez Lucas"),
                            rx.table.cell("lucas@example.com"),
                            rx.table.cell("Developer"),
                        ),
                        rx.table.row(
                            rx.table.row_header_cell("Manuel Gomez"),
                            rx.table.cell("Manuel@example.com"),
                            rx.table.cell("Developer"),
                        ),                        
                        rx.table.row(
                            rx.table.row_header_cell("Juan Falco"),
                            rx.table.cell("Juan@example.com"),
                            rx.table.cell("Developer"),
                        ),
                    
                    ),
 
                ),
        ),
    ),


app = rx.App()

app.add_page(index)
app.add_page(ejercitos)
app.add_page(persa)
app.add_page(romano)
app.add_page(vikingo)
app.add_page(griego)
app.add_page(intro)
app.add_page(romanosjuego)
app.add_page(persasjuego)
app.add_page(griegosjuego)
app.add_page(vikingosjuego)
app.add_page(quienessomos)

