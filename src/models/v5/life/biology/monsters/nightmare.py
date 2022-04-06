from models.nested_model import Model
from .space import SpaceAnimal, SpaceMonster
from .sea import SeaMonster


class CanOfNightmare(Model):
    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                yield from SpaceAnimal.multiple(4, 6)
                yield from SeaMonster.multiple(2, 6)
                yield from SpaceMonster.multiple(2, 6)
