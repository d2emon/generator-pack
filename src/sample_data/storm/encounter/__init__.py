from .clash import ClashEncounter, MeetEncounter, HaltEncounter
from .hint import HintEncounter
from .waste import WasteEncounter
from .delay import DelayEncounter


ENCOUNTER_TYPES = [
    ClashEncounter,
    MeetEncounter,
    HaltEncounter,
    HintEncounter,
    WasteEncounter,
    DelayEncounter,
]
