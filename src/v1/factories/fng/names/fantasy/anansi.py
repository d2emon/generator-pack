import random
from v1.fixtures.data_block import load_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import AnansiName
from v1.factories.fng.name_factory import NameFactory


class AnansiNameFactory(NameFactory):
    """Anansi Name Factory

    Anansi is a spider or spider-like trickster originating in Akan folklore, but it can also be found in Ashanti,
    Jamaican and Surinamese folklore. Despite being a trickster, he is often celebrated as a cunning and wise
    protagonist within his stories. Anansi is able to overcome stronger opponents through wit and cunning.
    Stories of the Anansi were passed on orally and survived the slave trade. In fact, it was a popular story among
    enslaved Africans because of the Anansi's ability to overcome stronger opponents. Anansi became a symbol of
    resistance and survival.

    While there is only 1 Anansi within the stories, their name does differ at times (often based on language).
    Anansi is also often represented as having a family, though they're not named. This name generator serves as a way
    to find names for these types of trickster beings and focuses on names in an Akan style. The names aren't real,
    however, merely based on real Akan names. The idea behind it is to create names representing the supernatural more
    than the real, while still being tied to both sides.
    Alternatively, the spiderfolk could be of help to you, too. Depending on the type of name you're looking for."""

    name_class = AnansiName
    default_blocks = load_data({
        1: fantasy.anansi.names1,
        8: fantasy.anansi.names8,
    })
    blocks_map = {
        1: 1,
        3: 1,
        5: 8,
    }

    def get_items(self) -> dict:
        items = super().get_items()
        return {
            1: items[1],
            2: random.randrange(len(items[1].value)),
            3: items[3],
            4: random.randrange(len(items[3].value)),
            5: items[5],
        }

    def validate(self, items) -> dict:
        # 2
        if items[2] < 1:
            items[2] = 1
        if (items[2] < 3) and (len(items[1]) > 4):
            items[2] = 3
        if items[2] > 5:
            items[2] = 5

        # 4
        if items[4] < 1:
            items[4] = 1
        if (items[4] < 3) and (len(items[3]) > 4):
            items[4] = 3
        if items[4] > 5:
            items[4] = 5

        # 2
        if (items[2] == 1) and (items[4] == 1):
            items[2] = 2

        return {
            0: items[1].value[:items[2]],
            1: items[5],
            2: items[3].value[items[4] - 1:],
        }
