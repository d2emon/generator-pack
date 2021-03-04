class Name:
    """
    Name model
    """

    def __init__(self, items):
        """
        :param items: Items of name
        """
        self.items = items

    @property
    def value(self) -> str:
        """
        :return: Name as string
        """
        return ''

    @classmethod
    def test_swear(cls, name) -> str:
        """
        Check name for bad words

        :param name: Uncleaned name
        :return: Cleaned name
        """
        return name

    @classmethod
    def prepare(cls, name) -> str:
        """
        Prepare name

        :param name: Unprepared name
        :return: Prepared name
        """
        return name.title()

    def __str__(self):
        value = self.value
        value = self.test_swear(value)
        value = self.prepare(value)
        return value

    def __repr__(self):
        return f"<Name: \"{self}\">"
