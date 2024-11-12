import reflex as rx
from .components.navbar import navbar

def carta() -> rx.Component:
    
    return rx.box(
        navbar(),  # Agrego la navbar.
        
        rx.box(
            rx.heading("CARTA", size="6", margin_bottom="20px",color_scheme = "blue"),  # Encabezado principal "CARTA"
            
            rx.box(
                rx.hstack(  # Apilo horizontalmente dos vstack, uno para "cafeteria" y otro para "panaderia"
                    rx.vstack(
                        # Encabezado para la sección de "CAFETERÍA"
                        rx.heading("CAFETERÍA", size="large", margin_bottom="10px",color_scheme = "blue"),
                        # Lista de productos de la cafetería con sus precios.
                        rx.text("Café chico: $8,888",color_scheme = "blue"),
                        rx.text("Café en jarra: $1,800",color_scheme = "blue"),
                        rx.text("Café doble: $2,100",color_scheme = "blue"),
                        rx.text("Café con leche: $2,100",color_scheme = "blue"),
                        rx.text("Té: $1,700",color_scheme = "blue"),
                        rx.text("Té con leche: $1,900",color_scheme = "blue"),
                        rx.text("Mate cocido: $1,900",color_scheme = "blue"),
                        rx.text("Submarino: $3,000",color_scheme = "blue"),
                        rx.text("Chocolate (frío o caliente): $2,600",color_scheme = "blue"),
                        align_items="flex-start",  # Alinea los ítems al inicio.
                    ),
                    rx.vstack(
                        # Encabezado para la sección de "PANADERÍA"
                        rx.heading("PANADERÍA", size="large", margin_bottom="10px",color_scheme = "blue"),
                        # Lista de productos de la panadería con sus precios.
                        rx.text("Medialunas/Facturas: $750",color_scheme = "blue"),
                        rx.text("Criollos: $600",color_scheme = "blue"),
                        rx.text("Tostadas por unidad: $900",color_scheme = "blue"),
                        rx.text("Mafalda: $1,700",color_scheme = "blue"),
                        align_items="flex-start",  # Alinea los ítems al inicio.
                    ),
                ),
                spacing="50px",  # Espacio entre los dos vstack.
                display="flex",
                align_items="center",
                justify_content="center",  # Centra horizontalmente el contenido.
                padding="20px",
            ),
            padding='20px'
        ),
        width="100%",  # Ancho completo del contenedor.
        min_height="100vh",  # Altura mínima del contenedor es el 100% del alto de la ventana.
        background="lightyellow",  # Color de fondo.
        padding="0",  # Sin padding adicional.
        margin="0",  # Sin margen adicional.
        overflow_x="hidden",  # Oculta el desbordamiento horizontal.
    )
