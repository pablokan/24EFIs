import reflex as rx 
import sqlite3
from datetime import datetime
from rxconfig import config
from hospital.funcionesbd import registrarPaciente, realizarConsulta, registrarConsulta, editarPaciente

#Definir el estado de la aplicacion
class State(rx.State):
    dni: str = ""
    nombre: str = ""
    correo: str = ""
    telefono: str = ""
    fNacimiento: str = ""
    pacientes: list[list] = []
    mensaje: str = ""
    consultaResultado: list[tuple] = []
    filtro: str = ""
    #Nuevas propiedades para el registro de consulta
    consulta: str = ""
    peso: float = 0.0
    altura: float = 0.0
    fecha_consulta: str = ""

    @rx.var(cache=True)
    def pacienteActual(self) -> list[list]:
        if self.filtro:
            term = self.filtro.lower()
            return [
                paciente for paciente in self.pacientes
                if term in str(paciente[0]).lower() or
                   term in paciente[1].lower() or
                   term in paciente[2].lower()
            ]
        return self.pacientes
    #Metodo para registrar
    def registrar(self, form_data: dict):
        self.dni = form_data["dni"]
        self.nombre = form_data["nombre"]
        self.correo = form_data["correo"]
        self.telefono = form_data["telefono"]
        self.fNacimiento = form_data["fecha_nacimiento"]

        msg = registrarPaciente(self.dni, self.nombre, self.correo, self.telefono, self.fNacimiento)
        self.mensaje = msg
        self.obtenerRegistros()
    
    #Metodo para editar
    def editar(self, form_data: dict):
        self.dni = form_data["dni"]
        self.nombre = form_data["nombre"]
        self.correo = form_data["correo"]
        self.telefono = form_data["telefono"]
        self.fNacimiento = form_data["fecha_nacimiento"]

        msg = editarPaciente(self.dni, self.nombre, self.correo, self.telefono, self.fNacimiento)
        self.mensaje = "Paciente actualizado" if msg == "Paciente actualizado" else msg
        self.obtenerRegistros()

    @rx.var
    def alert_mensaje(self) -> rx.Component:
        if self.mensaje == "Los datos del paciente ya existen":
            return rx.callout("Los datos del paciente ya existen.", icon="triangle_alert", color_scheme="red", role="alert")
        elif self.mensaje == "Paciente registrado":
            return rx.callout("Paciente registrado con éxito.", icon="check")
        elif self.mensaje == "Paciente actualizado":
            return rx.callout("Paciente actualizado correctamente.", icon="check", color_scheme="green")
        elif self.mensaje == "Consulta registrada":
            return rx.callout("Consulta registrada exitosamente.", icon="check", color_scheme="green")
        return None

    def obtenerRegistros(self):
        conn = sqlite3.connect('dbHospital.db')
        try:
            cursor = conn.execute('SELECT DNI, nombre, correo, telefono, fecha_nacimiento FROM datosp')
            registros = cursor.fetchall()
            self.pacientes = [
                [
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3],
                    datetime.strptime(registro[4], "%Y-%m-%d").strftime("%d-%m-%Y")
                ]
                for registro in registros
            ]
        except Exception as e:
            print(f"Error al obtener registros: {e}")
            self.pacientes = []
        finally:
            conn.close()

    def actualizarTabla(self):
        self.obtenerRegistros()

    def seleccionarFiltro(self, valor):
        self.filtro = valor

    def consultar(self, dni):
        self.consultaResultado = realizarConsulta(dni)

    def registrarNuevaConsulta(self, form_data: dict):
        dni = form_data["dni"]
        consulta = form_data["consulta"]
        peso = form_data["peso"]
        altura = form_data["altura"]
        fecha = form_data["fecha"]

        msg = registrarConsulta(dni, consulta, peso, altura, fecha)
        self.mensaje = msg
        if msg == "Consulta registrada":
            self.set_dni("")
            self.set_consulta("")
            self.set_peso(0.0)
            self.set_altura(0.0)
            self.set_fecha_consulta("")

#Funcion para mostrar los pacientes en la tabla
def mostrarPaciente(paciente):
    return rx.table.row(
        rx.table.cell(paciente[0]),  #DNI
        rx.table.cell(paciente[1]),  #Nombre
        rx.table.cell(paciente[2]),  #Correo
        rx.table.cell(paciente[3]),  #Telefono
        rx.table.cell(paciente[4])   #Fecha de Nacimiento
    )

#Funcion para mostrar el resultado de la consulta
def mostrarResConsulta(resultado):
    return rx.table.row(
        rx.table.cell(resultado[0]),  #Nombre
        rx.table.cell(resultado[1]),  #Consulta
        rx.table.cell(resultado[2]),  #Peso
        rx.table.cell(resultado[3]),   #Altura
        rx.table.cell(resultado[4]),    #Fecha
        rx.table.cell(resultado[5])    #imc
    )
