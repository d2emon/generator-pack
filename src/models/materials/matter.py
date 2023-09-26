from models.nested_model import NestedModel


class Matter(NestedModel):
    SOLID = 0
    LIQUID = 1
    GAS = 2

    state = None

    contents = NestedModel.contents_property()
