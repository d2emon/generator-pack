import random


EVENTS = [
    lambda: "Открытие {}".format(random.choice((
        "передового сельского хозяйства",
        "источника энергии",
        "промышленного материала",
        "передового производства",
        "драгоценного метала",
        "необычного вещества",
    ))),
    lambda: "Историческая личность ({})".format(random.choice((
        "мудрец",
        "мудрец",
        "изобретатель",
        "исследователь",
        "художник",
        "советник",
    ))),
    lambda: "Герой войны ({})".format(random.choice((
        "блестящий генерал",
        "блестящий генерал",
        "лидер элитного подразделения",
        "мастер шпионажа",
        "героиня боя",
        "средний солдат",
    ))),
    lambda: "Война ({})".format(random.choice((
        "успешная оборона от захватчиков",
        "успешное завоевание чужой армии",
        "успешное завоевание чужой армии",
        "поражение от захватчиков",
        "неудавшееся вторжение",
        "неудавшееся вторжение",
    ))),
    lambda: "Процветание королевства благодаря {}".format(random.choice((
        "территориальной экспансии",
        "территориальной экспансии",
        "территориальной экспансии",
        "избытку ресурсов",
        "избытку ресурсов",
        "победе над врагом",
    ))),
    lambda: "Упадок королевство из-за {}".format(random.choice((
        "сокращения территорий",
        "сокращения территорий",
        "потери торговых партнеров",
        "потери торговых партнеров",
        "потери источника основного ресурса",
        "потери источника основного ресурса",
    ))),
    lambda: "Стихийное бедствие ({})".format(random.choice((
        "пожар",
        "потоп",
        "землетрясение",
        "метеориты",
        "вулканы",
        "ужасные ураганы"
    ))),
    lambda: "Рукотворное бедствие ({})".format(random.choice((
        "пожар",
        "потоп",
        "голод",
        "мор",
        "загрязнение",
        "загрязнение"
    ))),
    lambda: "Увеличение королевства {}".format(random.choice((
        "через завоевания",
        "через завоевания",
        "через колонизацию",
        "через колонизацию",
        "дипломатическими средствами",
        "дипломатическими средствами",
    ))),
    lambda: "Религия ({})".format(random.choice((
        "основана новая религия",
        "увеличивается религиозный раскол",
        "увеличивается религиозный раскол",
        "основан культ",
        "основан культ",
        "исчезла старая религия",
    ))),
    lambda: "Астрологическое событие ({})".format(random.choice((
        "комета",
        "метеоритный дождь",
        "затмение",
        "затмение",
        "вспышка на солнце",
        "совмещение",
    ))),
    lambda: "Расцвет королевства",
    lambda: "Падение королевства",
    lambda: "Восстание ({}) возглавляемое {}".format(
        random.choice((
            "успешное",
            "успешное",
            "успешное",
            "успешное",
            "подавленое",
            "подавленое",
        )),
        random.choice((
            "армией",
            "крестьянством",
            "колониями",
            "анархистами",
            "рабами",
            "заключенными",
        )),
    ),
    lambda: "Политическая система {}".format(random.choice((
        "столкнулась с испытанием",
        "столкнулась с испытанием",
        "создана",
        "реформирована",
        "изменена",
        "развалилась",
    ))),
    lambda: "Культ {}".format(random.choice((
        "основан",
        "основан",
        "основан",
        "искоренен",
        "искоренен",
        "приобретает власть",
    ))),
    lambda: "Сильный лидер {}".format(random.choice((
        "у власти",
        "у власти",
        "умирает по естественным причинам",
        "убит",
        "канонизирован",
        "отрекается от власти",
    ))),
    lambda: "Слабый лидер {}".format(random.choice((
        "у власти",
        "умирает по естественным причинам",
        "убит",
        "убит",
        "насильно свергнут",
        "насильно свергнут",
    ))),
    lambda: "Геноцид {}".format(random.choice((
        "местного расового меньшинства",
        "местного расового меньшинства",
        "местного расового меньшинства",
        "группы иностранцев",
        "группы иностранцев",
        "религиозной секты",
    ))),
    lambda: "Население уезжает {}".format(random.choice((
        "на поиски ресурсов",
        "на поиски ресурсов",
        "за изобретением",
        "из-за катастрофы",
        "из-за репрессий",
        "в результате войны",
    ))),
]
