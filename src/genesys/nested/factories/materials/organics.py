from models.v5 import materials
from factories.nested_factory import NestedFactory as Factory
from .matter import MoleculeFactory
from .minerals import SaltFactory
from .water import WaterMoleculeFactory


class OrganicMoleculeFactory(MoleculeFactory):
    default_model = materials.OrganicMolecule

    def children(self):
        yield from self.elements('C', 'H', 'O')


class MethaneFactory(OrganicMoleculeFactory):
    default_model = materials.Methane

    def children(self):
        yield from self.elements('C', 'H')


class ChitinFactory(OrganicMoleculeFactory):
    default_model = materials.Chitin

    def children(self):
        yield from self.elements('C', 'H', 'N', 'O')


class ProteinsFactory(OrganicMoleculeFactory):
    default_model = materials.Proteins


class LipidsFactory(OrganicMoleculeFactory):
    default_model = materials.Lipids


class GlucidsFactory(OrganicMoleculeFactory):
    default_model = materials.Glucids


class AlcoholFactory(OrganicMoleculeFactory):
    default_model = materials.Alcohol


class PolymersFactory(OrganicMoleculeFactory):
    default_model = materials.Polymers


class OrganicFactory(Factory):
    default_model = materials.OrganicMatter

    def children(self):
        yield self.select_item(
            ProteinsFactory(),
            LipidsFactory(),
            GlucidsFactory(),
        )
        yield self.select_item(
            ProteinsFactory(),
            LipidsFactory(),
            GlucidsFactory(),
            None,
        )
        yield SaltFactory().probable(30)


class OilFactory(OrganicFactory):
    default_model = materials.Oil

    def children(self):
        yield LipidsFactory()


class PolymericFactory(OrganicFactory):
    default_model = materials.Polymeric

    def children(self):
        yield PolymersFactory()


class PlasticFactory(PolymericFactory):
    default_model = materials.Plastic


class RubberFactory(PolymericFactory):
    default_model = materials.Rubber


class KeratinFactory(OrganicFactory):
    default_model = materials.Keratin

    def children(self):
        yield ProteinsFactory()


class SweatFactory(OrganicFactory):
    default_model = materials.Sweat

    def children(self):
        yield WaterMoleculeFactory()
        yield SaltFactory()
        yield GlucidsFactory()
