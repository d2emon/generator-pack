from genesys.nested.models.models import Multiverse, Universe, Supercluster, Galaxy, GalaxyArm, StarSystem


multiverse = Multiverse.build(
    name='Мультиверс',
)
universe = Universe.build(
    parent=multiverse,
    name='Мир Номер Три',
)
cluster = Supercluster.build(
    parent=universe,
    name='Местное Скопление Галактик',
)
galaxy = Galaxy.build(
    parent=cluster,
    name='Млечный Путь',
)
galaxy_arm = GalaxyArm.build(
    parent=galaxy,
    name='Наш Рукав',
)
