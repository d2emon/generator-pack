from .model import Model


class NameItem(Model):
    """
    Name generator item
    """
    field_names = [
        'item_id',
        'block_id',
        'values',
        '_value',
    ]

    def __init__(self, item_id, value, block_id=None, **kwargs):
        """
        :param item_id: Id of item
        :param value: Item value
        """
        super().__init__(
            item_id=item_id,
            block_id=block_id,
            values=kwargs,
            _value=value,
        )
