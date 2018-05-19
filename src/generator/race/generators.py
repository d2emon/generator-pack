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
    base_parts = [
        ListData([]),
        ListData(["two arms and ","four arms and ","six arms and ","two arms and ","two arms and ","four arms and ","two arms and "]),
        ListData(["two legs, ","four legs, ","six legs, ","four legs, ","two legs, ","two legs, "]),
        ListData(["with a long, thin tail","with a long, thick tail","with a short, thin tail","with a short, thick tail","with remnants of what was once a tail","but they have no tail","with a long, strong and agile tail","with a short, strong tail","with a long, strong tail","with a short, muscular tail","with a long, muscular tail","with a long, weak tail","with a short, weak tail","with a long, useless tail","with a short, useless tail","with a short, stubby tail"]),
    ]

    def __init__(self, parts1=None, parts2=None, parts3=None):
        self.parts = self.base_parts
        if parts1 is not None:
            self.parts[1] = ListData(parts1)
        if parts2 is not None:
            self.parts[2] = ListData(parts2)
        if parts3 is not None:
            self.parts[3] = ListData(parts3)

    def __next__(self):
        return Body(
            part1=next(self.parts[1]),
            part2=next(self.parts[2]),
            part3=next(self.parts[3])
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
