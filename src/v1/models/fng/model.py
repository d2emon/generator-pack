class Model:
    """
    Base model
    """

    def __init__(self, items=None, **kwargs):
        """
        :param items: Items of model
        """
        self.items = items or {}
        self.items.update(kwargs)

    @property
    def value(self) -> str:
        """
        :return: Model as string
        """
        return ''

    @classmethod
    def prepare(cls, name) -> str:
        """
        Prepare model

        :param name: Unprepared model
        :return: Prepared model
        """
        return name

    def __str__(self):
        value = self.value
        value = self.prepare(value)
        return value

    def __repr__(self):
        return f"<Value: \"{self}\">"


class TextModel(Model):
    """
    Model for text data
    """

    def __init__(self, value, **kwargs):
        """
        :param value: Name Item for model
        """
        items = {}
        items.update(value.values if value is not None else {})
        items.update(kwargs)
        super().__init__(
            item_id=value.item_id if value is not None else None,
            value=str(value),
            **items,
        )

    @property
    def item_id(self) -> int:
        """
        :return: Model item Id
        """
        return self.items.get('item_id', -1)

    @property
    def value(self) -> str:
        """
        :return: Model as string
        """
        return self.items.get('value', "")

    def __len__(self):
        return len(str(self))

    def __repr__(self):
        return f"<Value: \"{self}\">"
