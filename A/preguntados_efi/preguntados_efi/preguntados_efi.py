"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .index import index # import del front-end - Pagina inicial
from .game import game

app = rx.App(style={rx.button: {"cursor":"pointer"}})
app.add_page(index)
app.add_page(game)