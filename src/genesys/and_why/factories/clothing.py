from factories.factory import Factory
from .slot import SlotFactory
from ..providers import PROVIDER


class Subfactories:
    def __init__(self, data):
        self.slot = SlotFactory(data)


class ClothingFactory(Factory):
    def __init__(self, data=None):
        super().__init__(data or PROVIDER)
        self.__subfactories = Subfactories(self.data_provider)

    def __call__(
        self,
        gender=None,
        items=None,
        *args,
        **kwargs,
    ):
        to_fill = items or self.data_provider.by_gender(gender)

        if not to_fill:
            return

        slots = self.__subfactories.slot()
        for slot in slots:
            item = to_fill.by_slot(slot).random()
            if item is not None:
                yield item

    def fill(
        self,
        doll,
        items=None,
        *args,
        **kwargs,
    ):
        to_fill = self(
            gender=doll.gender,
            items=items,
            *args,
            **kwargs,
        )

        for item in to_fill:
            doll.put_on(item)
