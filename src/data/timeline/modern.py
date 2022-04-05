import random


EVENTS = [
    lambda: "Война ({})".format(random.choice((
        "успешная оборона от захватчиков",
        "успешное завоевание чужой армии",
        "поражение на чужих берегах",
        "ведется дипломатически",
        "продолжающаяся оборона",
        "продолжающееся вторжение",
    ))),
    lambda: "Бедствие ({})".format(random.choice((
        "пожар",
        "потоп",
        "голод",
        "болезнь",
        "землетрясение",
        "погодные катаклизмы"
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
        "увеличивается религиозный раскол",
        "возрождение православия",
        "вынуждена уцйти в подполье",
        "приобретает светскую власть",
        "чистка \"неверных\"",
        "поглощен связаный культ",
    ))),
    lambda: "Астрологическое событие ({})".format(random.choice((
        "комета",
        "метеоритный дождь",
        "метеоритный дождь",
        "затмение",
        "совмещение",
        "совмещение",
    ))),

    lambda: "Скандал ({})".format(random.choice((
        "religious head",
        "religious head",
        "ruling family",
        "ruling family",
        "military leader",
        "high-level bureaucrat",
    ))),
    lambda: "Образование графства (или другого подразделения королевства)",
    lambda: "Ликвидация графства (или другого подразделения королевства)",
    lambda: "Восстание ({}) возглавляемое {}".format(
        random.choice((
            "успешное",
            "продолжающееся",
            "продолжающееся",
            "продолжающееся",
            "подавленое",
            "подавленое",
        )),
        random.choice((
            "крестьянством",
            "крестьянством",
            "анархистами",
            "анархистами",
            "рабами",
            "заключенными",
        )),
    ),
    lambda: "Политическая партия {}".format(random.choice((
        "challenged",
        "challenged",
        "created",
        "reformed",
        "replaced",
        "dissolved",
    ))),
    lambda: "Культ {}".format(random.choice((
        "formed",
        "formed",
        "forced underground",
        "forced underground",
        "rises to legitimacy",
        "rooted out",
    ))),
    lambda: "Лидер {}".format(random.choice((
        "found insane",
        "scandalised",
        "heralds prosperity",
        "assassinated",
        "abdicates",
        "roots out injustice",
    ))),
    lambda: "Раскол между {}".format(random.choice((
        "political contenders",
        "noble families",
        "noble families",
        "religious factions",
        "religious factions",
        "guilds",
    ))),
    lambda: "Политическая реформа {} {}".format(
        random.choice((
            "improves",
            "improves",
            "improves",
            "worsens",
            "worsens",
            "worsens",
        )),
        random.choice((
            "tax rates",
            "tax rates",
            "minority rights",
            "laws of conscription",
            "slavery",
            "system of law",
        )),
    ),
    lambda: "Крупные чудовища {}".format(random.choice((
        "population increases",
        "population increases",
        "hunted down",
        "hunted down",
        "establishes wilderness foothold",
        "eradicated from setting",
    ))),
    lambda: "Экономика ({})".format(random.choice((
        "tax increase",
        "raider activity rising",
        "economic boom",
        "recession",
        "trade route discovered",
        "guild unrest",
    ))),
    lambda: "Population {}".format(random.choice((
        "boom",
        "boom",
        "decline",
        "divided",
        "divided",
        "whispers revolt",
    ))),
    lambda: "Создание нового {}".format(random.choice((
        "food production",
        "manufacturing",
        "weaponry",
        "medicine",
        "defence",
        "transport/communication",
    ))),
    lambda: "Преступность {}".format(random.choice((
        "rises in urban areas",
        "rises in urban areas",
        "plagues the countryside",
        "plagues the countryside",
        "is ruthlessly quashed",
        "prompts new laws",
    ))),
    lambda: "Этническое меньшинство {}".format(random.choice((
        "seeks diplomatic sovereignty",
        "seeks diplomatic sovereignty",
        "suffers persecution",
        "foments sedition",
        "afforded special legal status",
        "migrates out of area",
    ))),
]