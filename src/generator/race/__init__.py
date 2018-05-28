from fixtures import race

from .generated import Generated
from .generators import *
from .face import *
from .fixtures import *



class Race(Generated):
    """
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

    """
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
    description_template = """
{short} {body}\n
{eyes}\n
{nose_mouth}\n{ears} {horns}\n
{skin}\n
{divercity}\n
\n\n\n
FACE
Eyes:\t{eyes}
Ears:\t{ears}
Nose:\t{nose}
Mouth:\t{mouth}
"""

    @property
    def nose_mouth(self):
        nose_mouth = [str(i) for i in [self.mouth, self.nose] if i is not None]
        text = "Their {} often make these aliens appear to be {}, but looks can be deceiving."
        return text.format(
            " and ".join(nose_mouth),
            self.appearance,
        )

    def __str__(self):
        return "These aliens are a type of {race_type}.".format(
            race_type=self.race_type,
        )

    @property
    def description(self):
        return self.description_template.format(
            short=str(self) or '',
            body=self.body or '',
            eyes=self.eyes or '',
            nose_mouth=self.nose_mouth or '',
            ears=self.ears or '',
            horns=self.horns or '',
            skin=self.skin or '',
            divercity=self.divercity or '',
            nose=self.nose or '',
            mouth=self.mouth or '',
        )
        # return text

    def __repr__(self):
        return """
Race type:\t{race}
Body:\t{body}
Appearance:\t{appearance}
Horns:\t{horns}
Ears:\t{ears}
Eyes:\t{eyes}
Nose:\t{nose}
Mouth:\t{mouth}
Skin:\t{skin}
Divercity:\t{divercity}
Divercity Color:\t{divercity_color}
        """.format(
            race=self.race_type,
            body=self.body,
            appearance=self.appearance,
            horns=self.horns,
            ears=self.ears,
            eyes=self.eyes,
            nose=self.nose,
            mouth=self.mouth,
            skin=self.skin,
            divercity=self.divercity,
            divercity_color=self.divercity_color
        )


class RaceGenerator:
    title = "mammal"
    skin = "skin"

    face_generator = FaceGenerator()
    body_generator = BodyGenerator(fixtures=RaceFixtures)
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
        if self.horns_generator is not None:
            horns = self.horns_generator.__next__()

        face = self.face_generator.generate(appearance[0], quality)

        return Race(
            race_type=self.title,
            body=self.body_generator.__next__(),
            appearance=appearance[1],
            horns=horns,
            skin=self.skin_generator.__next__(self.skin),
            divercity=self.divercity_generator.__next__(),
            **face,
        )


class MammalRaceGenerator(RaceGenerator):
    title = "mammal"


class AquaticRaceGenerator(RaceGenerator):
    title = "aquatic mammal"

    body_generator = BodyGenerator(fixtures=AquaticFixtures)
    horns_generator = AquaticHornsGenerator
    skin_generator = AquaticSkinGenerator



class AmphibianRaceGenerator(RaceGenerator):
    title = "amphibian"

    body_generator = BodyGenerator(fixtures=AmphibianFixtures)
    skin_generator = AmphibianSkinGenerator


class ReptileRaceGenerator(RaceGenerator):
    title = "reptile"
    skin = "scale "

    body_generator = BodyGenerator(fixtures=ReptileFixtures)
    skin_generator = ReptileSkinGenerator


class FishRaceGenerator(RaceGenerator):
    title = "fish"
    skin = "scale "

    face_generator = FaceGenerator(fixtures=FishFixtures)
    body_generator = BodyGenerator(fixtures=FishFixtures)
    skin_generator = FishSkinGenerator


class InvertebrateRaceGenerator(RaceGenerator):
    title = "invertebrate"

    body_generator = BodyGenerator(fixtures=InvertebrateFixtures)


class BirdRaceGenerator(RaceGenerator):
    title = "bird"
    skin = "feather "

    face_generator = FaceGenerator(fixtures=BirdFixtures)
    body_generator = BodyGenerator(fixtures=BirdFixtures)
    horns_generator = None
    # ears_generator = BirdEarsGenerator
    # mouth_generator = BeakGenerator
    # nose_generator = None
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
