import random


THINGS = dict()

class NameGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        if isinstance(self.data, str):
            return self.data
        if isinstance(self.data[0], str):
            return random.choice(self.data)
        else:
            return "".join(random.choice(n) for n in self.data)

    def parts(self):
        return self.generate().split("|")


class SubGenerator:
    def __init__(self, data):
        self.data = data
        if not isinstance(self.data, str):
            self.data = random.choice(self.data)
        # value, probability, amount = get_data(data)
        self.get_value(self.data)
        # print(self.value, self.amount, self.probability)

    def get_value(self, value):
        data = value.split(",")
        self.amount = [1]

        if len(data) > 1:
            self.get_amount(data[1])

        if len(data) > 1:
            probability = self.get_probability(data[1])
        else:
            probability = self.get_probability("1")

        if len(probability) > 1:
            self.probability = probability[0]
            self.amount = [1]
        else:
            self.probability = 100
        self.value = data[0]

    def get_amount(self, amount):
        r = amount.split("-")
        if len(r) > 1:
            # return Rand(r[0], r[1])
            self.amount = [int(r[0]), int(r[1])]
        else:
            self.amount = amount[0:0]

    def get_probability(self, probability):
        return (probability + "?").split("%")

    def __repr__(self):
        amount = "-".join([str(a) for a in self.amount])
        if self.probability != 100:
            amount += " ({}%)".format(self.probability)
        return "<Generator [{}] {}>".format(self.value, amount)


class Thing:
    things_n = 0

    def __init__(self, name, contains, namegen=None):
        self.name = name

        self.generators = []
        for d in contains:
            self.generators.append(SubGenerator(d))
        print("GENERATORS", self.name, self.generators)

        if (namegen is None):
            namegen = self.name
        self.namegen = NameGenerator(namegen)

        THINGS[name] = self
        self.things_n += 1

    @classmethod
    def get_thing(cls, key):
        return THINGS.get(key)

    @classmethod
    def clean(cls):
        for key, thing in THINGS.items():
            thing.clear()

    def clear(self):
        to_concat = []
        for i, g in enumerate(self.generators):
            if not isinstance(g.data, str):
                continue
            if g.data[0] == ".":
                sub_name = g.data[1:]
                sub = self.get_thing(sub_name)
                if sub is not None:
                    to_concat += sub.generators
                self.generators[i] = None
        # f = filter(lambda item: item is not None, self.generators + to_concat)
        # print(self.name, self.generators, "+", to_concat)
        # print(list(f))
        self.generators = list(filter(lambda item: item is not None, self.generators + to_concat))


# universe stuff
Thing("multiverse",["universe,10-30"],["multiverse","lasagnaverse","doughnutverse","towelverse","baconverse","sharkverse","nestedverse","tastyverse","upverse","downverse","layerverse","clusterverse","metaverse","quantiverse","paraverse","epiverse","alterverse","hypoverse","dimensioverse","planiverse","pluriverse","polyverse","maniverse","stackoverse","antiverse","superverse","upperverse","maxiverse","megaverse","babyverse","tinyverse","retroverse","ultraverse","topoverse","otherverse","bubbleverse","esreverse","versiverse","'verse","cookieverse","grandmaverse"])
Thing("universe",["supercluster,10-30"])
Thing("supercluster",["galaxy,10-30"],"galactic supercluster")
Thing("galaxy",["galaxy center","galaxy arm,2-6"])
Thing("galaxy arm",["galactic life,5%","dyson sphere,4%","dyson sphere,2%","star system,20-50","nebula,0-12","black hole,20%","black hole,20%"],"arm")
Thing("galaxy center",["black hole","galactic life,10%","dyson sphere,4%","dyson sphere,2%","star system,20-50","nebula,0-12"],"galactic center")

# meta
Thing("later", ["sorry"], "will do later")
Thing("error", ["sorry"], "Uh oh... It looks like you didn't supply a valid element to create.")
Thing("sorry", ["consolation universe"], "(Sorry!)")
Thing("consolation universe", [".universe"])