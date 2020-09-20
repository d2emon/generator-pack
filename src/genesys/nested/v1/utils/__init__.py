"""
================
Nested by Orteil
================
[ http://orteil.deviantart.com , https://twitter.com/Orteil42 , orteil42@gmail.com - more stuff like this at http://orteil.dashnet.org ]
This is the source-code. Use it wisely. (Better not use it without my permission though.)

I made this when I was bored at work around 2011; I've been progressively adding stuff to it since.
I am by no means a professional programmer (I do pixel-art and game-design), so please don't judge my code too harshly!

Wikipedia was used extensively for this project. I am now aware of the composition of everything. *Everything*.

(oh yeah, don't read all the code right now, it kind of ruins the surprise of finding things!)
"""
import random


def choose__(arr):
    return random.choice(arr)


def weighted_choose__(data, weight_choose=1):
    # Returns an element from an array at random according to a weight.
    # A weight of 2 means the first element will be picked roughly twice as often as the second; a weight of 0.5 means
    # half as often. A weight of 1 gives a flat, even distribution.
    weight_choose = weight_choose if weight_choose > 0 else 1
    return data[int(random.uniform(100) ^ weight_choose * len(data))]


def rand__(a, b):
    return random.randrange(a, b)


def check_missing_things__(things):
    all_contents = []
    for this_thing in things.values():
        for content in this_thing.contains:
            if isinstance(content, str):
                all_contents.append(content)
            else:
                map(all_contents.append, content)

    all_missing = []
    for content in all_contents:
        if content[0] == '.':
            content = content[1:]
        content = content.split(',')
        content = content[0]
        if content and not things[content]:
            all_missing.append(content)

    # remove duplicates
    # all_missing = filter(lambda elem, pos: all_missing.index(elem) == pos, all_missing)

    missing = '\n'.join(all_missing)
    return 'Things that are linked to, but don\'t exist :{}\n'.format(missing)


def title__(what):
    return what.title()
