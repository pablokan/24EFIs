import reflex as rx


def badge(icon: str, text: str, color_scheme: str):
    return rx.badge(
        rx.icon(icon, size=16), #aca le pongo el icono al estado
        text, #muestro lel valor del estado
        color_scheme=color_scheme, #aca asigno el color que tiene que ir
        radius="full", 
        variant="soft",
        size="3",
    )

def statuBadge(status: str): #cadena de texto actual que tiene el estadoo
    return rx.match( #con esto manejo las multipls condiciones 
        status,
        ("Iniciado", badge("loader", "Iniciado", "blue")),
        ("En Proceso", badge("clock", "En Proceso", "yellow")),
        ("Finalizado", badge("check", "Finalizado", "green")),
        badge("loader", status, "gray")  # caso por defecto si no cunmpllo las otras condiciones
    )
    
#aca se recibe los aprametro lo uso para darle estilos a los badges de los estados