from generator.generator import ListGenerator, PercentedGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import ListData
from fixtures.media.band import names1, names2, names3, names4, names5


class Band(Generated):
    title = "Band"


class BandSubGenerator(ListGenerator):
    generated_class = Band


class BandGenerator(PercentedGenerator):
    class BandSubGenerator1(BandSubGenerator):
        template = "{name1} {name2}"
        data = {
            'name1': ListData(names1),
            'name2': ListData(names2),
        }

    class BandSubGenerator2(BandSubGenerator):
        data = { 'name': ListData(names5) }

    class BandSubGenerator3(BandSubGenerator):
        template = "{name1} of {name2}"
        data = {
            'name1': ListData(names3),
            'name2': ListData(names4),
        }

    subgenerators = {
        30: BandSubGenerator1,
        70: BandSubGenerator2,
        100: BandSubGenerator3,
    }
