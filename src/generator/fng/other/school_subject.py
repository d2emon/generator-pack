from generator.generator.generated import ListGenerated
from generator.generator.generator_data import FileData


class SchoolSubject(ListGenerated):
    data = {'value': FileData("data/school-subjects.txt")}
