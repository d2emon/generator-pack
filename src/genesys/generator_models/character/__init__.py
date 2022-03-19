from ..generator_models import Model
from v1.factories.fng.description.character.character import FrameFactory
from v1.factories.fng.description.character.character.strange import StrangeFactory


class Character(Model):
    frame_generator = FrameFactory
    strange_generator = StrangeFactory

    def __init__(self, race=None, sex=Male):
        if race is None:
            race = Race
        self.sex = sex
        self.race = race
        self.generate()

    def generate(self):
        if self.sex.id == 1:
            specials = female_specials
        else:
            specials = male_specials
        special_generator = random.choice(specials)

        g = self.race.generators(self.sex.id)
        self.hair = g.hair.generate()
        self.face = g.face.generate()
        self.eyes = g.eyes.generate()
        self.promise = g.promise.generate()
        self.special = special_generator.generate()
        self.name = g.name.generate()
        self.frame = self.frame_generator.generate()
        self.strange = self.strange_generator.generate()
        self.attitude = g.attitude.generate()
        self.clothing = ClothingGenerator.generate(self.sex)

    @property
    def description(self):
        head = "%s a %s. %s over %s" % (
            self.hair,
            self.face,
            self.eyes,
            self.promise,
        )
        title = "This is the face of %s among %s. %s" % (
            self.name,
            self.race.plural,
            self.frame,
        )
        personality = "%s But nonetheless, %s." % (
            self.strange,
            self.attitude,
        )

        description = "\n".join([
            head,
            str(self.special),
            title,
            personality,
        ])

        for k, v in self.sex.replaces.items():
            description = description.replace(k, v)
        return description
