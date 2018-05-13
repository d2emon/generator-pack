from . import Generated, FileGenerator


class SchoolSubject(Generated):
    title = "School Subject"


class SchoolSubjectGenerator(FileGenerator):
    generated_class = SchoolSubject
    data_file = "data/school-subjects.txt"
