import random

from .generator_data import GeneratorData


class MarkovGenerator:
    chain_class = MarkovChain
    _chain = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def chain(cls):
        if cls._chain is None:
            cls._chain = cls.chain_class()
        return cls._chain

    @classmethod
    def generate(cls, length=32):
        name = cls.chain().generate(length)
        return cls(name)
