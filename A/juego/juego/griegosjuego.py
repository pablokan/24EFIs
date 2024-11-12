import reflex as rx
from .front import navigation_bar
from .back import Vida, Vida2


def eleccion_item(
    text: str, icon: str, num: str, on_click
        ) -> rx.Component:
            return rx.box(
                rx.vstack(
                    rx.image(icon, width="100%", height="100%", align="center", padding_y="1em"),
                    rx.text(text, size="4"),
                    rx.text(num, size="4"),
                    on_click=(on_click),
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
             
                underline="none",
                weight="medium",
                width="100%",
            )

def eleccion_items() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            eleccion_item("PELTASTA", "/griego1.jpg",'1', Vida2.perderVida(25)),
            eleccion_item("JINETE", "/griego2.jpg",'2',Vida2.perderVida(25)),
            eleccion_item("ARQUERO", "/griego3.jpg",'3',Vida2.perderVida(15)),
            eleccion_item("HOPLITA", "/griego4.jpg",'4',Vida2.perderVida(20)),
            eleccion_item("PITAGORICO", "/griego5.jpg",'5',Vida2.perderVida(10)),
            eleccion_item("THERAPEUTA", "/griego6.jpg",'6',Vida2.perderVida(5)),
            spacing="2",
            width="100%",
        ),

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
    )


def eleccion_item2(
    text: str, icon: str, num: str, on_click
        ) -> rx.Component:
            return rx.box(
                rx.vstack(
                    rx.image(icon, width="100%", height="100%", align="center", padding_y="1em"),
                    rx.text(text, size="4"),
                    rx.text(num, size="4"),
                    on_click=(on_click),
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
              
                
                underline="none",
                weight="medium",
                width="100%",
            )

def eleccion_items2() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            eleccion_item2("LANZERO", "/persas1.jpg",'1',Vida.perderVida(20)),
            eleccion_item2("JINETE", "/persas2.jpg",'2',Vida.perderVida(20)),
            eleccion_item2("INMORTAL", "/persas3.jpg",'3',Vida.perderVida(25)),
            eleccion_item2("ARQUEROS", "/persas4.jpg",'4',Vida.perderVida(15)),
            eleccion_item2("KARDAKES", "/persas5.jpg",'5',Vida.perderVida(15)),
            eleccion_item2("TIRIADES", "/persas6.jpg",'6',Vida.perderVida(15)),
            spacing="2",
            width="100%",
        ),

    )

def cajas2() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.vstack(
                    eleccion_items2(),
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
    )




def jueguito():
    

    
    return rx.card(
          rx.vstack(
               
                rx.heading("Vida:"),
                rx.badge(
                    Vida.vid.to_string()
                ),
                rx.badge(
                   Vida.msg               
                ),
                rx.button('reiniciar', on_click=Vida.reiniciar),
                
          ),
     )

def jueguito2():
    

    
    return rx.card(
          rx.vstack(
               
                rx.heading("Vida:"),
                rx.badge(
                    Vida2.vid.to_string()
                ),
                rx.badge(
                   Vida2.msg               
                ),
                rx.button('reiniciar', on_click=Vida2.reiniciar),
                
          ),
     )

def griegosjuego():
    
    return rx.container(
        
        navigation_bar(),
        
        cajas(),
        
       
        jueguito(),
        
        cajas2(),
        jueguito2(),



    ),
