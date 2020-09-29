from generated import life
from ...materials import WaterFactory


class JellyFactory(WaterFactory):
    default_model = life.Jelly
