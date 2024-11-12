import reflex as rx
from .backend import *
from .menu_pacientes import * 
from .menu_donantes import *


def index():
    page = rx.box(
                rx.vstack(
                    rx.heading(f"TRANSPLANTAR VIDA ",color="black",size="20"),
                    rx.link(
                        rx.button("Menu Pacientes",size="4", border="solid 2px black"),
                            href="/menu_pacientes",
                        ),
                    rx.link(
                        rx.button("Menu Donantes",size="4",border="solid 2px black"),
                            href="/menu_donantes",
                        ),
                    ),
                padding="20px",
                background="lightblue",
                height="100vh"
    )
    return page

app = rx.App()
app.add_page(index)
app.add_page(menu_pacientes,"/menu_pacientes")

app.add_page(menu_donantes,"/menu_donantes")
#Paginas menu pacientes
app.add_page(cargar_paciente,"/cargar_paciente")
app.add_page(eliminar_paciente,"/eliminar_paciente")
app.add_page(mostrar_tabla_pacientes,"/mostrar_tabla_pacientes")
app.add_page(buscar_paciente,"/buscar_paciente")

#Paginas menu donantes

app.add_page(cargar_donante,"/cargar_donante")
app.add_page(eliminar_donante,"/eliminar_donante")
app.add_page(mostrar_tabla_donantes,"/mostrar_tabla_donantes")
app.add_page(buscar_donante,"/buscar_donante")




