class Model:
    """
    Base model
    """

    def __init__(self, items):
        """
        :param items: Items of model
        """
        self.items = items

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
