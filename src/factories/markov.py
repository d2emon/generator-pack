from factories.factory import Factory


class MarkovFactory(Factory):
    class MarkovChain:
        def generate(self, length=32):
            raise NotImplementedError()

    def __init__(self, provider=None, chain=None):
        super().__init__(provider)
        self.chain = chain or self.MarkovChain()

    def value(self):
        return self.chain.generate()
