from .generator import Generated
from .generator.generator_data import ListData


from fixtures import race


import random


class RandomGenerator:
    data = []

    @classmethod
    def generate(cls):
        g = random.choice(cls.data)
        return g().__next__()


def int2str(i):
    data = {
        2: 'two',
        4: 'four',
        6: 'six',
    }
    return data.get(i)


class Body:
    def __init__(self, part1=None, part2=None, part3=None):
        self.part1 = part1
        self.part2 = part2
        self.part3 = part3

    def __str__(self):
        return "They have {}{}{}.".format(
            self.part1,
            self.part2,
            self.part3,
        )


class Horns(Generated):
    pass


class Nose(Generated):
    pass


class Mouth(Generated):
    pass


class Eyes(Generated):
    def __init__(self, **kwargs):
        self.count = kwargs.get('count', 2)
        self.sockets = kwargs.get('sockets', None)
        self.appearance = kwargs.get('appearance', None)
        self.quality = kwargs.get('quality', None)

    @property
    def count_str(self):
        return "{} eyes".format(int2str(self.count))

    def __str__(self):
        text = "They have {} which sit {} in their sockets and can often make them appear to be {}. Their eyesight is {}."
        return text.format(
            self.count_str,
            self.sockets,
            self.appearance,
            self.quality,
        )


class Ears(Generated):
    def __init__(self, **kwargs):
        self.ears = kwargs.get('ears', None)
        self.quality = kwargs.get('quality', None)

    def __str__(self):
        return "Their ears are {} and their hearing is {}.".format(
            self.ears,
            self.quality,
        )


class Skin(Generated):
    def __init__(self, **kwargs):
        self.skin = kwargs.get('skin', None)
        self.skin_type = kwargs.get('skin_type', None)
        self.cover = kwargs.get('cover', None)
        self.colors = kwargs.get('colors', None)
        self.aging = kwargs.get('aging', None)

    @property
    def color(self):
        return "".join(self.colors)

    def __str__(self):
        cover = ""
        if self.cover is not None:
            cover = self.cover
        text = "Their skin is {} {}\n"
        text += "{}colors are mostly {}, which tend to become {} as they age."
        return text.format(
            self.skin_type,
            cover,
            self.skin,
            self.color,
            self.aging,
        )


class Divercity(Generated):
    def __init__(self, **kwargs):
        self.m = kwargs.get('m', None)
        self.f = kwargs.get('f', None)
        self.color = kwargs.get('color', None)

    def __str__(self):
        return "The males are usually {m} than their female counter part and their colors are {color}. The females, however, are usually {f}.".format(
            m=self.m,
            f=self.f,
            color=self.color,
        )


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
            next(self.parts[1]),
            next(self.parts[2]),
            next(self.parts[3])
        )


class EyesGenerator:
    count = ListData(race.eyes_count)
    eyesockets = ListData(race.eyesockets)

    @classmethod
    def __next__(cls, appearance, quality):
        return Eyes(
            count=next(cls.count),
            sockets=next(cls.eyesockets),
            appearance=appearance,
            quality=quality,
        )


class MouthGenerator:
    mouths = ListData(race.mouths)

    @classmethod
    def __next__(cls):
        return Mouth(next(cls.mouths))


class NoseGenerator:
    noses = ListData(race.noses)

    @classmethod
    def __next__(cls):
        return Nose(next(cls.noses))


class FishNoseGenerator(NoseGenerator):
    noses = ListData(race.fish_noses)


class BeakGenerator(MouthGenerator):
    noses = ListData(race.beaks)


class EarsGenerator:
    ears = ListData(race.ears)

    @classmethod
    def __next__(cls, quality):
        return Ears(
            ears=next(cls.ears),
            quality=quality,
        )


class FishEarsGenerator(EarsGenerator):
    ears = ListData(race.fish_ears)


class BirdEarsGenerator(EarsGenerator):
    ears = ListData(race.bird_ears)


class HornsGenerator:
    horns = ListData(race.horns)

    @classmethod
    def __next__(cls):
        return Horns(next(cls.horns))


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


class Race:
    def __init__(self, **kwargs):
        self.race_type = kwargs.get('race_type')
        self.body = kwargs.get('body')
        self.appearance = kwargs.get('appearance')
        self.horns = kwargs.get('horns')
        self.ears = kwargs.get('ears')
        self.eyes = kwargs.get('eyes')
        self.nose = kwargs.get('nose')
        self.mouth = kwargs.get('mouth')
        self.skin = kwargs.get('skin')
        self.divercity = kwargs.get('divercity', [])
        self.divercity_color = kwargs.get('divercity_color')

    @property
    def nose_mouth(self):
        nose_mouth = [str(i) for i in [self.mouth, self.nose] if i is not None]
        # if self.mouth is not None:
        #     nose_mouth.append(str(self.mouth))
        # if self.nose is not None:
        #     nose_mouth.append(str(self.nose))
        return "".join(nose_mouth)

    def __str__(self):
        text = "Their {} often make these aliens appear to be {}, but looks can be deceiving."
        nose_mouth = text.format(
            self.nose_mouth,
            self.appearance,
        )

        text = "\n\n".join([
            "These aliens are a type of {title}. {body}",
            "{eyes}",
            "{nose_mouth}\n{ears} {horns}",
            "{skin}",
            "{divercity}"
        ])
        return text.format(
            title=self.race_type,
            body=self.body,
            eyes=self.eyes,
            nose_mouth=nose_mouth,
            ears=self.ears,
            horns=self.horns,
            skin=self.skin,
            divercity=self.divercity,
        )
        # return text


