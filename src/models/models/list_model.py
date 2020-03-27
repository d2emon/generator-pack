from .model import Model


class ListModel(Model):
    def description(self):
        return " ".join(self.value)
