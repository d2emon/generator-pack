from generator import Generated, ListGenerator


class SleeveLength():
    def __init__(self, name="long", is_long= False):
        self.name = name
        self.is_long = is_long

    def __repr__(self):
        return self.name


class Sleeves(Generated):
    def __init__(self):
        self.length = SleeveLength("long", True)
        self.width = "incredibly wide"
        self.reach = "his hands"
        self.decoration = "a single thread lining from top to bottom"

    def __repr__(self):
        return "%s and reach down to %s, they're decorated with %s" % (
            self.width,
            self.reach,
            self.decoration,
        )


class SleevesGenerator(ListGenerator):
    generated_class = Sleeves
    lengths = [
        SleeveLength("long", True),
        SleeveLength("very long", True),
        SleeveLength("fairly long", True),
        SleeveLength("short"),
        SleeveLength("very short"),
        SleeveLength("fairly short"),
    ]
    widths = [
        "incredibly wide",
        "very wide",
        "quite wide",
        "wide",
        "a little wide",
        "narrow",
        "quite narrow",
        "a little narrow",
        "a comfortable fit",
        "a loose fit",
    ]
    reachs = [
        "his hands",
        "just above his hands",
        "well below his hands",
        "below his hands",
        "well above his hands",
        "his wrists",
        "just below his wrists",
        "just above his wrists",
        "well above his wrists",
        "well below his wrists",
    ]
    decorations = [
        "a single thread lining from top to bottom",
        "several thread linings from top to bottom",
        "a single thread lining at the sleeve ends",
        "several thread linings at the sleeve ends",
        "a decorative band at the edges",
        "a decorative band almost at the edges",
        "a single thread lining and a decorative band",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.length = cls.generate_value(cls.lengths)
        generated.width = cls.generate_value(cls.widths)
        generated.reach = cls.generate_value(cls.reachs)
        generated.decoration = cls.generate_value(cls.decorations)
        return generated
