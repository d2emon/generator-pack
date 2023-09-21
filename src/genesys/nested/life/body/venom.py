from models.v5 import life
from ...materials import OrganicFactory, ProteinsFactory, LipidsFactory, MoleculeFactory


class VenomFactory(OrganicFactory):
    default_model = life.Venom

    def children(self):
        yield ProteinsFactory()
        yield LipidsFactory().probable(40)
        yield MoleculeFactory.element_factory('N').probable(40)
        yield MoleculeFactory.element_factory('Na').probable(40)
        yield MoleculeFactory.element_factory('Cl').probable(40)
