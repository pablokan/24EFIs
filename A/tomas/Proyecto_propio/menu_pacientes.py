import reflex as rx
from .backend import *

def menu_pacientes():
    page = rx.box(
                rx.vstack(
                    rx.heading("Menu Pacientes"),
                    rx.link(
                        rx.button("Cargar Paciente",size="4",border="solid 2px black"),
                        href = "/cargar_paciente"
                    ),
                    rx.link(
                        rx.button("Eliminar Pacientes",size="4",border="solid 2px black"),
                        href="/eliminar_paciente"
                    ),
                    rx.link(
                        rx.button("Ver lista paciente",size="4",border="solid 2px black"),
                        href="/mostrar_tabla_pacientes"
                    ),
                    rx.link(
                        rx.button("Buscar Paciente",size="4",border="solid 2px black"),
                        href="/buscar_paciente"
                    ),
                    rx.link(
                        rx.button("Volver",size="4",border="solid 2px black"),
                        href="/"
                    ),
                ),
                padding="20px",
                background="lightblue",
                height="100vh"
    )
    return page

def cargar_paciente():
    page = rx.box(
            rx.vstack(
                rx.heading("CARGAR PACIENTES"),
                rx.input(border="solid 2px grey",placeholder = "Nombre",on_blur=Base_datos.set_nombre),
                rx.input(border="solid 2px grey",placeholder = "Apellido",on_blur=Base_datos.set_apellido),
                rx.input(border="solid 2px grey",placeholder = "Telefono",on_blur=Base_datos.set_telefono),
                rx.input(border="solid 2px grey",placeholder = "Grupo Sanguineo",on_blur=Base_datos.set_sangre),
                rx.input(border="solid 2px grey",placeholder = "Organo en busqueda",on_blur=Base_datos.set_organo),  
                rx.button("Cargar", on_click=lambda: Base_datos.cargar_pacientes(
                                                Base_datos.nombre,                            
                                                Base_datos.apellido,
                                                Base_datos.telefono,
                                                Base_datos.sangre,
                                                Base_datos.organo,
                                            ),
                size="4",border="solid 2px black"),
                rx.text("Mensaje de Salida: ",
                    Base_datos.mensaje_salida_carga_paciente),
                rx.link(
                    rx.button("Volver",size="4",border="solid 2px black"),
                    href=("/menu_pacientes")
                ),
            ),
            padding="20px",
            background="lightblue",
            height="100vh"
    ) 
    return page

def eliminar_paciente():
    page = rx.box(
            rx.vstack(
                rx.heading("ELIMINAR PACIENTE"),
                rx.text("Eliminar paciente por el ID",size="5"),
                rx.input(border="solid 2px grey",placeholder="ID del paciente",on_blur=Base_datos.set_id),
                rx.button("Eliminar",size="4",border="solid 2px black",on_click=lambda:Base_datos.eliminar_paciente(
                                                    Base_datos.id,                                            
                    ),
                ),
                rx.text("Mensaje de salida: ",Base_datos.mensaje_salida_eliminacion_paciente, size="4"),
                                rx.link(
                    rx.button("Volver", size="4",border="solid 2px black"),
                    href=("/menu_pacientes")
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

def mostrar_tabla_pacientes():
    page = rx.box(
                rx.vstack(
                    rx.heading("REGISTROS PACIENTES"),
                    rx.link(
                        rx.button("Volver", size="4", border="solid 2px black"),
                        href=("/menu_pacientes")
                    ),
                    rx.button("Actualizar Registros", on_click=lambda:Base_datos.mostrar_tabla_pacientes(),size="4", border="solid 2px black"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("ID"),
                                    rx.table.column_header_cell("Nombre"),
                                    rx.table.column_header_cell("Apellido"),
                                    rx.table.column_header_cell("Telefono"),
                                    rx.table.column_header_cell("Grupo Sanguineo"),
                                    rx.table.column_header_cell("Organo en Busqueda"),
                                ),
                            ),
                        rx.table.body(
                            rx.foreach(
                                Base_datos.mensaje_salida_ver_pacientes, mostrarRegistro
                            )
                        )
                        )
                ),
                padding="20px",
                background="lightblue",
                height="100%"
                
    )
    return page

def buscar_paciente():
    page =  rx.box(
                rx.vstack(
                    rx.heading("Buscar Pacientes"),
                    rx.input(placeholder="Organo en Requerimiento",on_blur=Base_datos.set_organo,border="solid 2px grey"),
                    rx.input(placeholder="Grupo Sanguineo",on_blur=Base_datos.set_sangre,border="solid 2px grey"),
                    rx.button("Buscar Paciente", on_click=lambda:Base_datos.buscar_paciente(
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
                                        rx.table.column_header_cell("Busqueda"),
                                ),
                            ),                            
                    rx.table.body(
                            rx.foreach(
                                    Base_datos.mensaje_salida_busqueda_paciente, mostrarRegistro
                                )
                    ),
                   ),
                   
                    rx.link(
                        rx.button("Volver",size="4", border="solid 2px black"),
                        href=("/menu_pacientes")
                    )
                ),
                padding="20px",
                background="lightblue",
                height="100vh"
    )
    return page

