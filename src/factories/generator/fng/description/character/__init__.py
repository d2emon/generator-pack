from ..provider import DataProvider
from .marks import Scar, Birthmark, Moles, Frecles, SmoothSkin, SoftSkin


def char_gen():
    provider = DataProvider()

    srace = next(provider.races)
    mark = next(provider.marks)
    mark_from = next(mark.places_form)
    mark_through = next(mark.places_through)
    mark_to = next(mark.places_to)
    memory_type = next(mark.memory_types)
    memory_of = next(mark.memory_ofs)
    first_name = next(srace.first_name)
    last_name = next(srace.last_name)
    random20 = next(provider.names20)
    random22 = next(provider.names22)
    random23 = next(provider.names23)
    random24 = next(provider.names24)
    random25 = next(provider.names25)
    random26 = next(provider.names26)
    while random26 == random25:
        random26 = next(provider.names26)
    random27 = next(provider.names27)
    random28 = next(provider.names28)

    head = '{} a {}. {} over {}'.format(
        srace.hair,
        srace.face,
        srace.eyes,
        srace.promise,
    )
    name2 = '{} {} {} {} leaves {} of {}.'.format(
        mark,
        mark_from,
        mark_through,
        mark_to,
        memory_type,
        memory_of,
    )
    name3 = 'This is the face of {} {}, a true {} among {}. He stands {} others, despite his {} frame.'.format(
        first_name,
        last_name,
        random20,
        srace,

        random22,
        random23,
    )
    name4 = 'There\'s something {} about him, perhaps it\'s {} or perhaps it\'s simply {}. But nonetheless, people tend to {}, while {}.'.format(
        random24,
        random25,
        random26,

        random27,
        random28,
    )

    return '\n'.join([
        head,
        name2,
        name3,
        name4,
    ])
