import reflex as rx
from .backend import *


def bajas() -> rx.Component:
    page = rx.box(
        rx.heading("MENU DE BAJAS", size="7"),
        rx.vstack(
        baja_usuario_dialog(),
        baja_contenido_dialog(),
        baja_alquiler_dialog(),
        rx.link(
            rx.button("Volver atras"),
            href="/",
            ),
        ),
    )
    return page

def baja_usuario_dialog():
    page = rx.dialog.root(
        rx.dialog.trigger(rx.button("Dar de baja a un usuario")),
        rx.dialog.content(
            rx.vstack(
                rx.heading("Baja Usuario", size="7"),
                rx.form(
                    rx.vstack(
                        rx.input(placeholder="DNI usuario a dar de baja", name="dni"),
                        rx.button("Dar de baja", type="submit"),
                    ),
                    on_submit=lambda form_data: Plataforma.baja_usuario(form_data),
                    reset_on_submit=True,
                    
                ),
                spacing="4",
            ),
        ),

    )
    return page


def baja_contenido_dialog():
    page = rx.dialog.root(
        rx.dialog.trigger(rx.button("Dar de baja a un contenido")),
        rx.dialog.content(
            rx.vstack(
                rx.heading("Baja Contenido", size="7"),
                rx.form(
                    rx.vstack(
                        rx.input(placeholder="Titulo del contenido a dar de baja", name="titulo"),
                        rx.button("Dar de baja", type="submit"),
                    ),
                    on_submit=lambda form_data: Plataforma.baja_contenido(form_data),
                    reset_on_submit=True,
                ),
                spacing="4",
            ),
        ),
    )
    return page

#aca ahora tengo que hacer lo mismo que en altas alquiler
#Primero cargo el DNI del usuario
#si tiene alquiler registrado entonces tiene que fijarse que fecha de devolucion tiene
#si la fecha de devolucion es >= a la fecha actual entonces a alquilado=False asi queda disponible
#si la fecha de devolucion es < a la fecha actual entonces necesito hacer el calcule de dias que se paso
#para cobrar el importe de los dias que se paso


def baja_alquiler_dialog():
    page = rx.dialog.root(
                rx.dialog.trigger(rx.button("Dar de baja a un Alquiler")),
                rx.dialog.content(
                rx.vstack(
                    rx.container(
                            rx.heading("Devolver Alquiler"),
                            rx.input(placeholder="DNI del usuario",
                                    on_change=Plataforma.set_dni_usuario),
                            rx.button("Buscar", on_click=lambda: Plataforma.buscar_devolucion(Plataforma.dni_usuario)),
                            rx.text(f'Usuario Nombre: {Plataforma.nombre_usuario}'), 
                            rx.text(f'DNI usuario: {Plataforma.dni_usuario}'),
                            rx.text(f'Nombre de contenido: {Plataforma.nombre_titulo}'),                                       
                            rx.text(f'Fecha de alquiler: {Plataforma.fecha_alquiler}'),
                            rx.text(f'Fecha de devolucion: {Plataforma.fecha_devolucion}'),
                            rx.text(f'Importe a abonar: {Plataforma.importe}'),
                            rx.button("Devolucion de alquiler", on_click=lambda: Plataforma.devolucion_alquiler()),
                            rx.heading(Plataforma.mensaje),
                        spacing="4",
                    ),
                ),
            ),
        )
    return page

      