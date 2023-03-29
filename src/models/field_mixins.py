from models.model import Model


class WithName(Model):
    field_names = [
        'name',
    ]
    value_field_name = 'name'

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

    def get_name(self):
        return ''


class WithDescription(Model):
    field_names = [
        'description',
    ]

    name = Model.field_property('description', '')
