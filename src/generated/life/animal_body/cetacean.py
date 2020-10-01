"""
- CetaceanFlipper
- CetaceanFin
"""
from .limb import Limb, Tail


class CetaceanFlipper(Tail):
    default_name = 'flipper'


class CetaceanFin(Limb):
    default_name = 'fin'
