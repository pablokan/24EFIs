import reflex as rx
from .database import *
from datetime import datetime, timedelta


class Plataforma(rx.State):
    clicked_data: str = "Celda elegida: "
    datos: list[list] = []
    cabecera: list = []
    contenido: list[list]
    usuario: list[list]
    alquiler: list[list]
    form_data: dict = {}
    tabla_actual: str = "usuarios" 
    nombre_usuario: str
    dni_usuario: str
    nombre_titulo: str
    tipo_titulo: str
    cantidad_dias: int
    importe: float
    usuario_id: int
    contenido_id: int
    mensaje: str
    
    fecha_devolucion: str
    fecha_alquiler: str
    alquiler_id: int
    


    def obtenerDatos(self) -> None:
        db = Database('videostream', self.tabla_actual)
        if self.tabla_actual == 'alquileres':
            self.cabecera = [
            {'title': 'Orden', 'type': 'str'},
            {'title': 'Nombre', 'type': 'str'},
            {'title': 'DNI', 'type': 'str'},
            {'title': 'Título', 'type': 'str'},
            {'title': 'Fecha Alquiler', 'type': 'str'},
            {'title': 'Fecha Devolución', 'type': 'str'},
            {'title': 'Total', 'type': 'str'},
            {'title': 'Estado', 'type': 'str'}
        ]
            recordSet = db.obtener_alquileres_con_detalles()
            self.datos = []
            for registro in recordSet:
                if registro[-1] == 1:
                    estado = "Alquilado" if registro[-1] == 1 else "Disponible" 
                    self.datos.append([str(valor) for valor in registro[:-1]] + [estado])  
        else:
            self.cabecera = [{'title': c, 'type': 'str'} for c in db.fieldNames]
            recordSet = db.get_all()
            self.datos = [[str(valor) for valor in registro] for registro in recordSet]

    def clic_celda(self, pos) -> None:
        self.clicked_data = f"Celda elegida: {pos}"

    def manejarCeldaEditada(self, pos, data) -> None:
        col, row = pos
        nuevoValor = data['data']
        self.datos[row][col] = nuevoValor
        id = self.datos[row][0]
        campoModificado = self.cabecera[col]['title']
        db = Database('videostream', self.tabla_actual)
        db.upd(id, campoModificado, nuevoValor)

    def cambiarTabla(self, tabla: str) -> None:
        self.tabla_actual = tabla
        self.obtenerDatos()  

    def handle_submit(self, form_data: dict, tabla):
        self.form_data = form_data
        if tabla == "usuarios":
            db = Database("videostream", "usuarios")
            print("Datos del formulario:", self.form_data)
            db.insert_usuario(
                form_data.get('nombre'),  
                form_data.get('dni'),
                form_data.get('email'),
                form_data.get('telefono'),
                form_data.get('direccion')
            )
            db.close()
        if tabla == "contenido":
            db = Database("videostream", "contenido")
            print("Datos del formulario:", self.form_data)
            db.insert_contenido(
                form_data.get('titulo'),
                form_data.get('genero'),  
                form_data.get('ano'),
                form_data.get('director'),
                form_data.get('protagonista'),
                form_data.get('tipo_contenido')
            )
            db.close()



    def baja_usuario(self, form_data: dict):
        self.form_data = form_data
        db = Database("videostream", "usuarios")
        db.eliminar_usuario(self.form_data.get("dni"))
        db.close()
 
    def baja_contenido(self, form_data: dict):
        self.form_data = form_data
        db = Database("videostream", "contenidos")
        db.eliminar_contenido(self.form_data.get("titulo"))
        db.close()
    

    def buscar_usuario(self):
        db = Database("videostream", "usuarios")
        self.usuario = db.obtener_datos_usuario_por_dni(self.dni_usuario)  
        if self.usuario:
            usuario = self.usuario[0]
            self.nombre_usuario = usuario[1]
            self.usuario_id = usuario[0]
        else:
            self.nombre_usuario = "Usuario no encontrado"
        db.close()


    def buscar_contenido(self, titulo):
        db = Database("videostream", "contenidos")
        self.contenido = db.buscar_pelicula_por_titulo(titulo) 
        if self.contenido:
            contenido = self.contenido[0]
            self.contenido_id = contenido[0]
            self.nombre_titulo = contenido[1]
            self.tipo_titulo = contenido[-1]
        else:
            self.nombre_titulo = "Contenido no encontrado" 
        db.close()

    
    def calcular_importe(self):
        if self.tipo_titulo and self.cantidad_dias:
            if self.tipo_titulo == 'Película':
                self.importe = self.cantidad_dias * 8.5
            elif self.tipo_titulo == 'Serie':
                self.importe = self.cantidad_dias * 10.3
            else:
                self.importe = self.cantidad_dias * 5.5
        else:
            self.importe = 0


    def alquilar(self):
        db = Database("videostream", "alquileres")
        fecha_hoy = datetime.now()
        fecha_devolucion = fecha_hoy + timedelta(days=self.cantidad_dias)
        fecha_hoy = fecha_hoy.strftime("%Y-%m-%d")
        fecha_devolucion = fecha_devolucion.strftime("%Y-%m-%d") 
        db.insert_alquiler(self.usuario_id, self.dni_usuario, self.contenido_id, fecha_hoy, fecha_devolucion, self.importe, self.tipo_titulo, True)
        db.close()
        self.reiniciar_variables()


    

    def buscar_devolucion(self, dni):
        db = Database("videostream", "alquileres")
        self.alquiler = db.obtener_alquileres_con_detalles()
        if self.alquiler:
            for al in self.alquiler:
                if al[2] == dni and al[-1]:
                    self.alquiler_id = al[0]
                    self.usuario_id = al[1]
                    self.dni_usuario = al[2]
                    self.nombre_titulo = al[3]
                    self.fecha_alquiler = al[4]
                    self.fecha_devolucion = al[5]
                    self.importe = al[6]
                    self.tipo_titulo = al[7]
            fecha_hoy = datetime.now()
            fecha_hoy = fecha_hoy.strftime("%Y-%m-%d")
            if self.fecha_devolucion < fecha_hoy:
                cant_dias = fecha_hoy - self.fecha_devolucion
                importe_aux = self.importe
                importe_extra = self.calcular_importe(cant_dias)
                self.importe = importe_aux + importe_extra       
        else:
            self.nombre_titulo = "No hay alquileres registrados"
        
    def devolucion_alquiler(self):  
        db = Database("videostream", "alquileres")
        db.upd(self.alquiler_id, "alquilado", False)
        db.close()
        self.mensaje = f'Alquiler devuelto correctamente'



    def reiniciar_variables(self):
        self.usuario_id = None
        self.dni_usuario = None
        self.nombre_usuario = None
        self.contenido_id = None
        self.nombre_titulo = None
        self.tipo_titulo = None
        self.cantidad_dias = None
        self.importe = None
        self.contenido = None
        self.importe = 0
        
