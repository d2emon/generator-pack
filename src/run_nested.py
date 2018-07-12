import sys

from nested.thing import Thing
from nested.item import Item


def show_item(items):
    print(items)
    item_type = items[0]
    print(item_type)

    item = Item(item_type)
    item.grow(0)
    item.list()
    print(item)
    return items[1:]


def main(args):
    print("Building...")

    Thing.clean()

    # check_missing_things()
    # print("There are {} thing archetypes.".format(things_n))

    print('<div id="div0" class="thing"></div>')

    data = args
    while True:
        if len(data) <= 0:
            data = [input()]

        if data[0].lower() == 'q':
            break

        data = show_item(data)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)