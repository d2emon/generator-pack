class Roll:
    """
    Dice roll
    """

    def __init__(self, rolls):
        """
        Create factory

        :param dice: Dices data
        """
        super().__init__()
        self.rolls = rolls

    @property
    def result(self):
        """
        Get result of roll

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Roll result
        """
        return sum(self.rolls)
