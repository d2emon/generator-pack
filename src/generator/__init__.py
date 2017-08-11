class Generated():
    def __init__(self):
        self.generated_text = ""


class DataGenerator():
    generated_class = Generated

    @classmethod
    def generate_text(cls):
        raise AttributeError("No text to generate")

    @classmethod
    def generate(cls):
        generated = cls.generated_class()
        generated.generated_text = cls.generate_text()
        return generated

    @classmethod
    def generate_count(cls, count=1):
        return [cls.generate() for c in count]
