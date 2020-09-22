def thing(thing_name, children, name):
    class ThingModel(Model):
        class NameGenerator(Model.NameFactory):
            default = name

        class ChildrenGenerator(Model.ChildrenFactory):
            default = children

        @property
        def default_name(self):
            return thing_name

    return ThingModel
