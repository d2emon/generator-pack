from generator.generator.generated import ListGenerated
from generator.generator.data_provider import FileProvider


class SchoolSubject(ListGenerated):
    provider = FileProvider("data/school-subjects.txt")
