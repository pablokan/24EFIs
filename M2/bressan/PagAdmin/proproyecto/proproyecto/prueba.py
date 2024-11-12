#acumuladores y diccionario
class SelectState():
    #acumuladores
    tipo = str = "GPU"
    nombre = str = ""
    socket = str = ""
    stock = int = 0
    descripcion = str = ""
    precio = float = 0.0
    enlace = str = ""

    def change_tipo(self, valor):
        self.tipo = valor

    def change_nombre(self, valor):
        self.nombre = valor

    def change_socket(self, valor):
        self.socket = valor

    def change_stock(self, valor):
        self.stock = valor

    def change_descripcion(self, valor):
        self.descripcion = valor

    def change_precio(self, valor):
        self.precio = valor

    def change_enlace(self, valor):
        self.enlace = valor

    # diccionario
    def condition_stock(self):
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
        return dsocket[opt]

select_state = SelectState()

select_state.change_tipo("RAM")

print(select_state.condition_stock())