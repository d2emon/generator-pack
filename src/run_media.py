#! /usr/bin/python
import sys
import random

from media import new_album


def main(args):
    items = []
    for i in range(20):
        items.append(new_album())
    weeks = random.randint(1, 100)
    print("On week %d" % (weeks))
    for i in items:
        print(i.name, i.last_week(), i.total(i.weeks_in_chart()))
    for w in range(20):
        print("=" * 80)
        items.append(new_album())
        places = dict()
        for i in items:
            places[i.next_week()] = i
            # print(i.name, i.weekend(weeks), i.total(weeks))
        points = list(places.keys())
        points.sort(reverse=True)
        n = 1
        for p in range(0, 10):
            i = places[points[p]]
            print("%d.\t%s by %s\t%d\t%d\t%d" % (
                n,
                i.name,
                i.author,
                i.last_week(),
                i.total(i.weeks_in_chart()),
                i.weeks_in_chart()
            ))
            n += 1


if __name__ == "__main__":
    main(sys.argv[1:])
