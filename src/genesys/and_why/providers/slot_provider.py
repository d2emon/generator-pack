from data.and_why.slots import SLOTS


class BaseSlotProvider:
    @property
    def slots(self):
        raise NotImplementedError()


class SlotProvider(BaseSlotProvider):
    def __init__(self):
        self.__slots = SLOTS.values()

    @property
    def slots(self):
        return self.__slots


SLOT_PROVIDER = SlotProvider()
