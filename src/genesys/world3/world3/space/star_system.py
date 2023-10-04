from genesys.nested.models.models import StarSystem, Star, BarrenPlanet, VisitorPlanet, FuturePlanet, \
    TerraformedPlanet, GasGiant, AsteroidBelt
from .space import galaxy_arm


star_system = StarSystem.build(
    parent=galaxy_arm,
    name='Солнечная Система',
    children=[],
)
star = Star.build(
    parent=star_system,
    name='Солнце',
)
planets = [
    BarrenPlanet.build(
        parent=star_system,
        name='Вулкан',
    ),
    BarrenPlanet.build(
        parent=star_system,
        name='Меркурий',
    ),
    VisitorPlanet.build(
        parent=star_system,
        name='Венера',
    ),
    FuturePlanet.build(
        parent=star_system,
        name='Земля',
    ),
    TerraformedPlanet.build(
        parent=star_system,
        name='Марс',
    ),
    AsteroidBelt.build(
        parent=star_system,
        name='Пояс Астероидов',
    ),
    GasGiant.build(
        parent=star_system,
        name='Юпитер',
    ),
    GasGiant.build(
        parent=star_system,
        name='Сатурн',
    ),
    GasGiant.build(
        parent=star_system,
        name='Уран',
    ),
    GasGiant.build(
        parent=star_system,
        name='Нептун',
    ),
    AsteroidBelt.build(
        parent=star_system,
        name='Пояс Койпера',
    ),
]
