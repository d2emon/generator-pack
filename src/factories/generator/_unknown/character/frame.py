from factories.generator import Generated, ListGenerator


class Frame(Generated):
    def __init__(self):
        self.height = "tall among"
        self.frame = "thin"

    def __repr__(self):
        return "{{He}} stands %s others, despite {{his}} %s frame." % (
            self.height,
            self.frame,
        )


class FrameGenerator(ListGenerator):
    generated_class = Frame
    heights = [
        "tall among",
        "short among",
        "towering among",
        "towering above",
        "tall above",
        "big among",
        "high among",
        "small among",
        "average among",
        "ordinary among",
        "common among",
        "oddly among",
        "awkwardly among",
        "gracefully among",
        "graciously among",
        "elegantly among",
        "easily among",
        "tiny among",
        "seductively among",
        "alluringly among",
    ]
    frames = [
        "thin",
        "big",
        "fragile",
        "delicate",
        "lean",
        "narrow",
        "skinny",
        "slim",
        "light",
        "subtle",
        "scraggy",
        "bulky",
        "heavy",
        "hefty",
        "athletic",
        "brawny",
        "sturdy",
        "strong",
        "muscled",
        "tough",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.height = cls.generate_value(cls.heights)
        generated.frame = cls.generate_value(cls.frames)
        return generated
