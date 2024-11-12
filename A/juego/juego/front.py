import reflex as rx






def create_hover_link(link_url, link_text):
    """Create a link element with hover effect."""
    return rx.el.a(
        link_text,
        href=link_url,
        _hover={"color": "#FBBF24"},
    )
def create_small_icon(alt_text, icon_name):
    """Create a small icon element."""
    return rx.icon(
        alt=alt_text,
        tag=icon_name,
        height="1.5rem",
        width="1.5rem",
    )
    
def navigation_bar():
    """Create the main navigation bar."""
    return rx.flex(
        rx.box(
            "Epic Adventure",
            font_weight="700",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        rx.box(
            create_hover_link(
                link_url="/", link_text="Home"
            ),
            create_hover_link(
                link_url="/intro", link_text="Juego"
            ),
            create_hover_link(
                link_url="/ejercitos",
                link_text="WikiJuego",
            ),
            create_hover_link(
                link_url="/quienessomos", link_text="Quienes Somos"
            ),
            display=rx.breakpoints(
                {"0px": "none", "768px": "flex"}
            ),
            column_gap="1rem",
        ),
        rx.el.button(
            create_small_icon(
                alt_text="Menu", icon_name="menu"
            ),
            display=rx.breakpoints({"768px": "none"}),
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
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


