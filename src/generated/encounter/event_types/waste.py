from generated.encounter import Encounter
from generated.history.time import Time


class WasteEncounter(Encounter):
    # http://stormtower.ru/sovetyi-vedushhemu-i-igroku-nri/priklyucheniya-pripasyi-kak-sovershit-podvig-poka-ne-konchilas-eda.html
    allowed_at = [Time.DAY]
    description = "Трата ресурсов – ох, в пути возникла ситуация, когда вам " \
                  "пришлось израсходовать часть ресурсов: запас дров, " \
                  "дополнительные порции провианта, веревку и т.п."