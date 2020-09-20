import sys

from genesys.afactory.model import Item


# from v1.tag import Tag, get_DOM


ITEMS = []


def show_all():
    print("-" * 20)
    for c in ITEMS:
        print(c)
    print("-" * 20)


def show_item(items):
    print(items)
    item_type = items[0]
    print(item_type)
    print("=" * 20)

    if item_type.lower() == "all":
        show_all()
        return items[1:]

    item = Item.generate(item_type)

    print("-" * 20)
    print(item)
    print("-" * 20)
    for i, c in enumerate(item.children):
        print("{}\t{}".format(i + 1, c))

    return items[1:]


def main(*args):
    print('Building...')

    # clean_things()

    # check_missing_things()
    # print("There are {} thing archetypes.".format(things_n))

    data = args
    while True:
        print(data or 'NO DATA')
        if len(data) <= 0:
            data = [input()]

        if data[0].lower() == 'q':
            break

        data = show_item(data)


if __name__ == "__main__":
    sys_args = sys.argv[1:]
    main(*sys_args)
