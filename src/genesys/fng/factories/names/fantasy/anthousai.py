from utils import genders
from database.data_block import fill_data
from data.fng.names import fantasy
from models.fng.names.fantasy import AnthousaiName
from genesys.fng.factories.name_block_factory import NameBlockFactory, GenderNameBlockFactory
from genesys.fng.factories.name_factory import ComplexNameFactory, GenderFactory


class AnthousaiNameFactory(GenderNameBlockFactory):
    """Anthousai Name Factory

    Anthousai are flower nymphs, just as dryads are tree nymphs. But unlike dryads, anthousai aren't as well known
    outside of Greek mythology.
    Anthousai have hair that resembles hyacinths, a plant with flowers in vibrant colors ranging from white to blues to
    purples. Being nymphs, they're usually associated with female freedom and sexuality, but the extend of this can vary
    from simply free, female deities of nature to sexually promiscuous deities out to seduce men.

    Known anthousai names range are usually either color names or flower names, but we usually named flowers after Greek
    deities rather than the other way round. This name generator has both flower names and color names, but the flower
    names are mostly in Latin (as well as English or French depending on your choice below). Colors have their
    translation in brackets. Gender doesn't seem to matter for names, as Chloris is spelled with the masculine suffix
    despite being a woman."""

    class MaleNameFactory(ComplexNameFactory):
        model = AnthousaiName
        block_map = {
            'nm1': 1,
        }

    class FemaleNameFactory(ComplexNameFactory):
        model = AnthousaiName
        block_map = {
            'nm1': 2,
        }

    factory_classes = {
        genders.MALE: MaleNameFactory,
        genders.FEMALE: FemaleNameFactory,
    }
    default_data = fill_data(group_id='anthousai')({
        1: fantasy.anthousai.nm1,
        2: fantasy.anthousai.nm2,
    })
