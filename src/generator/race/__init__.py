from fixtures import race

from .generated import Generated
from .generators import *
from .face import *
from .fixtures import *



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
    description_template = """
{short} They have {body}.\n
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
            short=str(self),
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
\tARMS:\t{body.arms}
\tSIDE_FINS:\t{body.side_fins}
\tDORSAL_FIN:\t{body.dorsal_fin}
\tWINGS:\t{body.wings}
\tLEGS:\t{body.legs}
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
    title = "UNKNOWN"
    skin = "skin"
    fixtures = RaceFixtures

    def __init__(self, fixtures=None):
        fixtures = fixtures or self.fixtures

        self.face_generator = FaceGenerator(fixtures=fixtures)
        self.body_generator = BodyGenerator(fixtures=fixtures)
        self.horns_generator = fixtures.horns_generator
        # self.ears_generator = fixtures.ears_generator
        # self.eyes_generator = fixtures.eyes_generator
        # self.nose_generator = fixtures.nose_generator
        # self.mouth_generator = fixtures.mouth_generator
        self.skin_generator = fixtures.skin_generator

        self.divercity_generator = DivercityGenerator

        self.appearance_data = ListData(race.appearances)
        self.quality_data = ListData(race.qualities)

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
    fixtures = AquaticFixtures


class AmphibianRaceGenerator(RaceGenerator):
    title = "amphibian"
    fixtures = AmphibianFixtures


class ReptileRaceGenerator(RaceGenerator):
    title = "reptile"
    skin = "scale "
    fixtures = ReptileFixtures


class FishRaceGenerator(RaceGenerator):
    title = "fish"
    skin = "scale "
    fixtures = FishFixtures


class InvertebrateRaceGenerator(RaceGenerator):
    title = "invertebrate"
    fixtures = InvertebrateFixtures


class BirdRaceGenerator(RaceGenerator):
    title = "bird"
    skin = "feather "
    fixtures = BirdFixtures


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
