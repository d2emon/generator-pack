from .monster import Monster, MonsterBody, MonsterThoughts, MonsterThought
from genesys.nested.data import lookups


class DataProvider:
    sea_monster_thought = lookups.sea_monster_thoughts
    sea_monster = lookups.sea_monsters


class SeaMonsterBody(MonsterBody):
    class Factory(MonsterBody.Factory):
        data_provider_class = DataProvider


class SeaMonsterThought(MonsterThought):
    class Factory(MonsterThought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(MonsterThought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.sea_monster_thought)


class SeaMonsterThoughts(MonsterThoughts):
    class Factory(MonsterThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(MonsterThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from SeaMonsterThought.multiple(1, 2)


class SeaMonster(Monster):
    class Factory(Monster.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Monster.Factory.BaseFactory):
            def __next__(self):
                return '{} {}{}'.format(
                    next(self.provider.sea_monster[0]),
                    next(self.provider.sea_monster[1]),
                    next(self.provider.sea_monster[2]),
                )

        class ChildrenFactory(Monster.Factory.ChildrenFactory):
            body_class = SeaMonsterBody
            mind_class = SeaMonsterThoughts
