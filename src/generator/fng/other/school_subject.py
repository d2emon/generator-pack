from generator.generator.generated import ListGenerated
from generator.generator.data_provider import ListProvider


from fixtures.other.school_subject import school_subjects


class SchoolSubject(ListGenerated):
    provider = ListProvider(school_subjects)
