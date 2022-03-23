from v1.fixtures import genders
from v1.fixtures.data_block import fill_data
from v1.fixtures.fng.names import fantasy
from v3.models.fng.names.fantasy import ApocalypseNickname
from v1.factories.fng.name_block_factory import NameBlockFactory, GenderNameBlockFactory
from v1.factories.fng.name_factory import ComplexNameFactory, GenderFactory


class ApocalypseNicknameFactory(GenderNameBlockFactory):
    """Apocalypse Nickname Factory

    Not all names will fit mutants, and not all names will fit normal people caught up in a broken world, but there's
    plenty of names for both.
    Many names will overlap as well, like 'Anomaly', 'Ashes', 'Imp', 'Leech', 'Pickle', and 'Slime' to name just a few.
    Each of these names could be used for mutants and nicknames, depending on the meaning you put behind it.

    The names were mainly created as descriptive or role fulfilling names. Like 'Doc', 'Silence', 'Beak', and
    'Feathers'.
    'Doc' is either a doctor or somebody who really wants to be one. Silence is either a quiet person or a mute.
    Beak is most likely a mutant with either a real beak or a deformed face making it look like a beak. Feathers could
    be a mutant with actual feathers or just somebody who dresses up using feathers they found.

    Note that while some names will fit X-Men themed mutants, many of the names were created with less fortunate mutants
    in mind. This is also where the post-apocalyptic theme comes into play. The mutants I had in mind for this generator
    are simply people who were transformed by some sort of apocalypse.

    Quite a few of the names, especially the apocalypse-themed ones, can often be used for duos, like 'Bullet' and
    'Bulletproof', 'Daydream' and 'Nightmare' or 'Ash' and 'Soot'."""

    class MaleNameFactory(ComplexNameFactory):
        model = ApocalypseNickname
        block_map = {
            'nm1': genders.MALE,
        }

    class FemaleNameFactory(ComplexNameFactory):
        model = ApocalypseNickname
        block_map = {
            'nm1': genders.FEMALE,
        }

    class NeutralNameFactory(ComplexNameFactory):
        model = ApocalypseNickname
        block_map = {
            'nm1': genders.NEUTRAL,
        }

    factory_classes = {
        genders.MALE: MaleNameFactory,
        genders.FEMALE: FemaleNameFactory,
        genders.NEUTRAL: NeutralNameFactory,
    }
    default_data = fill_data(group_id='apocalypse')({
        genders.MALE: fantasy.apocalypse.namesMale,
        genders.FEMALE: fantasy.apocalypse.namesFemale,
        genders.NEUTRAL: fantasy.apocalypse.namesNeutral,
    })
