from factory.thing import Thing
from . import dummy


class MedievalWall(Thing):
    default_name = "stone wall"

    @classmethod
    def children_data(cls):
        yield dummy.Wood
        yield dummy.Stone
        yield dummy.Dirt.probable_factory(20)


class MedievalWalls(Thing):
    default_name = "stone walls"

    @classmethod
    def children_data(cls):
        yield dummy.Door.multiple_factory(1, 4)
        yield dummy.Window.multiple_factory(0, 6)
        yield Thing.list_factory([
            MedievalWall.multiple_factory(4),
            MedievalWall.multiple_factory(4, 8),
        ])


class MedievalRoom(Thing):
    default_name = "room"

    @classmethod
    def children_data(cls):
        yield dummy.Visitor.probable_factory(0.1)
        yield dummy.Ghost.probable_factory(0.1)
        yield MedievalWalls


class MedievalFireplace(Thing):
    default_name = "fireplace"

    @classmethod
    def children_data(cls):
        yield dummy.Fire
        yield dummy.Ash
        yield dummy.Wood
        yield dummy.Stone


class GreatHall(MedievalRoom):
    default_name = "throne room"

    @classmethod
    def children_data(cls):
        yield dummy.MedievalKing.probable_factory(90)
        yield dummy.MedievalQueen.probable_factory(90)
        yield dummy.Throne.multiple_factory(2)
        yield dummy.Wizard.multiple_factory(0, 3)
        yield dummy.MedievalNoble.multiple_factory(1, 6)
        yield dummy.MedievalGuard.multiple_factory(1, 4)
        yield dummy.MedievalServant.multiple_factory(1, 4)
        yield dummy.MedievalTable
        yield dummy.MedievalTable.probable_factory(60)
        yield dummy.MedievalChair.multiple_factory(3, 8)
        yield dummy.MedievalChest.multiple_factory(1, 4)
        yield dummy.MedievalClutter.multiple_factory(0, 4)
        yield dummy.MedievalMeat.probable_factory(30)
        yield dummy.SackOfMedievalFood.multiple_factory(0, 2)
        yield dummy.MedievalFood.multiple_factory(0, 2)
        yield dummy.SackOfGrain.probable_factory(50)
        yield MedievalFireplace
        yield MedievalFireplace.probable_factory(50)
        yield dummy.Dog.probable_factory(60)
        yield dummy.Dog.probable_factory(30)
        yield dummy.Cat.probable_factory(30)
        yield from MedievalRoom.children_data()


class MedievalResidentialArea(Thing):
    default_name = "housing district"

    @classmethod
    def children_data(cls):
        yield MedievalHouse.multiple_factory(3, 8)


class MedievalCommercialArea(Thing):
    default_name = "trade district"

    @classmethod
    def children_data(cls):
        yield dummy.MedievalInn.multiple_factory(1, 2)
        yield dummy.MedievalArmorShop.multiple_factory(0, 2)
        yield dummy.MedievalToolShop.multiple_factory(0, 2)
        yield dummy.MedievalClothingShop.multiple_factory(0, 2)
        yield dummy.MedievalButcherShop.multiple_factory(0, 2)
        yield dummy.MedievalFoodShop.multiple_factory(0, 2)
        yield dummy.MedievalApothecaryShop.multiple_factory(0, 2)


class MedievalMageQuarter(Thing):
    default_name = "mage district"

    @classmethod
    def children_data(cls):
        yield dummy.WizardTower.multiple_factory(1, 5)
        yield dummy.MedievalInn.multiple_factory(0, 1)
        yield dummy.MedievalApothecaryShop.multiple_factory(0, 3)


class MedievalBuilding(Thing):
    default_name = "building"

    @classmethod
    def children_data(cls):
        yield MedievalWalls
        yield dummy.Roof


class MedievalLivingQuarters(MedievalRoom):
    default_name = "living quarters"

    @classmethod
    def children_data(cls):
        yield dummy.MedievalPeasant.multiple_factory(0, 4)
        yield MedievalPantry
        yield dummy.MedievalTable
        yield dummy.MedievalTable.probable_factory(30)
        yield dummy.MedievalChair.multiple_factory(1, 6)
        yield dummy.MedievalChest.multiple_factory(0, 3)
        yield dummy.MedievalClutter.multiple_factory(0, 2)
        yield dummy.MedievalMeat.probable_factory(30)
        yield dummy.SackOfMedievalFood.multiple_factory(0, 2)
        yield dummy.MedievalFood.multiple_factory(0, 2)
        yield dummy.SackOfGrain.probable_factory(50)
        yield MedievalFireplace.probable_factory(90)
        yield dummy.Dog.probable_factory(60)
        yield dummy.Dog.probable_factory(30)
        yield dummy.Cat.probable_factory(30)
        yield dummy.Poultry.probable_factory(10)
        yield dummy.Insect.probable_factory(70)
        yield dummy.Insect.probable_factory(40)
        yield from MedievalRoom.children_data()


