from generated.encounter import event_types


ENCOUNTER_TYPES = [
    event_types.ClashEncounter,
    event_types.MeetEncounter,
    event_types.HaltEncounter,
    event_types.HintEncounter,
    event_types.WasteEncounter,
    event_types.DelayEncounter,
]


def encounter_by_time(time=None):
    if time is None:
        return [*ENCOUNTER_TYPES]
    else:
        return [encounter for encounter in ENCOUNTER_TYPES if time in encounter.allowed_at]
