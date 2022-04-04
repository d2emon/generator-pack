from data.scales import ITEMS


MIN_SCALE = -36
MAX_SCALE = 30


def in_scale(scale_from, scale_to=None, items=ITEMS):
    if scale_to is None:
        scale_to = scale_from + 2
        scale_from = scale_from - 1
    return filter(lambda i: i.width.scale in range(scale_from, scale_to), items)


def metric(scale):
    metrics = {
        -24: "и",
        -21: "з",
        -18: "а",
        -15: "ф",
        -12: "п",
        -9: "н",
        -6: "мк",
        -3: "м",
        0: "",
        3: "к",
        6: "М",
        9: "Г",
        12: "Т",
        15: "П",
        18: "Э",
        21: "З",
        24: "И",
    }
    return metrics.get(scale, "?") + "м"


def compared(scale):
    compares = {
        -36: "Струна",
        -24: "Нейтрино",
        -21: "Преон",
        -18: "Кварк",
        -15: "Частица",
        -12: "Водород",
        -9: "Молекула",
        -6: "Бактерия",
        -3: "Насекомое",
        0: "Человек",
        3: "Город",
        6: "Планета",
        9: "Звезда",
        12: "Система",
        15: "Туманность",
        18: "Скопление",
        21: "Галактика",
        24: "Кластер",
        27: "Вселенная",
    }
    return compares.get(scale, "?")