class RaceGenerator:
    title = "mammal"
    skin = "Their skin "

    body_generator = BodyGenerator()
    horns_generator = HornsGenerator
    ears_generator = EarsGenerator
    eyes_generator = EyesGenerator
    nose_generator = NoseGenerator
    mouth_generator = MouthGenerator
    skin_generator = SkinGenerator

    divercity_generator = DivercityGenerator

    appearance_data = ListData(race.appearances)
    quality_data = ListData(race.qualities)

    def __next__(self):
        appearance = self.appearance_data.unique(2)
        quality = self.quality_data.unique(2)

        horns = None
        nose = None
        mouth = None
        if self.horns_generator is not None:
            horns = self.horns_generator.__next__()
        if self.nose_generator is not None:
            nose = self.nose_generator.__next__()
        if self.mouth_generator is not None:
            mouth = self.mouth_generator.__next__()

        return Race(
            race_type=self.title,
            body=self.body_generator.__next__(),
            appearance=appearance[1],
            horns=horns,
            ears=self.ears_generator.__next__(
                quality=quality[1]
            ),
            eyes=self.eyes_generator.__next__(
                appearance=appearance[0],
                quality=quality[0]
            ),
            nose=nose,
            mouth=mouth,
            skin=self.skin_generator.__next__(self.skin),
            divercity=self.divercity_generator.__next__(),
        )


class MammalRaceGenerator(RaceGenerator):
    title = "mammal"


class AquaticRaceGenerator(RaceGenerator):
    title = "aquatic mammal"

    horns_generator = AquaticHornsGenerator
    skin_generator = AquaticSkinGenerator

    body_generator = BodyGenerator(
        ["a huge, powerful tail and small anal fin, ","a huge, muscular tail and small anal fin, ","a large, muscular tail and small anal fin, ","a large, powerful tail and small anal fin, ","a short, muscular tail and small anal fin, ","a long, powerful tail and small anal fin, ","a short, powerful tail and small anal fin, ","a long, muscular tail and small anal fin, ","a huge, powerful tail and small anal fin, ","a huge, muscular tail and long anal fin, ","a large, muscular tail and long anal fin, ","a large, powerful tail and long anal fin, ","a short, muscular tail and long anal fin, ","a long, powerful tail and long anal fin, ","a short, powerful tail and long anal fin, ","a long, muscular tail and long anal fin, "],
        ["two arms and ","four arms and ","two strong side fins and ","four strong side fins and ","six strong side fins and ","two side fins and ","four side fins and ","six side fins and ","two large side fins and ","four large side fins and ","six large side fins and ","two powerful arms and ","four powerful arms and ","two powerful side fins and ","four powerful sidefins and ","two huge side fins and ","four huge side fins and "],
        ["a huge dorsal fin","a small dorsal fin","a thick, long dorsal fin","a thin, long dorsal fin","a wide, sail-like dorsal fin","a ribbon-like dorsal fin","a long, ribbon-like dorsal fin","a short, ribbon-like dorsal fin","a huge, sail-like dorsal fin","a short, strong dorsal fin","a long, strong dorsal fin","a short, pointy dorsal fin","a long, pointy dorsal fin","a long, streamlined dorsal fin","a short, streamlined dorsal fin"],
    )



class AmphibianRaceGenerator(RaceGenerator):
    title = "amphibian"

    skin_generator = AmphibianSkinGenerator

    body_generator = BodyGenerator(
        parts3 = ["but they have no tail","with a huge, powerful tail","with a long, muscular tail","with a long, powerful tail","with a long, strong and agile tail","with a long, strong tail","with a long, thick tail","with a long, thin tail","with a long, useless tail","with a long, weak tail","with a short, muscular tail","with a short, powerful tail","with a short, strong tail","with a short, stubby tail","with a short, thick tail","with a short, thin tail","with a short, useless tail","with a short, weak tail","with a thick, powerful tail","with remnants of what was once a tail"],
    )


