import reflex as rx
from .pages.login import login
from .pages.ticket import ticket
from .pages.estadosTicket import estadosTicket
from .pages.usuariosTicket import usuariosTicket
from .backend.db_estados import TablaEstados
from .backend.db_ticket import TablaTicket
from .backend.db_usuarios import TablaUser



def index() -> rx.Component:
    
    page = (
        login(),
    )
    
    return page


app = rx.App()
app.add_page(index)
app.add_page(login, route="/login")
app.add_page(ticket, route="/ticket", on_load=TablaTicket.obtenerTicket) #los on_load es como el on_mount que se cargan los datos una ves que se renderiz la pagina sirve para mostrar los datos, ademas aca defino las rutas de la secciones de la pagina
app.add_page(estadosTicket, route="/estadosTicket", on_load=TablaEstados.obtenerEstados)
app.add_page(usuariosTicket, route="/usuariosTicket", on_load=TablaUser.obtenerUsuarios)

#el on_mount  sirve para los coponentes individuales y el on_load para los componentes que dependen de paginas como @rx.page