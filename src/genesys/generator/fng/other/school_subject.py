from genesys.generator import Generated
from genesys.generator import ListProvider


from fixtures.other.school_subject import school_subjects


class SchoolSubject(Generated):
    provider = ListProvider(school_subjects)
