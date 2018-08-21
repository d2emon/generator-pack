class Troop():
    name = ""
    move = 9
    roadBonus = 0
    chargeMove = 12
    missileRange = 0

    def __init__(self):
        self.formation = None


class ArmoredFoot(Troop):
    name = "Armored Foot"
    move = 6
    chargeMove = 6


class HeavyFoot(Troop):
    name = "Heavy Foot"


class AxeThrower(HeavyFoot):
    name = "Heavy Foot(Axe)"
    missileRange = 3


class SpearThrower(AxeThrower):
    name = "Heavy Foot(Spear)"


class Landsknechte(Troop):
    name = "Landsknechte"
    move = 12
    chargeMove = 15


class LightFoot(Troop):
    name = "Light Foot"


class Archer(LightFoot):
    name = "Archers"
    missileRange = 15


class Crossbowman(Troop):
    name = "Crossbowman"
    move = 12
    missileRange = 18


class Arquibusier(Crossbowman):
    name = "Arquibusier"


class Longbowman(Troop):
    name = "Longbowman"
    move = 12
    chargeMove = 15
    missileRange = 21


class TurkArcher(Troop):
    name = "Turk Archer"
    missileRange = 21


class HeavyCrossbowman(Troop):
    name = "Heavy Crossbowman"
    chargeMove = 9
    missileRange = 24


class HeavyHorse(Troop):
    name = "Heavy Horse"
    move = 12
    roadBonus = 3
    chargeMove = 18


class MediumHorse(Troop):
    name = "Medium Horse"
    move = 18
    roadBonus = 6
    chargeMove = 24


class LightHorse(Troop):
    name = "Light Horse"
    move = 24
    roadBonus = 6
    chargeMove = 30


class LightHorseJavelineer(LightHorse):
    name = "Light Horse (Javeline)"
    missileRange = 18


class Catapult(Troop):
    name = "Catapult"
    move = 6
    roadBonus = 3


class Wagon(Troop):
    name = "Wagon"
    move = 6
    roadBonus = 6
