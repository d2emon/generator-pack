import random
import unittest
from models.distance import Distance
from models.distance.distance_group import DistanceGroup
from models.encounters import Encounter
from models.encounters.clash import ClashEncounter, MeetEncounter, HaltEncounter
from models.encounters.hint import HintEncounter
from models.encounters.waste import WasteEncounter
from models.encounters.delay import DelayEncounter



class TestEncounterModel(unittest.TestCase):
    def setUp(self):
        self.distance = Distance(
            distance=random.randrange(0, 1000),
            distance_group=DistanceGroup(
                description='DESCRIPTION',
            ),
        )
        return super().setUp()

    def test_encounter(self):
        encounter_text = '\n'.join([
            str(self.distance),
            'DESCRIPTION',
        ])

        encounter = Encounter(
            distance=self.distance,
            is_surprised=False,
            is_surprising=False,
        )

        encounter.description = 'DESCRIPTION'

        self.assertEqual(encounter.distance, self.distance)
        self.assertFalse(encounter.is_surprised)
        self.assertFalse(encounter.is_surprising)
        self.assertEqual(encounter.text, encounter_text)
        self.assertEqual(str(encounter), 'DESCRIPTION')

    def test_encounter_surprised(self):
        encounter_text = '\n'.join([
            str(self.distance),
            'DESCRIPTION',
            'Столкновение застигнуто врасплох',
        ])

        encounter = Encounter(
            description='DESCRIPTION',
            distance=self.distance,
            is_surprised=True,
            is_surprising=False,
        )

        self.assertTrue(encounter.is_surprised)
        self.assertFalse(encounter.is_surprising)
        self.assertEqual(encounter.text, encounter_text)

    def test_encounter_surprising(self):
        encounter_text = '\n'.join([
            str(self.distance),
            'DESCRIPTION',
            'Партия застигнута врасплох',
        ])

        encounter = Encounter(
            description='DESCRIPTION',
            distance=self.distance,
            is_surprised=False,
            is_surprising=True,
        )

        self.assertFalse(encounter.is_surprised)
        self.assertTrue(encounter.is_surprising)
        self.assertEqual(encounter.text, encounter_text)

    def test_clash_encounter(self):
        encounter = ClashEncounter(
            distance=self.distance,
        )

        self.assertEqual(encounter.description, ClashEncounter.encounter_class_description)

    def test_meet_encounter(self):
        encounter = MeetEncounter(
            distance=self.distance,
        )

        self.assertEqual(encounter.description, MeetEncounter.encounter_class_description)

    def test_halt_encounter(self):
        encounter = HaltEncounter(
            distance=self.distance,
        )

        self.assertEqual(encounter.description, HaltEncounter.encounter_class_description)

    def test_delay_encounter(self):
        encounter = DelayEncounter(
            distance=self.distance,
        )

        self.assertEqual(encounter.description, DelayEncounter.encounter_class_description)

    def test_hint_encounter(self):
        encounter = HintEncounter(
            distance=self.distance,
        )

        self.assertEqual(encounter.description, HintEncounter.encounter_class_description)

    def test_waste_encounter(self):
        encounter = WasteEncounter(
            distance=self.distance,
        )

        self.assertEqual(encounter.description, WasteEncounter.encounter_class_description)


if __name__ == "__main__":
    unittest.main()
