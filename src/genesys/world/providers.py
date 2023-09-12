
import config
from database.file_database import TextDatabase


class WorldDataProvider:
    def __init__(self, names):
        self.names = [*names]


DATABASE = TextDatabase(
    'world.txt',
    DATABASE_ROOT=config.DATA_PATH,
)


DEFAULT_DATA_PROVIDER = WorldDataProvider(
    names=DATABASE.data,
)
