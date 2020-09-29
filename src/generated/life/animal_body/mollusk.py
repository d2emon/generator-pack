from genesys.model.model import Model
from ...materials import Molecule


class ClamShell(Model):
    elements = Model.children_property(Molecule)
