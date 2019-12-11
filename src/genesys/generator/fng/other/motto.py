from genesys.generator import Generated
from genesys.generator import ListProvider


from fixtures.other import mottos


class Motto(Generated):
    provider = ListProvider(mottos)
