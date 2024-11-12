import reflex as rx

# Formulario base 
def form_field(
    label: str,  # Etiqueta
    placeholder: str, # Valor que se muestra en el campo sin modificar
    type: str, # Tipo de dato que recibe
    name: str, # Nombre
    icon: str, # Icono
    default_value: str = "", # Valor por defecto
) -> rx.Component:
    # Devolver un componente
    formulario = rx.form.field(
        rx.flex(
            rx.hstack(
                # Parte superior del campo
                rx.icon(icon, size=16, stroke_width=1.5),
                rx.form.label(label),
                align="center",
                spacing="2",
            ),
            # Controlar los valores ingresados segun el tipo
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type, default_value=default_value
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )

    return formulario