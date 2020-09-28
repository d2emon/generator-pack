"""
# new Thing("space monster",["space monster thoughts",["tentacle,0-6","fish fin,0-4","",""],"stinger,20%",["crustacean claw,0-4",""],["crustacean leg,0-8",""],["crustacean shell","scales","fur","exoskeleton",""],["mouth,1-2","beak,1-2"],"skull,80%",["eye,1-8","simple eye,1-8","",""],"weird soft organ,0-4","weird hard organ,0-4"],[["C'","Vr'","Ksh","Zn'","Sh","Hrl","X","O","Yog","Gorg","Morg","Marg","Magg"],["","","agn","soth","norgn","ngas","alx","orx","rgl","iirn","egw","thulh","t","g","m"],["org","orgon","orgus","orkus","oid","us","u","esth","ath","oth","um","ott","aur"],[""," the Forgotten"," the Entity"," the Ancient"," the Starchild"," the Seeder"," the Leech"," the Timeless"," the Eon"," the Many"," the Countless"," the Boundless"," the Prisoner"," the Child"," the Form"," the Shape"," the Drifter"," the Swarm"," the Vicious"," the Warden"," the Ender"," the Unworldly"," the Unfriendly"," the All-Consumer"]]);
# new Thing("space monster thoughts",["space monster thought,1-2"],["thoughts"]);
# new Thing("space monster thought",[],["WWWWWWWIDER THAN STARRRRRRS","AWAKENNNN MY CHILDRENNNNNN","GALAXIESSSSS SHALL FALLLLLLL","I AMMMMMM INFFFFFINITE","I SSSSSSSPAN AGESSSS","WWWWWWEEEEE ARE UNDYINGGGGGG","WE COMMMMMMMME","WE ANSSSSSWER THE CALLLLLLL","I TRAVELLLLLLL SLLLLLLUMBERING","FROMMMMMM FARRRRRR I COMMMME","IIIIII MUSSST SCREEEAAAM","I AMMMM AWAKENED","ALLLLLL FEAR MEEEEE","NOOOOONE SHALL LIVE","I MUSSSSST EATTTTT","DEEEEEEEEP I SSSSLUMBER","IIIII SHALL CONSSSSUME","IIIII SHALL DEVOUUUUURRRRR","LIFFFFFFE MUSSSSST PERISHHHHH","NNNNNNNNURISHMENT","ALL SHALLLLLLL GO INSSSSSSANE","SSSSSSANITY SHALL YIELDDDDD","EXXXXXILED I WASSSSS","EONSSSSS I HAVE SLUMBERED","EONSSSSS I HAVE WAITED","MORTALSSSSSS BEHOLDDDDD","I COMMMMME FROM DEEP","IMMMMMMOBILE I WATCHHHH","SSSSSKITTER","HHHHHHHEY HOW YOU DOIN'","AWKWAAAAAAAAARD"]);

# new Thing("space animal",["space animal thoughts,85%","space animal body"],[]);
# new Thing("space animal body",[["tentacle,0-6","crustacean leg,0-8","fish fin,0-4","mammal leg,1-6","",""],["insect wing,0-6","",""],["crustacean claw,0-4","",""],"flesh,40%","snout,3%","stinger,10%","whiskers,3%",["crustacean shell","scales","fur","exoskeleton",""],["mouth,1-4","beak,1-4",""],"skull,30%","mind,50%",["eye,1-2","eye,1-6","simple eye,1-6",""],"weird soft organ,50%","weird soft organ,20%","weird hard organ,50%","weird hard organ,20%"],["body"]);
# new Thing("space animal thoughts",["space animal thought,1-3"],["thoughts"]);
# new Thing("space animal thought",[],[
]);
"""
from generated.nested_v2.models import Mind
from genesys.nested.factories.v2.thing_builder import ListFactory
from .monster import Monster, MonsterBody, MonsterThoughts, MonsterThought
from ..animal_body import SimpleEye, CrustaceanLeg, CrustaceanClaw, Tentacle, FishFin, Stinger, Mouth, Beak, Skull, \
    WeirdSoftOrgan, WeirdHardOrgan, MammalLeg, InsectWing, Flesh, Snout, Whiskers
from generated.life.body.body import Eye
from genesys.nested.data import lookups


