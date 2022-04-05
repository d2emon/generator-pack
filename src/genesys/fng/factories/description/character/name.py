from genesys.fng.factories.name_factory import NameFactory
from models.fng.description import Eyes


class CharacterNameFactory(NameFactory):
    child_class = Eyes
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


class MaleNameFactory(NameFactory):
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


class FemaleNameFactory(MaleNameFactory):
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