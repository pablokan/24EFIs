import reflex as rx
from .tablero import Tablero

def index() -> rx.Component:
    index = rx.aspect_ratio(
        rx.flex(        
            rx.card(
                # HEADER
                rx.flex(
                    rx.heading(
                        'Preguntados v0.1',
                        width='100%',
                        align='center',
                        size='15',
                    ),
                ),
                rx.flex(
                    rx.vstack(
                        rx.text('Alumnos:'),
                        rx.text(' ● Benavidez, Tomas'),
                        rx.text(' ● Blengino, Giuliano'),
                        rx.text(' ● Cambria, Valentino'),
                    gap='5px',
                    ),
                ),
                rx.center(
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.button('Jugar',size='4'),
                        ),
                        rx.dialog.content(
                            rx.vstack(
                                rx.heading('Ingrese el nombre de los jugadores',size='3',align='center'),
                                rx.hstack(
                                    rx.vstack(
                                        rx.text(
                                            'Jugador 1',
                                            size='3',
                                            text_align='left',
                                            weight='medium',
                                            width='100%',
                                        ),
                                        rx.input(
                                            placeholder='Jugador 1',
                                            type='text',
                                            on_change=Tablero.set_jug1_nom
                                        ),
                                    ),
                                    rx.vstack(
                                        rx.text(
                                            'Jugador 2',
                                            size='3',
                                            text_align='left',
                                            weight='medium',
                                            width='100%',
                                        ),
                                        rx.input(
                                            placeholder='Jugador 2',
                                            type='text',
                                            on_change=Tablero.set_jug2_nom
                                        ),
                                    ),
                                    align='center',
                                    justify='center',
                                ),
                                rx.link(
                                    rx.button('Jugar',size='4',on_click=Tablero.setearNombres()),
                                    href='/game'
                                ),
                                align='center',
                            ),
                        ),
                    ),
                padding='2em',
                ),
            width='100%',
            max_width='30em',
            height='100%',
            max_height='20em',
            padding='3em',
            border_radius='10px',
            border='solid',
            border_color='darkred',
            bg='firebrick',
            ),
        width='100%',
        height='100%',
        justify='center',
        padding_top='10em',
        ),
    ratio=16/9,
    )
    return index