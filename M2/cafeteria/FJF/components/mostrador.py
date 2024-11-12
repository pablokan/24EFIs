import reflex as rx


def mostrador() -> rx.Component:

    mostra = rx.box(
        # Encabezado del mostrador con botón
        rx.heading(
            "MOSTRADOR",
            size="large",
            weight="bold",
            color="#333",
            padding='15px'
            ),

    padding="0",
    margin="0",
    width="100%",
    background='lightyellow'
    )
    return mostra