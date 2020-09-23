from genesys.model.model import Model


def thing(thing_name, children, name):
    class ThingModel(Model):
        class NameFactory:
            default = name

        class ChildrenFactory:
            default = children

        default_name = thing_name

    return ThingModel
