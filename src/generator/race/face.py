from num2words import num2words

from generator import ListData, Generated

from .fixtures import RaceFixtures, FishFixtures, BirdFixtures


lang = 'en'


class FacePart(Generated):
    def __str__(self):
        return self.value


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


class EyesGenerator:
    count = RaceFixtures.eyes_count
    eyesockets = RaceFixtures.eyesockets

    @classmethod
    def __next__(cls, appearance, quality):
        return Eyes(
            count=next(cls.count),
            sockets=next(cls.eyesockets),
            appearance=appearance,
            quality=quality,
        )


class MouthGenerator:
    mouths = RaceFixtures.mouths

    @classmethod
    def __next__(cls):
        return Mouth(next(cls.mouths))


class NoseGenerator:
    noses = RaceFixtures.noses

    @classmethod
    def __next__(cls):
        return Nose(value=next(cls.noses))


class FishNoseGenerator(NoseGenerator):
    noses = FishFixtures.noses


class BeakGenerator(MouthGenerator):
    noses = BirdFixtures.noses


class EarsGenerator:
    ears = RaceFixtures.ears

    @classmethod
    def __next__(cls, quality):
        return Ears(
            ears=next(cls.ears),
            quality=quality,
        )


class FishEarsGenerator(EarsGenerator):
    ears = FishFixtures.ears


class BirdEarsGenerator(EarsGenerator):
    ears = BirdFixtures.ears
