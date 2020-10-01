"""
- Abomination
- Abomination Body
- Abomination Head
- Abomination Torso
"""
from ..animal_body import CrustaceanClaw, Stinger
from ..body import Person, Head, Torso, Body


class AbominationHead(Head):
    default_name = 'misshapen head'

    # soft_organs = Body.children_property(WeirdSoftOrgan)
    # hard_organs = Body.children_property(WeirdHardOrgan)


class AbominationTorso(Torso):
    default_name = 'misshapen torso'

    # soft_organs = Torso.children_property(WeirdSoftOrgan)
    # hard_organs = Torso.children_property(WeirdHardOrgan)


class AbominationBody(Body):
    default_name = 'misshapen body'

    claws = Body.children_property(CrustaceanClaw)
    stingers = Body.children_property(Stinger)
    # soft_organs = Body.children_property(WeirdSoftOrgan)
    # hard_organs = Body.children_property(WeirdHardOrgan)


class Abomination(Person):
    default_name = '*PERSON*| (abomination)'
