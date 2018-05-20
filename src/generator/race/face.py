from num2words import num2words

from fixtures import race
from generator.generator.generator_data import ListData
from generator import Generated


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
        return "{} eyes".format(num2words(self.count, lang=self.lang))

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
        return Nose(value=next(cls.noses))


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
