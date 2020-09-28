"""
Single-celled Organisms

- Bacteria
- BacteriaBody
- BacteriaThoughts
- BacteriaThought
"""
from generated.life.cell import Cell
from generated.mind import SimpleThoughts, Thought
from ..organism import Organism, BasicBody
from genesys.nested.data import lookups


class DataProvider:
    bacteria_thought = lookups.bacteria_thoughts
    bacteria_type = lookups.bacteria_types
    bacteria_subtype = lookups.bacteria_subtypes


class BacteriaBody(BasicBody, Cell):
    default_name = 'body'


class BacteriaThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.bacteria_thought)


class BacteriaThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            thought_class = BacteriaThought


class Bacteria(Organism):
    class Factory(Organism.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Organism.Factory.BaseFactory):
            def __next__(self):
                return '{}{}'.format(
                    next(self.provider.bacteria_subtype),
                    next(self.provider.bacteria_type),
                )

        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = BacteriaBody
            mind_class = BacteriaThoughts
