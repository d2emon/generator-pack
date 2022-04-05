from factories.list_factory import ListFactory
from factories.generator import Generated


from data.fixtures.fixtures import school_subjects


class SchoolSubject(Generated):
    provider = ListFactory(school_subjects)
