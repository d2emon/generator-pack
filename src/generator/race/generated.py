from generator import Generated


class Body(Generated):
    title = "Body"
    fields = [
        'arms',
        'winged_arms',
        'clawed_arms',
        'wings',
        'legs',
        'tail',
        'side_fins',
        'dorsal_fin',
        'part1',
        'part2',
        'part3',
    ]

    def __str__(self):
        arms = ", ".join([str(i) for i in [
            self.side_fins,
            self.wings,
            self.winged_arms,
            self.clawed_arms,
            self.arms,
        ] if i is not None])
        return "{}{}{}({}{}{})".format(
            arms,
            self.legs or ', but no legs, like a snake with arms, ',
            self.tail or 'but they have no tail',
            self.part1 or '',
            self.part2 or '',
            self.part3 or '',
        )


class BodyParts(Generated):
    def __str__(self):
        return str(self.value)


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
        return "{} and {}".format(
            ", ".join([c for c in self.colors[:-1] if c is not None]),
            self.colors[-1]
        )

    def __str__(self):
        text = """Their skin is {} {}
Their {} colors are mostly {}, which tend to become {} as they age."""
        return text.format(
            self.skin_type,
            self.cover or '',
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
