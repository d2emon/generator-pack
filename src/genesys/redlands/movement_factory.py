from factories.list_model_factory import ListModelFactory
from data.redlands.movements import MOVEMENTS
from models.redlands.movement import Movement


class MovementFactory(ListModelFactory):
    model = Movement

    def __init__(self, data=None):
        super().__init__(data or MOVEMENTS)
