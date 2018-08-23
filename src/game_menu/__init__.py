#! /usr/bin/env python
from menu import Menu

from .galaxy_menu import list_galaxies


def show_menu():
    menu = Menu(
        title="Generators",
        options=[
            ("Galaxies", list_galaxies),
            ("Exit", Menu.CLOSE),
        ],
        prompt=">",
        # refresh=refreshHandler,
    )
    menu.open()
