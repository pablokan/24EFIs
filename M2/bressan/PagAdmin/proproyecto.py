import reflex as rx
from proproyecto.cruddb import Crud

class EditDataButton(rx.State):
    #con lista
    componente: list
    
    def asignar_datos(self, currvalue):
        self.componente = currvalue
        print(f": {self.componente}")
    
    def change_tipo(self, value):
        self.componente[1]=value
        print(f"nueva lista: {self.componente} ")
    
    def change_nombre(self, value):
        self.componente[2] = value
        print(f"nueva lista: {self.componente} ")
    
    def change_socket(self, value):
        self.componente[3] = value
        print(f"nueva lista: {self.componente} ")
    
    def change_stock(self, value):
        self.componente[4] = value
        print(f"nueva lista: {self.componente} ")
    
    def change_descripcion(self, value):
        self.componente[5] = value
        print(f"nueva lista: {self.componente} ")
    
    def change_precio(self, value):
        self.componente[6] = value
        print(f"nueva lista: {self.componente} ")
    
    def change_enlace(self, value):
        self.componente[7] = value
        print(f"nueva lista: {self.componente} ")
    
    def cambiar_db(self):
        Crud.modificar(self.componente[0], self.componente[1], self.componente[2], self.componente[3], self.componente[4], self.componente[5], self.componente[6], self.componente[7])
        TableForEachState.get_data()

     
#acumuladores y diccionario agregar datos
class AddDataButton (rx.State):
    #acumuladores
    tipo: str = ""
    nombre: str = ""
    socket: str = ""
    stock:  int = 0
    descripcion: str = ""
    precio: float = 0.0
    enlace: str = ""
    w: list[str] = []
    #print("valores en selectaste")
    #print(print(f"Tipo: {tipo}, Nombre: {nombre}, Socket: {socket}, Stock: {stock}, Descripcion: {descripcion}, Precio: {precio}, Enlace: {enlace}"))
    #print("valores de w")
    #print(f"valores de w: {w}")

    def change_tipo (self, valor: str):
        self.tipo = valor
        self.w = self.condition_stock(self.tipo)

    def change_nombre (self,valor):
        self.nombre = valor

    def change_socket (self,valor):
        self.socket = valor

    def change_stock (self,valor):
        self.stock = valor

    def change_descripcion (self,valor):
        self.descripcion = valor

    def change_precio (self,valor):
        self.precio = valor

    def change_enlace (self,valor):
        self.enlace = valor

    #diccionario
    def condition_stock(self,  valor):
        dsocket = {
            "RAM": ["DDR3", "DDR4"],
            "CPU": ["AMD", "INTEL"],
            "Almacenamiento": ["SSD", "HDD"],
            "GPU": ["AMD", "NVIDIA"],
            "Fuente": ["all"],
            "Gabinete": ["all"],
            "Motherboard": ["all"]
        }
        opt = self.tipo
        lista = dsocket.get(opt, [])
        return lista
    
    #agregar datos a bd
    def add_button(self):
        tipo = self.tipo
        nombre = self.nombre
        socket = self.socket
        stock = self.stock
        descripcion = self.descripcion
        precio = self.precio
        enlace = self.enlace
        print("Valores a agregar:")
        print(f"Tipo: {tipo}, Nombre: {nombre}, Socket: {socket}, Stock: {stock}, Descripcion: {descripcion}, Precio: {precio}, Enlace: {enlace}")
    
        stock = int(stock)  # si o si entero
        precio = float(precio)  # si o si un float
        #Crud.agregar(tipo, nombre, compatibilidad_socket, stock, descripcion, precio, enlace)
        Crud.agregar(tipo, nombre, socket, stock, descripcion, precio, enlace)
        TableForEachState.get_data()


#operaciones Base de datos/tabla
class TableForEachState(rx.State):
    items: list[list] = []

    #obtener lista para monstrar
    def get_data(self):
        self.items = Crud.listar()

    # borrar datos x id
    def delete_buton(self, component_id):
        Crud.eliminar(component_id)
        self.get_data()
    
    
