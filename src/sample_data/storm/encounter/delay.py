from generated.history.encounters.encounter import Encounter


class DelayEncounter(Encounter):
    is_daily = True
    is_nightly = False
    description = "Задержка в пути — что-то пошло не так и вы потеряли время, " \
                  "заблудились, вынуждены идти кружным путем, подвернули ногу " \
                  "и т.п."
