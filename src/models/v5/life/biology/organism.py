from models.v5.model import Model
from models.v5.mind import Psyche


class BasicBody(Model):
    default_name = 'body'


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
