from genesys.model.model import Model
from .elements import Atom
from .matter import Matter


class Fire(Model):
    content = Model.child_property(Atom)

    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('C'),
            kwargs.get('O'),
        ]


class Ash(Matter):
    contents = Matter.children_property(Matter)

    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('organic_matter'),
            kwargs.get('C'),
        ]
