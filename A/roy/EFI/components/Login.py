import reflex as rx
from ..backend.backend import PasswordState
from ..backend.login import Login


def logo():
    return rx.image(
        src="/logo.png",
        width="150px",
        height="auto",
    )

            

def loginContent():
    return rx.flex(
        logo(),
        rx.form.root(
            rx.flex(
                rx.form.field(
                    rx.input(
                        rx.input.slot(
                            rx.icon("user", color="#46A758", size=30),
                        ),
                        placeholder="Email",
                        background="transparent",
                        border="1px solid #50575f",
                        height="2.5rem",
                        width="20rem",
                        style={
                            "outline-color": "#46A758",
                            "& input::placeholder": {
                                "color": "#50575f", 
                            },
                            "& input": {
                                "color": "#fff",  
                            },
                        },
                        type="email",
                        name="email",
                    ),
                ),
                rx.form.field(
                    rx.input(
                        rx.input.slot(
                            rx.icon("lock", color="#46A758", size=30),
                        ),
                        rx.input.slot(
                            rx.button(
                                rx.icon("eye", color="#46A758", size=30),
                                background_color="transparent",
                                cursor="pointer",
                                on_click=PasswordState.verContraseña,  # agregamos el evento al boton para cambiar el estado del input type password
                                type="button",
                            ),
                        ),
                        placeholder="Contraseña",
                        width="20rem",
                        height="2.5rem",
                        background="transparent",
                        border="1px solid #50575f",
                        style={
                            "outline-color": "#46A758",
                            "& input::placeholder": {
                                "color": "#50575f", 
                            },
                            "& input": {
                                "color": "#fff",  
                            },
                        },
                        type=rx.cond(
                            PasswordState.verPassword,  # Hacemos una condicion para ver la contraseña, si es verdadero se pone texto y si no password
                            "text",
                            "password",
                        ),
                        name="contraseña",
                    ),
                ),
                rx.cond(
                    Login.esValido,
                    rx.text(""),
                    rx.text("Usuario no valido", color="red"),
                ),
                rx.form.submit(
                    rx.button(
                        "Iniciar Sesión",
                        type="submit",
                        background_color="#46A758",
                    ),
                    as_child=True
                ),
                direction="column",
                spacing="5",
            ),
            on_submit=Login.obtener_dato_login, #mando los datos que pone el usuario en los campos para hacer las validaciones
            reset_on_submit=True,
        ),
        background_color="#232629",
        justify="center",
        align="center",
        direction="column",
        border_radius="10px",
        border="1px solid #46A758",
        padding="1rem",
    )
