from genesys.nested.models import Model
from .mind import Psyche


class BasicBody(Model):
    pass


class Organism(Model):
    body = Model.child_property(BasicBody)
    psyche = Model.child_property(Psyche)

    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            body_class = BasicBody
            mind_class = Psyche

            def builders(self):
                yield self.body_class
                yield self.mind_class
