import random

from fixtures import race
from generator.generator.generator_data import ListData
from .generated import Body, Horns, Skin, Divercity, Arms, Wings, Legs, Tail


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
            self.arms = fixtures.arms
            self.wings = fixtures.wings
            self.legs = fixtures.legs
            self.tails = fixtures.tails
            self.limbs = fixtures.limbs
        else:
            self.parts = []
            self.arms = []
            self.wings = []
            self.legs = []
            self.tails = []
            self.limbs = []

    def generateOrNone(self, generate_class, data=None):
        if data is None:
            return None
        return generate_class(data)

    def __next__(self):
        if self.limbs.data:
            limbs = next(self.limbs)
        else:
            limbs = dict(
                arms=next(self.arms),
                legs=next(self.legs),
            )
        return Body(
            arms=self.generateOrNone(Arms, limbs.get('arms')),
            wings=self.generateOrNone(Wings, limbs.get('wings')),
            legs=self.generateOrNone(Legs, limbs.get('legs')),
            tail=self.generateOrNone(Tail, next(self.tails)),

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