class DataProvider:
    space_monster_thought = lookups.space_monster_thoughts
    space_monster = lookups.space_monsters
    space_animal_thought = lookups.space_animal_thoughts
    space_animal = lookups.space_animals


class SpaceMonsterBody(MonsterBody):
    class Factory(MonsterBody.Factory):
        data_provider_class = DataProvider


class SpaceMonsterThought(MonsterThought):
    class Factory(MonsterThought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(MonsterThought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.space_monster_thought)


class SpaceMonsterThoughts(MonsterThoughts):
    class Factory(MonsterThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(MonsterThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from SpaceMonsterThought.multiple(1, 2)


class SpaceMonster(Monster):
    class Factory(Monster.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Monster.Factory.BaseFactory):
            def __next__(self):
                return ''.join([
                    next(self.provider.space_monster[0]),
                    next(self.provider.space_monster[1]),
                    next(self.provider.space_monster[2]),
                    next(self.provider.space_monster[3]),
                ])

        class ChildrenFactory(Monster.Factory.ChildrenFactory):
            body_class = SpaceMonsterBody
            mind_class = SpaceMonsterThoughts


class SpaceAnimalBody(SpaceMonsterBody):
    liquid = SpaceMonsterBody.child_property(Mind)

    class Factory(SpaceMonsterBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SpaceMonsterBody.Factory.ChildrenFactory):
            legs = property(lambda self: ListFactory([
                Tentacle.multiple(0, 6),
                CrustaceanLeg.multiple(0, 8),
                FishFin.multiple(0, 4),
                MammalLeg.multiple(1, 6),
                [],
                [],
            ]))
            wings = property(lambda self: ListFactory([
                InsectWing.multiple(0, 6),
                [],
                [],
            ]))
            claws = property(lambda self: ListFactory([
                CrustaceanClaw.multiple(0, 4),
                [],
                [],
            ]))
            mouths = property(lambda self: ListFactory([
                Mouth.multiple(1, 4),
                Beak.multiple(1, 4),
            ]))
            eyes = property(lambda self: ListFactory([
                Eye.multiple(1, 2),
                Eye.multiple(1, 6),
                SimpleEye.multiple(1, 6),
                [],
            ]))

            def builders(self):
                yield from next(self.legs)
                yield from next(self.wings)
                yield from next(self.claws)
                yield Flesh.probable(40)
                yield Snout.probable(3)
                yield Stinger.probable(10)
                yield Whiskers.probable(3)
                yield next(self.shells)
                yield from next(self.mouths)
                yield Skull.probable(30)
                yield Mind.probable(50)
                yield from next(self.eyes)
                yield WeirdSoftOrgan.probable(50)
                yield WeirdSoftOrgan.probable(20)
                yield WeirdHardOrgan.probable(50)
                yield WeirdHardOrgan.probable(20)


class SpaceAnimalThought(SpaceMonsterThought):
    class Factory(SpaceMonsterThought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(SpaceMonsterThought.Factory.BaseFactory):
            def __next__(self):
                return ''.join([
                    next(self.provider.space_animal_thought[0]),
                    next(self.provider.space_animal_thought[1]),
                    next(self.provider.space_animal_thought[2]),
                    next(self.provider.space_animal_thought[3]),
                    next(self.provider.space_animal_thought[4]),
                    next(self.provider.space_animal_thought[5]),
                    next(self.provider.space_animal_thought[6]),
                ])


class SpaceAnimalThoughts(SpaceMonsterThoughts):
    class Factory(SpaceMonsterThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SpaceMonsterThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from SpaceAnimalThought.multiple(1, 3)


class SpaceAnimal(SpaceMonster):
    class Factory(SpaceMonster.Factory):
        data_provider_class = DataProvider

        class BaseFactory(SpaceMonster.Factory.BaseFactory):
            def __next__(self):
                return ''.join([
                    next(self.provider.space_animal[0]),
                    next(self.provider.space_animal[1]),
                    next(self.provider.space_animal[2]),
                    next(self.provider.space_animal[3]),
                    next(self.provider.space_animal[4]),
                    next(self.provider.space_animal[5]),
                ])

        class ChildrenFactory(SpaceMonster.Factory.ChildrenFactory):
            body_class = SpaceAnimalBody
            mind_class = SpaceAnimalThoughts.probable(85)
