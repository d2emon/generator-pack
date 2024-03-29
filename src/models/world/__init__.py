from models.complex_model import ComplexModel
from .shape import WorldShape
from .size import WorldSize
from .world_type import WorldType


"""
        # Общие вопросы о создаваемом мире
        # 1. Сколько лун у вашего мира?
        # 2. Сколько созвездий в ночном небе?
        # 3. Сколько солнц?
        # 4. Владение земельным наделом важно для социального статуса?
        # 5. Насколько опасна тут зима?
        # 6. Какая музыка популярна среди простого народа?
        # 7. Какое морское сражение было самым масштабным в истории?
        # 8. Что популярнее — вино или пиво?
        # 9. Какое домашнее животное самое распространённое?
        # 10. Какое самое распространённое имя?
        # 11. Есть ли какой-либо символ, обозначающий этот мир в целом?
        # 12. Кто — самый известный убийца? Кого он убил?
        # 13. Как богатые предпочитают тратить деньги?
        # 14. Какой цвет предпочитает знать?
        # 15. Какие истории рассказывают детям этого мира, чтобы они не попали в беду?
        # 16. Какого цвета небо?
        # 17. Есть ли в мире священные города?
        # 18. Появилась ли одна раса прежде остальных?
        # 19. Случались ли недавно крупные войны?
        # 20. Какой праздник празднуют с наибольшим размахом?
        # 21. Сколько сезонов в этом мире?
        # 22. Древние артефакты разбросаны по миру?
        # 23. Правителями самой могучей державы мира становятся по наследству или в результате выборов?
        # 24. Что ценнее — корова или золотая монета?
        # 25. Часты ли болезни и эпидемии?
        # 26. Какие опасные существа блуждают в ночи?
        # 27. Существует ли общемировой язык?
        # 28. Какой музыкальный инструмент наиболее распространён?
        # 29. Какой праздник самый странный?
        # 30. Есть ли животные, на которых запрещено охотиться и убивать?
        # 31. Как называется этот мир?
        # 32. Кто самый известный музыкальный исполнитель?
        # 33. Политиков любят или презирают?
        # 34. Какая битва была самой известной в истории?
        # 35. Какое морское существо самое опасное?
        # 36. Какой природный катаклизм наиболее частый?
        # 37. Что воспринимается как самая опасная форма магии?
        # 38. Драконы миф, частое зрелище, или не существуют?
        # 39. Каким особым способом здесь казнят отпетых преступников?
        # 40. Кто в этом мире самый известный военачальник?
        # 41. Все расы этого мира происходят из одной перворасы?
        # 42. Есть ли огнестрельное оружие?
        # 43. Насколько глубоки океаны? Есть ли в них разумная жизнь?
        # 44. Какой высоты самые высокие городские стены этого мира?
        # 45. Появлялись ли боги в физической форме?
        # 46. Напишите четверостишие об известном правителе.
        # 47. Какой музыкальный жанр популярен среди элиты?
        # 48. Сколько дней в году?
        # 49. Городская охрана считается в основном честной или в основном коррумпированной?
        # 50. Чего больше боятся крестьяне — неурожая или злых чудовищ?
        # 51. Есть ли народные герои, часто упоминаемые в балладах и байках?
        # 52. Какой самый быстрый способ перемещения?
        # 53. Какая смерть считается достойной?
        # 54. Народу позволено вступать в брак свободно или браки происходят по расчету?
        # 55. Люди мира поклоняется нескольким богам одновременно или только одному?
        # 56. Рабство — частое явление?
        # 57. Что воспринимается самым бесчестным преступлением?
        # 58. Какого цвета облака?
        # 59. Много ли курящих?
        # 60. Есть ли перенаселённые области?
        # 61. Как отреагирует бездомный, увидев колдовство?
        # 62. Сколько спален в доме представителя среднего класса?
        # 63. Корабли движимы ветром, углём, или чем-то иным?
        # 64. Какова выживаемость пациентов лекаря?
        # 65. Какая древняя империя считается самой могущественной?
        # 66. Есть ли обширная сеть подземных пещер под миром? Кто её населяет?
        # 67. Кто самый великий волшебник?
        # 68. Есть ли у кого-то из монархов страшные тайны?
        # 69. Общепризнано ли кровопускание или другие «ненаучные» методы лечения?
        # 70. Мир круглый, плоский, или иной формы?
        # 71. Какого цвета луны?
        # 72. Сколько дней в неделе?
        # 73. Оборотни — реальная угроза или страшилка?
        # 74. Народ в основном монотеистичен?
        # 75. Есть ли расовое недопонимание в мире или разные народы относятся друг к другу спокойно?
        # 76. Часты ли видения и пророчества?
        # 77. Кто-либо ставил ужасные незаконные эксперименты на магах?
        # 78. Существует ли воскрешение? Как это влияет на политику?
        # 79. Какова средняя продолжительность жизни среди богатых? Среди бедных?
        # 80. Есть ли воздушные корабли?
        # 81. Кто-либо взбирался на высочайшую гору мира?
        # 82. Учителя достаточно богаты или ужасно бедны?
        # 83. Какие есть в этом мире особые виды металла?
        # 84. Есть ли какая-либо угроза, против которой всё население мира обязано сплотиться?
        # 85. Когда в последний раз убивали значимого политика?
        # 86. Где видят границу мироздания?
        # 87. Какой народ или империя считается самым мощным в военном отношении?
        # 88. Что является самым желаемым ресурсом?
        # 89. Как в богатых домах подают мясные блюдо? Применяют ли магию?
        # 90. Напишите популярный в этом мире фразеологизм, вроде «не играй с огнём».
        # 91. Книги редки и ценны?
        # 92. Существует ли лотерея?
        # 93. Есть ли какой-либо часто встречающийся врождённый дефект организма?
        # 94. Существуют ли гильдии искателей приключений?
        # 95. Что является валютой в разных регионах мира?
        # 96. Происходит ли где-либо политическая или военная интервенция?
        # 97. Какая организация самая «злая» и что мешает ей захватить мир?
        # 98. Голодают ли бедняки?
        # 99. Все дороги ведут в…
        # 100. Есть ли хоть что-либо за пределами этого мира?
        101. Какая морская рыба самая большая? Её хоть раз удалось поймать?
        102. Как опасно путешествовать по морю? (По десятибалльной шкале).
        103. Какое животное чаще всего используют для перевозки грузов?
        104. Насколько безопасны дороги?
        105. Есть ли нелегальные вещества? Какие? Как контролируют их распространение?
        106. Похищали ли когда-либо мага из-за его способностей?
        107. Насколько часты и открыты культы?
        108. Кто самый могущественный политик?
        109. Насколько легко перемещаться между измерениями?
        110. Если похитят наследника самого могущественного трона, как отреагирует народ?
        111. Разрушала ли целый город природная катастрофа?
        112. Назван ли мир в честь знаменитой личности или события? Если нет, то что послужило источником его названия?
        113. Выгодно ли быть искателем приключений? Или этим занимаются только бедняки, которым нечего терять?
        114. Насколько стар мир?
        115. Кто самый знаменитый деятель искусства? Ремесленник?
        116. Есть ли единое политическое объединение, вроде ООН?
        117. Какой процент населения — мужчины?
        118. Нежить — серьёзная угроза или байка?
        119. Мир вращается вокруг солнца или наоборот?
        120. Пытались ли злые силы установить контроль над миром?
"""

