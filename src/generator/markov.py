import random
from . import DataGenerator


class MarkovChain():
    def __init__(self, data=None, length=2, data_list=None):
        if data is None:
            self.data = dict()
        else:
            self.data = data
        self.length = length
        if data_list is not None:
            self.parse_list(data_list)

    def parse_str(self, data="", length=None):
        if not length:
            length = self.length
        data = (" " * length) + data + ("\n" * length)
        for i in range(len(data)-length):
            block_end = i + length
            block = data[i:block_end]
            if self.data.get(block) is None:
                self.data[block] = []
            self.data[block].append(data[block_end:block_end + length])

    def parse_list(self, data=[], length=None):
        for s in data:
            self.parse_str(s, length)


class MarkovGenerator(DataGenerator):
    def __init__(self, chain=None):
        self.chain = chain

    def generate_chain(self, length=16):
        generated = " " * self.chain.length
        while len(generated) < length:
            block = generated[-self.chain.length:]
            next_blocks = self.chain.data.get(block)
            if next_blocks is None:
                break
            generated += random.choice(next_blocks)
            if generated[-1] == "\n":
                break
        return generated.strip()
