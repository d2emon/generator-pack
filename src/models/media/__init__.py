#! /usr/bin/python
import random

from .media_item import MediaItem
from .chart import Chart


def simulate(albums_count=20, start_week=None, weeks=20):
    start_week = start_week or random.randint(1, 100)
    albums = [MediaItem() for _ in range(albums_count)]

    for week in range(start_week, start_week + weeks):
        albums.append(MediaItem())
        week_chart = Chart(albums)

        print("On week {}".format(week))
        for n in range(10):
            print("{position}.\t{album}{album.weeks:>4}".format(
                position=n + 1,
                album=week_chart[n],
            ))
            album = week_chart[n]
            print([album.history[i] for i in range(1, album.weeks + 1)])
        print("-" * 80)
