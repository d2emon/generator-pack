from genesys.generator import AlbumGenerator
from genesys.generator import BandGenerator

from .history import BoxHistory


class MediaItem:
    def __init__(self, name=None, author=None, opening=None):
        self.name = name or str(AlbumGenerator.generate())
        self.author = author or str(BandGenerator.generate())

        self.history = BoxHistory(opening)

    def __repr__(self):
        return "{item.name:<32} by {item.author:<32} {item.last_week:>16n}$ {item.total:>16n}$".format(
            item=self,
        )

    @property
    def next(self):
        return next(self.history)

    @property
    def weeks(self):
        return len(self.history) - 1

    @property
    def last_week(self):
        return self.history.last

    @property
    def total(self):
        return self.history.total()
