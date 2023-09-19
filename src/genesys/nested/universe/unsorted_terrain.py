from factories.thing.nested_factory import NestedFactory


class ContinentFactory(NestedFactory):
    pass


class AncientContinentFactory(ContinentFactory):
    pass


class MedievalContinentFactory(ContinentFactory):
    pass


class FutureContinentFactory(ContinentFactory):
    pass


class OceanFactory(NestedFactory):
    pass


class SkyFactory(NestedFactory):
    pass


class TerraformedSkyFactory(SkyFactory):
    pass


class FutureSkyFactory(SkyFactory):
    pass


class DysonSurfaceFactory(NestedFactory):
    pass
