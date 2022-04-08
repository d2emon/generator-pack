from genesys.nested.data.lookups.lookup import Lookup


sea_monsters = [
    Lookup('giant', 'timeless', 'colossal', 'abyssal', 'forgotten', 'ancient', 'gigantic', 'monstrous'),
    Lookup(
        'craze', 'drift', 'dredge', 'dread', 'slumber', 'dream', 'wander', 'frost', 'magma', 'stone', 'slime', 'ooze',
        'egg', 'larva', 'grudge', 'stride', 'flail', 'wail', 'time', 'star', 'crystal', 'terror', 'horror', 'scream',
        'wrath', 'burst', 'dark', 'deep', 'tickle',
    ),
    Lookup('fin', 'tail', 'sinker', 'sunk', 'singer', 'song', 'polyp', 'rifter', 'glider', 'squirmer', 'titan',
        'colossus', 'mind', 'queen', 'king', 'child', 'guardian', 'seer', 'whale', 'worm', 'spider', 'crab', 'leech',
        'fish', 'shark', 'squid', 'saur', 'buddy', 'lord',
    ),
]
sea_monster_thoughts = Lookup(
    'IIIIII MUSSST SCREEEAAAM', 'I AMMMM AWAKENED', 'ALLLLLL FEAR MEEEEE', 'NOOOOONE SHALL LIVE', 'I MUSSSSST EATTTTT',
    'DEEEEEEEEP I SSSSLUMBER', 'IIIII SHALL CONSSSSUME', 'IIIII SHALL DEVOUUUUURRRRR', 'LIFFFFFFE MUSSSSST PERISHHHHH',
    'NNNNNNNNURISHMENT', 'ALL SHALLLLLLL GO INSSSSSSANE', 'SSSSSSANITY SHALL YIELDDDDD', 'EXXXXXILED I WASSSSS',
    'EONSSSSS I HAVE SLUMBERED', 'EONSSSSS I HAVE WAITED', 'MORTALSSSSSS BEHOLDDDDD', 'I COMMMMME FROM DEEP',
    'IMMMMMMOBILE I WATCHHHH', 'SSSSSKITTER', 'THEY FFFFFLOAAAAAT',
)
space_monsters = [
    Lookup('C\'', 'Vr\'', 'Ksh', 'Zn\'', 'Sh', 'Hrl', 'X', 'O', 'Yog', 'Gorg', 'Morg', 'Marg', 'Magg'),
    Lookup('', '', 'agn', 'soth', 'norgn', 'ngas', 'alx', 'orx', 'rgl', 'iirn', 'egw', 'thulh', 't', 'g', 'm'),
    Lookup('org', 'orgon', 'orgus', 'orkus', 'oid', 'us', 'u', 'esth', 'ath', 'oth', 'um', 'ott', 'aur'),
    Lookup(
        '', ' the Forgotten', ' the Entity', ' the Ancient', ' the Starchild', ' the Seeder', ' the Leech',
        ' the Timeless', ' the Eon', ' the Many', ' the Countless', ' the Boundless', ' the Prisoner', ' the Child',
        ' the Form', ' the Shape', ' the Drifter', ' the Swarm', ' the Vicious', ' the Warden', ' the Ender',
        ' the Unworldly', ' the Unfriendly', ' the All-Consumer',
    ),
]
space_monster_thoughts = Lookup(
    'WWWWWWWIDER THAN STARRRRRRS', 'AWAKENNNN MY CHILDRENNNNNN', 'GALAXIESSSSS SHALL FALLLLLLL',
    'I AMMMMMM INFFFFFINITE', 'I SSSSSSSPAN AGESSSS', 'WWWWWWEEEEE ARE UNDYINGGGGGG', 'WE COMMMMMMMME',
    'WE ANSSSSSWER THE CALLLLLLL', 'I TRAVELLLLLLL SLLLLLLUMBERING', 'FROMMMMMM FARRRRRR I COMMMME',
    'IIIIII MUSSST SCREEEAAAM', 'I AMMMM AWAKENED', 'ALLLLLL FEAR MEEEEE', 'NOOOOONE SHALL LIVE', 'I MUSSSSST EATTTTT',
    'DEEEEEEEEP I SSSSLUMBER', 'IIIII SHALL CONSSSSUME', 'IIIII SHALL DEVOUUUUURRRRR', 'LIFFFFFFE MUSSSSST PERISHHHHH',
    'NNNNNNNNURISHMENT', 'ALL SHALLLLLLL GO INSSSSSSANE', 'SSSSSSANITY SHALL YIELDDDDD', 'EXXXXXILED I WASSSSS',
    'EONSSSSS I HAVE SLUMBERED', 'EONSSSSS I HAVE WAITED', 'MORTALSSSSSS BEHOLDDDDD', 'I COMMMMME FROM DEEP',
    'IMMMMMMOBILE I WATCHHHH', 'SSSSSKITTER', 'HHHHHHHEY HOW YOU DOIN\'', 'AWKWAAAAAAAAARD',
)
space_animals = [
    Lookup('e', 'a', 'o', '', '', '', '', '', ''),
    Lookup('sm', 'cr', 'shn', 'sh', 'sn', 'gl', 'g', 'm', 'c', 'x', 'h', 'dr', 'r', 'l'),
    Lookup('o', 'a', 'u', 'i', 'e', 'ee'),
    Lookup(
        'x', 'b', 'rv', 'z', 's', 'gg', 'g', 'k', 'rf', 'gl', 'bl', 'th', 'kt', 'm', 'sh', 'l', 'dr', 'v', 'p', 'nt',
        'nk',
    ),
    Lookup('o', 'a', 'i', 'u', 'e'),
    Lookup(
        'n', 'ne', 'se', 'b', 'm', 'l', 's', 'sh', 'th', 't', 'sk', 'zer', 'bbler', 'ggler', 'ddler', 'ter', 'nt', 'r',
        'r', 'r',
    ),
]
space_animal_thoughts = [
    Lookup('sk\'', 'mop', 'nanu', 'nug', 'gmap', 'shmu', 'dna', 'no', 'xle', 'doda', 'daia', 'de', ''),
    Lookup('g ', 'gek ', 'th ', 'iap ', 'glib ', 'ph ', 'd\'t ', 'neig\'', 'dip ', 'shna ', 'sh '),
    Lookup('sk\'', 'mop', 'nanu', 'nug', 'gmap', 'shmu', 'dna', 'no', 'xle', 'doda', 'daia', 'de', ''),
    Lookup('g ', 'gek ', 'th ', 'iap ', 'glib ', 'ph ', 'd\'t ', 'neig\'', 'dip ', 'shna ', 'sh '),
    Lookup('mi', 'di', 'glu', 'dra', 'shwa', 'ama', ''),
    Lookup('ben', 'ri', 'nap', 'dap', 'top', 'gog'),
    Lookup('.', '.', '.', '.', '!', '?'),
]
