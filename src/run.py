#! /usr/bin/env python
from menu import Menu
from menu_utils import MenuHandler
from generator.space.galaxy import GalaxyGenerator
from generator.space.planet import PlanetGenerator


galaxies = []


class GalaxyHandler(MenuHandler):
    def __init__(self, galaxy):
        self.galaxy = galaxy

    @property
    def text(self):
        return self.galaxy.generated_text

    def handle(self):
        planets = []
        for i in range(10):
            planets.append(GalaxyHandler(PlanetGenerator.generate()).menuOption)
        menu = Menu(
            title=self.text,
            options=planets + [
                ("Back", Menu.CLOSE),
                ("Exit", exit),
            ]
        )
        menu.open()


def list_galaxies():
    global galaxies
    galaxies = []
    for i in range(10):
        galaxies.append(GalaxyHandler(GalaxyGenerator.generate()).menuOption)
    menu = Menu(
        title="Galaxies",
        options=galaxies + [("Exit", Menu.CLOSE), ]
    )
    menu.open()


def main():
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


if __name__ == "__main__":
    main()
