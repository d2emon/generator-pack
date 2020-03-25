from models.storm.encounters.encounter import Encounter


class HintEncounter(Encounter):
    is_daily = True
    is_nightly = False
    description = "Подсказка – вы получили относительно ценную информацию. " \
                  "Узнали о том, что поблизости чудовища, что рядом находится " \
                  "деревня, что недавно здесь проходил путешественник и т.п."
