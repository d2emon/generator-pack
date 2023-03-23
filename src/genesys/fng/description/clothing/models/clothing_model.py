from models.descriptive_model import DescriptiveModel, FactoryModel


class ClothingModel(DescriptiveModel, FactoryModel):

    @classmethod
    def model_factory(cls, *args, **kwargs):
        return None
