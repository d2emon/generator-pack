from v3.models import Model


class Movement(Model):
    @property
    def title(self):
        return self.data.get('title', '')

    def __str__(self):
        return self.title
