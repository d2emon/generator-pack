from ...biology import Life


class BlackHoleLife(Life):
    class Factory(Life.Factory):
        def children(self):
            # yield Crustacean.probable(0.2)
            yield None
