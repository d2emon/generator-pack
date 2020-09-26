import math
from .scalable import Scalable


class World(Scalable):
    def __init__(self, name, size, scale=0):
        scale = (scale + 6) / 2
        Scalable.__init__(self, name, math.sqrt(size), scale=scale)


WORLDS = [
    World("Grand Theft Auto III", 9),
    World("Grand Theft Auto: Vice City", 14),
    World("Mafia", 31),
    World("Grand Theft Auto: San Andreas", 36),
    World("The Elder Scrolls V: Skyrim", 37),
    World("Fallout III", 39),
    World("The Elder Scrolls IV: Oblivion", 41),
    World("Red Dead Redemption", 41),
    World("Far Cry 3", 46),
    World("Far Cry 2", 80),
    World("Grand Theft Auto V", 81),
    World("The Witcher III: Wild Hunt", 135),
    World("World of Wacraft", 145),
    World("Superman Returns", 207),
    World("Operation Flashpoint: Dragon Rising", 350),
    World("Burnout Paradise", 518),
    World("True Crime: Los Angeles", 621),
    World("Just Cause 2", 1036),
    World("Asheron's Call", 1295),
    World("Test Drive Unlimited", 1600),
    World("The Crew", 5000),
    World("Fuel", 14400),
    World("Guild Wars NightFall", 38850),
    World("The Elder Scrolls II: Daggerfall", 161600),
    World("Minecraft", 40, 8), # 6.4 7
]