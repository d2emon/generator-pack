from models.name_block import NameBlock
from models.name.name import TextModel
from factories.model_factory import ModelFactory


class DataFactory(ModelFactory):
    """
    Factory for block data
    """
    @property
    def model(self):
        return TextModel


class FactoriesBlock:
    def __init__(self, model, blocks):
        self.model = model
        self.blocks = blocks

    def factory(self, factory_id):
        return DataFactory(self.blocks.filtered(group_id=factory_id))


def load_data(data) -> dict:
    """
    Load data into dict

    :param data: Dict with data to load
    :return: Dict with NameBlocks
    """
    return {item_id: DataFactory(NameBlock.filled(*values)) for item_id, values in data.items()}
