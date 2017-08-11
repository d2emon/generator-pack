from . import Generated, ParamGenerator, GeneratorTemplate


class StoryConcept(Generated):
    def __repr__(self):
        return "StoryConcept: \"%s\"" % (self.generated_text)


class StoryConceptGenerator(ParamGenerator):
    generated_class = StoryConcept

    @classmethod
    def character(cls):
        return GeneratorTemplate.generate(
            "data/story-concept/character1.txt",
            "data/story-concept/character2.txt",
        )

    @classmethod
    def event(cls):
        return GeneratorTemplate.generate(
            "data/story-concept/event1.txt",
            "data/story-concept/event2.txt",
        )

    @classmethod
    def generate_text(cls, character=False):
        if character:
            return cls.character()
        else:
            return cls.event()
