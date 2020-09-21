from .factory import Factory


class DiceFactory(Factory):
    """
    Generate dice roll
    """

    def __init__(self, dices):
        super().__init__()
        self.dices = dices

    @property
    def data(self):
        return self.dices

    def roll(self, *args, **kwargs):
        """
        Roll dices

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Roll results
        """
        return self.dices.roll(*args, **kwargs)

    def build(self, *args, **kwargs):
        """
        Get result of roll

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Roll result
        """
        return sum(self.roll(*args, **kwargs))
