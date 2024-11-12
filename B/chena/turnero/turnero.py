import reflex as rx
from.backend import State, main_table

# Al cargar la pagina, cargar los datos de los clientes 
@rx.page(on_load=State.cargar_datos)
def index() -> rx.Component:
    # Pagina 
    page = rx.box(
            # Tabla general
            main_table(),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )
    return page

app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="grass"
    ),
)
app.add_page(index)
