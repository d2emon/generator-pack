from generated import materials
from ..factory import Factory
from .matter import MoleculeFactory
from .minerals import SaltFactory


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
        yield self.select_factory(
            ProteinsFactory(),
            LipidsFactory(),
            GlucidsFactory(),
        )
        yield self.select_factory(
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