# Магия и создаваемый мир
# 1.  Как отреагирует попрошайка, если получит обладающий магией
#     волшебный предмет?
# 2.  Существует ли магия воскрешения? Если да, она зарезервирована для
#     могучих и богатых, или беднота тоже имеет шанс вернуться из
#     мёртвых?
# 3.  Как магия влияет на ведение войны? Полны ли поля сражения взрывов
#     огнешаров и зачарованного оружия?
# 4.  Если кто-то публично заявит, что имеет магический дар, ему
#     предложат работу? Отправят на виселицу?
# 5.  Алхимия — магия или наука?
# 6.  Есть ли виды магии в мире кроме обычных двух (арканной и
#     божественной)?
# 7.  Насколько просто создать зачарованное оружие?
# 8.  Магия исходит от земли, неба, воды, или ещё чего-то?
# 9.  Магия изначально добра, зла, или зависит от владельца?
# 10. Можно ли вложить магию в обыденный вещи вроде доспех и украшений?
# 11. Откуда черпает свою магию самое волшебное место мира?
# 12. Волшебниками рождаются или становятся?
# 13. Стремились ли страны или организации ограничивать количество
#     магии в мире?
# 14. Какой процент населения верит в магию?
# 15. Энергия на заклинания берётся с потолка или опустошает какой-либо
#     ресурс?

# Религия и создаваемый мир
# 1.  Боги реальны?
# 2.  Насколько активны боги в делах мира? (по дестибальной шкале).
# 3.  Сколько богов?
# 4.  Насколько могущественной должна быть личность, чтобы простые люди
#     воспринимали её как бога?
# 5.  Как жрецы получают волшебную силу?
# 6.  Выбрали ли вы пантеон из существующего сеттинга или придумали
#     сами?
# 7.  Есть ли бог жизни? А бог смерти? Они противостоят друг другу?
# 8.  Есть ли бог природы? А бог цивилизации? Они противостоят друг
#     другу?
# 9.  Простые крестьяне молятся тем же богам, что богачи?
# 10. Заботит ли богов происходящее на земле?
# 11. Есть ли главный бог?
# 12. Есть ли злые боги? Если нет, есть ли демоны или дьяволы?
# 13. Боги отвечают на молитвы прямым вмешательством, неочевидно, или
#     пропускают мимо ушей?
# 14. Могут ли боги умереть? Если да, то как?
# 15. Олицетворяет ли каждый бог определённую область существования?
#     Например: жизнь, смерть, природа, земледелие, убийство, любовь,
#     красота, скорость, война, празднество, весна, осень, лето, зима,
#     плодородие, строительство/архитектура, игры, превосходство
#     гуманоидной формы, тьма, свет, прошлое и/или будущее, морское
#     путешествие, торговля.


class World(ComplexModel):
    children = {
        'shape': WorldShape,
        'world_type': WorldType,
        'size_class': WorldSize,
    }

    value = ComplexModel.field_property('name', '')

    name = ComplexModel.field_property('name', '')
    shape = ComplexModel.field_property('shape')
    size_class = ComplexModel.field_property('size_class')
    world_size = ComplexModel.field_property('world_size', 0)
    world_type = ComplexModel.field_property('world_type')

    @property
    def field_names(self):
        yield "name"
        yield "world_size"
        yield "size_class"

        # Children
        yield "shape"
        yield "world_type"

    @property
    def description(self):
        return "\n".join([
            f"{self}"
            f"{self.world_type} {self.shape} ({self.world_size} миль)",
            f"{self.world_type.description}",
            f"Возможные столкновения: {self.world_type.encounters}",
            f"{self.shape.description}",
            f"{self.size_class.description}",
        ])
