from models.v5 import life
from ...materials import OrganicFactory, ProteinsFactory, LipidsFactory, MoleculeFactory


class VenomFactory(OrganicFactory):
    default_model = life.Venom

    def children(self):
        yield ProteinsFactory()
        yield LipidsFactory().probable(40)
        yield MoleculeFactory.from_elements('N').probable(40)
        yield MoleculeFactory.from_elements('Na').probable(40)
        yield MoleculeFactory.from_elements('Cl').probable(40)
