from .factory import Factory


class DiceFactory(Factory):
    def __init__(self, dices=None):
        super().__init__(dices)

    def model(self, *args, **kwargs):
        """
        Roll dice

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Roll result
        """
        return sum(self.provider.roll())
