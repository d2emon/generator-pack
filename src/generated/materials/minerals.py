from ..model import Model
from .matter import Matter


class Rock:
    contents = Matter.children_property(Matter)

    def __init__(self, **kwargs):
        self.contents = [
            kwargs.get('Si'),
            kwargs.get('Al'),  # 30
            kwargs.get('Fe'),  # 20
            kwargs.get('K'),  # 20
            kwargs.get('Na'),  # 50
            kwargs.get('Ca'),  # 50
        ]


class Silica(Rock):
    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('Si'),
            kwargs.get('O'),
        ]


class Diamond(Rock):
    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('C'),
        ]


class Magma(Rock):
    pass


class Iron(Rock):
    pass


class Salt(Matter):
    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('Ch'),
            kwargs.get('Na'),
        ]
