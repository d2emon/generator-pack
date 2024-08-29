from genesys.world import WorldFactory


def show_multiple(name, generated, factoryClass):
    print(name)
    for value in generated:
        print(f"\t{value}")


def build_all():
    factories = [
        WorldFactory,
    ]

    for factoryClass in factories:
        factory = factoryClass()
        generated = [factory() for _ in range(10)]
        show_multiple(factoryClass.__name__, generated, factoryClass)


if __name__ == "__main__":
    build_all()
