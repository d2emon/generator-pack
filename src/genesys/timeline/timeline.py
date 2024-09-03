from factories.model_factory import ModelFactory
from .age.prehistory import Prehistory
from .age.ancient import Ancient
from .age.past import Past
from .age.modern import Modern
from .models import Timeline


class TimelineFactory(ModelFactory):
    model = Timeline

    def __init__(self):
        super().__init__()
        self.__prehistory = Prehistory()
        self.__ancient = Ancient()
        self.__past = Past()
        self.__modern = Modern()

    def args_factory(self, *args, **kwargs):
        yield from self.__prehistory(*args, **kwargs)
        yield from self.__ancient(*args, **kwargs)
        yield from self.__past(*args, **kwargs)
        yield from self.__modern(*args, **kwargs)