class MedievalBedroom(MedievalRoom):
    default_name = "bedroom"

    @classmethod
    def children_data(cls):
        yield dummy.MedievalPeasant.multiple_factory(0, 2)
        yield dummy.MedievalBed
        yield dummy.MedievalBed.probable_factory(20)
        yield dummy.MedievalTable.probable_factory(30)
        yield dummy.MedievalChair.multiple_factory(0, 4)
        yield dummy.MedievalChest.multiple_factory(0, 2)
        yield dummy.MedievalClutter.multiple_factory(0, 2)
        yield MedievalFireplace.probable_factory(40)
        yield dummy.Dog.probable_factory(10)
        yield dummy.Dog.probable_factory(10)
        yield dummy.Cat.probable_factory(20)
        yield dummy.Insect.probable_factory(70)
        yield dummy.Insect.probable_factory(40)
        yield from MedievalRoom.children_data()


class MedievalPantry(MedievalRoom):
    default_name = "pantry"

    @classmethod
    def children_data(cls):
        yield dummy.MedievalPeasant.probable_factory(10)
        yield dummy.MedievalMeat.multiple_factory(0, 4)
        yield dummy.SackOfMedievalFood.multiple_factory(0, 8)
        yield dummy.MedievalFood.multiple_factory(0, 8)
        yield dummy.SackOfGrain.multiple_factory(0, 6)
        yield dummy.AleKeg.multiple_factory(0, 3)
        yield dummy.MedievalChest.multiple_factory(0, 2)
        yield dummy.MedievalClutter.multiple_factory(0, 2)
        yield dummy.Insect.multiple_factory(0, 4)
        yield from MedievalRoom.children_data()


class MedievalHouse(MedievalBuilding):
    house_types = Thing.list_factory([
        "a small", "a large", "a big", "a cozy", "a bland", "a boring", "an old", "a new", "a freshly-painted",
        "a pretty", "an old-fashioned", "a creepy", "a spooky", "a gloomy", "a tall", "a tiny", "a fine",
        "a happy little",
    ])
    default_name = "{} hovel"

    @classmethod
    def generate_name(cls):
        return cls.default_name.format(cls.house_types.next())

    @classmethod
    def children_data(cls):
        yield MedievalLivingQuarters
        yield MedievalBedroom
        yield MedievalBedroom.probable_factory(50)
        yield from MedievalBuilding.children_data()


class NobleMedievalLivingQuarters(Thing):
    default_name = "living quarters"

    @classmethod
    def children_data(cls):
        yield dummy.Wizard.probable_factory(10)
        yield dummy.MedievalNoble.multiple_factory(0, 4)
        yield dummy.MedievalServant.multiple_factory(0, 3)
        yield MedievalPantry.multiple_factory(0, 2)
        yield dummy.MedievalTable
        yield dummy.MedievalTable.probable_factory(60)
        yield dummy.MedievalChair.multiple_factory(1, 8)
        yield dummy.MedievalChest.multiple_factory(1, 4)
        yield dummy.MedievalClutter.multiple_factory(0, 4)
        yield dummy.MedievalMeat.probable_factory(30)
        yield dummy.SackOfMedievalFood.multiple_factory(0, 2)
        yield dummy.MedievalFood.multiple_factory(0, 2)
        yield dummy.SackOfGrain.probable_factory(50)
        yield MedievalFireplace
        yield MedievalFireplace.probable_factory(50)
        yield dummy.Dog.probable_factory(60)
        yield dummy.Dog.probable_factory(30)
        yield dummy.Cat.probable_factory(30)
        yield from MedievalRoom.children_data()


class NobleMedievalBedroom(Thing):
    default_name = "bedroom"

    @classmethod
    def children_data(cls):
        yield dummy.MedievalNoble.multiple_factory(0, 2)
        yield dummy.MedievalServant.multiple_factory(0, 2)
        yield dummy.MedievalBed
        yield dummy.MedievalBed.probable_factory(20)
        yield dummy.MedievalTable.probable_factory(50)
        yield dummy.MedievalChair.multiple_factory(0, 4)
        yield dummy.MedievalChest.multiple_factory(1, 3)
        yield dummy.MedievalClutter.multiple_factory(0, 3)
        yield MedievalFireplace.probable_factory(80)
        yield dummy.Dog.probable_factory(10)
        yield dummy.Dog.probable_factory(10)
        yield dummy.Cat.probable_factory(20)
        yield from MedievalRoom.children_data()


