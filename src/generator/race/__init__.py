from fixtures import race

from .generated import Generated
from .generators import *
from .face import *



class Race(Generated):
    fields = [
        'race_type',
        'body',
        'appearance',
        'horns',
        'ears',
        'eyes',
        'nose',
        'mouth',
        'skin',
        'divercity',
        'divercity_color',

    ]

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
        nose_mouth = [i.value for i in [self.mouth, self.nose] if i is not None]
        # if self.mouth is not None:
        #     nose_mouth.append(str(self.mouth))
        # if self.nose is not None:
        #     nose_mouth.append(str(self.nose))
        return "".join(nose_mouth)

    def __str__(self):
        return "These aliens are a type of {race_type}.".format(
            race_type=self.race_type,
        )

    @property
    def description(self):
        text = "Their {} often make these aliens appear to be {}, but looks can be deceiving."
        nose_mouth = text.format(
            self.nose_mouth,
            self.appearance,
        )

        text = "\n\n".join([
            "{short} {body}",
            "{eyes}",
            "{nose_mouth}\n{ears} {horns}",
            "{skin}",
            "{divercity}"
        ])
        return text.format(
            short=str(self) or '',
            body=self.body or '',
            eyes=self.eyes or '',
            nose_mouth=nose_mouth or '',
            ears=self.ears.value or '',
            horns=self.horns or '',
            skin=self.skin or '',
            divercity=self.divercity or '',
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

    body_generator = BodyGenerator(
        parts1=["a huge, powerful tail and small anal fin, ","a huge, muscular tail and small anal fin, ","a large, muscular tail and small anal fin, ","a large, powerful tail and small anal fin, ","a short, muscular tail and small anal fin, ","a long, powerful tail and small anal fin, ","a short, powerful tail and small anal fin, ","a long, muscular tail and small anal fin, ","a huge, powerful tail and small anal fin, ","a huge, muscular tail and long anal fin, ","a large, muscular tail and long anal fin, ","a large, powerful tail and long anal fin, ","a short, muscular tail and long anal fin, ","a long, powerful tail and long anal fin, ","a short, powerful tail and long anal fin, ","a long, muscular tail and long anal fin, "],
        parts2=["two arms and ","four arms and ","two strong side fins and ","four strong side fins and ","six strong side fins and ","two side fins and ","four side fins and ","six side fins and ","two large side fins and ","four large side fins and ","six large side fins and ","two powerful arms and ","four powerful arms and ","two powerful side fins and ","four powerful sidefins and ","two huge side fins and ","four huge side fins and "],
        parts3=["a huge dorsal fin","a small dorsal fin","a thick, long dorsal fin","a thin, long dorsal fin","a wide, sail-like dorsal fin","a ribbon-like dorsal fin","a long, ribbon-like dorsal fin","a short, ribbon-like dorsal fin","a huge, sail-like dorsal fin","a short, strong dorsal fin","a long, strong dorsal fin","a short, pointy dorsal fin","a long, pointy dorsal fin","a long, streamlined dorsal fin","a short, streamlined dorsal fin"],
    )
    horns_generator = AquaticHornsGenerator
    skin_generator = AquaticSkinGenerator



class AmphibianRaceGenerator(RaceGenerator):
    title = "amphibian"

    body_generator = BodyGenerator(
        parts3 = ["but they have no tail","with a huge, powerful tail","with a long, muscular tail","with a long, powerful tail","with a long, strong and agile tail","with a long, strong tail","with a long, thick tail","with a long, thin tail","with a long, useless tail","with a long, weak tail","with a short, muscular tail","with a short, powerful tail","with a short, strong tail","with a short, stubby tail","with a short, thick tail","with a short, thin tail","with a short, useless tail","with a short, weak tail","with a thick, powerful tail","with remnants of what was once a tail"],
    )
    skin_generator = AmphibianSkinGenerator


class ReptileRaceGenerator(RaceGenerator):
    title = "reptile"
    skin = "Their scale "

    body_generator = BodyGenerator(
        parts1=["two arms and two legs, ","two arms and four legs, ","two arms and six legs, ","four arms and two legs, ","four arms and four legs, ","four arms and six legs, ","six arms and two legs, ","six arms and four legs, ","two arms, but no legs, like a snake with arms, ","four arms, but no legs, like a snake with arms, ","six arms, but no legs, like a snake with arms, "],
        parts2=[""],
        parts3=["with a long, thin tail","with a long, thick tail","with a short, thin tail","with a short, thick tail","with remnants of what was once a tail","but they have no tail","with a long, strong and agile tail","with a short, strong tail","with a long, strong tail","with a short, muscular tail","with a long, muscular tail","with a long, weak tail","with a short, weak tail","with a long, useless tail","with a short, useless tail","with a short, stubby tail"],
    )
    skin_generator = ReptileSkinGenerator


class FishRaceGenerator(RaceGenerator):
    title = "fish"
    skin = "Their scale "

    body_generator = BodyGenerator(
        ["a huge, powerful tail and small anal fin, ","a huge, muscular tail and small anal fin, ","a large, muscular tail and small anal fin, ","a large, powerful tail and small anal fin, ","a short, muscular tail and small anal fin, ","a long, powerful tail and small anal fin, ","a short, powerful tail and small anal fin, ","a long, muscular tail and small anal fin, ","a huge, powerful tail and small anal fin, ","a huge, muscular tail and long anal fin, ","a large, muscular tail and long anal fin, ","a large, powerful tail and long anal fin, ","a short, muscular tail and long anal fin, ","a long, powerful tail and long anal fin, ","a short, powerful tail and long anal fin, ","a long, muscular tail and long anal fin, "],
        ["two strong side fins and ","four strong side fins and ","six strong side fins and ","two side fins and ","four side fins and ","six side fins and ","two large side fins and ","four large side fins and ","six large side fins and ","two powerful side fins and ","four powerful sidefins and ","two huge side fins and ","four huge side fins and "],
        ["a huge dorsal fin","a small dorsal fin","a thick, long dorsal fin","a thin, long dorsal fin","a wide, sail-like dorsal fin","a ribbon-like dorsal fin","a long, ribbon-like dorsal fin","a short, ribbon-like dorsal fin","a huge, sail-like dorsal fin","a short, strong dorsal fin","a long, strong dorsal fin","a short, pointy dorsal fin","a long, pointy dorsal fin","a long, streamlined dorsal fin","a short, streamlined dorsal fin"],
    )
    ears_generator = FishEarsGenerator
    nose_generator = FishNoseGenerator
    skin_generator = FishSkinGenerator


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

    body_generator = BodyGenerator(
        ["two huge wings and ","four huge wings and ","two huge, powerful wings and ","four huge, powerful wings and ","two huge and two smaller wings and ","two enormous wings and ","four enormous wings and ","two large and four smaller wings and ","four smaller wings and ","two smaller wings and "],
        ["two strong, clawed legs, ","two small, clawed legs, ","four strong, clawed legs, ","four small, clawed legs, ","two strong legs, ","four strong legs, ","two small legs, ","four small legs, ","two thin, long legs, ","two long, strong legs, "],
        ["with a huge tail","with a huge, wide tail","with a huge, powerful tail","with a long, powerful tail","with a long, elegant tail","with a short, elegant tail","with a short, powerful tail","with a wide, powerful tail","with a wide, elegant tail","with a short tail"],
    )
    horns_generator = None
    ears_generator = BirdEarsGenerator
    mouth_generator = BeakGenerator
    nose_generator = None
    skin_generator = BirdSkinGenerator


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
