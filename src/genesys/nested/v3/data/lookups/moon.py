from .lookup import Lookup


moons = Lookup(*map(
    lambda color: '{} moon'.format(color),
    [
        'young',
        'old',
        'large',
        'small',
        'pale',
        'white',
        'dark',
        'black',
        'old',
    ],
))
