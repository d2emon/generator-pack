from .model import Model


class ComplexModel(Model):
    static_field_names = []
    children = {}

    @property
    def field_names(self):
        yield from self.static_field_names
        yield from self.children.keys()

    def with_children(self):
        """
        Fill model with random children

        :return:
        """
        for k, v in self.children.items():
            if self.data.get(k) is None:
                child = v()
                self.data[k] = child.with_children() if isinstance(child, ComplexModel) else child

        return self
