"""
There’s nothing like working on a project to remind you of the tools you don’t have. I’m putting the final touches on
the Swords of Telm supplement and finding that I need to fill in a few historical gaps. While I have a relatively
complete history in my head (meaning the setting’s history, not my head’s), I don’t mind seeking some polyhedral
guidance.

The tables below cover four eras of a setting’s history. Setting is a loose term—it can apply to a kingdom, a
geographic area, or maybe even an entire world—regardless, it’s up to you to define, based on the size of your
campaign and how you choose to interpret the results. The events you generate represent major turning points—things
that you’d expect to read about in the history scrolls. And, since events often seem to become less significant with
age, you’ll note that the number of these turning points decreases as one travels back along the setting’s timeline.
The implication is that the more distant the era, the more pivotal the events.
"""
import random
from dice.dice import Dice


class Event:
    def __init__(self, year=0, title="<UNKNOWN>"):
        self.year = year
        self.title = title

    def __str__(self):
        return "{} лет назад: {}".format(self.year, self.title)

    def __repr__(self):
        return str(self)


class Era:
    count_dice = Dice(max_value=4)
    years_dice = Dice(max_value=10)
    events = []

    @classmethod
    def generate_years(cls):
        count = cls.count_dice.roll()
        return (sum(cls.years_dice.roll()) for _ in count)

    @classmethod
    def generate(cls):
        for year in cls.generate_years():
            event = random.choice(cls.events)
            yield Event(year, event())


class Prehistory(Era):
    """
    Any event that occurred before recorded history. In most cases, this era is described in speculative terms,
    typically describing how the setting came to be peopled and serving as a precursory justification of the setting’s
    ancient period (see below). As a result, prehistory events may or may not have actually happened, but because
    they’re so broadly foundational and there is little evidence (or need) to dispute them, they are offered with the
    weight of scholarly truth or religious faith. Roll 1d4 events, each spaced 1d10x1000 years apart:

    :return:
    """
    count_dice = Dice(max_value=4)
    years_dice = Dice(max_value=10, multiplier=1000)
    events = [
        lambda: "Божественное очищение через {}".format(random.choice((
            "потоп",
            "землетрясение",
            "извержение",
            "болезнь",
            "космическое событие",
            "магическую энергию",
        ))),
        lambda: "Расцвет {}".format(random.choice((
            "человеческой подрасы",
            "человеческой подрасы",
            "гуманоидной расы",
            "гуманоидной расы",
            "монстров",
            "планарных существ",
        ))),
        lambda: "Упадок {}".format(random.choice((
            "человеческой подрасы",
            "гуманоидной расы",
            "гуманоидной расы",
            "монстров",
            "монстров",
            "планарных существ",
        ))),
        lambda: "Прибытие {}".format(random.choice((
            "новых богов",
            "планарных существ",
            "планарных существ",
            "человеческих племен",
            "гуманоидных племен",
            "пришельцев",
        ))),
        lambda: "Исчезновение {}".format(random.choice((
            "старых богов",
            "старых богов",
            "планарных существ",
            "планарных существ",
            "популяции монстров",
            "могущественной смертной расы",
        ))),
        lambda: "Смертные получают знания {}".format(random.choice((
            "о письме",
            "об основных технологиях",
            "об основных технологиях",
            "о божественном порядке",
            "о новых технологиях",
            "о псионике",
        ))),
        lambda: "Смертные были наказаны за {}".format(random.choice((
            "чрезмерную гордость",
            "падение нравов",
            "поклонение ложным богам",
            "поклонение злым богам",
            "игнорирование богов",
            "то, что поддались греху",
        ))),
        lambda: "Смертным угрожают {}".format(random.choice((
            "планарные существа",
            "злобные чудовища",
            "злобные чудовища",
            "неконтролируемая магическая энергия",
            "неконтролируемая технология",
            "превосходящие виды",
        ))),
    ]