#Obtener datos de bd y ponerlo en tabla/boton editar y eliminar
def table_content(item: list):
    item_pos=item[0]
    #mostrar objetos en la lista por posicion
    return rx.table.row(
        rx.table.cell(item[0]),  # ID
        rx.table.cell(item[1]),  # Tipo
        rx.table.cell(item[2]),  # Nombre
        rx.table.cell(item[3]),  # Socket
        rx.table.cell(item[4]),  # Stock
        rx.table.cell(item[5]),  # Descripcion
        rx.table.cell(item[6]),  # Precio
        rx.table.cell(item[7]),  # Enlace/Foto
        #celda botones
        rx.table.cell(
            rx.hstack(
                rx.dialog.root(
                    #trigger desplegable
                    rx.dialog.trigger(
                        rx.button(
                            "Editar",
                            on_click= lambda: EditDataButton.asignar_datos(item),
                        ),
                    ),
                    rx.dialog.content(
                        rx.dialog.title("Editar entrada"),
                        rx.dialog.description("Solo ingrese los valores que quiere editar"),
                        rx.form(
                            rx.input(
                                placeholder="Tipo",
                                on_change=EditDataButton.change_tipo,
                            ),
                            rx.input(
                                placeholder="Nombre",
                                on_change=EditDataButton.change_nombre,
                            ),
                            rx.input(
                                placeholder="Socket",
                                on_change=EditDataButton.change_socket,
                            ),
                            rx.input(
                                placeholder="Stock",
                                on_change=EditDataButton.change_stock,
                                type="number",
                            ),
                            rx.input(
                                placeholder="Descripcion",
                                on_change=EditDataButton.change_descripcion,
                            ),
                            rx.input(
                                placeholder="Precio",
                                on_change=EditDataButton.change_precio,
                                type="number",
                            ),
                            rx.input(
                                placeholder="Enlace",
                                on_change=EditDataButton.change_enlace,
                            ),
                        ),
                        rx.flex(
                            rx.dialog.close(
                                rx.button(
                                    "Aceptar",
                                    on_click= lambda : EditDataButton.cambiar_db(),
                                ),
                            ),
                        ),
                    ),
                ),
                #boton eliminar
                rx.dialog.root(
                    #trigger desplegable
                    rx.dialog.trigger(
                        rx.button(
                            "Eliminar",
                            color_scheme="red",
                            radius="full",
                        )
                    ),
                    #desplegable confirmar eliminar
                    rx.dialog.content(
                        rx.dialog.title("Confirmar Eliminacion"),
                        rx.dialog.description("Esta seguro que desea eliminar la entrada?. La eliminacion sera permanente"),
                        rx.dialog.close(
                            rx.button(
                                "ACEPTAR",
                                on_click=lambda:TableForEachState.delete_buton(item_pos),
                            ),
                        ),

                    ),

                ),
            ),
        ),
    )


#Front
@rx.page(on_load=TableForEachState.get_data)
#actualizar pagina al iniciar
def index():
    return rx.vstack( 
        rx.table.root(
            #titulos de cada  columna
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("ID"),
                    rx.table.column_header_cell("Tipo"),
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell("Socket"),
                    rx.table.column_header_cell("Stock"),
                    rx.table.column_header_cell("Descripcion"),
                    rx.table.column_header_cell("Precio"),
                    rx.table.column_header_cell("Enlace"),
                    rx.table.column_header_cell("Botones"),
                ),
            ),
            #contenido de la tabla
            rx.table.body(
                rx.foreach(
                    TableForEachState.items, table_content
                ),
            ),
            width="100%",
        ),
        rx.dialog.root(
            #(trigger menu desplegable) boton  para agregar componente
            rx.dialog.trigger(
                rx.button(
                    "+ Agregar Componente" 
                ),        
            ),
        #contenido menu desplegable
        rx.dialog.content(
            #titulo
            rx.dialog.title(
                "Agregar Nuevo Producto"
            ),
            #descripcion
            rx.dialog.description(
                "Ingrese  los datos del producto rellenando todos los campos"
            ),
            #casillas rellenar y botones
            rx.form(
                rx.flex(
                    #select tipo
                    rx.select(
                        ["RAM","CPU","Almacenamiento","GPU","Fuente","Gabinete","Motherboard"],
                        placeholder="Tipo de producto",
                        color_scheme="blue",
                        #value=AddDataButton.tipo,
                        on_change=AddDataButton.change_tipo,
                        required= True,
                    ),
                    #input nombre
                    rx.input(
                        placeholder="Nombre del producto",
                        value=AddDataButton.nombre,
                        on_change=AddDataButton.change_nombre,
                        required=True,
                    ),
                    #select socket
                    rx.select(
                        AddDataButton.w,
                        placeholder="tipo de socket",
                        color_scheme="blue",
                        value=AddDataButton.socket,
                        on_change=AddDataButton.change_socket,
                        required=True
                    ),
                    #input stock
                    rx.input(
                        placeholder="Cant. en Stock",
                        value=AddDataButton.stock,
                        on_change=AddDataButton.change_stock,
                        required=True,
                        type="number",
                    ),
                    #input descripcion
                    rx.input(
                        placeholder="Descripción del producto",
                        value=AddDataButton.descripcion,
                        on_change=AddDataButton.change_descripcion,
                    ),
                    #input precio
                    rx.input(
                        type="number",
                        placeholder="Precio del producto",
                        value=AddDataButton.precio,
                        on_change=AddDataButton.change_precio,
                    ),
                    #input link,foto
                    rx.input(
                        placeholder="Link de la foto",
                        value=AddDataButton.enlace,
                        on_change=AddDataButton.change_enlace,
                    ),
                    #Boton Aceptar
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Aceptar",
                                #funcionalidad aceptar
                                on_click=AddDataButton.add_button
                            ),
                        ),
                    #Boton Cancelar
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                #Funcionalidad cancelar
                            ),
                        ),
                    ),
                    ),
                    direction="column",
                ), 
            ),
            rx.badge(f"Tipo:{AddDataButton.tipo}"),
            rx.badge(f"Nombre: {AddDataButton.nombre}"),
            rx.badge(f"Socket: {AddDataButton.socket}"),
            rx.badge(f"Stock: {AddDataButton.stock}"),
            rx.badge(f"Descripcion: {AddDataButton.descripcion}"),
            rx.badge(f"Precio: {AddDataButton.precio}"),
            rx.badge(f"Enlace: {AddDataButton.enlace}"),
            #max_width="450px"
        )
        #TableForEachState.add_dialog()


        ),
    )

app = rx.App()
app.add_page(index)