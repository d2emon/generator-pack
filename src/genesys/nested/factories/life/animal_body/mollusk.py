from generated import life
from ...factory import Factory
from ...materials import MoleculeFactory


class ClamShellFactory(Factory):
    default_model = life.ClamShell

    def children(self):
        yield MoleculeFactory.from_elements('Ca')