class MedievalTemple(MedievalRoom):
    default_name = "{} {} {}"
    temple_types = Thing.list_factory([
        "temple of the", "church of the", "chapel of the", "house of the", "abbey of the", "cathedral of the",
        "shrine of the", "sanctuary of the", "priory of the",
    ])
    deity_epithets = Thing.list_factory([
        "blinding", "sacred", "holy", "unholy", "bloody", "cursed", "marvellous", "wondrous", "pious", "miraculous",
        "endless", "unending", "undying", "infinite", "unworldly", "worldly", "divine", "demonic", "ghostly",
        "monstrous", "tentacled", "all-knowing", "rational", "pretty good", "vengeful", "hallowed"
    ])
    temple_deities = Thing.list_factory([
        "light", "star", "beam", "sphere", "goddess", "god", "lords", "sisterhood", "brotherhood", "skies", "pact",
        "sect", "harmony", "discord", "child", "entity", "ghost", "builders", "makers", "guide", "wit", "story", "tale",
        "unicorn", "flame", "fountain", "locust", "squid", "gembaby", "father", "mother",
    ])

    @classmethod
    def generate_name(cls):
        return cls.default_name.format(
            cls.temple_types.next(),
            cls.deity_epithets.next(),
            cls.temple_deities.next(),
        )

    @classmethod
    def children_data(cls):
        yield dummy.MedievalPriest.multiple_factory(1, 3)
        yield dummy.MedievalNoble.multiple_factory(0, 2)
        yield dummy.MedievalPeasant.multiple_factory(0, 4)
        yield dummy.MedievalAltar.multiple_factory(1, 2)
        yield dummy.MedievalTable.probable_factory(70)
        yield dummy.MedievalBench.multiple_factory(2, 6)
        yield dummy.MedievalChair.multiple_factory(1, 3)
        yield dummy.MedievalChest.multiple_factory(1, 4)
        yield dummy.MedievalClutter.multiple_factory(0, 4)
        yield MedievalFireplace.probable_factory(20)
        yield from MedievalRoom.children_data()


class GiantMonsterCage(Thing):
    default_name = "giant cage"

    @classmethod
    def children_data(cls):
        yield Thing.list_factory([
            dummy.Dragon,
            dummy.SeaMonster,
        ])


class CastleKeep(MedievalBuilding):
    default_name = "castle keep"

    @classmethod
    def children_data(cls):
        yield GreatHall
        yield NobleMedievalLivingQuarters.multiple_factory(1, 3)
        yield NobleMedievalBedroom.multiple_factory(2, 5)
        yield from MedievalBuilding.children_data()


class Portcullis(Thing):
    default_name = "portcullis"

    @classmethod
    def children_data(cls):
        yield dummy.Wood
        yield dummy.Metal


class Moat(Thing):
    default_name = "moat"

    @classmethod
    def children_data(cls):
        yield dummy.Water.probable_factory(50)
        yield dummy.Dirt


class MedievalMonument(Thing):
    monument_types = Thing.list_factory([
        "fountain", "memorial", "statue", "well", "altar",
    ])

    @classmethod
    def generate_name(cls):
        return cls.monument_types.next()

    @classmethod
    def children_data(cls):
        yield Thing.list_factory([
            dummy.Stone,
            dummy.Dirt,
        ])


class WatchTower(MedievalBuilding):
    default_name = "watchtower"

    @classmethod
    def children_data(cls):
        yield dummy.MedievalGuard.multiple_factory(1, 8)
        yield dummy.MedievalChest.probable_factory(30)
        yield from MedievalBuilding.children_data()


class Townwall(Thing):
    default_name = "townwall"

    @classmethod
    def children_data(cls):
        yield dummy.MedievalGuard.multiple_factory(1, 8)
        yield WatchTower.multiple_factory(1, 6)
        yield MedievalWall


class Gatehouse(Thing):
    default_name = "gatehouse"

    @classmethod
    def children_data(cls):
        yield dummy.MedievalGuard.multiple_factory(1, 3)
        yield Portcullis.multiple_factory(1, 2)
        yield dummy.Wood
        yield MedievalWall


class Castle(Thing):
    default_name = "castle"

    @classmethod
    def children_data(cls):
        yield dummy.MedievalPeasant.multiple_factory(1, 4)
        yield dummy.MedievalNoble.multiple_factory(0, 2)
        yield dummy.MedievalGuard.multiple_factory(2, 8)
        yield CastleKeep
        yield GiantMonsterCage.probable_factory(1)
        yield WatchTower.multiple_factory(1, 6)
        yield MedievalTemple.probable_factory(30)
        yield dummy.MedievalInn.probable_factory(40)
        yield MedievalHouse.multiple_factory(1, 4)
        yield MedievalMonument.probable_factory(20)
        yield Moat.probable_factory(30)
        yield Gatehouse
