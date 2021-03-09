from factories.generator import Generated
from num2words import num2words


class Limbs(Generated):
    @property
    def count(self):
        if type(self.value) is dict:
            return self.value.get('count')
        return self.value

    @property
    def countText(self):
        return num2words(self.count)

    @property
    def description(self):
        if type(self.value) is dict:
            return self.value.get('description')
        return ''


class Arms(Limbs):
    title = "Arms"

    def __str__(self):
        return "{}{} arms".format(self.countText, self.description)


class WingedArms(Limbs):
    title = "Winged arms"

    def __str__(self):
        return "{}{} winged arms".format(self.countText, self.description)


class ClawedArms(Limbs):
    title = "Clawed arms"

    def __str__(self):
        return "{}{} clawed arms".format(self.countText, self.description)


class Legs(Limbs):
    title = "Legs"

    def __str__(self):
        return " and {}{} legs, ".format(self.countText, self.description)


class Wings(Limbs):
    title = "Wings"

    def __str__(self):
        return "{}{} wings".format(self.countText, self.description)


class SideFins(Limbs):
    title = "Side fins"

    def __str__(self):
        return "{}{} side fins".format(self.countText, self.description)


class DorsalFin(Limbs):
    title = "Dorsal fin"

    def __str__(self):
        return "a {}{} dorsal fin".format(self.countText, self.description)


class Tail(Generated):
    title = "Tail"

    def __init__(self, value=dict(), **kwargs):
        value.update(kwargs)
        self.length = value.get('length')
        self.text = value.get('description')
        self.remnants = value.get('remnants', False)

    def __str__(self):
        if self.remnants:
            return "with remnants of what was once a tail"
        return "with a {}{} tail".format(
            self.length or '',
            self.text or ''
        )
