from models.nested_model import NestedModel


class Model(NestedModel):
    # Name model
    def __init__(self):
        super().__init__()
        self.value = None
        self.generated_text = ''
