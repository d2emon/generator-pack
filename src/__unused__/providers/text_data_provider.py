from factories.factory import Factory
from factories.list_factory import ListFactory


class TextDataProvider(Factory):
    # default = generator_data
    block_id = ''
    groups = ListFactory()
    data = {}

    def __call__(self):
        return self.parts()

    @property
    def block(self):
        """
        Get all data from current block

        :return: Block data
        """
        return self.data.get(self.block_id, {})

    def factory(self, group_id=None):
        """
        Get factory from current block by group

        :param group_id: Factory group id
        :return: Factory
        """
        return self.block.get(group_id or next(self.groups))

    def parts(self, group_id=None, *args, **kwargs):
        """
        Next items from factories

        :param group_id: Factory group id
        :param args: Item args
        :param kwargs: Item kwargs
        :return: Generated items
        """
        return next(self.factory(group_id))
