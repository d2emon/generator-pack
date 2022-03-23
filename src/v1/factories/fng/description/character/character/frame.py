from factories.dict_factory import DictFactory
# TODO: Fix circular and uncomment
# from genesys.generator_models.character import Frame


# TODO: Remove it
class Frame:
    pass


class FrameFactory(DictFactory):
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
