from .edges import EDGES

__d4 = 1
__d6 = 2
__d8 = 3
__d10 = 4
__d12 = 5


TEMPLATES = [
    {
        'title': 'Авантюрист',
        'stats': {
            'agility': __d6,
            'smarts': __d8,
            'spirit': __d6,
            'strength': __d4,
            'vigor': __d6,
        },
        'skills': {
            'Lockpicking': __d4,
            'Notice': __d6,
            'Driving': __d4,
            'Survival': __d4,
            'Fighting': __d4,
            'Healing': __d4,
            'Stealth': __d4,
            'Taunt': __d4,
            'Investigation': __d6,
            'Persuasion': __d6,
            'Streetwise': __d6,
        },
        'hindrances': [],
        'edges': [
            EDGES.get('Sixth Sense'),
            EDGES.get('Luck'),
        ],
    },
    {
        'title': 'Атаман',
        'stats': {
            'agility': __d8,
            'smarts': __d4,
            'spirit': __d6,
            'strength': __d6,
            'vigor': __d6,
        },
        'skills': {
            'Riding': __d6,
            'Lockpicking': None,
            'Notice': None,
            'War': __d8,
            'Driving': None,
            'Survival': None,
            'Fighting': __d8,
            'Intimidation': __d4,
            'Healing': None,
            'Stealth': None,
            'Taunt': None,
            'Investigation': None,
            'Shooting': __d6,
            'Persuasion': None,
            'Streetwise': None,
        },
        'hindrances': [],
        'edges': [
            EDGES.get('Command'),
            EDGES.get('Hold the Line!'),
        ],
    },
    {
        'title': 'Боец',
        'stats': {
            'agility': __d8,
            'smarts': __d4,
            'spirit': __d4,
            'strength': __d8,
            'vigor': __d8,
        },
        'skills': {
            'Riding': None,
            'Lockpicking': None,
            'Notice': __d4,
            'War': __d4,
            'Driving': None,
            'Survival': None,
            'Fighting': __d10,
            'Intimidation': __d6,
            'Healing': None,
            'Stealth': None,
            'Taunt': None,
            'Investigation': None,
            'Shooting': __d10,
            'Persuasion': None,
            'Streetwise': None,
        },
        'hindrances': [],
        'edges': [
            EDGES.get('Brawny'),
            EDGES.get('Nerves of Steel'),
        ],
    },
]
