#! /usr/bin/python
import media.chart
import random

from generator.album import AlbumGenerator
from generator.band import BandGenerator


def new_album():
    openweekend = random.randint(100000000, 500000000)
    return chart.MediaItem(
        name=AlbumGenerator.generate(),
        author=BandGenerator.generate(),
        openweekend=openweekend
    )


def simulate(args):
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
