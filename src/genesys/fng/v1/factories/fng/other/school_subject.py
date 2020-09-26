from providers import ListProvider
from factories.generator import Generated


from genesys.fixtures.fixtures import school_subjects


class SchoolSubject(Generated):
    provider = ListProvider(school_subjects)
