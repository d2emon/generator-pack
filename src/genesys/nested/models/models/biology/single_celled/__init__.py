"""
Single-celled Organisms
"""
from ..cell import Cell
from ..mind import Thoughts, Thought
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
            def __next__(self):
                return next(self.provider.bacteria_thought)


class BacteriaThoughts(Thoughts):
    class Factory(Thoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(Thoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from BacteriaThought.multiple(1)


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
