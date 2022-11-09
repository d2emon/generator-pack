"""
Anansi Name.

Anansi is a spider or spider-like trickster originating in Akan folklore, but it can also be found
in Ashanti, Jamaican and Surinamese folklore. Despite being a trickster, he is often celebrated as
a cunning and wise protagonist within his stories. Anansi is able to overcome stronger opponents
through wit and cunning. Stories of the Anansi were passed on orally and survived the slave trade.
In fact, it was a popular story among enslaved Africans because of the Anansi's ability to overcome
stronger opponents. Anansi became a symbol of resistance and survival.

While there is only 1 Anansi within the stories, their name does differ at times (often based on
language). Anansi is also often represented as having a family, though they're not named. This name
generator serves as a way to find names for these types of trickster beings and focuses on names in
an Akan style. The names aren't real, however, merely based on real Akan names. The idea behind it
is to create names representing the supernatural more than the real, while still being tied to both
sides.
Alternatively, the spiderfolk could be of help to you, too. Depending on the type of name you're
looking for.
"""

import random
from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.fantasy import AnansiName


DB = Database('anansi', {
    1: fantasy.anansi.names1,
    8: fantasy.anansi.names8,
})


class AnansiNameFactory(ComplexFactory):
    """Anansi Name Factory."""

    model = AnansiName
    default_data = DB
    block_map = {
        'nm1': 1,
        'nm3': 1,
        'nm5': 8,
    }

    def build_kwargs(self, *args, **kwargs) -> dict:
        """
        Build data for model.

        Returns:
            dict: Data for model.
        """
        nm1 = self.get_field('nm1', *args, **kwargs)
        nm3 = self.get_field('nm3', *args, **kwargs)
        nm5 = self.get_field('nm5', *args, **kwargs)
        return {
            1: nm1,
            2: random.randrange(len(nm1.value)),
            3: nm3,
            4: random.randrange(len(nm3.value)),
            5: nm5,
        }

    def __call__(self, *args, **kwargs) -> AnansiName:
        """
        Validate data for model.

        :param items dict: Data for model
        :return: Data for model
        :rtype: dict
        """
        items = self.build_kwargs(*args, **kwargs)

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

        model = self.model(
            nm0=items[1].value[:items[2]],
            nm1=items[5],
            nm2=items[3].value[items[4] - 1:],
        )

        return model
