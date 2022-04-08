from .lookup import Lookup


stars = Lookup(*map(
    lambda color: '{} star'.format(color),
    [
        'white',
        'faint',
        'yellow',
        'red',
        'blue',
        'green',
        'purple',
        'bright',
        'double',
        'twin',
        'triple',
        'old',
        'young',
        'dying',
        'small',
        'giant',
        'large',
        'pale',
        'dark',
        'hell',
        'horrific',
        'twisted',
        'spectral',
    ],
))
