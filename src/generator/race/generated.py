class Generated:
    title = "<UNTITLED>"
    fields = []

    def __init__(self, value=None, **kwargs):
        self.value = value
        for field in self.fields:
            setattr(self, field, kwargs.get(field))

    def __str__(self):
        return self.value


class Body(Generated):
    title = "Body"
    fields = [
        'part1',
        'part2',
        'part3',
    ]

    def __str__(self):
        return "They have {}{}{}.".format(
            getattr(self, 'part1', None),
            getattr(self, 'part2', None),
            getattr(self, 'part3', None),
        )


class Horns(Generated):
    title = "Horns"


class Skin(Generated):
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
        text += "{}colors are mostly {}, which tend to become {} as they age."
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
