import reflex as rx
from .formulario import form_field
from .clientes_db import(
    seleccionar_cliente,seleccionar_todos,borrar_cliente,
    modificar_cliente,insertar_cliente,crear_tabla
)

# Crear tabla
crear_tabla()

# Clase Cliente 
class Cliente(rx.Model,table=True):
    nombre: str
    email: str
    telefono: str
    direccion: str
    fecha: str
    horario: str

# Estados y eventos
class State(rx.State):
    # Lista de Clientes
    users: list[Cliente] = []
    # Valor al buscar 
    search_value: str = ""
    # Cliente seleccionado
    cliente_actual: Cliente = Cliente()

    # Cargar todos los clientes de la base de datos
    def cargar_datos(self):
        # Obtiene todos los clientes de la base de datos, aplicando filtros de búsqueda si es necesario.
        all_users = seleccionar_todos()

        # Filtrar la lista de usuarios si hay un valor de búsqueda
        if self.search_value:
            search_value = self.search_value.lower()
            filtered_users = [
                user for user in all_users 
                if search_value in user.nombre.lower()
                or search_value in user.email.lower()
                or search_value in user.telefono.lower()
                or search_value in user.direccion.lower()
            ]
            self.users = filtered_users
        else:
            self.users = all_users

    # Guardar valor de busqueda 
    def filtrar_valores(self, search_value):
        # Actualizar el valor de búsqueda y cargar clientes filtrados
        self.search_value = search_value
        self.cargar_datos()

    # Agregar cliente con datos del formulario
    def agregar_cliente(self, form_data):
        # Fecha y horario del formulario
        fecha = form_data["date"]
        horario = form_data["time"]

        # Verificar si ya existe un cliente con la misma fecha y horario
        all_users = seleccionar_todos()
        for user in all_users:
            if user.fecha == fecha and user.horario == horario:
                # Mostrar mensaje de error
                return rx.toast.error("El horario ya está ocupado. Por favor elige otro.", position="bottom-right")
        
        # Si no hay conflictos, inserta el cliente
        insertar_cliente(
            form_data["name"], form_data["email"], form_data["phone"],
            form_data["address"], form_data["date"],form_data["time"]
        )
        # Cargar datos de los clientes
        self.cargar_datos()
        
        # Avisar que el cliente ha sido agregado
        return rx.toast.info(f"El cliente {form_data['name']} ha sido agregado.", position="bottom-right")

    # Seleccionar cliente y guardarlo 
    def obtener_cliente(self,user_id):
        self.cliente_actual = seleccionar_cliente(user_id)
    
    # Acceder a un cliente y borrarlo por medio de su ID
    def eliminar_cliente(self, user_id):
        borrar_cliente(user_id)
        # Cargar datos de los clientes 
        self.cargar_datos()
        # Avisar que el usuario fue eliminado
        return rx.toast.info("El usuario ha sido eliminado.", position="bottom-right") 

    # Modificar cliente mediante su ID 
    def actualizar_cliente(self,form_data):
        print(self.cliente_actual)
        c = self.cliente_actual
        user_id = c[0]
        #modificar_cliente(
        #    user_id , form_data["name"], form_data["email"], 
        #    form_data["phone"], form_data["address"], form_data["date"], form_data["time"]
        #)
        modificar_cliente(c[0], c[1], c[2], c[3], c[4])


        # Cargar datos 
        self.cargar_datos()

