import random
from v1.fixtures.genders import MALE
from v1.models.fng.names.name import Name
from .factory import Factory


class NameFactory(Factory):
    """
    Factory for name

    Class fields:

    - child_class: Class for name
    - default_blocks: Default data blocks
    - blocks_map: Map for data blocks
    """

    child_class = Name
    default_blocks = {}
    blocks_map = {}

    def __init__(self, blocks=None):
        """
        :param blocks: Data blocks for factory
        """
        self.__factories = blocks or self.default_blocks

    @property
    def factories(self):
        """
        :return: Factories for complex factory
        """
        return self.__factories

    def factory(self, factory_id):
        """
        Get child factory by factory_id

        :param factory_id: Id of factory
        :return: Child factory
        """
        return self.__factories.get(factory_id)

    def from_factory(self, factory_id, *args, **kwargs):
        """
        Get value from factory by factory_id

        :param factory_id: Id of factory or None
        :param args: Args for name generation
        :param kwargs: Kwargs for name generation
        :return: New value
        """
        factory = self.factory(factory_id)
        return factory(*args, **kwargs) if factory is not None else None

    def get_items(self, *args, **kwargs) -> dict:
        """
        :return: Dict with generated data
        """
        return {item_id: self.from_factory(block_id, *args, **kwargs) for item_id, block_id in self.blocks_map.items()}

    def validate_items(self, items) -> dict:
        """
        Validate items

        :param items: Name items
        :return: Validated name items
        """
        return items

    def get_value(self, *args, **kwargs) -> dict:
        """
        Generate name with factory by item_id

        :param item_id: Id of item or None
        :return: Generated name
        """
        items = self.get_items(*args, **kwargs)
        items = self.validate_items(items)
        return items


class ComplexNameFactory(NameFactory):
    """
    Complex Factory for name

    Class fields:

    - factory_classes: Classes for child factories
    """

    factory_classes = {}

    def __init__(self, blocks=None):
        """
        :param blocks: Data blocks for factory
        """
        super().__init__({gender_id: factory(blocks) for gender_id, factory in self.factory_classes.items()})
        self.__blocks = blocks

    def factory_id(self):
        """
        Get random factory_id

        :return: Child factory id
        """
        return random.randrange(100)

    def __call__(self, *args, factory_id=None, **kwargs) -> Name:
        """
        Generate name

        :param args: Args for name generation
        :param factory_id: Id of factory or None
        :param kwargs: Kwargs for name generation
        :return: Generated name
        """
        factory = self.factory(factory_id if factory_id is not None else self.factory_id())
        return factory(*args, **kwargs)


class GenderNameFactory(ComplexNameFactory):
    def factory_id(self):
        """
        Get random factory_id

        :return: Child factory id
        """
        return MALE
