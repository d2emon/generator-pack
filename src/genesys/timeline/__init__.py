"""
There’s nothing like working on a project to remind you of the tools you don’t have. I’m putting the final touches on
the Swords of Telm supplement and finding that I need to fill in a few historical gaps. While I have a relatively
complete history in my head (meaning the setting’s history, not my head’s), I don’t mind seeking some polyhedral
guidance.

The tables below cover four eras of a setting’s history. Setting is a loose term—it can apply to a kingdom, a
geographic area, or maybe even an entire world—regardless, it’s up to you to define, based on the size of your
campaign and how you choose to interpret the results. The events you generate represent major turning points—things
that you’d expect to read about in the history scrolls. And, since events often seem to become less significant with
age, you’ll note that the number of these turning points decreases as one travels back along the setting’s timeline.
The implication is that the more distant the era, the more pivotal the events.
"""
from providers.data_manager import DataManager
from . import era, timeline


class TimelineManager(DataManager):
    class DataProvider(DataManager.DataProvider):
        def __init__(self):
            # self.__desert_encounters = DataItemFactory(groups.DESERT_ENCOUNTERS)
            self.__prehistory = era.Prehistory()
            self.__ancient = era.Ancient()
            self.__past = era.Past()
            self.__modern = era.Modern()

        @property
        def prehistory(self):
            return self.__prehistory

        @property
        def ancient(self):
            return self.__ancient

        @property
        def past(self):
            return self.__past

        @property
        def modern(self):
            return self.__modern

        @property
        def timeline(self):
            yield from self.prehistory.events()
            yield from self.ancient.events()
            yield from self.past.events()
            yield from self.modern.events()

    @classmethod
    def timeline(cls):
        return timeline.TimelineModel(cls.get_provider().timeline)


"""
Final Words
You’re free to use these tables in whatever way best supports your vision of the setting. Determine a number of events 
from each era, then connect them however you see fit. The idea is to let the table results inspire patterns that 
explain how the setting got to be the way it is today. Suggestions are always welcome, and if you create a timeline 
you’re proud of, please post it in the comments section.

"""