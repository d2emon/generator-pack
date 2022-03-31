import random
import unittest
from models.history.event import Event


class TestEventModel(unittest.TestCase):
    def test_event_max_time(self):
        year = random.randrange(0, 100)
        title = str(random.uniform(0, 100))
        event_text = f"{year} лет назад: {title}"

        event = Event(
            year=year,
            title=title,
        )

        self.assertEqual(event.value, title)
        self.assertEqual(str(event), event_text)


if __name__ == "__main__":
    unittest.main()
