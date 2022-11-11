from database.data_block import NameBlock
from .races import races
from .marks import marks


data_items = NameBlock(
    *races(),
    *marks(),
)
