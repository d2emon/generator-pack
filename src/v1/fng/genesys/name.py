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

    def __str__(self):
        return self.test_swear(self.value)
