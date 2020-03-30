from factories.factory.name import NameFactory


class AlienNameGenerator(NameFactory):
    groups = ('race1', 'race2', 'race3')
    block_id = 'aliens'
