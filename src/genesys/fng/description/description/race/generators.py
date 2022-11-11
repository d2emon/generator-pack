import random

from data.fixtures.fixtures import race
from factories.factory import Factory
from factories.list_factory import ListFactory
from .generated import Body, Horns, Skin, Divercity
from .limbs import Arms, WingedArms, ClawedArms, SideFins, DorsalFin, Wings, Legs, Tail


class RandomGenerator:
    data = []

    @classmethod
    def generate(cls):
        g = random.choice(cls.data)
        return g().__next__()


class BasicGenerator:
    generated_class = None

    def __init__(self, data=None):
        self.data = data

    def generateOrNone(self, generated_class, data=None):
        if data is None:
            return None
        return generated_class(data)

    def value(self, *args, **kwargs):
        return {
            'value': next(self.data),
        }

    def __next__(self, *args, **kwargs):
        return self.generated_class(**self.value(*args, **kwargs))



class BodyGenerator(BasicGenerator):
    generated_class = Body

    def __init__(self, fixtures=None):
        if fixtures is not None:
            self.parts = [
                fixtures.body1,
                fixtures.body2,
                fixtures.body3,
            ]
            self.arms = fixtures.arms
            self.legs = fixtures.legs
            self.tails = fixtures.tails
        else:
            self.parts = []
            self.arms = []
            self.legs = []
            self.tails = []

    def value(self, *args, **kwargs):
        limbs = dict()

        limbs1 = next(self.arms)
        if type(limbs1) is not dict:
            limbs['arms'] = limbs1
        else:
            limbs.update(limbs1)

        limbs2 = next(self.legs)
        if type(limbs2) is not dict:
            limbs['legs'] = limbs2
        else:
            limbs.update(limbs2)

        side_fins = limbs.get('side_fins')
        arms = limbs.get('arms')
        winged_arms = limbs.get('winged_arms')
        clawed_arms = limbs.get('clawed_arms')
        legs = limbs.get('legs')
        dorsal_fin = limbs.get('dorsal_fin')
        wings = limbs.get('wings')

        # print('FINS', side_fins)
        # print('ARMS', arms)
        # print('WINGS', wings)
        # print('LEGS', legs)

        return dict(
            arms=self.generateOrNone(Arms, arms),
            winged_arms=self.generateOrNone(WingedArms, winged_arms),
            clawed_arms=self.generateOrNone(ClawedArms, clawed_arms),
            side_fins=self.generateOrNone(SideFins, side_fins),
            dorsal_fin=self.generateOrNone(DorsalFin, dorsal_fin),
            wings=self.generateOrNone(Wings, wings),
            legs=self.generateOrNone(Legs, legs),
            tail=self.generateOrNone(Tail, next(self.tails)),

            part1=next(self.parts[0]),
            part2=next(self.parts[1]),
            part3=next(self.parts[2])
        )


class HornsGenerator(BasicGenerator):
    generated_class = Horns


class SkinGenerator(BasicGenerator):
    generated_class = Skin

    def __init__(self, **kwargs):
        self.skins = kwargs.get('skins', ListFactory(None, race.skins))
        self.covers = kwargs.get('covers', Factory())
        self.colors = kwargs.get('colors', ListFactory(None, race.skin_colors))
        self.color_chances = kwargs.get('color_chances', race.skin_color_chances)
        self.agings = kwargs.get('agings', ListFactory(None, race.agings))

    def generate_colors(self):
        chances = [c for c in self.color_chances if c >= random.randint(100)]
        return self.colors.unique(len(chances))

    def value(self, skin="Their skin ", *args, **kwargs):
        return {
            'skin': skin,
            'skin_type': next(self.skins),
            'cover': next(self.covers),
            'colors': self.generate_colors(),
            'aging': next(self.agings),
        }


class DivercityGenerator(BasicGenerator):
    generated_class = Divercity

    divercity = ListFactory(race.divercities)
    colors = ListFactory(race.divercity_colors_data)

    def value(self, *args, **kwargs):
        divercity = self.divercity.unique(2)
        return {
            'm': divercity[0],
            'f': divercity[1],
            'color': next(self.colors),
        }
