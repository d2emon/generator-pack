from .matter import Matter, Silica


class Rock(Matter):
    contents = Matter.children_property(Matter)

    class Factory(Matter.Factory):
        def children(self):
            yield Silica
            yield Matter.from_atoms('Al').probable(30)
            yield Matter.from_atoms('Fe').probable(20)
            yield Matter.from_atoms('K').probable(20)
            yield Matter.from_atoms('Na').probable(50)
            yield Matter.from_atoms('Ca').probable(50)


class Diamond(Rock):
    class Factory(Matter.Factory):
        def children(self):
            yield Matter.from_atoms('C')


class Magma(Rock):
    pass


class Iron(Rock):
    class Factory(Matter.Factory):
        def children(self):
            yield Matter.from_atoms('Fe')