class ReptileRaceGenerator(RaceGenerator):
    title = "reptile"
    skin = "Their scale "

    skin_generator = ReptileSkinGenerator

    body_generator = BodyGenerator(
        ["two arms and two legs, ","two arms and four legs, ","two arms and six legs, ","four arms and two legs, ","four arms and four legs, ","four arms and six legs, ","six arms and two legs, ","six arms and four legs, ","two arms, but no legs, like a snake with arms, ","four arms, but no legs, like a snake with arms, ","six arms, but no legs, like a snake with arms, "],
        [""],
        ["with a long, thin tail","with a long, thick tail","with a short, thin tail","with a short, thick tail","with remnants of what was once a tail","but they have no tail","with a long, strong and agile tail","with a short, strong tail","with a long, strong tail","with a short, muscular tail","with a long, muscular tail","with a long, weak tail","with a short, weak tail","with a long, useless tail","with a short, useless tail","with a short, stubby tail"],
    )


class FishRaceGenerator(RaceGenerator):
    title = "fish"
    skin = "Their scale "

    ears_generator = FishEarsGenerator
    nose_generator = FishNoseGenerator
    skin_generator = FishSkinGenerator

    body_generator = BodyGenerator(
        ["a huge, powerful tail and small anal fin, ","a huge, muscular tail and small anal fin, ","a large, muscular tail and small anal fin, ","a large, powerful tail and small anal fin, ","a short, muscular tail and small anal fin, ","a long, powerful tail and small anal fin, ","a short, powerful tail and small anal fin, ","a long, muscular tail and small anal fin, ","a huge, powerful tail and small anal fin, ","a huge, muscular tail and long anal fin, ","a large, muscular tail and long anal fin, ","a large, powerful tail and long anal fin, ","a short, muscular tail and long anal fin, ","a long, powerful tail and long anal fin, ","a short, powerful tail and long anal fin, ","a long, muscular tail and long anal fin, "],
        ["two strong side fins and ","four strong side fins and ","six strong side fins and ","two side fins and ","four side fins and ","six side fins and ","two large side fins and ","four large side fins and ","six large side fins and ","two powerful side fins and ","four powerful sidefins and ","two huge side fins and ","four huge side fins and "],
        ["a huge dorsal fin","a small dorsal fin","a thick, long dorsal fin","a thin, long dorsal fin","a wide, sail-like dorsal fin","a ribbon-like dorsal fin","a long, ribbon-like dorsal fin","a short, ribbon-like dorsal fin","a huge, sail-like dorsal fin","a short, strong dorsal fin","a long, strong dorsal fin","a short, pointy dorsal fin","a long, pointy dorsal fin","a long, streamlined dorsal fin","a short, streamlined dorsal fin"],
    )


class InvertebrateRaceGenerator(RaceGenerator):
    title = "invertebrate"

    body_generator = BodyGenerator(
        ["two arms and ","four arms and ","six arms and ","four winged arms and ","two winged arms and ","six winged arms and ","two clawed arms and ","four clawed arms and ","two wings, two arms and ","four wings, two arms and ","two wings, four arms and ","four wings, four arms and ","two wings, six arms and ","two wings, two clawed arms and ","two clawed arms, two normal arms and "],
        ["two legs, ","four legs, ","six legs, ","four legs, ","two legs, "],
        ["but they have no tail","with a huge, powerful tail","with a long, muscular tail","with a long, powerful tail","with a long, strong and agile tail","with a long, strong tail","with a long, thick tail","with a long, thin tail","with a long, useless tail","with a long, weak tail","with a short, muscular tail","with a short, powerful tail","with a short, strong tail","with a short, stubby tail","with a short, thick tail","with a short, thin tail","with a short, useless tail","with a short, weak tail","with a thick, powerful tail","with remnants of what was once a tail"],
    )


class BirdRaceGenerator(RaceGenerator):
    title = "bird"
    skin = "Their feather "

    horns_generator = None
    ears_generator = BirdEarsGenerator
    mouth_generator = BeakGenerator
    nose_generator = None
    skin_generator = BirdSkinGenerator

    body_generator = BodyGenerator(
        ["two huge wings and ","four huge wings and ","two huge, powerful wings and ","four huge, powerful wings and ","two huge and two smaller wings and ","two enormous wings and ","four enormous wings and ","two large and four smaller wings and ","four smaller wings and ","two smaller wings and "],
        ["two strong, clawed legs, ","two small, clawed legs, ","four strong, clawed legs, ","four small, clawed legs, ","two strong legs, ","four strong legs, ","two small legs, ","four small legs, ","two thin, long legs, ","two long, strong legs, "],
        ["with a huge tail","with a huge, wide tail","with a huge, powerful tail","with a long, powerful tail","with a long, elegant tail","with a short, elegant tail","with a short, powerful tail","with a wide, powerful tail","with a wide, elegant tail","with a short tail"],
    )


class RandomRaceGenerator(RandomGenerator):
    data = [
        MammalRaceGenerator,
        AquaticRaceGenerator,
        AmphibianRaceGenerator,
        ReptileRaceGenerator,
        FishRaceGenerator,
        InvertebrateRaceGenerator,
        BirdRaceGenerator,
        MammalRaceGenerator,
    ]
