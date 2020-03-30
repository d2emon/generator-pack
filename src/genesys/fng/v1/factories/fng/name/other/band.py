from factories.factory import ListFactory
from factories.generator import ListGenerator, PercentGenerator
from factories.generator import Generated
from sample_data.fixtures import names1, names2, names3, names4, names5


class Band(Generated):
    title = "Band"


class BandSubGenerator(ListGenerator):
    generated_class = Band


class BandGenerator(PercentGenerator):
    class BandSubGenerator1(BandSubGenerator):
        template = "{name1} {name2}"
        data = {
            'name1': ListFactory(names1),
            'name2': ListFactory(names2),
        }

    class BandSubGenerator2(BandSubGenerator):
        data = { 'name': ListFactory(names5) }

    class BandSubGenerator3(BandSubGenerator):
        template = "{name1} of {name2}"
        data = {
            'name1': ListFactory(names3),
            'name2': ListFactory(names4),
        }

    subgenerators = {
        30: BandSubGenerator1,
        70: BandSubGenerator2,
        100: BandSubGenerator3,
    }
