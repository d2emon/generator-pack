from genesys.nested.factories.nested_factory import NestedFactory
from models.materials import organics
from models.v5 import materials
from utils.nested import select_item
from .elements import MoleculeFactory
from .minerals import SaltFactory
from .water import WaterMoleculeFactory


# Organic Molecules


class OrganicMoleculeFactory(MoleculeFactory):
    model = organics.OrganicMolecule
    contents = 'C', 'H', 'O'


class ProteinsFactory(OrganicMoleculeFactory):
    model = organics.Proteins


class LipidsFactory(OrganicMoleculeFactory):
    model = organics.Lipids


class GlucidsFactory(OrganicMoleculeFactory):
    model = organics.Glucids


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
    model = organics.OrganicMatter
    has_glucids = True
    has_lipids = True
    has_proteins = True
    salt_probability = 30
    second_molecule = True

    @classmethod
    def organic_molecules(cls, required=False):
        if cls.has_glucids:
            yield GlucidsFactory.one()
        if cls.has_lipids:
            yield LipidsFactory.one()
        if cls.has_proteins:
            yield ProteinsFactory.one()
        if not required:
            yield None

    @classmethod
    def salt(cls):
        if cls.salt_probability:
            yield SaltFactory.probable(cls.salt_probability)

    def children(self):
        yield select_item(self.organic_molecules(True))
        if self.second_molecule:
            yield select_item(self.organic_molecules(False))
        yield from self.salt()


class OilFactory(OrganicFactory):
    model = organics.Oil
    has_glucids = False
    has_lipids = True
    has_proteins = False
    salt_probability = 0
    second_molecule = False


class PolymericFactory(OrganicFactory):
    model = organics.Polymeric
    salt_probability = 0
    second_molecule = False

    @classmethod
    def organic_molecules(cls, required=False):
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
