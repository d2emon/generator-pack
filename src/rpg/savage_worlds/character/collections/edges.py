from .collection import Collection
from rpg.savage_worlds.savage_worlds.edge import Edge, Hindrance


class CharacterEdges(Collection):
    def __init__(self):
        super().__init__([])

    @property
    def edges(self):
        return list(self.search(Edge))

    @property
    def hindrances(self):
        return list(self.search(Hindrance))

    @property
    def minor_hindrances(self):
        return [item for item in self.hindrances if not item.is_big]

    @property
    def major_hindrances(self):
        return [item for item in self.hindrances if item.is_big]

    def set_values(self, items):
        self.items = items
