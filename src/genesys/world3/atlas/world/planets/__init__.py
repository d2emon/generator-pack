from ..stars import Star
from ..sun_system import StarSystem, AsteroidBelt, Comet
from ..earth import Planet


sun_system = StarSystem(
    'Солнечная Система',
    Star('Солнце'),
    [
        Planet('Меркурий'),
        Planet('Венера'),
        Planet('Земля'),
        Planet('Марс'),
        AsteroidBelt('Пояс Астероидов'),
        Planet('Юпитер'),
        Planet('Сатурн'),
        Planet('Уран'),
        Planet('Нептун'),
        Planet('Плутон'),
        Comet('Комета'),
    ],
)
