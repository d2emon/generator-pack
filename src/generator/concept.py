from . import Generated, ParamGenerator, GeneratorTemplate


class ArtConcept(Generated):
    def __repr__(self):
        return "ArtConcept: \"%s\"" % (self.generated_text)


class StoryConcept(Generated):
    def __repr__(self):
        return "StoryConcept: \"%s\"" % (self.generated_text)


class ArtConceptGenerator(ParamGenerator):
    generated_class = ArtConcept

    @classmethod
    def generate_place(cls):
        return GeneratorTemplate.generate([
            "data/art-concept/place1.txt",
            "data/art-concept/place2.txt",
        ])

    @classmethod
    def generate_being(cls):
        return GeneratorTemplate.generate([
            "data/art-concept/being1.txt",
            "data/art-concept/being2.txt",
        ])

    @classmethod
    def generate_value(cls, being=False):
        if being:
            return cls.generate_being()
        else:
            return cls.generate_place()


class StoryConceptGenerator(ParamGenerator):
    generated_class = StoryConcept

    @classmethod
    def character(cls):
        return GeneratorTemplate.generate([
            "data/story-concept/character1.txt",
            "data/story-concept/character2.txt",
        ])

    @classmethod
    def event(cls):
        return GeneratorTemplate.generate([
            "data/story-concept/event1.txt",
            "data/story-concept/event2.txt",
        ])

    @classmethod
    def generate_value(cls, character=False):
        if character:
            return cls.character()
        else:
            return cls.event()
