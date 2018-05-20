from generator import Generated


class Body(Generated):
    title = "Body"
    fields = [
        'part1',
        'part2',
        'part3',
    ]

    def __str__(self):
        return "They have {}{}{}.".format(
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
