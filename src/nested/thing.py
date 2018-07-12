import random


THINGS = dict()


class SubGenerator:
    def __init__(self, data):
        self.data = data
        print("SUB GEN", data)
        # if not instanceof(data, str):
        #     data = Choose(data)
        # value, probability, amount = get_data(data)
        self.get_value(self.data)
        print(self.value, self.amount, self.probability)

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


class Thing:
    things_n = 0

    def __init__(self, name, contains, namegen=None):
        self.name = name

        self.contains = None
        self.generators = []

        self.parse(contains)
        self.namegen = namegen
        if (self.namegen is None):
            self.namegen = self.name

        THINGS[name] = self
        self.things_n += 1

    def parse(self, data):
        print("PARSE", self.name, data)
        self.contains = data
        self.generators = []
        for d in data:
            self.generators.append(SubGenerator(d))

    @classmethod
    def get_thing(cls, key):
        return THINGS.get(key)

    @classmethod
    def clean(cls):
        for key, thing in THINGS.items():
            thing.clear()

    def clear(self):
        to_concat = []
        for i, c in enumerate(self.contains):
            if not isinstance(c, str):
                continue
            if c[0] == ".":
                sub = self.get_thing(c[1:])
                if sub is not None:
                    to_concat += sub.contains
                self.contains[i] = ""
        self.contains += to_concat

        self.contains = filter(lambda item: item, self.contains)


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