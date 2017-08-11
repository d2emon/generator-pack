#! /usr/bin/python
import sys
import chart
import random
from generator import album


def main(args):
    items = []
    for i in range(20):
        openweekend = random.randint(100000000, 500000000)
        print("On openweekend: %d" % (openweekend))
        items.append(chart.MediaItem(album.generate(), openweekend))
    weeks = random.randint(1, 100)
    print("On week %d" % (weeks))
    for i in items:
        print(i.name, i.last_week(), i.total(i.weeks_in_chart()))
    for w in range(20):
        print("=" * 80)
        openweekend = random.randint(100000000, 500000000)
        # print("On openweekend: %d" % (openweekend))
        items.append(chart.MediaItem(album.generate(), openweekend))
        places = dict()
        for i in items:
            places[i.next_week()] = i
            # print(i.name, i.weekend(weeks), i.total(weeks))
        points = list(places.keys())
        points.sort(reverse=True)
        for p in range(0, 10):
            i = places[points[p]]
            print("%s\t%d\t%d\t%d" % (i.name, i.last_week(), i.total(i.weeks_in_chart()), i.weeks_in_chart()))


if __name__ == "__main__":
    main(sys.argv[1:])
