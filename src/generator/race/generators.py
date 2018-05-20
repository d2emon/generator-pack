import random

from fixtures import race
from generator.generator.generator_data import ListData
from .generated import Body, Horns, Skin, Divercity


class RandomGenerator:
    data = []

    @classmethod
    def generate(cls):
        g = random.choice(cls.data)
        return g().__next__()


class BodyGenerator:
    def __init__(self, fixtures=None):
        if fixtures is not None:
            self.parts = [
                fixtures.body1,
                fixtures.body2,
                fixtures.body3,
            ]
        else:
            self.parts = []

    def __next__(self):
        return Body(
            part1=next(self.parts[0]),
            part2=next(self.parts[1]),
            part3=next(self.parts[2])
        )


class HornsGenerator:
    horns = ListData(race.horns)

    @classmethod
    def __next__(cls):
        return Horns(value=next(cls.horns))


class AquaticHornsGenerator(HornsGenerator):
    horns = ListData(race.aquatic_horns)


class SkinGenerator:
    skins = ListData(race.skins)
    covers = ListData(race.covers)
    colors = [ListData(color) for color in race.skin_colors]
    agings = ListData(race.agings)

    @classmethod
    def __next__(cls, skin="Their skin "):
        cover = None
        if cls.covers is not None:
            cover = next(cls.covers)

        return Skin(
            skin=skin,
            skin_type=next(cls.skins),
            cover=cover,
            colors=[next(color) for color in cls.colors], # unique
            aging=next(cls.agings),
        )


class AquaticSkinGenerator(SkinGenerator):
    covers = None


class AmphibianSkinGenerator(SkinGenerator):
    covers = ListData(race.mucouses)


class ReptileSkinGenerator(SkinGenerator):
    covers = ListData(race.reptile_scales)


class FishSkinGenerator(SkinGenerator):
    covers = ListData(race.fish_scales)


class BirdSkinGenerator(SkinGenerator):
    covers = ListData(race.feathers)


class DivercityGenerator:
    divercity = ListData(race.divercities)
    colors = ListData(race.divercity_colors_data)

    @classmethod
    def __next__(cls):
        divercity = cls.divercity.unique(2)
        return Divercity(
            m=divercity[0],
            f=divercity[1],
            color=next(cls.colors),
        )
