from generated.encounter import Encounter
from models.history.time import Time


class DelayEncounter(Encounter):
    allowed_at = [Time.DAY]
    description = "Задержка в пути — что-то пошло не так и вы потеряли время, " \
                  "заблудились, вынуждены идти кружным путем, подвернули ногу " \
                  "и т.п."
