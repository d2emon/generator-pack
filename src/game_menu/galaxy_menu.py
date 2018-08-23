from menu import Menu

from generator.space.galaxy import GalaxyGenerator
from generator.space.planet import PlanetGenerator

from .menu_handler import MenuHandler


galaxies = []


class GalaxyHandler(MenuHandler):
    def __init__(self, galaxy):
        self.galaxy = galaxy

    @property
    def text(self):
        return self.galaxy.generated_value

    def handle(self):
        planets = []
        for i in range(10):
            planets.append(GalaxyHandler(PlanetGenerator.generate()).option)
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
        galaxies.append(GalaxyHandler(GalaxyGenerator.generate()).option)
    menu = Menu(
        title="Galaxies",
        options=galaxies + [("Exit", Menu.CLOSE), ]
    )
    menu.open()
