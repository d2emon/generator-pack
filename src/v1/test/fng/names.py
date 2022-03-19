from v1.factories.fng.names import AlienNameFactory, AmazonNameFactory, AnansiNameFactory, AngelNameFactory, \
    AnimalSpeciesNameFactory, AnimatronicNameFactory, AnimeNameFactory, AnthousaiNameFactory, \
    ApocalypseNicknameFactory, ArtificialIntelligenceNameFactory, BanditNameFactory, BansheeNameFactory, \
    BarbarianNameFactory


def show_multiple(name, generated):
    print(name)
    for value in generated:
        print(f"\t{value}")


def test(count=10):
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
        BanditNameFactory,
        BansheeNameFactory,
        BarbarianNameFactory,
    ]
    for factoryClass in factories:
        factory = factoryClass()
        generated = factory.multiple(count=count)
        show_multiple(factoryClass.__name__, generated)
