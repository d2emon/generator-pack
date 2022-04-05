from .template import Template
from .origin import Origin
from .movement import Movement


class Character(Template):
    @property
    def name(self):
        return self.data.get('name', '<UNNAMED>')

    @property
    def template(self):
        return self.data.get('template', Template())

    @property
    def origin(self):
        return self.data.get('origin', Origin())

    @property
    def movement(self):
        return self.data.get('movement', Movement())

    @property
    def stats(self):
        return self.template.stats

    @property
    def skills(self):
        return self.template.skills

    @property
    def hindrances(self):
        return self.template.hindrances

    @property
    def edges(self):
        return self.template.edges

    @property
    def traits(self):
        return self.origin.traits

    @property
    def charisma(self):
        return self.template.charisma

    @property
    def pace(self):
        return self.template.pace

    def __str__(self):
        return self.name
