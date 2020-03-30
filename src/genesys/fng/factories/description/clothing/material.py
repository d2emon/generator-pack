from genesys.fng.models.description.clothing.material import Material
from factories.factories.list_factory import ListFactory


class MaterialFactory(ListFactory):
    def __init__(self, provider):
        self.provider = provider

    def __next__(self):
        model = Material()
        material = next(self.provider.materials)
        name = material[0]
        if len(material) > 1:
            description = material[1]
        else:
            description = material[0]
        model.name = name
        model.description = description
        model.rarity = next(self.provider.rarities)
        return model
