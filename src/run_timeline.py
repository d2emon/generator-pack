from generator_log import setup
from show_multiple import build_from_factories
from genesys.timeline.timeline import TimelineFactory


DEBUG = True
COUNT = 2


def build_all():
    factories = [
        TimelineFactory,
    ]
    build_from_factories(factories, count=COUNT, describe=True)
    # for factoryClass in factories:
    #     factory = factoryClass()
    #     generated = [factory() for _ in range(COUNT)]
    #     for timeline_id, timeline in enumerate(generated):
    #         print(f"\t{timeline_id + 1}:")
    #         print(timeline)
    #         # items = list(timeline)
    #         # for item in items:
    #         #     print(f"\t\t{item}")
    #         #     print(repr(item))


if __name__ == "__main__":
    if DEBUG:
        setup()
    build_all()
