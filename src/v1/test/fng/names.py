from v1.factories.fng.names import AlienNameFactory, AmazonNameFactory, AnansiNameFactory, AngelNameFactory, \
    AnimalSpeciesNameFactory, AnimatronicNameFactory, AnimeNameFactory, AnthousaiNameFactory, \
    ApocalypseNicknameFactory, ArtificialIntelligenceNameFactory, BanditNameFactory, BansheeNameFactory, \
    BarbarianNameFactory


def show_multiple(name, generated, factoryClass):
    print(name)
    for value in generated:
        print(f"\t{value}")


def test():
    factories = [
        AlienNameFactory,
        AmazonNameFactory,
        AnansiNameFactory,
        AngelNameFactory,
        AnimalSpeciesNameFactory,
        AnimatronicNameFactory,
        AnimeNameFactory,
        AnthousaiNameFactory,
        ApocalypseNicknameFactory,
        ArtificialIntelligenceNameFactory,

        # BanditNameFactory,
        # BansheeNameFactory,
        # BarbarianNameFactory,
    ]

    for factoryClass in factories:
        factory = factoryClass()
        generated = factory.build10()
        show_multiple(factoryClass.__name__, generated, factoryClass)
