import reflex as rx
import sqlite3

# # ACA VAMOS A HACER LA CONEXION CON LA BASE DE DATOS SOBRE LA TABLA TICKET

# Conexión y obtención de datos de la tabla TICKET.
class TablaTicket(rx.State):
    ticket: list[list[str]] = []

    def obtenerTicket(self):  # Imprime los datos de la tabla ticket
        conn = sqlite3.connect("tickets.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM TICKET")  # Selecciona todos los registros
        # Convierte cada tupla en un diccionario con claves para facilitar el acceso.
        self.ticket =  cursor.fetchall()
        conn.close()
        
        
        
    def agregarTicket(self, form_data: dict):
        asunto = form_data.get("asunto")
        solicitante = form_data.get("solicitante")
        contacto = form_data.get("contacto")
        mensaje = form_data.get("mensaje")
        
        # valor predeterminados para los nuevos tickets
        estado_id = 1
        estado_nombre = "Iniciado"
        
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        
        # agrego los datos en la tabla TICKET
        cursor.execute(
            '''
            INSERT INTO TICKET (ASUNTO, SOLICITANTE, ESTADO_ID, ESTADO_NOMBRE, CONTACTO, MENSAJE)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (asunto, solicitante, estado_id, estado_nombre, contacto, mensaje) #parametros para insertar en la base de datos
        )
        
        conn.commit()
        conn.close()

        # Actualiza la lista de tickets después de agregar uno nuevo
        self.obtenerTicket()

        
        
    def eliminarUsuario(self, id: int):
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM TICKET WHERE ID = ?', (id,)) #selecciono el id en la bse de datos y elimino el selecciionado
        
        conn.commit()
        conn.close()
        
        # Actualizar la lista después de eliminar
        self.obtenerTicket()



    ticketActual: list = [] #temporal para guardar los fdatos del ticket actual
    
    def obtener_ticket(self, ticket: list):
        """Obtiene el ticket seleccionado para editar."""
        self.ticketActual = ticket

    def editarTicket(self, form_data: dict):
        """Edita un ticket en la base de datos, sin cambiar el estado."""
        # obengo el ID del ticket a partir del ticket actual seleccionado
        ticket_id = self.ticketActual[0]  # El ID debe estar en la primera posición de la lista
        

        # Obtiene los datos del formulario
        asunto = form_data.get("asunto")
        solicitante = form_data.get("solicitante")
        contacto = form_data.get("contacto")
        mensaje = form_data.get("mensaje")

        # conecto a la base de datos
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()

        # ejecuto la actualización en la tabla TICKET sin modificar el estado del tickett
        cursor.execute(
            '''
            UPDATE TICKET 
            SET ASUNTO = ?, SOLICITANTE = ?, CONTACTO = ?, MENSAJE = ? 
            WHERE ID = ?
            ''',
            (asunto, solicitante, contacto, mensaje, ticket_id)
        )

        # connfirmo los cambios y cierra la conexión
        conn.commit()
        conn.close()

        # Actualiza la lista de tickets después de la edición
        self.obtenerTicket()