from .lookup import Lookup


terraformed_moons = Lookup(*map(
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
        'green',
        'lush',
        'blue',
        'city',
        'colonized',
        'life',
    ],
))
