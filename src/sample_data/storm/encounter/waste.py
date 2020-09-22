from genesys.storm.storm import Encounter


class WasteEncounter(Encounter):
    # http://stormtower.ru/sovetyi-vedushhemu-i-igroku-nri/priklyucheniya-pripasyi-kak-sovershit-podvig-poka-ne-konchilas-eda.html
    is_daily = True
    is_nightly = False
    description = "Трата ресурсов – ох, в пути возникла ситуация, когда вам " \
                  "пришлось израсходовать часть ресурсов: запас дров, " \
                  "дополнительные порции провианта, веревку и т.п."
