from v1.fixtures.data_block import NameItem, NameBlock
from v1.models.fng.model import Model, TextModel


class Factory:
    """
    Factory for various data

    Class fields:

    - child_class: Class for generated
    """

    child_class = Model

    def is_valid(self, value) -> bool:
        """
        Check value

        :param value: Value to check
        :return: If value is valid
        """
        return True

    def get_value(self, *args, **kwargs):
        """
        Generate new value

        :param args: Args for name generation
        :param kwargs: Kwargs for name generation
        :return: Generated value
        """
        raise NotImplementedError()

    def get_child(self, value):
        """
        Get child with value

        :param value: Generated value
        :return: Generated child
        """
        return self.child_class(value)

    def __call__(self, *args, **kwargs):
        """
        Generate valid value

        :param args: Args for name generation
        :param kwargs: Kwargs for name generation
        :return: Generated value
        """
        value = self.get_value(*args, **kwargs)
        while not self.is_valid(value):
            value = self.get_value(*args, **kwargs)
        return self.get_child(value)

    def values(self, count=10) -> list:
        """
        Generate 10 names

        :return: List of 10 names
        """
        return [self(item_id=item_id * 10) for item_id in range(count)]


class DataFactory(Factory):
    """
    Factory for block data
    """

    child_class = TextModel

    def __init__(self, block):
        """
        :param block: Data block for factory
        """
        self.block = block

    def get_value(self, *args, **kwargs):
        """
        Generate new value

        :param args: Args for name generation
        :param kwargs: Filter for data block
        :return: Generated value
        """
        return next(self.block.filtered(**kwargs))


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
    return {item_id: DataFactory(NameBlock().fill(*values)) for item_id, values in data.items()}