class Ancient(Era):
    """
    These events occurred during the setting’s distant past, typically describing the rise (and possible fall) of an
    ancestral race or explaining the remnants of a now-extinct culture. Like prehistory, ancient events are offered
    with a fair amount of speculation. However, unlike prehistory, there is more evidence of ancient culture (in the
    form of monuments, burial mounds and tombs, lost scrolls, et al.) to inspire scholarly debate and varied
    interpretation. As a result, there is usually enough doubt surrounding ancient events to prevent taking them at
    face value. Roll 2d6 events, each spaced 1d10x100 years apart:

    :return:
    """
    count_dice = Dice(2, 6)
    years_dice = Dice(max_value=10, multiplier=100)
    events = [
        lambda: "Катаклизм ({})".format(random.choice((
            "технология вышла из под контроля",
            "технология вышла из под контроля",
            "магия вышла из под контроля",
            "вмешательство демонов",
            "естественная катастрофа",
            "космическое событие"
        ))),
        lambda: "Возникновение империи",
        lambda: "Падение империи",
        lambda: "Массовая миграция {} в регион".format(random.choice((
            "человеческих племен",
            "человеческих племен",
            "человеческих племен",
            "человеческих племен",
            "гуманоидов",
            "чудовищ",
        ))),
        lambda: "Массовый исход из региона ({})".format(random.choice((
            "человеческих племен",
            "человеческих племен",
            "гуманоидов",
            "гуманоидов",
            "чудовищ",
            "чудовищ",
        ))),
        lambda: "Открытие {}".format(random.choice((
            "передового сельского хозяйства",
            "источника энергии",
            "промышленного материала",
            "передового производства",
            "драгоценного метала",
            "необычного вещества",
        ))),
        lambda: "Историческая личность ({})".format(random.choice((
            "волшебник",
            "мудрец",
            "пророк",
            "изобретатель",
            "художник",
            "раб",
        ))),
        lambda: "Война ({})".format(random.choice((
            "успешная оборона от захватчиков",
            "успешная оборона от захватчиков",
            "успешное завоевание чужой армии",
            "успешное завоевание чужой армии",
            "поражение от захватчиков",
            "неудавшееся вторжение",
        ))),
        lambda: "Процветание империи благодаря {}".format(random.choice((
            "территориальной экспансии",
            "территориальной экспансии",
            "золотому веку",
            "золотому веку",
            "возрождению",
            "возрождению",
        ))),
        lambda: "Упадок империи из-за {}".format(random.choice((
            "сокращения территории",
            "сокращения территории",
            "имперского декаданса",
            "имперского декаданса",
            "технологической отсталости",
            "отсталости в военном плане",
        ))),
        lambda: "Религия ({})".format(random.choice((
            "основана новая религия",
            "основана новая религия",
            "основана новая религия",
            "основана новая религия",
            "исчезла старая религия",
            "исчезла старая религия",
        ))),
        lambda: "Астрологическое событие ({})".format(random.choice((
            "комета",
            "парад звезд",
            "парад планет",
            "возникновение новой звезды",
            "вспышка на солнце",
            "совмещение",
        ))),
    ]


class Past(Era):
    """
    These events occurred after the setting’s ancient period but before the last living generation. About two-thirds of
    these events should provide general support for the setting’s background, while the remaining third forms the
    foundation for present-day adventure hooks. Depending on the setting’s age, this period can span a really long
    time; I recommend rolling 4d6 events, each spaced 1d10x10 years apart, but add as many more as you feel are
    necessary to represent sufficiently the era’s duration:

    :return:
    """
    count_dice = Dice(4, 6)
    years_dice = Dice(max_value=10, multiplier=10)
    events = [
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


class Modern(Era):
    """
    These are events that have occurred within the lifespan of the last living generation; only those living under the
    setting’s rocks will not have some memory of these events, either as a participant, a live observer, or as a direct
    relation to same. Because people tend to have relatively short attention spans, and because the effects of these
    events may still be felt, these events have artificial prominence that the stuff of older histories do not. As a
    rule of thumb, each of these events should form the basis for a current adventure hook, either as stand-alone
    instance or as an extension of an event from a previous era. Roll 2d6 events, each spaced 1d10 years apart:

    :return:
    """
    count_dice = Dice(2, 6)
    years_dice = Dice(max_value=10)
    events = [
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


def generate():
    for event in Prehistory.generate():
        yield event
    for event in Ancient.generate():
        yield event
    for event in Past.generate():
        yield event
    for event in Modern.generate():
        yield event

"""
Final Words
You’re free to use these tables in whatever way best supports your vision of the setting. Determine a number of events 
from each era, then connect them however you see fit. The idea is to let the table results inspire patterns that 
explain how the setting got to be the way it is today. Suggestions are always welcome, and if you create a timeline 
you’re proud of, please post it in the comments section.

"""