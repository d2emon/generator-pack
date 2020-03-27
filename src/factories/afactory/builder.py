from models.afactory.builder import Item, Item1


class Builder:
    def __init__(self):
        self.__ready = False
        self.__result = None
        self.reset()

    def reset(self):
        self.__result = Item()
        self.__ready = False

    def build_step_1(self):
        self.__result.name = "Name1"

    def build_step_2(self):
        self.__result.value = 1
        self.__ready = True

    @property
    def result(self):
        if not self.__ready:
            return None
        return self.__result


class Builder1(Builder):
    def reset(self):
        super().reset()
        self.__result = Item1()

    def build_step_1(self):
        self.__result.name = "Name11"

    def build_step_2(self):
        super().build_step_2()
        self.__result.value = 2


class Builder2(Builder):
    def reset(self):
        super().reset()
        self.__result = Item()

    def build_step_1(self):
        self.__result.name = "Name12"

    def build_step_2(self):
        super().build_step_2()
        self.__result.value = 3


class Director:
    def __init__(self, builder=None):
        self.builder = builder or Builder()

    def set_builder(self, builder):
        self.builder = builder

    def build(self, valued=False):
        self.builder.reset()
        self.builder.build_step_1()
        if valued:
            self.builder.build_step_2()
        return self.builder.result
