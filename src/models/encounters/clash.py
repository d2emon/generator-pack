from models.encounters import Encounter
from models.history.time import Time


class ClashEncounter(Encounter):
    allowed_at = [Time.DAY, Time.NIGHT]

    encounter_class_description = "Столкновение – хо-хо, а вот и орки. В смысле, сейчас будет драка." \
        "Возможное столкновение – при неблагоприятных условиях, плохих бросках, " \
        "злобном ведущем и т.п. ситуациях, используйте этот вариант. В принципе, он " \
        "ничем не отличается от первоначального, кроме одного – вам предстоит " \
        "встреча с кем-то совершенно не в духе. При «путевой встрече» это могут " \
        "быть нечистые на руку караванщики, которые, если группа искателей " \
        "приключений кажется им легкой добычей, нападут. При «привале» — герои " \
        "встретятся с облюбовавшим это же место медведем или патрулем зверолюдей."


class MeetEncounter(ClashEncounter):
    # http://stormtower.ru/interesnyie-mesta/tipyi-landshafta-dlya-odinochnyih-i-massovyih-srazheniy.html
    allowed_at = [Time.DAY, Time.NIGHT]

    encounter_class_description = "Путевая встреча – не связанное с «военными действиями» " \
        "событие, характерное для этой местности. Встреча с " \
        "купеческими караванами на дороге или с дровосеком в лесу – " \
        "вот и все примеры."


class HaltEncounter(ClashEncounter):
    allowed_at = [Time.DAY]

    encounter_class_description = "Привал – если вы сейчас же не сделаете привал (короткий, на " \
        "1 час), то или лошадь захромает, или уровень усталости " \
        "группы повысится."
