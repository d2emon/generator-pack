from v3.factories import ListModelFactory
from ..data.movements import MOVEMENTS
from ..models.movement import Movement


class MovementFactory(ListModelFactory):
    model = Movement

    def __init__(self, data=None):
        super().__init__(data or MOVEMENTS)
