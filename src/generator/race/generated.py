from num2words import num2words

from generator import Generated


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


class Legs(Limbs):
    title = "Legs"

    def __str__(self):
        return " and {}{} legs, ".format(self.countText, self.description)


class Wings(Limbs):
    title = "Wings"

    def __str__(self):
        return "{}{} wings and".format(self.countText, self.description)


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


class Body(Generated):
    title = "Body"
    fields = [
        'arms',
        'wings',
        'legs',
        'tail',
        'part1',
        'part2',
        'part3',
    ]

    def __str__(self):
        return "They have {}{}{}{}({}{}{}).".format(
            self.arms or '',
            self.wings or '',
            self.legs or ', but no legs, like a snake with arms, ',
            self.tail or 'but they have no tail',
            self.part1 or '',
            self.part2 or '',
            self.part3 or '',
        )


class BodyParts(Generated):
    def __str__(self):
        return self.value


class Horns(BodyParts):
    title = "Horns"


class Skin(BodyParts):
    title = "Skin"
    fields = [
        'skin_type',
        'cover',
        'skin',
        'colors',
        'aging',
    ]

    @property
    def color(self):
        return "".join(self.colors)

    def __str__(self):
        cover = ""
        if self.cover is not None:
            cover = self.cover
        text = "Their skin is {} {}\n"
        text += "Their {} colors are mostly {}, which tend to become {} as they age."
        return text.format(
            self.skin_type,
            cover,
            self.skin,
            self.color,
            self.aging,
        )


class Divercity(Generated):
    title = "Divercity"
    fields = [
        'm',
        'f',
        'color',
    ]

    def __str__(self):
        return "The males are usually {m} than their female counter part and their colors are {color}. The females, however, are usually {f}.".format(
            m=self.m,
            f=self.f,
            color=self.color,
        )
