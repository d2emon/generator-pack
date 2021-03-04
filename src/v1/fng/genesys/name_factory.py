import random
from v1.fng.genesys.name import Name
from v1.fng.genesys.genders import MALE


class NameFactory:
    """
    Factory for name

    Class fields:

    - name_class: Class for name
    - default_blocks: Default data blocks
    - blocks_map: Map for data blocks
    """

    name_class = Name
    default_blocks = {}
    blocks_map = {}

    def __init__(self, blocks=None):
        """
        :param blocks: Data blocks for factory
        """
        self.blocks = blocks or self.default_blocks

    def get_name(self, item_id=None) -> Name:
        """
        Generate name with factory by item_id

        :param item_id: Id of item or None
        :return: Generated name
        """
        name = ''
        while name == '':
            name = self()

        return name

    def get_items(self) -> dict:
        """
        :return: Dict with generated data
        """
        return {item_id: next(self.blocks[block_id]) for item_id, block_id in self.blocks_map.items()}

    def validate(self, items) -> dict:
        """
        Validate items

        :param items: Name items
        :return: Validated name items
        """
        return items

    def __call__(self, *args, **kwargs) -> Name:
        """
        Generate name

        :param args: Args for name generation
        :param kwargs: Kwargs for name generation
        :return: Generated name
        """
        items = self.get_items()
        items = self.validate(items)
        return self.name_class(items)

    def names(self) -> list:
        """
        Generate 10 names

        :return: List of 10 names
        """
        return [self(factory_id=item_id * 10) for item_id in range(10)]


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
        super().__init__(blocks)
        self.__factories = {gender_id: factory(self.blocks) for gender_id, factory in self.factory_classes.items()}

    @property
    def factories(self) -> dict:
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
        factory = self.factory(factory_id if factory_id is None else self.factory_id())

        name = ''
        while name == '':
            name = factory()

        return name


class GenderNameFactory(ComplexNameFactory):
    def factory_id(self):
        """
        Get random factory_id

        :return: Child factory id
        """
        return MALE
