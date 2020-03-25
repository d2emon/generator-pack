from factories.factory import SimpleItem
from sample_data import get_from_group


class DesertEncounter(SimpleItem):
    default_data = [item.get('value') for item in get_from_group('desert-encounters')]
