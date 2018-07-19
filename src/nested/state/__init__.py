from ..thing import Thing
from ..children import ChildGenerator


class Continent(Thing):
    child_generators = [
        ChildGenerator("country", (1, 10)),
        ChildGenerator("sea", (1, 5)),
    ]
    names_data = [
        ["continent of "],
        ["A","Eu","Ame","Ocea","Anta","Atla"],
        ["frica","rtica","ropa","rica","nia","sia","ntide"],
    ]
    """
    [
        ["Eu","A","O","E"],
        ["rt","lt","rm","t","tr","tl","str","s","m","fr"],
        ["a","o","e","i"],
        ["ri","ni","ti","fri","",""],
        ["sia","nia","ca"]
    ]
    """

# new Thing("country",["region,1-10","battlefield,10%",".biome"],[["country of "],["Li","Arme","Le","Molda","Slove","Tur","Afgha","Alba","Alge","Tu","Fran","Baha","Su","Austra","Germa","In","Ara","Austri","Be","Ba","Bra","Ru","Chi","Ja","Tai","Bangla","Gha","Bou","Bo","Tas","Ze","Mon","Mo","Ne","Neder","Spai","Portu","Po","Por","Mol","Bul","Bru","Bur","Gro","Syl","Gui","Da","Gree","Bri","Ita"],["ly","dania","mas","vania","ce","nea","nau","topia","garia","gal","laska","golia","nisia","land","snia","livia","mania","than","nin","pan","wan","zil","ssia","na","rein","lgium","bia","ny","ce","stan","distan","nistan","dan","lia","nia","via","sia","tia","key","desh","dia"]]);
# new Thing("region",["capital","city,1-10","village,2-15"],[["north ","east ","south ","west ","north-west ","north-east ","south-west ","south-east ","center ","oversea "],["hilly","rainy","lush","foggy","desertic","green","tropical","rich","barren","scorched"],[" region"]]);


class MedievalContinent(Continent):
    child_generators = [
        ChildGenerator("medieval land", (1, 6)),
        ChildGenerator("sea", (1, 5)),
    ]
    names_data = ["explored continent"]


class AncientContinent(Continent):
    child_generators = [
        ChildGenerator("ancient land", (1, 5)),
        ChildGenerator("sea", (1, 5)),
    ]
    names_data = ["continent"]


class FutureContinent(Continent):
    child_generators = [ChildGenerator("future city", (20, 50))]
    names_data = [
        ["united continent of "],
        ["Eu","A","O","E","Ca","Ma"],
        ["rt","lt","rm","t","tr","tl","str","s","m","fr"],
        ["a","o","e","i"],
        ["ri","ni","ti","fri","",""],
        ["sia","nia","ca"]
    ]
    # ["A","Eu","Ame","Ocea","Anta","Atla"],["frica","rtica","ropa","rica","nia","sia","ntide"]


CONTENTS = [
    Continent,
    MedievalContinent,
    AncientContinent,
    FutureContinent,
]