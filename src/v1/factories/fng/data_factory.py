from v1.fixtures.data_block import NameBlock
from v1.models.fng.model import TextModel
from v1.factories.factory import Factory


class FactoriesBlock:
    def __init__(self, model, blocks):
        self.model = model
        self.blocks = blocks

    def factory(self, factory_id):
        return DataFactory(self.blocks.filtered(group_id=factory_id))


class DataFactory(Factory):
    """
    Factory for block data
    """
    @property
    def model(self):
        return TextModel


def load_data(data) -> dict:
    """
    Load data into dict

    :param data: Dict with data to load
    :return: Dict with NameBlocks
    """
    return {item_id: DataFactory(NameBlock().fill(*values)) for item_id, values in data.items()}
