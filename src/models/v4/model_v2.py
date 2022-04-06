from models.placeholder import Placeholder
from .generating import GeneratingModel
from .model import Model as BaseModel
from .interface.base import BaseModelInterface


class Model(BaseModel, GeneratingModel, BaseModelInterface):
    def build_children(self):
        if not any(isinstance(child, Placeholder) for child in super().children):
            return
        super().children = (
            child.model if isinstance(child, Placeholder) else child
            for child in super().children
        )
