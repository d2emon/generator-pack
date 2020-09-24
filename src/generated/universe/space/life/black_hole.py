from generated.nested_v2.models.biology import Life


class BlackHoleLife(Life):
    class Factory(Life.Factory):
        def children(self):
            # yield Crustacean.probable(0.2)
            yield None
