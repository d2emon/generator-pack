from providers.list_provider import ListProvider
from factories.generator import Generated


from genesys.fixtures.fixtures import school_subjects


class SchoolSubject(Generated):
    provider = ListProvider(school_subjects)
