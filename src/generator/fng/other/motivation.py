from generator.generator.generated import ListGenerated
from generator.generator.generator_data import FileData


class CharacterGoal(ListGenerated):
    data = {'value': FileData("data/motivation.txt")}
