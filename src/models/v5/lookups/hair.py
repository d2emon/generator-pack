from .lookup import Lookup


hair = Lookup(*map(
    lambda color: '{} hair'.format(color),
    [
        'brown', 'black', 'gray', 'light', 'blond', 'red', 'dark',
    ],
))
