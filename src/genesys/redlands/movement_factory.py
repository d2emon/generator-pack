from factories.list_model_factory import ListModelFactory
from data.redlands.movements import MOVEMENTS
from models.redlands.movement import Movement


class MovementFactory(ListModelFactory):
    default_data = MOVEMENTS
    model = Movement
