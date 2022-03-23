from factories.dict_factory import DictFactory
# TODO: Fix circular
# from genesys.generator_models.character import Strange


# TODO: Remove it
class Strange:
    pass


class StrangeFactory(DictFactory):
    generated_class = Strange
    descriptions = [
        "alluring",
        "ambiguous",
        "appealing",
        "bewildering",
        "bizarre",
        "captivating",
        "charming",
        "curious",
        "different",
        "enigmatic",
        "enthralling",
        "enticing",
        "extraordinary",
        "fascinating",
        "incomprehensible",
        "inexplicable",
        "intriguing",
        "irregular",
        "misleading",
        "mystifying",
        "obscure",
        "odd",
        "puzzling",
        "seductive",
        "wonderful",
    ]
    weirdnesses = [
        "a feeling of anguish",
        "a feeling of arogance",
        "a feeling of coldness",
        "a feeling of comfort",
        "a feeling of delight",
        "a feeling of guilt",
        "a feeling of hospitality",
        "a feeling of indifference",
        "a feeling of joy",
        "a feeling of regret",
        "a feeling of remorse",
        "a feeling of sadness",
        "a feeling of shame",
        "{{his}} attitude",
        "{{his}} bravery",
        "{{his}} clumsiness",
        "{{his}} company",
        "{{his}} composure",
        "{{his}} decency",
        "{{his}} disposition",
        "{{his}} fortunate past",
        "{{his}} friendly demeanor",
        "{{his}} gentleness",
        "{{his}} good looks",
        "{{his}} good will",
        "{{his}} goodwill",
        "{{his}} hatred",
        "{{his}} humility",
        "{{his}} kindness",
        "{{his}} odd companions",
        "{{his}} odd friends",
        "{{his}} painful past",
        "{{his}} patience",
        "{{his}} perseverance",
        "{{his}} persistence",
        "{{his}} personality",
        "{{his}} presence",
        "{{his}} reputation",
        "{{his}} sense of comradery",
        "{{his}} sense of honor",
        "{{his}} sense of humor",
        "{{his}} sense of justice",
        "{{his}} sensitivity",
        "{{his}} suffering",
        "{{his}} sympathy",
        "{{his}} tenderness",
        "{{his}} unfortunate past",
        "{{his}} unusual alliances",
        "{{his}} unusual looks",
        "{{his}} warmth",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.description = cls.generate_value(cls.descriptions)
        generated.weirdnesses = cls.generate_value(cls.weirdnesses, count=2)
        return generated
