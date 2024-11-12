import reflex as rx
from .tablero import * # Importa back-end gestion del tablero

@rx.page(on_load=Tablero.resetear()) # Declarada como metodo para poder resetear los contadores al recargar la pagina (reinicia el juego)
def game() -> rx.Component:
    page = rx.aspect_ratio( # Aspect ratio para mantener relacion 16:9
        rx.flex(
           # HEADER
           rx.heading(
               'Preguntados v0.1',
               width='100%',
               align='center',
               size='10',
               ),
        align='center',
        width='100%',
        height='10%',
        border='solid',
        border_radius='10px',
        margin_bottom='1em',
        ),
        rx.flex(
            # BOTON
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button("SIGUIENTE TURNO", color_scheme="green", on_click=lambda: Tablero.cargar_pregunta(), size='4'),  #despues del onclik se mustra la pantalla con preguntas y respuestas
                ),
                rx.dialog.content(
                    rx.dialog.title(Tablero.pregunta), #pone la pregunta como titulo
                    rx.box(
                        #usa rx.foreach para crear un boton con cada una de las respuestas
                        rx.foreach( #recorre la lista de respuestas y crea un boton con cada una
                            Tablero.respuestas, 
                            lambda respuesta: rx.button( 
                                respuesta["texto"], 
                                color_scheme=Tablero.color_boton,
                                on_click=lambda: Tablero.verificar_respuesta(respuesta["texto"]),
                            )
                        ),
                        display="flex",
                        flex_direction="column",
                        gap="10px"
                    ),
                    rx.flex(
                        rx.text(Tablero.respuesta,align='center',margin='1em'),
                        rx.dialog.close(
                            rx.button("Continuar", variant='soft',color_scheme="gray",on_click=Tablero.calcularGanador()), #boton para cerrar el cartel donde aparece la pregunta y la respuesta
                        ),
                        spacing="3",
                        justify="center",
                        flex_direction='column',
                    ),
                    style={"max_width": 500},
                ),
                on_open_change=Tablero.calcularGanador()
            ),
            align='center',
            justify="center",
           ),

        rx.flex(  
           # BODY
            rx.box(
               # JUGADOR 1
                rx.heading(
                    Tablero.jug1_nom,
                    font_size='2em', # Se puede reemplazar con Tablero.jug1.nom
                    width='100%',
                    height='10%',
                    align='center',
                    ),
                rx.vstack( # Vertical stack que crea los tableros
                    rx.foreach( # Renderizado dinamico de cada tablero
                        Tablero.jug1.tablero,   # Obtiene la lista 'tablero' (lista de objetos Casilla) y por cada uno renderiza
                        renderizarCasilla,      # Funcion declarada en .tablero que crea objetos cond para renderizar dinamicamente la "ficha" segun en que casilla esta
                        ),
                width='100%',
                height='80%',
                align='center'
                ),
            width='45%',
            height='100%',
            ),
            rx.box(
                rx.center(
                    rx.vstack(
                        rx.heading('Turno',size='8'),
                        rx.cond(
                            Tablero.turno,
                            rx.icon('circle-arrow-left',size=75),
                            rx.icon('circle-arrow-right',size=75),
                        ),
                        justify='center',
                        align='center',
                        width='100%',
                    ),
                height='70%',
                ),
                width='10%',
                height='100%',
            ),
            rx.box(
               # JUGADOR 2
               rx.heading(
                    Tablero.jug2_nom, # Se puede reemplazar con Tablero.jug2.nom
                    font_size='2em',
                    width='100%',
                    height='10%',
                    align='center',
                    ),
                rx.vstack( # Igual jug1
                    rx.foreach( # Igual a jug1
                        Tablero.jug2.tablero,
                        renderizarCasilla,
                    ),
                width='100%',
                height='80%',
                align='center'
                ),
               width='45%',
               height='100%',
            ),
        padding='1em',
        width='100%',
        height='80%',
        border='solid',
        border_radius='10px',
        margin_top='1em',
        ),
        # ALERTA PARA GANADOR
        rx.flex(
            rx.alert_dialog.root(
                rx.alert_dialog.content(
                    rx.vstack(
                        rx.heading('GANADOR', align='center',),
                        rx.text(Tablero.jugGanador, align='center',),
                        rx.center(
                            rx.hstack(
                                rx.alert_dialog.cancel(
                                    rx.button(
                                        'Volver a jugar',
                                        on_click=Tablero.resetear # El boton cancel del alert dialog tambien llama a la funcion que resetea el juego
                                    ),
                                    align='center',
                                    justify='center',
                                ),
                                rx.link(
                                    rx.button('Salir del juego',),
                                    href='/',
                                )
                            ),
                        ),
                    justify='center',
                    align='center',
                    ),
                justify='center',
                align='center',
                ),
                open=Tablero.hayGanador
            ),
        justify='center',
        align='center',
        ),
    width='100%',
    height='100%',
    padding='2em',
    flex_direction='column',
    ratio=16/9,
    ),

    return page