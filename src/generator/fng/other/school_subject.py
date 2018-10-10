from generator.generator.generated import Generated
from generator.generator.data_provider import ListProvider


from fixtures.other.school_subject import school_subjects


class SchoolSubject(Generated):
    provider = ListProvider(school_subjects)
