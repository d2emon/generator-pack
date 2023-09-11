# TODO: Convert to ModelFactory
class ThingFactory:
    THINGS = {}

    def __init__(self, name, contents=[], namegen=None):
        self.name = name
        self.contents = contents

        if namegen is None:
            self.namegen = self.name
        else:
            self.namegen = namegen

        self.THINGS[name] = self

    @classmethod
    def check_missing(cls):
        for factory in cls.THINGS:
            for item in factory.items:
                factory_id = item.factory_id
                if factory_id and cls.THINGS.get(factory_id) is None:
                    yield factory_id

    @classmethod
    def cleanup(cls):
        for factory in cls.THINGS:
            for item in factory.content:
                item.cleanup()

    def children_factory(self):
        for items in self.content:
            item = items.item

            if item.factory is None:
                return

            if not item.check_probability():
                return

            for _ in item.get_amount():
                yield self.model(item.factory)
