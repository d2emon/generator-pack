from models.nested_model import NestedModel


class Matter(NestedModel):
    SOLID = 0
    LIQUID = 1
    GAS = 2

    state = SOLID

    @property
    def contents(self):
        return self.children
    
    @contents.setter
    def contents(self, value):
        self.children = value


class Gas(Matter):
    state = Matter.GAS
