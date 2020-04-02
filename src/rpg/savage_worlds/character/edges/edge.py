class BaseEdge:
    is_big = False
    title = ''

    @property
    def cost(self):
        if not isinstance(self, Hindrance):
            return 2
        elif self.is_big:
            return -2
        else:
            return -1

    def __str__(self):
        return self.title

    def use(self):
        pass


class Edge(BaseEdge):
    is_big = False


class Hindrance(BaseEdge):
    is_big = False


class BigHindrance(Hindrance):
    is_big = True


class Ace(Edge):
    title = 'Ас'


class Inventor(Edge):
    title = 'Изобретатель'


class Swift(Edge):
    title = 'Стремительный'


class Mystic:
    class MadScience(Edge):
        title = 'Мистический дар (безумная наука)'
