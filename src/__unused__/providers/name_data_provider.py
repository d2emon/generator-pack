from .text_data_provider import TextDataProvider


class NameDataProvider(TextDataProvider):
    block_id = 'names'
    name_group_id = 'aliens'

    @property
    def block(self):
        """
        Get all data from current block with current group id

        :return: Block data
        """
        return self.data.get(self.block_id, {}).get(self.name_group_id)

    def parts(self, race_id=None, *args, **kwargs):
        """
        Next items from factories

        :param race_id: Race id
        :param args: Item args
        :param kwargs: Item kwargs
        :return: Generated items
        """
        return [next(part) for part in self.factory(race_id)]
