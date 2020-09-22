from orm.models import Model as BaseModel


class Model(BaseModel):
    # factories.generator.Generated
    def __init__(self):
        self.value = None
        self.generated_text = ''
