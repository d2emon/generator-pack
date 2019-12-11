from factory import SimpleItem
from sample_data import get_from_group


class SailingConditions(SimpleItem):
    default_data = [item.get('value') for item in get_from_group('sailing-conditions')]
