from models.nested_model import NestedModel


class GodThoughts(NestedModel):
    # Thoughts
    default_name = 'thoughts'


class GodPsyche(NestedModel):
    # Psyche
    default_name = 'psyche'
    thoughts = NestedModel.contents_property()


class God(NestedModel):
    # body = NestedModel.child_property(Body)
    psyche = NestedModel.child_property(GodPsyche)
    # clothes = NestedModel.child_property(ClothingSet)
    # computer = NestedModel.child_property(Computer)

    @property
    def thoughts(self):
        return self.psyche and self.psyche.thoughts