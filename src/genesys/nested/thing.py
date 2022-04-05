from .name import NameFactory
from .instance import Instance


class Thing:
    things = {}

    def __init__(self, name, *child_factories, name_data=None) -> None:
        self.name = name
        self.child_factories = child_factories
        self.name_factory = NameFactory(self.name_data or self.name)

        self.things[name] = self

    def children_factory(self, parent=None):
        for factory in self.child_factories:
            for thing in factory():
                if thing is None:
                    continue

                yield Instance(
                    thing=self,
                    parent=parent,
                )
