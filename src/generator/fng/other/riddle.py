from generator.generator.generated import ListGenerated
from generator.generator.data_provider import ListProvider

from fixtures.other.riddle import riddle


class Riddle(ListGenerated):
    provider = ListProvider(riddle)

    def __init__(self, args):
        question, answer = args
        super().__init__(question)
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question

    def __repr__(self):
        return "Question: {}\nAnswer: {}\n".format(self.question, self.answer)
