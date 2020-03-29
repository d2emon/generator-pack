from .collection import Collection
from .. import edge


class CharacterEdges(Collection):
    def __init__(self):
        super().__init__([])

    @property
    def edges(self):
        return [e for e in self.items if isinstance(e, edge.Edge)]

    @property
    def hindrances(self):
        return [e for e in self.items if isinstance(e, edge.Hindrance)]

    @property
    def value(self):
        return sum(e.cost for e in self.items)

    def set_edges(self, edges):
        self.items = [e() for e in edges]