# Mostrar datos de un Cliente en una columna 
def show_person(user: Cliente):
    # Tabla completa 
    table_row = rx.table.row(
        # Celdas con datos del cliente 
        rx.table.cell(user.nombre,
                    font_size = "14px",
                    auto_capitalize=True),
        rx.table.cell(user.email,
                      font_size= "14px",
                      _hover ={"text_decoration_line":
                               "underline"
                               },
                      weight="medium"),
        rx.table.cell(user.telefono,
                      weight="medium"),
        rx.table.cell(user.direccion,
                      weight="medium"),
        rx.table.cell(user.fecha,
                      weight="medium"),
        rx.table.cell(user.horario,
                      weight="medium"),
        rx.table.cell(
            rx.hstack(# Boton para editar datos del cliente
            update_customer_dialog(user),
            # Boton para borrar el cliente
            rx.button(
                    rx.icon("trash-2"),
                    rx.text("Eliminar"),
                    variant = "soft",
                    color_scheme="red",
                    # Al hacer click, borrar cliente usando la ID 
                    on_click=lambda: State.eliminar_cliente(user.id)),
            ),
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )
    return table_row

# Boton para agregar cliente a la tabla y a la base de datos
def add_customer_button() -> rx.Component:
    add_customer = rx.dialog.root(
        rx.dialog.trigger(
            # Boton para gregar al cliente con icono "+" 
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Agregar cliente", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        # Dialogo superior del formulario
        rx.dialog.content(
            rx.hstack(
                # Icono de usuario
                rx.badge(
                    rx.icon(tag="users", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    # Titulo del formulario
                    rx.dialog.title(
                        "Agregar nuevo cliente",
                        weight="bold",
                        margin="0",
                    ),
                    # Subtitulo del formulario 
                    rx.dialog.description(
                        "Llene el formulario con los datos del cliente",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                # Campos del formulario
                rx.form.root(
                    rx.flex(
                        # Espacio para nombre 
                        form_field(
                            "Nombre",
                            "Nombre del cliente",
                            "text",
                            "name",
                            "user",
                        ),
                        # Espacio para email
                        form_field(
                            "Email",
                            "ejemplo@gmail.com", 
                            "email", 
                            "email", 
                            "mail"
                        ),
                        # Espacio para telefono
                        form_field(
                            "Telefono",
                            "Telefono", 
                            "tel", 
                            "phone", 
                            "phone"),
                        # Espacio para direccion 
                        form_field(
                            "Direccion", 
                            "Direccion", 
                            "text", 
                            "address", 
                            "home"
                        ),
                        form_field(
                            "Fecha",
                            "dd/mm/yyyy",
                            "date",
                            "date",
                            "calendar",
                        ),
                        form_field(
                            "Horario",
                            "",
                            "time",
                            "time",
                            "alarm_clock",
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        # Cerrar el formulario al tocar el boton "Cancelar"
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        # Enviar datos del formulario al tocar el boton "Agregar"
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Agregar"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    # EVENT HANDLER
                    # Agregar el cliente a la base de datos 
                    on_submit=State.agregar_cliente,
                    reset_on_submit=False, 
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )
    return add_customer

# Formulario para editar datos de un cliente
def update_customer_dialog(user: Cliente):
    update_customer = rx.dialog.root(
        rx.dialog.trigger(
            # Boton que abre el formulario
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Edit", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
                # Al hacer click, obtener cliente
                on_click=lambda: State.obtener_cliente(user.id),
            ),
        ),
        # Dialogo e icono superior del formulario
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    # Titulo
                    rx.dialog.title(
                        "Editar cliente",
                        weight="bold",
                        margin="0",
                    ),
                    # Descripcion
                    rx.dialog.description(
                        "Edita la informacion del cliente ",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Espacio para nombre
                        form_field(
                            "Nombre",
                            "Nombre del cliente",
                            "text",
                            "nombre",
                            "user",
                            # Nombre del usuario 
                            user.nombre,
                        ),
                        # Espacio para email
                        form_field(
                            "Email",
                            "cliente@reflex.dev",
                            "email",
                            "email",
                            "mail",
                            # Email del usuario
                           user.email,
                        ),
                        # Telefono
                        form_field(
                            "Telefono",
                            "Telefono del cliente",
                            "tel",
                            "telefono",
                            "phone",
                            # Telefono del usuario
                            user.telefono,
                        ),
                        # Direccion
                        form_field(
                            "Direccion",
                            "Direccion del cliente",
                            "text",
                            "direccion",
                            "home",
                            # Direccion del usuario
                            user.direccion,
                        ),
                        # Fecha 
                        form_field(
                            "Fecha",
                            "dd/mm/yyyy",
                            "date",
                            "direccion",
                            "calendar",
                            # Fecha del usuario
                            user.fecha,
                        ),
                        # Horario
                        form_field(
                            "Horario",
                            "",
                            "time",
                            "hora",
                            "alarm_clock",
                            # Horario del usuario
                            user.horario,
                        ),                        
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        # Cerrar formulario al tocar el boton "Cancelar"
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        # Boton para enviar los datos del formulario
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Agregar cliente"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    # Al mandar los datos, llamar funcion modificar cliente
                    on_submit = State.actualizar_cliente,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )
    return update_customer


def main_table():
    # Contiene la tabla, el botón de agregar cliente y el buscador
    table = rx.fragment(
        rx.flex(
            # Boton de agregar cliente
            add_customer_button(),
            rx.spacer(),
            # Buscador 
            rx.input(
                rx.input.slot(rx.icon("Search")),
                placeholder="Busque aqui...", # Valor por defecto
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                # Al escribir, llamar funcion filtrar_valores
                on_change=lambda value: State.filtrar_valores(value),
                ),
                justify="end",
                align="center",
                spacing="3",
                wrap="wrap",
                width="100%",
                padding_bottom="1em",
                ),        
        # Componente principal de la tabla
        rx.table.root(
            # Encabezado de la tabla
            rx.table.header(
                rx.table.row(
                    # Titulo de cada columna 
                    rx.foreach(
                        ["Nombre", "Email", "Telefono", "Direccion", "Fecha", "Horario"],
                        lambda title: rx.table.column_header_cell(
                            rx.text(title, fontsize="12px", weight="bold")
                        ),
                    ),
                ),
            ),
            # Cuerpo de la tabla
            rx.table.body(
                rx.foreach(State.users, show_person),
            ),
            width = "100%",
            variant = "surface",
            # Al cargar la tabla, cargar datos de clientes
            on_mount=State.cargar_datos
        ),
            width="100%",
            height = "100vh",
            padding = "2em",
    )
    return table
