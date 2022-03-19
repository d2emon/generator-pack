from .factory import Factory


class DiceFactory(Factory):
    """
    Generate dice roll
    """

    def __init__(self, dice):
        """
        Create factory

        :param dice: Dices data
        """
        super().__init__()
        self.dice = dice

    def roll(self, *args, **kwargs):
        """
        Roll dices

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Roll results
        """
        return self.dice.roll(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        Main factory method

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Roll result
        """
        return sum(self.roll(*args, **kwargs))
