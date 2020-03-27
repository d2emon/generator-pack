from factories.generator import Generated
from factories.generator import ListProvider


from sample_data.fixtures import school_subjects


class SchoolSubject(Generated):
    provider = ListProvider(school_subjects)
