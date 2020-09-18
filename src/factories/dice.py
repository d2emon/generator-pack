from .factory import Factory


class DiceFactory(Factory):
    """
    Generate dice roll
    """

    def __init__(self, dices):
        super().__init__()
        self.dices = dices

    def roll(self, *args, **kwargs):
        """
        Roll dices

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Roll results
        """
        return self.dices.roll(*args, **kwargs)

    def model(self, *args, **kwargs):
        """
        Roll dice

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Roll result
        """
        return sum(self.roll(*args, **kwargs))
