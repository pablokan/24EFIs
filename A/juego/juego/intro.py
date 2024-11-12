import reflex as rx
from .front import navigation_bar



class State(rx.State):
    """The app state."""

    ...


def eleccion_item(
    text: str, icon: str, href: str
        ) -> rx.Component:
            return rx.link(
                rx.vstack(
                    rx.image(icon, width="100%", height="400px", align="center", padding_y="1em"),
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


def eleccion_items() -> rx.Component:
    return rx.hstack(
        eleccion_item("ROMANOS", "/romanos_escudo.jpg", "/romanosjuego"),
        eleccion_item("PERSAS", "/persas_escudo.jpg", "/persasjuego"),
        eleccion_item("VIKINGOS", "/vikingos_escudo.jpg", "/vikingosjuego"),
        eleccion_item("GRIEGOS", "/griegos_escudo.jpg", "/griegosjuego"),
        
        spacing="2",
        width="100%",
    )


def cajas() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.vstack(
                    
               
                eleccion_items(),
                spacing="40",
                
                left="0px",
                top="0px",
                z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("accent", 3),
                align="start",
                height="100%",
               
                width="100%",
                ),
            ),
        ),
        
    ),

def intro():
    # Griego Page
    return rx.container(
          navigation_bar(),
          rx.heading(
                        "Elije tu ejercito", size="9", weight="bold", align="center", color_scheme="red", high_contrast=True
                    ),
          cajas(),
          
 
                    
                ),
        
    