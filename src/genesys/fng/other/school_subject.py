from factories.list_factory import ListFactory
from models.fng.names.name import Name
from data.fixtures.fixtures import school_subjects


class SchoolSubject(Name):
    provider = ListFactory(school_subjects)
