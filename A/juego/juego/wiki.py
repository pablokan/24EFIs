import reflex as rx
import pandas as pd
import json
from .front import navigation_bar

personajes= pd.read_csv("personajes.csv")

with open("personajes.json", "r") as archivo:
    personajesjson = json.load(archivo)


class FlexPlaygroundState(rx.State):
    columna: str = "PODER"


def select(label, items, value, on_change):
    return rx.flex(
        rx.text(label),
        rx.select.root(
            rx.select.trigger(),
            rx.select.content(
                *[
                    rx.select.item(item, value=item)
                    for item in items
                ]
            ),
            value=value,
            on_change=on_change,
        ),
        align="center",
        justify="center",
        direction="column",
    )



def selectors():
    return rx.flex(
        select(
            "Elegir columna",
            ["ALTURA","PODER", "DEFENSA", "VIDA"],
            FlexPlaygroundState.columna,
            FlexPlaygroundState.set_columna,
        ),
    ),
def selectorRadar():
    return rx.box(
        selectors(),
        
        width="100%",
    )



def radar_simple():
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key=FlexPlaygroundState.columna,
            stroke="#8884d8",
            fill="#8884d8",
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="NOMBRE"),
        rx.recharts.polar_radius_axis(
            angle=90, domain=[0, 30]
        ),
        data=personajesjson,
        width="100%",
        height=300,
    )



def sidebar_item(
    text: str, icon: str, href: str
        ) -> rx.Component:
            return rx.link(
                rx.hstack(
                    rx.icon(icon),
                    rx.text(text, size="4"),
                    width="100%",
                    padding_x="0.5rem",
                    padding_y="0.75rem",
                    align="center",
                    style={
                        "_hover": {
                            "bg": rx.color("accent", 4),
                            "color": rx.color("accent", 11),
                        },
                        "border-radius": "0.5em",
                    },
                ),
                href=href,
                underline="none",
                weight="medium",
                width="100%",
            )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Ejercitos", "sword", "/ejercitos"),
        sidebar_item("Persa", "swords", "/persa"),
        sidebar_item("Romano", "shield", "/romano"),
        sidebar_item("Vikingo", "axe", "/vikingo"),
        sidebar_item("Griego", "scroll", "/griego"),
        spacing="1",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    
                    rx.heading(
                        "Wiki", size="7", weight="bold"
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                spacing="5",
                position="fixed",
                left="0px",
                top="0px",
                z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("accent", 3),
                align="start",
                height="100%",
               
                width="16em",
            ),
        ),
        
    )
# Pagina Ejercitos 
def ejercitos():
   
     return rx.container(
             navigation_bar(), 
             sidebar(),   
              
                 
    
            rx.hstack(
                 
                            rx.data_table(
                                data=personajes[["NOMBRE", "ALTURA", "PODER","DEFENSA","VIDA"]],
                                pagination=True,
                                search=True,
                                sort=True,
                                resizable=True,
                                
                                
                            ),
            ),

            selectorRadar(), 
            rx.vstack(
                radar_simple(),
                
            ),
        )
# Persa 
def persa():
    
    return rx.container(
        navigation_bar(),
        sidebar(),
        rx.heading("Imperio Persa", size="9"),
        rx.text(
            "Los persas eran un pueblo de origen indoeuropeo que habitaba en la región de Persia, en la actual Irán. "
            "El Imperio persa fue uno de los más grandes de la antigüedad, "
            "y su ejército estaba compuesto por soldados de diversas regiones y etnias.",
            size="5",
        ),
        rx.image(src="/mapa_persa.png", width="5000px"),
        rx.text("Cartas y escudo:", size="9"),
        rx.image(src="/pe.jpeg", width="1000px"),
    ),
