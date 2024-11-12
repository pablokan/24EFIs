import reflex as rx

def navbar_link(text, href):
    nav = rx.link(
        rx.text(
            text,
            color="white",
            font_size="lg",
            font_weight="bold",
            _hover={"color": "cyan"}
        ),
        href=href,
        padding="0 15px",
    )
    return nav

def navbar() -> rx.Component:
    page =  rx.box(

        rx.hstack(
            rx.heading(
                "Coffe FJF",
                size="lg",
                weight="bold",
                color="white",
            ),

            rx.hstack(
                navbar_link("Mesas", "/"),
                navbar_link("Pedidos", "/fjf"),
                navbar_link("Carta", "/carta"),
                justify="end",
                spacing="5",
            ),
            justify="between",
            align_items="center",
            padding="15px 30px",
            background="linear-gradient(90deg, #333, #555)",  
            box_shadow="0px 4px 10px rgba(0, 0, 0, 0.3)",
            width="100%",
        ),
        padding="0",
        margin="0",
        width="100%",
    )
    return page 