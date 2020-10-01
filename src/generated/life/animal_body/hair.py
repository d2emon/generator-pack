"""
- Hair
- Fur
- Whiskers
"""
from genesys.model.model import Model
from ...materials import Keratin


class Hair(Model):
    # bacterias = Model.child_property(Bacteria)
    keratin = Model.child_property(Keratin)


class Fur(Hair):
    pass


class Whiskers(Hair):
    pass
