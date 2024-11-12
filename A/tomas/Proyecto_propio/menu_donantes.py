import reflex as rx
from .backend import *

def menu_donantes():
    page = rx.box(
            rx.vstack(
                    rx.heading("Menu Donantes"),
                    rx.link(
                        rx.button("Cargar Donante", size="4", border="solid 2px black"),
                        href = "/cargar_donante"
                    ),
                    rx.link(
                        rx.button("Eliminar Donante",size="4", border="solid 2px black"),
                        href="/eliminar_donante"
                    ),
                    rx.link(
                        rx.button("Ver lista Donante",size="4", border="solid 2px black"),
                        href="/mostrar_tabla_donantes"
                    ),
                    rx.link(
                        rx.button("Buscar Donante",size="4", border="solid 2px black"),
                        href="/buscar_donante"
                    ),
                    rx.link(
                        rx.button("Volver",size="4", border="solid 2px black"),
                        href="/"
                    ),
                ),
                padding="20px",
                background="lightblue",
                height="100vh"
    )
    return page

def cargar_donante():
    page = rx.box(
            rx.vstack(
                rx.heading("CARGAR DONANTE"),
                rx.input(border="solid 2px grey",placeholder = "Nombre",on_blur=Base_datos.set_nombre),
                rx.input(border="solid 2px grey",placeholder = "Apellido: ",on_blur=Base_datos.set_apellido),
                rx.input(border="solid 2px grey",placeholder = "Telefono: ",on_blur=Base_datos.set_telefono),
                rx.input(border="solid 2px grey",placeholder = "Grupo SAnguineo: ",on_blur=Base_datos.set_sangre),
                rx.input(border="solid 2px grey",placeholder = "Organno en Donacion: ",on_blur=Base_datos.set_organo),  
                rx.button("Cargar", on_click=lambda: Base_datos.cargar_donantes(
                                                Base_datos.nombre,                            
                                                Base_datos.apellido,
                                                Base_datos.telefono,
                                                Base_datos.sangre,
                                                Base_datos.organo,
                                            ),
                size="4",border="solid 2px black"),
                rx.text("Mensaje de salida: ",
                    Base_datos.mensaje_salida_carga_donantes),
                rx.link(
                    rx.button("Volver",size="4",border="solid 2px black"),
                    href=("/menu_donantes")
                ),
            ),
            padding="20px",
            background="lightblue",
            height="100vh"
    ) 
    return page

def eliminar_donante():
    page = rx.box(
            rx.vstack(
                rx.heading("ELIMINAR DONANTE"),
                rx.text("Eliminar donante por el ID",size="5"),
                rx.input(border="solid 2px grey",placeholder="ID del Donante",on_blur=Base_datos.set_id),
                rx.button("Eliminar",size="4",border="solid 2px black", on_click=lambda:Base_datos.eliminar_donante(
                                                    Base_datos.id,                                            
                    ),
                ),
                rx.text("Mensaje de salida: ",Base_datos.mensaje_salida_eliminacion_donante,size="4"),
                                rx.link(
                    rx.button("Volver",size="4",border="solid 2px black"),
                    href=("/menu_donantes")
                ),
            ),
            padding="20px",
            background="lightblue",
            height="100vh"
    )
    return page


def mostrarRegistro(record: list):
    records = rx.table.row(
            rx.foreach(
                record,
                lambda x: rx.table.cell(x),
            ),
    )
    return records

def mostrar_tabla_donantes():
    page = rx.box(
                rx.vstack(
                    rx.heading("REGISTROS DONANTES"),
                    rx.link(
                        rx.button("Volver",size="4", border="solid 2px black"),
                        href=("/menu_donantes")
                    ),
                    rx.button("Actualizar Registros", on_click=lambda:Base_datos.mostrar_tabla_donantes(),size="4", border="solid 2px black"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("ID"),
                                    rx.table.column_header_cell("Nombre"),
                                    rx.table.column_header_cell("Apellido"),
                                    rx.table.column_header_cell("Telefono"),
                                    rx.table.column_header_cell("Grupo SAnguineo"),
                                    rx.table.column_header_cell("Organo en Donacion"),
                                ),
                            ),
                        rx.table.body(
                            rx.foreach(
                                Base_datos.mensaje_salida_ver_donantes, mostrarRegistro
                            ),
                        ),
                        ),
                ),
                padding="20px",
                background="lightblue",
                height="100%"
                
    )
    return page

def buscar_donante():
    page =  rx.box(
                rx.vstack(
                    rx.heading("Buscar Donante"),
                    rx.input(placeholder="Organo en Donacion",on_blur=Base_datos.set_organo,border="solid 2px grey"),
                    rx.input(placeholder="Grupo Sanguineo",on_blur=Base_datos.set_sangre,border="solid 2px grey"),
                    rx.button("Buscar Paciente", on_click=lambda:Base_datos.buscar_donante(
                                                            Base_datos.organo,
                                                            Base_datos.sangre),
                              size="4", border="solid 2px black"
                            ),
                    
                   rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                        rx.table.column_header_cell("Nombre"),
                                        rx.table.column_header_cell("Apellido"),
                                        rx.table.column_header_cell("Telefono"),
                                        rx.table.column_header_cell("Grupo Sanguineo"),
                                        rx.table.column_header_cell("Donacion"),
                                ),
                            ),                            
                    
                    rx.table.body(
                            rx.foreach(
                                    Base_datos.mensaje_salida_busqueda_donante, mostrarRegistro
                                )
                    ),
                   ),
                    rx.link(
                        rx.button("Volver",size="4", border="solid 2px black"),
                        href=("/menu_donantes")
                    )
                ),
                padding="20px",
                background="lightblue",
                height="100vh"
    )
    return page
