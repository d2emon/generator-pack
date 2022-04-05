from .descriptive_model import DescriptiveModel


class ListModel(DescriptiveModel):
    @property
    def description(self):
        return " ".join(self.value)
