from .lookup import Lookup


interstellar_clouds = Lookup(*map(
    lambda color: '{} interstellar cloud'.format(color),
    [
        'a bright pink',
        'a faint',
        'a fading',
        'a pale',
        'a fluo',
        'a glowing',
        'a green',
        'a bright green',
        'a dark brown',
        'a brooding',
        'a magenta',
        'a bright red',
        'a dark red',
        'a blueish',
        'a deep blue',
        'a turquoise',
        'a teal',
        'a golden',
        'a multicolored',
        'a silver',
        'a dramatic',
        'a luminous',
        'a colossal',
        'a purple',
        'a gold-trimmed',
        'an opaline',
        'a silvery',
        'a shimmering',
    ],
))
