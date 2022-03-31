from generated.encounter import Encounter
from models.history.time import Time


class HintEncounter(Encounter):
    allowed_at = [Time.DAY]
    description = "Подсказка – вы получили относительно ценную информацию. " \
                  "Узнали о том, что поблизости чудовища, что рядом находится " \
                  "деревня, что недавно здесь проходил путешественник и т.п."