# Romano 
def romano():
    
    return rx.container(
        navigation_bar(),
        sidebar(),
        rx.heading("Imperio Romano", size="9"),
        rx.text(
            "Los romanos fueron un pueblo de origen latino que habitaba en la península itálica. "
            "El Imperio romano fue uno de los más grandes de la antigüedad, "
            "y su ejército estaba compuesto por soldados de diversas regiones y etnias.",
            size="5",
            align="justify",
            weight="bold",
            color_scheme="indigo",
        ),
        rx.image(
             src="/Roman_Empire.png", 
             width="1000px", 
              ),
        rx.text(rx.flex( rx.text.strong("Legionario:")),
                "del latín: legionarius, era un soldado de infantería pesada integrante de una unidad militar del ejército romano, formada, normalmente, por ciudadanos romanos mayores de quince años. Era conocido por su disciplina y orden. \n", trim='normal',
                align='justify',
                ),
        rx.text(rx.flex(rx.text.strong("Pretoriano:")),
                " era un cuerpo militar que servía de escolta y protección a los emperadores romanos. Antes de los emperadores, esta escolta ya era usada por los líderes militares desde la época de los Escipiones alrededor del año 275 a. C. Los miembros de la Guardia Pretoriana estaban entre las más diestras y célebres fuerzas militares de la historia antigua.\n " ),
        rx.text(rx.flex(rx.text.strong("Hastatus:")),
                " Los asteros (en latín, «hastati» y en singular, «hastatus», que puede traducirse literalmente como «lancero» o «luchador con lanza») eran una clase de infantería en los ejércitos de la República romana. Eran los hombres más jóvenes y pobres de la legión, los cuales solo podían permitirse equipos modestos, para cumplir con su labor como la infantería ligera. Estas unidades se disolvieron tras las reformas de Mario de 107 a. C.\n" ),
        rx.text(rx.flex(rx.text.strong("Arquero auxiliar:")),
                " Sagittarii (en singular, sagittarius) era el nombre que recibían en la Antigua Roma los arqueros que formaban parte de las tropas auxiliares. Presumiblemente, y hasta épocas muy tardías, la mayor parte de los sagittarii eran arqueros de infantería, que se desplazaban a pie.\n" ),
        rx.text("Cartas y escudo:", size="9"),
        
        rx.image(src="/ro.jpeg", width="1000px"),
    ),
 # Vikingo Page

def vikingo():
   
    return rx.container(
        navigation_bar(),
        sidebar(),
        rx.heading("Vikingos", size="9"),
        rx.text(
            "Los vikingos fueron un pueblo de origen escandinavo que habitaba en la región de Escandinavia. "
            "Los vikingos eran conocidos por sus incursiones en Europa y su habilidad en la navegación.",
            size="5",
            
        ),
        rx.image(
             src="/vikingo_territorios.jpg", 
             width="1000px", 
              ),
        rx.text(rx.flex( rx.text.strong("*************:")),
                "*************",
                trim='normal',
                align='justify',
                ),
        rx.text(rx.flex(rx.text.strong("*************:")),
                " era un cuerpo militar que servía de escolta y protección a los emperadores romanos. Antes de los emperadores, esta escolta ya era usada por los líderes militares desde la época de los Escipiones alrededor del año 275 a. C. Los miembros de la Guardia Pretoriana estaban entre las más diestras y célebres fuerzas militares de la historia antigua.\n " ),
        rx.text(rx.flex(rx.text.strong("*************:")),
                " Los asteros (en latín, «hastati» y en singular, «hastatus», que puede traducirse literalmente como «lancero» o «luchador con lanza») eran una clase de infantería en los ejércitos de la República romana. Eran los hombres más jóvenes y pobres de la legión, los cuales solo podían permitirse equipos modestos, para cumplir con su labor como la infantería ligera. Estas unidades se disolvieron tras las reformas de Mario de 107 a. C.\n" ),
        rx.text(rx.flex(rx.text.strong("*************:")),
                " *************.\n" ),
        rx.text("Cartas y escudo:", size="9"),
        rx.image(src="/vi.jpeg", width="1000px"),        
    ),

# Griego Page

def griego():
    
    return rx.container(
        navigation_bar(),
        sidebar(),
        rx.heading("Griego", size="9"),
        rx.text(
            "Los griegos fueron un pueblo de origen helénico que habitaba en la región de Grecia. "
            "Los griegos eran conocidos por su cultura y su influencia en la antigüedad.",
            size="5",
        
        ),
        rx.text("Cartas y escudo:", size="9"),
        rx.image(src="/gr.jpeg", width="1000px"),
    ),

