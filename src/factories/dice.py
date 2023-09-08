from models.roll import Roll
from .model_factory import ModelFactory


class DiceFactory(ModelFactory):
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

    @property
    def model(self):
        """Model to build.

        Returns:
            Model: Model class
        """
        return Roll

    @property
    def data(self):
        return self.dice

    def roll(self, *args, **kwargs):
        """
        Roll dices

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Roll results
        """
        return self.dice.roll(*args, **kwargs)

    def model_factory(self, *args, **kwargs):
        """Create model

        Args:
            *args: Data args.
            **kwargs: Data kwargs.

        Returns:
            Model: Resulting model
        """
        return self.model(self.roll(*args, **kwargs))
