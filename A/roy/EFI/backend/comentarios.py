import reflex as rx 
from datetime import datetime 

class Comentarios(rx.State):
    comentario: str = ""
    form_data: dict = {}
    listaDeComentarios: list[tuple[str, str]] = []
    
    def obtenerComentario(self, form_data: dict): #aca obtenemos el comentario que el admin puso en el campo de texto lo guardamos en form_data despues lo pasamos a comentario, despues sacamos la fecha de hoy la formatemaos y lo almacenamos en una lista para que podamos hacer un foreach sobre ella
        self.form_data = form_data
        self.comentario = self.form_data["comentario"]
        ahora = datetime.now()
        formateado = ahora.strftime("%d/%m/%Y - %H:%M")
        self.listaDeComentarios.append((self.comentario, formateado))