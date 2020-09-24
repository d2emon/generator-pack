from generated.materials import OrganicMolecule, Methane, Chitin, Proteins, Lipids, Glucids, Alcohol, Polymers,\
    OrganicMatter, Oil, Polymeric, Plastic, Rubber
from ..factory import Factory
from .matter import MoleculeFactory
from .minerals import SaltFactory


class OrganicMoleculeFactory(MoleculeFactory):
    default_model = OrganicMolecule

    def children(self):
        yield from self.elements('C', 'H', 'O')


class MetaneFactory(OrganicMoleculeFactory):
    default_model = Methane

    def children(self):
        yield from self.elements('C', 'H')


class ChitinFactory(OrganicMoleculeFactory):
    default_model = Chitin

    def children(self):
        yield from self.elements('C', 'H', 'N', 'O')


class ProteinsFactory(OrganicMoleculeFactory):
    default_model = Proteins


class LipidsFactory(OrganicMoleculeFactory):
    default_model = Lipids


class GlucidsFactory(OrganicMoleculeFactory):
    default_model = Glucids


class AlcoholFactory(OrganicMoleculeFactory):
    default_model = Alcohol


class PolymersFactory(OrganicMoleculeFactory):
    default_model = Polymers


class OrganicMatterFactory(Factory):
    default_model = OrganicMatter

    def children(self):
        yield self.factory(
            ProteinsFactory(),
            LipidsFactory(),
            GlucidsFactory(),
        )
        yield self.factory(
            ProteinsFactory(),
            LipidsFactory(),
            GlucidsFactory(),
            None,
        )
        yield SaltFactory().probable(30)


class OilFactory(OrganicMatterFactory):
    default_model = Oil

    def children(self):
        yield LipidsFactory()


class PolymericFactory(OrganicMatterFactory):
    default_model = Polymeric

    def children(self):
        yield PolymersFactory()


class PlasticFactory(PolymericFactory):
    default_model = Plastic


class RubberFactory(PolymericFactory):
    default_model = Rubber
