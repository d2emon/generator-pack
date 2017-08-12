from . import Generated, FileGenerator


class SchoolSubject(Generated):
    def __repr__(self):
        return "School Subject: \"%s\"" % (self.generated_text)


class SchoolSubjectGenerator(FileGenerator):
    generated_class = SchoolSubject
    data_file = "data/school-subjects.txt"
