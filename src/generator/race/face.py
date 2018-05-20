from num2words import num2words

from generator import ListData, Generated

from .fixtures import RaceFixtures, FishFixtures, BirdFixtures


lang = 'en'


class FacePart(Generated):
    def __str__(self):
        return self.value or ''


class Nose(FacePart):
    title = "Nose"


class Mouth(FacePart):
    title = "Mouth"


class Eyes(FacePart):
    title = "Eyes"
    fields = [
        'count',
        'sockets',
        'appearance',
        'quality',
    ]

    @property
    def count_str(self):
        return "{} eyes".format(num2words(self.count, lang=lang))

    def __str__(self):
        text = "They have {} which sit {} in their sockets and can often make them appear to be {}. Their eyesight is {}."
        return text.format(
            self.count_str,
            self.sockets,
            self.appearance,
            self.quality,
        )


class Ears(FacePart):
    title = "Ears"
    fields = [
        'ears',
        'quality',
    ]

    def __str__(self):
        return "Their ears are {} and their hearing is {}.".format(
            self.ears,
            self.quality,
        )


class BaseGenerator:
    generated_class = Generated
    default_data = None

    def __init__(self, data=None):
        self.data = data or self.default_data

    def generate(self):
        if self.data is None:
            return None
        return self.generated_class(next(self.data))

    @classmethod
    def __next__(cls):
        return cls.generated_class(next(cls.data))


class EyesGenerator(BaseGenerator):
    generated_class = Eyes
    count = RaceFixtures.eyes_count
    eyesockets = RaceFixtures.eyesockets

    def generate(self, appearance, quality):
        return self.generated_class(
            count = next(self.count),
            sockets = next(self.eyesockets),
            appearance=appearance,
            quality=quality,
        )

    @classmethod
    def __next__(cls, appearance, quality):
        return cls.generated_class(
            count=next(cls.count),
            sockets=next(cls.eyesockets),
            appearance=appearance,
            quality=quality,
        )


class MouthGenerator(BaseGenerator):
    generated_class = Mouth
    data = RaceFixtures.mouths


class NoseGenerator(BaseGenerator):
    generated_class = Nose
    data = RaceFixtures.noses


class EarsGenerator(BaseGenerator):
    generated_class = Ears
    data = RaceFixtures.ears

    def generate(self, quality):
        return self.generated_class(
            ears=next(self.data),
            quality=quality,
        )

    @classmethod
    def __next__(cls, quality):
        return cls.generated_class(
            ears=next(cls.data),
            quality=quality,
        )


class FaceGenerator:
    default_fixtures = RaceFixtures

    def __init__(self, fixtures=None, data=None):
        # BaseGenerator.__init__(self, data)
        self.fixtures = fixtures or self.default_fixtures

        self.eyes_generator = EyesGenerator(self.fixtures)
        self.ears_generator = EarsGenerator(self.fixtures.ears)
        self.nose_generator = NoseGenerator(self.fixtures.noses)
        self.mouth_generator = MouthGenerator(self.fixtures.mouths)

    def generate(self, appearance, quality):
        return {
            'eyes': self.eyes_generator.generate(appearance, quality[0]),
            'ears': self.ears_generator.generate(quality[1]),
            'nose': self.nose_generator.generate(),
            'mouth':self.mouth_generator.generate()
        }


class FishFaceGenerator(FaceGenerator):
    default_fixtures = FishFixtures


class BirdFaceGenerator(FaceGenerator):
    default_fixtures = BirdFixtures
