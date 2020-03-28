from models.models import Model
from factories.factories.list_factory import ListFactory
from .belt import SleeveBandGenerator


class SleeveLength:
    def __init__(self, name="long", is_long= False):
        self.name = name
        self.is_long = is_long

    def __repr__(self):
        return self.name


class Sleeves(Model):
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


class DressSleevesGenerator(SleevesGenerator):
    lengths = [
        SleeveLength("very long", True),
        SleeveLength("quite long", True),
        SleeveLength("a little too long", True),
        SleeveLength("purposely too long", True),
        SleeveLength("incredibly long", True),
        SleeveLength("the length of her arms", True),
        SleeveLength("longer than her arms", True),
        SleeveLength("slightly shorter than her arms", True),
        SleeveLength("almost the length of her arms", True),
        SleeveLength("fairly short"),
        SleeveLength("a little short"),
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
    change_positions = [
        "just below the shoulder",
        "just below the elbow",
        "just above the elbow",
        "below the shoulder",
        "below the elbow",
        "above the elbow",
        "well below the shoulder",
        "well below the elbow",
        "well above the elbow",
        "at the elbow",
        "at the shoulder",
    ]
    change_types = [
        "they change color and where ",
        "",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.length = cls.generate_value(cls.lengths)
        generated.width = cls.generate_value(cls.widths)
        generated.reach = cls.generate_value(cls.reachs)
        generated.decoration = cls.generate_value(cls.decorations)
        generated.change_position = cls.generate_value(cls.change_positions)
        generated.change_type = cls.generate_value(cls.change_types)
        generated.bands = SleeveBandGenerator.generate()
        return generated
