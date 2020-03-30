from genesys.fng.providers.names.fantasy.alien import DataProvider


class NameFactory:
    class DataProvider:
        pass

    def __init__(self, provider=None):
        self.provider = provider or self.DataProvider()
        self.parts = {}

    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError()

    @property
    def factories(self):
        raise NotImplementedError()

    def generate(self):
        self.parts = {part_id: next(factory) for part_id, factory in self.factories.items()}
        self.parts.update({part_id: self.part(part_id) for part_id, factory in self.factories.items()})
        return self.parts

    def is_valid(self, part_id):
        return True

    def part(self, part_id):
        if self.is_valid(part_id):
            return self.parts.get(part_id)

        factory = self.factories.get(part_id)
        self.parts[part_id] = next(factory)
        return self.part(part_id)


class AlienName:
    def __init__(self, *parts):
        self.__parts = parts

    @property
    def parts(self):
        for part_id, part in enumerate(self.__parts):
            if part_id == 3:
                yield part if self.__parts[2] else ''
            else:
                yield part

    @property
    def name(self):
        return ''.join(self.parts).title()


class AlienNameFactory:
    class DataProvider(DataProvider):
        pass

    class BaseAlienNameFactory(NameFactory):
        @property
        def factories(self):
            raise NotImplementedError()

        def is_valid(self, part_id):
            if self.parts[part_id] is None:
                return False
            elif part_id == 4:
                return self.parts[part_id] not in (self.parts[0], self.parts[3])
            else:
                return True

        def __next__(self):
            parts = self.generate()
            return AlienName([
                parts[0],
                parts[1],
                parts[2],
                parts[3],
                parts[4],
            ])

    class AlienNameFactory1(BaseAlienNameFactory):
        @property
        def factories(self):
            return (
                self.provider.nm1,
                self.provider.nm2,
                self.provider.nm3,
                self.provider.nm4,
                self.provider.nm5,
            )

    class AlienNameFactory2(BaseAlienNameFactory):
        @property
        def factories(self):
            return (
                self.provider.nm6,
                self.provider.nm7,
                self.provider.nm8,
                self.provider.nm10,
                self.provider.nm11,
            )

    class AlienNameFactory3(BaseAlienNameFactory):
        @property
        def factories(self):
            return (
                self.provider.nm12,
                self.provider.nm13,
                self.provider.nm14,
                self.provider.nm15,
                self.provider.nm16,
            )

    def __init__(self, name_id=0, provider=None):
        self.name_id = name_id
        self.provider = provider or self.DataProvider()

    def __iter__(self):
        return self

    def __next__(self):
        return self.get_name()

    def get_factory(self, name_id=0):
        if name_id < 4:
            return self.AlienNameFactory1(self.provider)
        elif name_id < 7:
            return self.AlienNameFactory2(self.provider)
        else:
            return self.AlienNameFactory3(self.provider)

    @classmethod
    def is_valid(cls, names):
        return True

    def get_name(self, name_id=0):
        names = next(self.get_factory(name_id))
        return AlienName(names) if self.is_valid(names) else self.get_name(name_id)
