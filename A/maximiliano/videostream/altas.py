import reflex as rx
from .backend import *


def altas() -> rx.Component:
    page = rx.box(
        rx.heading("MENU DE ALTAS", size="7"),
        rx.vstack(
        alta_usuario_dialog(),
        alta_contenido_dialog(),
        alta_alquiler_dialog(),
        rx.link(
            rx.button("Volver atras"),
            href="/",
            ),
        ),
    )
    return page


def alta_usuario_dialog():
    page = rx.dialog.root(
        rx.dialog.trigger(rx.button("Agregar Nuevo Usuario")),
        rx.dialog.content(
            rx.vstack(
                rx.heading("Agregar Nuevo Usuario", size="7"),
                rx.form(
                    rx.vstack(
                        rx.input(placeholder="Nombre", name="nombre"),
                        rx.input(placeholder="DNI", name="dni"),
                        rx.input(placeholder="Email", name="email"),
                        rx.input(placeholder="Teléfono", name="telefono"),
                        rx.input(placeholder="Dirección", name="direccion"),
                        rx.button("Agregar Usuario", type="submit"),
                    ),
                    on_submit=lambda form_data: Plataforma.handle_submit(form_data, "usuarios"),
                    reset_on_submit=True,
                ),
                spacing="4",
            ),
        ),
    )
    return page

def alta_contenido_dialog():
    page = rx.dialog.root(
        rx.dialog.trigger(rx.button("Agregar Nuevo Contenido")),
        rx.dialog.content(
            rx.vstack(
                rx.heading("Agregar Nuevo Contenido", size="7"),
                rx.form(
                    rx.vstack(
                        rx.input(placeholder="Título", name="titulo"),
                        rx.input(placeholder="Genero", name="genero"),
                        rx.input(placeholder="Año", name="ano"),
                        rx.input(placeholder="Director", name="director"),
                        rx.input(placeholder="Protagonista", name="protagonista"),
                        rx.input(placeholder="Tipo de Contenido", name="tipo_contenido"),
                        rx.button("Agregar Contenido", type="submit"),
                    ),
                    on_submit=lambda form_data: Plataforma.handle_submit(form_data, "contenido"),
                    reset_on_submit=True,
                ),
                spacing="4",
            ),
        ),
    )
    return page



def alta_alquiler_dialog():
    page = rx.dialog.root(
        rx.dialog.trigger(rx.button("Alquilar Contenido")),
        rx.dialog.content(
            rx.vstack(
                rx.container(
                    rx.heading("Alquilar"),
                    rx.input(placeholder="DNI del usuario",
                             on_change=Plataforma.set_dni_usuario),
                    rx.button("Buscar", on_click=lambda: Plataforma.buscar_usuario(Plataforma.dni_usuario)),
                    rx.heading(Plataforma.nombre_usuario),
                    rx.input(placeholder="Nombre del título", 
                             on_change=Plataforma.set_nombre_titulo),
                    rx.button("Buscar", on_click=lambda: Plataforma.buscar_contenido(Plataforma.nombre_titulo)),
                    rx.heading(f'Tipo de contenido: {Plataforma.tipo_titulo} - {Plataforma.nombre_titulo}'),         
                    rx.input(placeholder="Cantidad de días", on_change=Plataforma.set_cantidad_dias),
                    rx.button("Calcular importe:", on_click=lambda: Plataforma.calcular_importe(Plataforma.cantidad_dias)),
                    rx.heading("Importe a cobrar ", Plataforma.importe),
                    rx.button("Alquilar", 
                              on_click=lambda: Plataforma.alquilar(Plataforma.nombre_usuario,
                                                                   Plataforma.dni_usuario,
                                                                   Plataforma.nombre_titulo,
                                                                   Plataforma.cantidad_dias,
                                                                   Plataforma.importe)),
                ),
                spacing="4",
            ),
        ),
    )
    return page

      