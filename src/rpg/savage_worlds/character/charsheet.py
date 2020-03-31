from rpg.savage_worlds.character.traits.skills import skill


def show_stats(character):
    print(character.agility)
    print(character.smarts)
    print(character.spirit)
    print(character.strength)
    print(character.vigor)
    print('Шаг:\t{}'.format(character.pace))
    print('Защита:\t{}'.format(character.parry))
    print('Харизма:\t{}'.format(character.charisma))
    print('Стойкость:\t{}'.format(character.toughness))
    print('Неиспользованных Улучшений:\t{}'.format(max(0, character.unused_stat_points)))
    print()


def show_edges(character):
    print('Черты:')
    for edge in character.edges:
        print('\t{}'.format(edge))
    print('Обычные черты:')
    print('Цветные черты:')
    print('Неиспользованных Улучшений:\t{}'.format(max(0, character.unused_points)))
    print()


def show_skills(character):
    print('Умения:')
    for skill_class in skill.SKILLS:
        print('\t{}'.format(character.get_skill(skill_class)))
    print('\tНеиспользованных Улучшений:\t{}'.format(max(0, character.unused_skill_points)))
    print()


def show_hindrances(character):
    print('Изъяны:')
    for hindrance in character.hindrances:
        print('\t{}'.format(hindrance))
    print('Увечья:')
    print('Отпечатки:')
    print('Возможных больших изъянов:\t{}'.format(max(0, character.unused_big_hindrance_points)))
    print('Возможных малых изъянов:\t{}'.format(max(0, character.unused_small_hindrance_points)))
    print()


def show_equipment(character):
    print('Валюта:\t{}'.format(character.money))
    print()
    print('Снаряжение:')
    print('\tСнаряжение\tКачество\tВес')
    for equipment in character.equipment:
        print('\t{}'.format(equipment))


def charsheet(character):
    print('Имя:')
    print('Происхождение:')
    print('Движение:')
    print('Концепция:')
    print('Ранг:')
    print('Повышения:')
    print('Погружение:')
    print('Фишки:')
    print('\tОбычные:')
    print('\tЦветные:')
    print()

    show_stats(character)
    show_edges(character)
    show_skills(character)
    show_hindrances(character)

    print('Сила:')
    print('\tСила\tЦена\tДистанция\tУрон/эффект\tДлительность')
    print()

    print('Оружие:')
    print('\tОружие\tДистанция\tСк\tУрон\tББ\tВес\tЗаметки')
    print()

    show_equipment(character)

    print('Максимальный вес:')
    print('Нагрузка:')
    print('Штраф:')
    print()

    print('Ранения:')
    print('Усталость:')
    print()

    print('Патроны:')
    print('Пункты Силы:')
    print()

    print(character.bio)
    print(character.unused_points)
