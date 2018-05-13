import random
from .generator import ListGenerator, PercentedGenerator
from .generator.generated import Generated
from .generator.generator_data import ListData
from data.band import names1, names2, names3, names4, names5


class Band(Generated):
    title = "Band"


class BandSubGenerator(ListGenerator):
    generated_class = Band


class BandGenerator(PercentedGenerator):
    class BandSubGenerator1(BandSubGenerator):
        data_list1 = ListData(names1)
        data_list2 = ListData(names2)

        @classmethod
        def __next__(cls):
            return "%s %s" % (
                cls.data_list1.__next__(),
                cls.data_list2.__next__(),
            )

    class BandSubGenerator2(BandSubGenerator):
        data_list = ListData(names5)

    class BandSubGenerator3(BandSubGenerator):
        data_list1 = ListData(names3)
        data_list2 = ListData(names4)

        @classmethod
        def __next__(cls):
            return "%s of %s" % (
                cls.data_list1.__next__(),
                cls.data_list2.__next__(),
            )

    subgenerators = {
        30: BandSubGenerator1,
        70: BandSubGenerator2,
        100: BandSubGenerator3,
    }
