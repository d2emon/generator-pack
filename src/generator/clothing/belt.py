from generator import Generated, ListGenerator


class Belt(Generated):
    def __init__(self):
        self.size = "thin"
        self.name = "leather belt"
        self.buckle = "a big belt buckle"
        self.decoration = "purely decorative and a sign of wealth",

    def __repr__(self):
        return self.name

    @property
    def description(self):
        return "%s %s, which is held together by %s" % (
            self.size,
            self.name,
            self.buckle,
        )


class BeltGenerator(ListGenerator):
    generated_class = Belt
    sizes = [
        "thin",
        "thick",
        "simple",
        "small",
        "big",
        "light",
        "dark",
        "large",
        "long",
        "wide",
        "small",
    ]
    names = [
        "leather belt",
        "cloth belt",
        "rope belt",
        "cloth band",
    ]
    buckles = [
        "a big belt buckle",
        "a simple knot",
        "a small belt buckle",
        "an intricate knot",
        "an ornate pin",
        "a decorative pin",
    ]
    decorations = [
        "purely decorative and a sign of wealth",
        "mostly decorative and a sign of wealth",
        "entirely decorative and a way to show off",
        "solely decorative and a status symbol",
        "mostly decorative, but does serve its purpose",
        "partially decorative, but mostly a purposeful addition",
        "slightly decorative, but mostly there to hang things from",
        "almost entirely a functional addition",
        "purely a functional addition",
        "a functional addition, but does have some decorative value",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.size = cls.generate_value(cls.sizes)
        generated.name = cls.generate_value(cls.names)
        generated.buckle = cls.generate_value(cls.buckles)
        generated.decoration = cls.generate_value(cls.decorations)
        return generated
