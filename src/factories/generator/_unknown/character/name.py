from factories.generator import Generated, ListGenerator


class Name(Generated):
    def __init__(self):
        self.firstname = "Adam"
        self.lastname = "Adwell"
        self.title = ""

    def __repr__(self):
        # names18[random18] + " " + names19[random19] + ", a true " + names20[random20]
        return "%s %s, a true %s" % (
            self.firstname,
            self.lastname,
            self.title,
        )


class NameGenerator(ListGenerator):
    generated_class = Name
    firstnames = []
    lastnames = []
    titles = [
        "hero",
        "friend",
        "leader",
        "pioneer",
        "romancer",
        "fortune-hunter",
        "explorer",
        "daredevil",
        "globetrotter",
        "mercenary",
        "dreamer",
        "visionary",
        "idealist",
        "genius",
        "champion",
        "master",
        "prodigy",
        "spectacle",
        "guardian",
        "angel",
        "paladin",
        "warrior",
        "hunter",
        "warden",
        "defender",
        "sentinel",
        "victor",
        "winner",
        "challenger",
        "ally",
        "protector",
        "vanquisher",
        "vindicator",
        "romanticist",
        "stargazer",
        "nobleman",
        "utopian",
        "adventurer",
        "opportunist",
        "pioneer",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.firstname = cls.generate_value(cls.firstnames)
        generated.lastname = cls.generate_value(cls.lastnames)
        generated.title = cls.generate_value(cls.titles)
        return generated


class MaleNameGenerator(NameGenerator):
    firstnames = [
        "Adam",
        "Adan",
        "Addison",
        "Brock",
        "Brodie",
        "Brody",
        "Brooks",
        "Bruce",
        "Bruno",
        "Bryan",
        "Bryant",
        "Bryce",
        "Brycen",
        "Bryson",
        "Byron",
        "Cade",
        "Caden",
        "Cael",
        "Caiden",
        "Cale",
        "Gunnar",
        "Irving",
        "Isaac",
        "Jamal",
        "Jamar",
        "Kade",
        "Maverick",
        "Max",
        "Orion",
        "Orlando",
    ]
    lastnames = [
        "Adwell",
        "Afton",
        "Barnett",
        "Barney",
        "Barnfield",
        "Chilson",
        "Chilton",
        "Cawthorn",
        "Davenport",
        "Davey",
        "Dallin",
        "Eustice",
        "Eustis",
        "Evatt",
        "Falcon",
        "Faley",
        "Falkner",
        "Geary",
        "Gedman",
        "Gedney",
        "Hanshaw",
        "Hansley",
        "Hanson",
        "Lamkin",
        "Lamkins",
        "Lamm",
        "Lockridge",
        "Locks",
        "Lockwood",
        "Masser",
        "Massey",
        "Massingale",
        "Rosemond",
        "Shepherd",
        "Shepley",
        "Wakeley",
        "Wakelin",
    ]


class FemaleNameGenerator(MaleNameGenerator):
    firstnames = [
        "Allyson",
        "Allyssa",
        "Camille",
        "Camryn",
        "Daphne",
        "Elyse",
        "Elyssa",
        "Emily",
        "Faith",
        "Jayde",
        "Julie",
        "Juliet",
        "Kylee",
        "Melinda",
        "Melissa",
        "Sarina",
        "Sasha",
    ]
