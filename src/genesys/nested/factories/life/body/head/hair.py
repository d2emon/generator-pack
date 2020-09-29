from generated import life
from ....factory import Factory
from ....materials import KeratinFactory
from ..skin import DeadSkinFactory


class DandruffFactory(Factory):
    default_model = life.Dandruff

    def children(self):
        yield DeadSkinFactory()


class HairFactory(Factory):
    default_model = life.Hair

    def children(self):
        # yield Bacteria.probable(30)
        yield KeratinFactory()


class HeadHairFactory(HairFactory):
    default_model = life.HeadHair
    names = ["brown", "black", "gray", "light", "blonde", "red", "dark"]

    def generate_name(self):
        return f"{self.select_item(*self.names)} hair"

    def children(self):
        yield DandruffFactory()
        yield from super().children()
