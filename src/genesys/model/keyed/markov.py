from models.model import Model


class MarkovUnit(Model):
    fields = [
        'prev',
        'value',
    ]

    def __init__(self, prev, value):
        super().__init__(prev=prev, value=value)

    @property
    def prev(self):
        return self['prev']

    @property
    def value(self):
        return self['value']

    def __str__(self):
        return str(self.value)


class MarkovChain(Model):
    fields = [
        'units',
    ]

    def __init__(self, units=None):
        super().__init__(units=units or [])

    @property
    def units(self):
        return self['units']

    @property
    def last(self):
        return self.units[-1] if len(self.units) else ''

    @property
    def value(self):
        return ''.join(map(str, self.units)).strip()

    def __len__(self):
        return len(self.units)

    def __str__(self):
        return self.value

    def reset(self):
        self['units'] = []

    def append(self, unit):
        self.units.append(unit)
