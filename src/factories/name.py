import random
from genesys.fng.providers.list_item import ListItemProvider
from models.models.name import Name
from sample_data import genders
from factories.factory import Factory


def random_generator(selector, generator_id=None, max_value=10):
    return selector(generator_id or random.randrange(max_value))


class TextFactory(Factory):
    class DataProvider:
        # default = generator_data
        block_id = ''
        groups = ListItemProvider([])
        data = {}

        @property
        def block(self):
            return self.data.get(self.block_id, {})

        def factory(self, group_id=None):
            return self.block.get(group_id or next(self.groups))

        def parts(self, group_id=None, **params):
            return next(self.factory(group_id))

    def model(self, group_id=None, *args, **params):
        return Name(*self.provider.parts(group_id=group_id, **params), generator=self)


class NameFactory(TextFactory):
    class DataProvider(TextFactory.DataProvider):
        block_id = 'names'
        name_group_id = 'aliens'

        @property
        def block(self):
            return self.data.get(self.block_id, {}).get(self.name_group_id)

        def parts(self, race_id=None, **params):
            return [next(part) for part in self.factory(race_id)]

    gender = genders.NEUTRAL

    def model(self, race_id=None, *args, **params):
        return Name(*self.provider.parts(race_id=race_id, **params), generator=self)


class ListNameFactory(NameFactory):
    class DataProvider(NameFactory.DataProvider):
        # default = []
        data = ListItemProvider([])

        def query(self, **params):
            return self.data

        def parts(self, gender=genders.NEUTRAL, **params):
            data = self.query(gender=gender, **params)
            return next(data) if data is not None else []

    def model(self, gender=genders.NEUTRAL, *args, **params):
        return Name(*self.provider.get_parts(gender=gender, **params), generator=self)


class GenderListNameFactory(ListNameFactory):
    class DataProvider(ListNameFactory.DataProvider):
        # default = {}
        data = {}

        def query(self, gender=genders.NEUTRAL, **params):
            return self.data.get(gender, None)