#Definir la interfaz de Reflex
def interfaz():
    return rx.vstack(
        rx.hstack(
            rx.heading("Registro de Pacientes", level=1),
            justify="center",
        ),
        State.alert_mensaje,
        rx.hstack(
            #Dialogo para registrar un paciente
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button("Agregar Paciente", variant="classic", color_scheme="green")
                ),
                rx.dialog.content(
                    rx.dialog.title("Agregar Nuevo Paciente"),
                    rx.dialog.description("Llena el formulario con la informacion del paciente"),
                    rx.form(
                        rx.flex(
                            rx.input(placeholder="DNI", name="dni"),
                            rx.input(placeholder="Nombre", name="nombre"),
                            rx.input(placeholder="Correo", name="correo"),
                            rx.input(placeholder="Telefono", name="telefono"),
                            rx.input(placeholder="Fecha de Nacimiento (YYYY-MM-DD)", name="fecha_nacimiento"),
                            rx.flex(
                                rx.dialog.close(
                                    rx.button("Cancelar", variant="soft", color_scheme="gray"),
                                ),
                                rx.dialog.close(
                                    rx.button("Registrar", type="submit")
                                ),
                                spacing="3",
                                justify="end",
                            ),
                            direction="column",
                            spacing="4",
                        ),
                        on_submit=State.registrar,
                        reset_on_submit=False,
                    ),
                    max_width="450px",
                ),
            ),
            #Dialogo para editar un paciente
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button("Editar Paciente", variant="classic", color_scheme="blue")
                ),
                rx.dialog.content(
                    rx.dialog.title("Editar Paciente"),
                    rx.dialog.description("Modifica los datos del paciente y guarda los cambios"),
                    rx.form(
                        rx.input(placeholder="DNI", name="dni"),
                        rx.input(placeholder="Nombre", name="nombre"),
                        rx.input(placeholder="Correo", name="correo"),
                        rx.input(placeholder="Telefono", name="telefono"),
                        rx.input(placeholder="Fecha de Nacimiento (YYYY-MM-DD)", name="fecha_nacimiento"),
                        rx.flex(
                            rx.dialog.close(rx.button("Cancelar", variant="soft", color_scheme="gray")),
                            rx.dialog.close(rx.button("Guardar Cambios", type="submit")),
                            spacing="3", justify="end",
                        ),
                        on_submit=State.editar,
                    ),
                ),
            ),
            #Dialogo para registrar una consulta
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button("Generar Consulta", variant="classic", color_scheme="red")
                ),
                rx.dialog.content(
                    rx.dialog.title("Registrar Nueva Consulta"),
                    rx.dialog.description("Llena el formulario con la informacion de la consulta"),
                    rx.form(
                        rx.flex(
                            rx.input(placeholder="DNI", name="dni"),
                            rx.input(placeholder="Diagnostico", name="consulta"),
                            rx.input(placeholder="Peso", name="peso"),
                            rx.input(placeholder="Altura", name="altura"),
                            rx.input(placeholder="Fecha (YYYY-MM-DD)", name="fecha"),
                            rx.flex(
                                rx.dialog.close(
                                    rx.button("Cancelar", variant="soft", color_scheme="gray"),
                                ),
                                rx.dialog.close(
                                    rx.button("Registrar Consulta", type="submit")
                                ),
                                spacing="3",
                                justify="end",
                            ),
                            direction="column",
                            spacing="4",
                        ),
                        on_submit=State.registrarNuevaConsulta,
                        reset_on_submit=False,
                    ),
                    max_width="450px",
                ),
            ),
            spacing="4",  #Espacio entre botones
            justify="center",  #Centra los botones
        ),
        #Campo de filtro
        rx.hstack(
            rx.input(
                placeholder="Buscar por DNI, Nombre o Correo",
                value=State.filtro,
                on_change=State.seleccionarFiltro,
                width="300px"
            ),
            justify="center",
        ),
        #Boton para actualizar tabla
        rx.hstack(
            rx.button("Actualizar Tabla", on_click=State.actualizarTabla),
            justify="center",
        ),
        #Campo de consulta
        rx.hstack(
            rx.input(
                placeholder="DNI para consulta",
                value=State.dni,
                on_change=State.set_dni,
                width="200px"
            ),
            rx.button("Consultar", on_click=lambda: State.consultar(State.dni)),
            justify="center",
        ),
        #Contenedor para ambas tablas
        rx.hstack(
            #Tabla de pacientes
            rx.box(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("DNI"),
                            rx.table.column_header_cell("Nombre"),
                            rx.table.column_header_cell("Correo"),
                            rx.table.column_header_cell("Telefono"),
                            rx.table.column_header_cell("Fecha de Nacimiento"),
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(State.pacienteActual, mostrarPaciente),  #Iterar correctamente
                    ),
                ),
                max_height="400px",
                overflow_y="auto",
                width="83%",  #Ancho de la tabla de pacientes
                border="1px solid #ccc",
                padding="10px",
            ),
            #Tabla de resultados de consultas
            rx.box(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Nombre"),
                            rx.table.column_header_cell("Consulta"),
                            rx.table.column_header_cell("Peso"),
                            rx.table.column_header_cell("Altura"),
                            rx.table.column_header_cell("Fecha"),
                            rx.table.column_header_cell("IMC"),
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(State.consultaResultado, mostrarResConsulta),  #Iterar correctamente
                    ),
                ),
                max_height="400px",
                overflow_y="auto",
                width="70%",  #Ancho de la tabla de consultas
                border="1px solid #ccc",
                padding="10px",
            ),
        ),
    )

#Crear la aplicacion
app = rx.App(config=config)
app.add_page(interfaz, route="/")
app()