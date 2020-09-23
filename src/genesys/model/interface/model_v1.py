class ModelInterface:
    @property
    def image(self):
        """
        Get image from factory.name

        :return: Model image
        """
        raise NotImplementedError()

    @property
    def position(self):
        """
        Get next position from factory.position_factory

        :return: Model position
        """
        raise NotImplementedError()

    @property
    def factory(self):
        raise NotImplementedError()

    @property
    def template(self):
        raise NotImplementedError()

    def generate_children(self, *args, **kwargs):
        """
        Get Things.get_thing

        from

        factory.custom_factory()

        or

        next from factory for factory in Things.get_factories(self.factory name

        :param args:
        :param kwargs:
        :return: Generator of models with thing.name for every thing
        """
        raise NotImplementedError()

    def describe_gen(self, **kwargs):
        """
        :param kwargs:
        :return: Model factory's description factory with kwargs and children
        """
        raise NotImplementedError()

    @classmethod
    def get_factory(cls, name='error'):
        """
        Get thing by name

        :param name:
        :return: Thing
        """
        raise NotImplementedError()

    @classmethod
    def generate(cls, factory_name, parent=None):
        """
        Get model with factory by name and parent and add it to models list
        :param factory_name: Name of factory
        :param parent: Model parent
        :return: Generated model
        """
        raise NotImplementedError()
