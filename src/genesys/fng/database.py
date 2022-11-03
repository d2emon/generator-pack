from database.data_block import fill_data


class Database:
    def __init__(self, group_id, data):
        self.data = fill_data(group_id=group_id)(data)
