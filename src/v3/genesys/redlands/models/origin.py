from v3.models import Model


class Origin(Model):
    @property
    def title(self):
        return self.data.get('title', '')

    @property
    def traits(self):
        return self.data.get('traits', {})

    def __str__(self):
        return self.title
