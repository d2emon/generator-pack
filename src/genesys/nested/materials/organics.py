from models.v5 import materials
from factories.thing.nested_factory import NestedFactory as Factory
from utils.nested import select_item
from .matter import MoleculeFactory
from .minerals import SaltFactory
from .water import WaterMoleculeFactory


class OrganicMoleculeFactory(MoleculeFactory):
    # TODO: Refactor it
    default_model = materials.OrganicMolecule
    contents = 'C', 'H', 'O'


class MethaneFactory(OrganicMoleculeFactory):
    # TODO: Refactor it
    default_model = materials.Methane
    contents = 'C', 'H'


class ChitinFactory(OrganicMoleculeFactory):
    model = materials.Chitin
    contents = 'C', 'H', 'N', 'O'


class ProteinsFactory(OrganicMoleculeFactory):
    # TODO: Refactor it
    default_model = materials.Proteins


class LipidsFactory(OrganicMoleculeFactory):
    # TODO: Refactor it
    default_model = materials.Lipids


class GlucidsFactory(OrganicMoleculeFactory):
    # TODO: Refactor it
    default_model = materials.Glucids


class AlcoholFactory(OrganicMoleculeFactory):
    # TODO: Refactor it
    default_model = materials.Alcohol


class PolymersFactory(OrganicMoleculeFactory):
    # TODO: Refactor it
    default_model = materials.Polymers


class OrganicFactory(Factory):
    model = materials.OrganicMatter

    def children(self):
        yield select_item(
            ProteinsFactory(),
            LipidsFactory(),
            GlucidsFactory(),
        )
        yield select_item(
            ProteinsFactory(),
            LipidsFactory(),
            GlucidsFactory(),
            None,
        )
        yield SaltFactory().probable(30)


class OilFactory(OrganicFactory):
    model = materials.Oil

    def children(self):
        yield LipidsFactory.one()


class PolymericFactory(OrganicFactory):
    # TODO: Refactor it
    default_model = materials.Polymeric

    def children(self):
        yield PolymersFactory()


class PlasticFactory(PolymericFactory):
    # TODO: Refactor it
    default_model = materials.Plastic


class RubberFactory(PolymericFactory):
    # TODO: Refactor it
    default_model = materials.Rubber


class KeratinFactory(OrganicFactory):
    # TODO: Refactor it
    default_model = materials.Keratin

    def children(self):
        yield ProteinsFactory()


class SweatFactory(OrganicFactory):
    # TODO: Refactor it
    default_model = materials.Sweat

    def children(self):
        yield WaterMoleculeFactory()
        yield SaltFactory()
        yield GlucidsFactory()
