import reflex as rx 
from ..components.Login import loginContent

def login():
    return rx.flex(
        loginContent(),
        background="center/cover url('/fondoLogin.png')",
        width="100%",
        height="100vh",
        justify="center",
        align="center",
    )