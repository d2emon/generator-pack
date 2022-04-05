"""
- Abomination
- Abomination Body
- Abomination Head
- Abomination Torso
"""
from ..animals import Animal, CrustaceanClaw
from ..animal_body import Stinger, WeirdOrgan
from ..body import Head, Torso, Body


class AbominationHead(Head):
    default_name = 'misshapen head'

    weird_organs = Body.children_property(WeirdOrgan)


class AbominationTorso(Torso):
    default_name = 'misshapen torso'

    weird_organs = Body.children_property(WeirdOrgan)


class AbominationBody(Body):
    default_name = 'misshapen body'

    claws = Body.children_property(CrustaceanClaw)
    stingers = Body.children_property(Stinger)
    weird_organs = Body.children_property(WeirdOrgan)


class Abomination(Animal):
    default_name = '*PERSON*| (abomination)'
