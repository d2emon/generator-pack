from .special import SpecialSignGenerator
from .race import Race


class Character():
    def __init__(self):
        self.race = Race

    def generate(self):
        self.hair = self.race.hair_generator.generate()
        self.face = self.race.face_generator.generate()
        self.eyes = self.race.eyes_generator.generate()
        self.promise = self.race.promise_generator.generate()
        self.special= SpecialSignGenerator.generate()

    @property
    def description(self):
        head = "%s a %s. %s over %s" % (
            self.hair,
            self.face,
            self.eyes,
            self.promise,
        )
        # name3 = "This is the face of %s %s, a true %s among %s. He stands %s others, despite his %s frame." % (
        #     first_name,
        #     last_name,
        #     random20,
        #     race,
        #
        #     random22,
        #     random23,
        # )
        # name4 = "There's something %s about him, perhaps it's %s or perhaps it's simply %s. But nonetheless, people tend to %s, while %s." % (
        #     random24,
        #     random25,
        #     random26,
        #
        #     random27,
        #     random28,
        # )

        return "\n".join([
            head,
            str(self.special),
            # name3,
            # name4,
        ])
