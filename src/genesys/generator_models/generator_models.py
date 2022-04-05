from models.v4.model import Model as BaseModel


class Model(BaseModel):
    # factories.generator.Generated
    def __init__(self):
        super().__init__()
        self.value = None
        self.generated_text = ''
