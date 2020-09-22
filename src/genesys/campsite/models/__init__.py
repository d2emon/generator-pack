class Campsite:
    def __init__(
        self,
        description='',
        resources=None,
        encounters=None,
    ):
        self.description = description
        self.resources = resources or []
        self.encounters = encounters or []
