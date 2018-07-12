THINGS = dict()


class Thing:
    things_n = 0

    def __init__(self, name, contains, namegen=None):
        self.name = name
        self.contains = contains
        self.namegen = namegen
        if (self.namegen is None):
            self.namegen = self.name

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