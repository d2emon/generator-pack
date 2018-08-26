from generator.generator.generated import Generated
from generator.generator.generator_data import ListData

from fixtures.other.riddle import riddle


class Riddle(Generated):
    data = ListData(riddle)

    def __init__(self, question, answer=""):
        super().__init__(question)
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question

    def __repr__(self):
        return "Question: {}\nAnswer: {}\n".format(self.question, self.answer)

    @classmethod
    def generate(cls):
        next_data = next(cls.data)
        return cls(*next_data)
