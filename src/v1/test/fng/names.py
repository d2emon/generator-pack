from v1.factories.fng.names import AlienNameFactory, AmazonNameFactory, AnansiNameFactory, AngelNameFactory, \
    AnimalSpeciesNameFactory, AnimatronicNameFactory, AnimeNameFactory, AnthousaiNameFactory, \
    ApocalypseNicknameFactory, ArtificialIntelligenceNameFactory, BanditNameFactory, BansheeNameFactory, \
    BarbarianNameFactory


def show_multiple(factory):
    print(factory.__name__)
    for value in factory.instance().multiple(count=10):
        print(f"\t{value}")


def test():
    show_multiple(AlienNameFactory)
    show_multiple(AmazonNameFactory)
    show_multiple(AnansiNameFactory)
    show_multiple(AngelNameFactory)
    show_multiple(AnimalSpeciesNameFactory)
    show_multiple(AnimatronicNameFactory)
    show_multiple(AnimeNameFactory)
    show_multiple(AnthousaiNameFactory)
    show_multiple(ApocalypseNicknameFactory)
    show_multiple(ArtificialIntelligenceNameFactory)
    show_multiple(BanditNameFactory)
    show_multiple(BansheeNameFactory)
    show_multiple(BarbarianNameFactory)
