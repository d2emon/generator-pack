from models.encounters.events.clash import ClashEncounter, MeetEncounter, HaltEncounter
from models.encounters.events.hint import HintEncounter
from models.encounters.events.waste import WasteEncounter
from models.encounters.events.delay import DelayEncounter


ENCOUNTER_TYPES = [
    ClashEncounter,
    MeetEncounter,
    HaltEncounter,
    HintEncounter,
    WasteEncounter,
    DelayEncounter,
]


def encounter_by_time(time=None):
    if time is None:
        return [*ENCOUNTER_TYPES]
    else:
        return [encounter for encounter in ENCOUNTER_TYPES if time in encounter.allowed_at]
