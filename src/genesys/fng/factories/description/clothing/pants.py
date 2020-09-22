class PantsGenerator(SleevesGenerator):
    generated_class = Pants
    styles = [
        "rough",
        "elegant",
        "fancy",
        "graceful",
        "luxurious",
        "relatively simple",
        "majestic",
        "modest",
        "noble",
        "ornate",
        "rather simple",
        "refined",
        "stylish",
        "traditional",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.width = cls.generate_value(cls.widths)
        generated.style = cls.generate_value(cls.styles)
        return generated
