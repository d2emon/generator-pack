from models.model import Model


class WithName(Model):
    name = Model.field_property('name', '')

    @property
    def name(self) -> str:
        """Get model value.

        Returns:
            str: Model value.
        """
        if self['name'] is None:
            self['name'] = self.get_name()

        return self['name']

    @name.setter
    def name(self, value: str):
        """Set model value.

        Args:
            value (str): Model value.
        """
        self['name'] = value

    @property
    def value(self) -> str:
        """Get model value.

        Returns:
            str: Model value.
        """
        return self.name

    @value.setter
    def value(self, value: str) -> None:
        """Set model value.

        Args:
            value (str): Model value.
        """
        self.name = value

    def get_name(self):
        return ''
