from .starship import Starship

from .starwars import StarWars
from .startrack import StarTrack
from .halo import Halo
from .eve import EveOnline
from .masseffect import MassEffect
from .stargate import StarGate


Babylon5 = [
    Starship("Star Fury", 10, "Babylon5"),
    Starship("Whitestar", 476, "Babylon5"),
    Starship("Ворлонский разрушитель планет", 5000, "Babylon5"),
]

Interstellar = [
    Starship("Endurance", 65, "Interstellar"),
]

NASA = [
    Starship("ISS", 73, "NASA"),
]

SpaceOdyssey = [
    Starship("Discovery One", 140, "2001 Space Odyssey"),
]

BattlestarGalactica = [
    Starship("Galactica", 1445, "Battlestar Galactica"),
]

V = [
    Starship("V Mothership", 3200, "V"),
]

Wh40k = [
    Starship("Dictator", 5100, "Warhammer 40000"),
    Starship("Eternal Crusader", 10000, "Warhammer 40000"),
]

Lexx = [
    Starship("Lexx", 10000, "Lexx"),
]

IndependenceDay =[
    Starship("City Destroyer Invasion Mothership", 24000, "Independence Day"),
    Starship("Пчеломатка", 4500000, "Independence Day"),
]

Oblivion = [
    Starship("TET", 100000, "Oblivion"),
]

Biggest = [
    # Куб боргов
    Starship("Корабли Визитеров", 3200, "Визитеры"),
    # Корабль-улей рейфов
    # Ворлонский разрушитель планет
    # Lexx
    # Разрушитель "Палач"
    Starship("Хайлайнер", 20000, "Дюна"),
    # Ви-Джер,
    Starship("Мобильная крепость зентради", 600000, "Макрос"),
    # Пчеломатка

    Starship("Элизиум", 60000, "Элизиум"),
    # Тэт
    # Звезда смерти
    # Гуррен Лаган
]

STARSHIPS = StarWars\
            + StarTrack\
            + Babylon5\
            + Halo\
            + Interstellar\
            + NASA\
            + SpaceOdyssey\
            + MassEffect\
            + BattlestarGalactica\
            + V\
            + StarGate\
            + EveOnline\
            + Wh40k\
            + Lexx\
            + IndependenceDay\
            + Oblivion\
            + Biggest
