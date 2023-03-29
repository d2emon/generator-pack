from models.tree_model import TreeModel


class Model(TreeModel):
    # Name model
    def __init__(self):
        super().__init__()
        self.value = None
        self.generated_text = ''
