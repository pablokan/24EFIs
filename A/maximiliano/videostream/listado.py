import reflex as rx
from .backend import Plataforma

def listado() -> rx.Component:  
    page = rx.box(
                    rx.heading(f'Menu de visulizacion de las diferentes tablas... {Plataforma.tabla_actual}'),
                    rx.hstack(
                        rx.button("USUARIOS", on_click=lambda: Plataforma.cambiarTabla("usuarios")),
                        rx.button("CONTENIDOS", on_click=lambda: Plataforma.cambiarTabla("contenido")),
                        rx.button("ALQUILERES", on_click=lambda: Plataforma.cambiarTabla("alquileres")),
                        rx.link(
                        rx.button("VOLVER ATRAS"),
                        href="/", 
                    ),                    ),
                    rx.heading(Plataforma.clicked_data, align='center'),
                    rx.divider(size='4'),
                    rx.box(
                        rx.data_editor(
                            columns=Plataforma.cabecera,
                            data=Plataforma.datos,
                            row_height=20,
                            smooth_scroll_x=True,
                            smooth_scroll_y=True,
                            column_select="single",
                            height="100vh",
                            on_cell_clicked=Plataforma.clic_celda,
                            on_cell_edited=Plataforma.manejarCeldaEditada,
                        ),
                        align='center',
                        justify='center',
                        width='100%',
                        height='100vh', 
                        style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'},
                    ),
            )

    return page
