from genesys.nested.factories.nested_factory import NestedFactory
from models import minerals
from models.materials import organics
from models.v5 import materials
from utils.nested import select_item
from .molecules import MoleculeFactory, SaltFactory
from .water import WaterMoleculeFactory


# Organic Molecules


class OrganicMoleculeFactory(MoleculeFactory):
    model = materials.OrganicMolecule
    contents = 'C', 'H', 'O'


class ProteinsFactory(OrganicMoleculeFactory):
    model = materials.Proteins


class LipidsFactory(OrganicMoleculeFactory):
    model = materials.Lipids


class GlucidsFactory(OrganicMoleculeFactory):
    model = materials.Glucids


class AlcoholFactory(OrganicMoleculeFactory):
    model = organics.Alcohol


class PolymersFactory(OrganicMoleculeFactory):
    model = organics.Polymers


# Chitin


class ChitinMoleculeFactory(OrganicMoleculeFactory):
    contents = 'C', 'H', 'N', 'O'


class ChitinFactory(NestedFactory):
    model = organics.Chitin

    def children(self):
        yield ChitinMoleculeFactory.one()


# Organics


class OrganicFactory(NestedFactory):
    model = materials.OrganicMatter

    @classmethod
    def organic_molecules(cls, required=False):
        yield ProteinsFactory.one()
        yield LipidsFactory.one()
        yield GlucidsFactory.one()

        if not required:
            yield None

    def children(self):
        yield select_item(self.organic_molecules(True))
        yield select_item(self.organic_molecules(False))
        yield SaltFactory.one().probable(30)


class OilFactory(OrganicFactory):
    model = minerals.Oil

    def children(self):
        yield LipidsFactory.one()


class PolymericFactory(OrganicFactory):
    model = materials.Polymeric

    def children(self):
        yield PolymersFactory.one()


class PlasticFactory(PolymericFactory):
    model = organics.Plastic


class RubberFactory(PolymericFactory):
    model = organics.Rubber


# Future
# TODO: Refactor it


class KeratinFactory(OrganicFactory):
    model = materials.Keratin

    def children(self):
        yield ProteinsFactory.one()


class SweatFactory(OrganicFactory):
    model = materials.Sweat

    def children(self):
        yield WaterMoleculeFactory.one()
        yield SaltFactory.one()
        yield GlucidsFactory.one()
