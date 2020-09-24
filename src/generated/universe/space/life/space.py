from generated.nested_v2.models.biology import Life, Habitat


class GalacticLife(Life):
    class Factory(Life.Factory):
        probability = 100

        def children(self):
            if not self.check_probability(self.probability):
                return
            # yield SpaceMonster.probable(1)
            # yield from SpaceAnimal.multiple(1, 12)
            yield None
