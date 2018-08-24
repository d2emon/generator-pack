from generator.generator import ListGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import FileData


class SchoolSubject(Generated):
    title = "School Subject"


class SchoolSubjectGenerator(ListGenerator):
    generated_class = SchoolSubject
    data = { 'name': FileData("data/school-subjects.txt") }
