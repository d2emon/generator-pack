"""Encounter model class."""
from models.model import Model


class Encounter(Model):
    """Encounter model.

    Attributes:
        allowed_at (Collection): Is encounter allowed daily or nightly.
        encounter_class_description (str): Default encounter description.
    """

    allowed_at = []
    encounter_class_description = ''

    def __init__(
        self,
        distance=None,
        is_surprised=False,
        is_surprising=False,
        description=None,
        *args,
        **kwargs,
    ):
        """Initialize encounter model.

        Args:
            distance (Distance, optional): Distance to encounter. Defaults to None.
            is_surprised (bool, optional): Is encounter surprised. Defaults to False.
            is_surprising (bool, optional): Is party surprised. Defaults to False.
            description (_type_, optional): Encounter description. Defaults to None.
        """
        super().__init__(*args, **kwargs)

        self.__description = description
        self.distance = distance
        self.is_surprised = is_surprised
        self.is_surprising = is_surprising

    @property
    def description(self) -> str:
        """Get encounter description.

        Returns:
            str: Encounter description.
        """
        if self.__description is None:
            return self.encounter_class_description
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        """Set encounter description.

        Args:
            value (str): Encounter description.
        """
        self.__description = value

    @property
    def value(self) -> str:
        """Get encounter value.

        Returns:
            str: Encounter value.
        """
        return self.description
    
    @value.setter
    def value(self, value: str) -> None:
        """Set encounter value.

        Args:
            value (str): Encounter value.
        """
        self.description = value

    @property
    def text(self) -> str:
        """Get encounter text.

        Returns:
            str: Encounter text.
        """
        text = [
            self.distance,
            self.description,
        ]

        if self.is_surprising:
            text.append("Партия застигнута врасплох")

        if self.is_surprised:
            text.append("Столкновение застигнуто врасплох")

        return '\n'.join(map(str, text))
