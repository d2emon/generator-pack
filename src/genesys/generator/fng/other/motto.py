from genesys.generator import Generated
from genesys.generator import ListProvider


from sample_data.fixtures import mottos


class Motto(Generated):
    provider = ListProvider(mottos)
