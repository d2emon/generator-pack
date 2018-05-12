#! /usr/bin/python
import sys
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
