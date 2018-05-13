# from . import DataGenerator
from .generator_data import GeneratorData

import random


class MarkovChain(GeneratorData):
    startchar = " "
    breakchar = "\n"

    def __init__(self, data_list=None, length=2, data=dict()):
        self.data = data
        self.length = length
        if data_list is not None:
            self.parse_list(data_list, length=length)

    def select(self, prev=""):
        if len(prev) < self.length:
            return self.startchar * self.length
        if prev[-1] == self.breakchar:
            return None

        block = prev[-self.length:]
        next_blocks = self.data.get(block)
        if next_blocks is None:
            return None
        return random.choice(next_blocks)

    def parse_list(self, data=[], length=None):
        for s in data:
            self.parse_str(s, length)

    def parse_str(self, data="", length=None):
        if not length:
            length = self.length
        data = (self.startchar * length) + data + (self.breakchar * length)
        for i in range(len(data)-length):
            block_end = i + length
            block = data[i:block_end]
            if self.data.get(block) is None:
                self.data[block] = []
            self.data[block].append(data[block_end:block_end + length])

    def generator(self):
        return MarkovGenerator(self)


class MarkovGenerator():
    def __init__(self, chain=MarkovChain()):
        self.chain = chain

    def generate(self, length=16):
        generated = ""
        while len(generated) < length:
            block = self.chain.select(generated)
            if block is None:
                break
            generated += block
        return generated.strip()
