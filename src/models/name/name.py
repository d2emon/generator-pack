from ..generated_model import GeneratedModel


class TextModel(GeneratedModel):
    """
    Model for text data
    """

    def __init__(self, *args, **kwargs):
        """
        :param value: Name Item for model
        """
        values = {
            'args': args,
        }
        # items.update(value.values if value is not None else {})
        values.update(kwargs)

        super().__init__(
            # item_id=item_id,
            # value=str(value),
            **values,
        )

    @property
    def item_id(self) -> int:
        """
        :return: Model item Id
        """
        return self.data.get('item_id', -1)
