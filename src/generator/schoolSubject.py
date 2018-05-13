from .generator import FileGenerator
from .generator.generated import Generated


class SchoolSubject(Generated):
    title = "School Subject"


class SchoolSubjectGenerator(FileGenerator):
    generated_class = SchoolSubject
    data_file = "data/school-subjects.txt"
