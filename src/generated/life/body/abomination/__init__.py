"""
- Abomination
- Abomination Psyche
- Abomination Thoughts
- Abomination Thought
- Abomination Body
- Abomination Head
- Abomination Torso
"""
from genesys.model.model import Model
from ..person import Person
from ..head import Head
from ..torso import Torso
from ..body import Body


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

    # claws = Body.children_property(CrustaceanClaw)
    # stingers = Body.children_property(Stinger)
    # soft_organs = Body.children_property(WeirdSoftOrgan)
    # hard_organs = Body.children_property(WeirdHardOrgan)


class AbominationThought(Model):
    # Thought
    pass


class AbominationThoughts(Model):
    # Thoughts
    default_name = 'thoughts'


class AbominationPsyche(Model):
    # Psyche
    default_name = 'psyche'


class Abomination(Person):
    default_name = '*PERSON*| (abomination)'
