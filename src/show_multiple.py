def show(name, generated, factoryClass):
    print(f"Generate \"{name}\" from {factoryClass}")
    for value_id, value in enumerate(generated):
        print(f"\t{value_id + 1}\t{value}")


def build_from_factories(factories, count):
    for factoryClass in factories:
        factory = factoryClass()
        generated = [factory() for _ in range(count)]
        show(factoryClass.__name__, generated, factoryClass)
