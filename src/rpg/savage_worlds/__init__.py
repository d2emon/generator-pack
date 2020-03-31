from .intro import *

from .campaigns import space1889
from .campaigns import deadlands
from .campaigns import weird_wars
from .campaigns import solomon_kane
from .campaigns import rippers

from .character import *
from .equipment import *  # 50 55 60 65
from .basic_rules import *  # 66 70 75 80
from .situationary_rules import *  # 85 90 95 100 105
from .forces import *  # 107 110 115 120
from .campaigning import *  # 125 130
from .bestiary import *  # 135 140 145
from .modules import *  # 149 150 160 165
from .tables import *  # 166
# 170

"""
Savage Worlds
=============

Settings
--------

Although Savage Worlds is a generic rules system, Pinnacle has released "Savage Settings" - campaign settings or
modules designed specifically for the Savage Worlds rules. These have included Evernight, 50 Fathoms, Necessary Evil,
Rippers, and Low Life. Pinnacle has also published setting books based on the company's earlier lines, including
Deadlands: Reloaded as well as the Tour of Darkness, Necropolis, and Weird War II settings based on the Weird Wars line.

Beginning with 50 Fathoms, the majority of settings released by Pinnacle feature a concept known as a "Plot Point
Campaign". In such campaigns, a series of loosely defined adventure scenarios are presented. A main storyline is
presented as a series of "Plot Points" and additional side-quests (or "Savage Tales") expand the scope of the campaign.
This format allow a group of characters to explore the game universe while playing through (or disregarding) the main
storyline in a manner similar to that of role-playing video games.

A licensing system is in place for electronic and book publishers to release material for the Savage Worlds game. Such
"Savaged!" licensees are allowed to use the Savage Worlds mascot "Smiling Jack" as a logo on their products. Multiple
PDF adventure scenarios are available using this licensing system, as well as setting related supplements like the
Vampire Earth RPG Sourcebook and the Shaintar Player's Guide.

System
------

### Character creation

Player characters are built using a point allocation system, though game masters are encouraged to design non-player
characters to the needs of the game rather than to fit the system. Characters in Savage Worlds are composed of a
variety of statistics. These include Race, Traits, Edges, Hindrances and sometimes Powers.

#### Race

A character's race usually refers to their species, which may grant or impose modifiers to characteristics. In some
settings (such as the Pirates of the Spanish Main RPG) this may instead refer to nationality, which typically does not.
Nationality based differences may occur in campaigns where certain Skill specializations, Edges and Hindrances are
affected by cultural or technological differences or are included to add flavor to a character. For instance, in
Deadlands: Reloaded a non-Chinese character may learn Chinese Martial Arts but cannot acquire and use its Chi-based
Powers. In Weird War II American, British, or French soldiers have special Edges and Hindrances to reflect their
different national and military cultures.

#### Traits (Attributes & Skills)

A character's traits are characteristics that are rated by a single polyhedral die. The more sides the trait is rated
in, the better the character is at the trait - ranging from a 4-sided die (d4 - the lowest) to a 12-sided die (d12 -
the highest). So a character with a Strength trait of a ten-sided die (d10) is stronger than a character whose Strength
trait is rated with a six-sided die (d6). Traits are divided into Attributes, which are inherent, and Skills, which are
learned.

The five Attributes used in Savage Worlds are Agility (Physical Precision and Speed), Smarts (Mental Power), Spirit
(Willpower), Strength (Physical Power) and Vigor (Physical Health). Attributes start at Level 1 (d4) and cost one point
per additional level; Level 1 (d4) in an Attribute would cost nothing and Level 5 (d12) would cost four points. The
number of points assigned to spend on Attributes is usually 5 points, but can be more in certain gameworlds.

Attributes are also used to set the point cost of skills in that Attribute's group. The player can buy levels in a
Skill at cost as long as its level is lower than its controlling Attribute. The point cost doubles if the Skill level
exceeds the controlling Attribute. For instance, Healing is a Smarts-based skill. If a character had a Smarts of Level
1 (4-sided die, or d4) and wants to buy the Healing skill at Level 2 (six-sided die, or d6), it will cost 3 points -
one point for Healing at Level 1 (d4) and two points for Healing at Level 2 (d6). If they had a Smarts of Level 2 (or
d6) it would only have cost 2 points - one point for Level 1 (d4) and another for Level 2 (d6). The number of points
assigned to spend on Skills is usually 15 points, but can be more in certain gameworlds.

In addition to Attributes a character has the following derived statistics: Pace (ground speed), Parry (the ability to
defend one's self), Toughness (resistance to damage) and Charisma (presence and charm). Some setting supplements add a
fifth derived statistic such as Reason (Problem Solving), Sanity (Mental Health) or Grit (Mental Strength) to reflect
the special needs of the gameworld.

Like in the FUDGE and FATE systems the skills are broad and allow the character to use them for a variety of related
tasks. For instance, a character with Fighting would not just be skilled in fighting with their bare hands or with
melee weapons. They might also be able to identify and counter an opponent's fighting style, know the name and
reputation of a skilled fighter they meet, figure out the nationality and rank of a soldier by their uniform and
insignia, or locate and hire a mercenary or bodyguard. Healing could be used to diagnose an illness, identify medicinal
herbs or pharmaceutical drugs, find a healer or medical specialist, or prevent a disease outbreak in an encampment by
organizing sanitation protocols.

#### Edges and Hindrances

Characters are also customized with advantages and disadvantages known as Edges and Hindrances. Edges and Hindrances,
unlike Traits, are not rated with dice. Edges (character advantages) cost points, are based on their character Rank
(Novice, Seasoned, Veteran, Heroic, or Legendary), and are unlocked as the character levels up. They are also grouped
by Type, which may - depending on the campaign or world - affect their availability. Beginning Edges can only be
granted at character creation. Social Edges affect interaction skills. Combat Edges affect the character's fighting
skills and Leadership Edges affect group or massed combat. Professional Edges are related to the character's job or
role and affects their career skills. Power, Weird, or Wild Card Edges are supernatural, paranormal, or superhuman
advantages and grant bonuses to Powers; they may not be available in mundane game worlds. Hindrances (character
disadvantages) grant points and are ranked as Minor (which grants a character point) or Major (which grants two
character points).

#### Powers

Some gameworlds have the option of granting superhuman abilities to characters -usually with a magical, mystical,
technological, psionic, racial, or mutant origin. They are ranked like Edges (Novice, Seasoned, Veteran, Heroic, or
Legendary) and can be expanded by leveling up.

### Task resolution
Dice are rolled to determine the outcome of character actions and interactions in the game. Usually a trait die is
rolled against a target number of four. If the roll equals or exceeds the target number, the action succeeds; otherwise
it fails.

If a player rolls the highest number possible on a given die (such as an 8 on an eight-sided die), the die may be
re-rolled and its result added to the initial roll. This is known as "Acing". A die may continue to Ace as long as the
highest die number is rolled.

Player characters and significant non-player characters are known as "Wild Cards". Wild Cards get to roll a second die,
known as a "Wild Die", alongside their trait rolls. This roll may Ace as normal. The player of the Wild Card uses the
higher of the two rolls (trait die or Wild Die) to determine the actual result of the roll. In addition Wild Cards also
receive a number of Bennies (Slang for benefits, also called poker chips in Dead Lands) per session. These can be
traded in to reduce or negate damage from a given attack, or to reroll a trait die, and are used as rewards for good
play.

Combat initiative is determined by a standard deck of playing cards (with two jokers); characters act in sequence
according to the fall of the cards from highest to lowest. Ties are broken by suit (in order from best to worst,
spades, hearts, diamonds, clubs). Jokers beat all other cards and additionally give bonuses on rolls made in the round
one receives them. The deck is shuffled at the end of every round in which a joker was dealt.

Any player that receives a Joker during initiative may take his action at any time during the round. So if he wishes to
act first, or in response to another PC or NPC acting he may at any point.

History
-------

In 1997, Pinnacle published Deadlands: the Great Rail Wars, a miniature wargame set in the "Weird West" world of
Hensley's Deadlands role-playing game. The rules were a greatly simplified version of the full Deadlands system,
focused on single-figure skirmishes.

In 2003 the rules from The Great Rail Wars were revised and expanded into a generic, simple but complete role-playing
system and retitled Savage Worlds. At Origins 2003, Savage Worlds was awarded the Gamer's Choice Award in the
Roleplaying Game category.[2] The main rulebook was revised and released as a PDF format eBook in late 2004, with a
print version following in early 2005. The same year, Great White Games began releasing rules expansions in the form of
several PDF format genre toolkit books. Self-contained miniature skirmish games based upon the Savage Worlds engine
were also released in print and PDF form.

Deadlands Reloaded, a version of the classic Pinnacle game using the Savage Worlds rules, was released in May 2006. In
late 2005, Pinnacle entered into an agreement with WizKids to publish self-contained RPGs set in the worlds of Pirates,
Rocketmen, and MageKnight using the Savage Worlds rules.[3] Of the three licenses, only The Pirates of the Spanish Main
RPG saw release, and was published in April 2007. Pinnacle released another licensed game, The Savage World of Solomon
Kane, in 2007.[4]

In October 2007, Pinnacle released the Savage Worlds Explorer's Edition, a digest size paperback edition of the rules.
It featured the revisions to melee damage rules first introduced in Deadlands Reloaded, as well as new chase rules, and
was released at Origins 2007. At that event, Deadlands Reloaded won the Origins Award in the category of Best
Roleplaying Game Supplement.[5]

In August 2011, Pinnacle released Savage Worlds Deluxe, a hardcover and expanded version of the rules found in the
Explorer's Edition.

In August 2012, Pinnacle released the digest size paperback edition of the Deluxe rules, Savage Worlds Deluxe
Explorer's Edition.

In 2015 Pinnacle announced a series of supplements converting Rifts to the Savage Worlds system.[6]

In 2018 Pinnacle announced a new edition: Savage Worlds Adventure Edition (#SWADE). It funded in six minutes on
Kickstarter, and went on to make $524,170 from 5,289 backers [7].

====

Дневник Авантюриста
===================

Кости и карты
-------------

Для игры требуется стандартный набор игральных костей: d4, d6, d8, d10 и d12. В некоторых редких случаях используется
d20. Также для игры требуется покерная колода, состоящая из 54 карт. Кости используются для проверок успешности
действий персонажей во время игры, а карты — для определения очередности действий персонажей во время сражений[1].

Правила
-------

В основу игры положены простые и понятные правила. Когда необходимо совершить проверку успешности того или иного
действия персонажа, кидается игральная кость, соответствующая уровню навыка или характеристики персонажа. Например,
если навык Стрельбы равен d6, для проверки результативности выстрела используется соответствующая игральная кость.
Персонажи игроков, называемые дикими картами, во время каждой проверки бросают дополнительный дикий кубик (обычно —
d6), и могут выбирать лучший результат.

Ход игры
--------

Во время игры один из участников игры становится ведущим. Он придумывает и рассказывает историю, в которой персонажи
других игроков принимают активное участие. Также ведущий берёт на себя роли всех не принадлежащих игрокам персонажей,
включая монстров, противников и некоторых союзников. В отличие от других подобных игр, во время битв игроки
контролируют не только своих персонажей, но и союзников. Такой подход делает игру более насыщенной, а вооруженные
столкновения более тактическими, с равноценным участием всех игроков в конфликте.

«Дневник авантюриста» изначально создавался с оглядкой на жанр пальп, широко представленный в западном искусстве. Для
этого жанра характерны герои, способности которых отличаются от таковых у среднестатистических людей, но не дотягивают
до способностей сильных супергероев. Для симуляции такого подхода каждый персонаж игрока в начале игровой сессии
получает от двух до пяти фишек, с помощью которых он может влиять на ситуацию в наиболее напряженные моменты. Например,
вовремя потраченная фишка может спасти жизнь персонажу. Такой подход делает историю более непредсказуемой и интересной
как для игроков, так и для ведущего[2].

Игровые миры
------------

Начиная с 2003 года было издано множество игровых миров для Дневника авантюриста. Среди наиболее ярких стоит назвать:

*   Deadlands Reloaded, которые стали четвертой редакцией этого мира.
*   Weird Wars II, совмещающие Вторую Мировую Войну и сверхъестественные ужасы.
*   Rippers, рассказывающий о борьбе секретного общества с чудовищами в конце XIX века.
*   Savage World of Solomon Kane, созданный по мотивам творчества Роберта Говарда.

В настоящий момент Savage Worlds обладает бесплатной лицензией, позволяющий любому издательству выпускать собственные
игровые миры, если они соответствуют определённому стандарту качества. Среди таких сторонних лицензий стоит отметить:

*   Suzerain — метавселенную, объединяющую множество миров: от киберпанка до древнегреческого эпоса.
*   Realms of Cthulhu, созданную по мотивам творчества Лавкрафта.
*   Shaintar, созданный в стилистике героического фэнтези.

На 2013 год выпущено около шестидесяти игровых миров для Дневника авантюриста в виде коммерческих продуктов и
неизвестное число фанатских.

Кампании (англ. Plot Point Campaign)
------------------------------------

Это одна из ключевых особенностей игровых миров для Дневника авантюриста. Кампания состоит из ключевых сцен, которые
идут в определённом порядке и связаны между собой общим сюжетом. Однако между этими сценами ведущий может свободно
вставлять собственные сюжеты, дополняя или видоизменяя центральный сюжет.

Такие кампании являются отличным подспорьем для ведущего, облегчая его работу при подготовке к игре. В них можно найти
описания и характеристики союзников и противников, описания локаций, где будет происходить действие, а также они
содержат всю необходимо справочную информацию.

Часто такие кампании входят в состав книги, описывающей игровой мир. Также есть несколько примеров отдельных кампаний,
изданных в дополнение к книге игрового мира.

Русское издание
---------------

На территории России и стран СНГ игра издается под именем «Savage Worlds: Дневник авантюриста» (издание версии
оригинальных правил от 2011 года, с внесением накопившихся правок, «эрраты»). Издание осуществляет Студия 101, также
выпустившая на российский рынок настольную ролевую игру «Фиаско». В планы студии входит как локализация англоязычных
игровых миров, так и выпуск собственных игровых миров и дополнений для «Дневника авантюриста». На настоящий момент
выпущены материалы по следующим игровым мирам:

*   «Красная земля» — альтернативная история гражданской войны в России 1920-х годов, в которой различные политические
    течения получили в свои руки сверхъестественные силы[3].
*   «Волчье солнце» — игра про людей, обладающих сверхъестественными способностями и вполне человеческими проблемами.
    Место действия — современная Россия.
*   «Deadlands: Мёртвые Земли» — мистический Дикий Запад с элементами альтернативной истории [4].
*   «Hellfrost: Ледяное Пекло» — эпическое фэнтези в антураже раннего средневековья со скандинавским колоритом.

Независимая студия Eternal Order выпустила официальный игровой мир под Savage Worlds по лицензии Студии 101:

*   «Багровый песок» — военно-историческая игра посвященная Афганской войне 1979-1989 года.

Независимыми разработчиками анонсировано несколько игровых миров под лицензией «Savage Fun»:

*   «Terminus esT» — рассказывает о буднях офицеров военно-космического флота Солнечной системы XXV века.
*   «Гильдия Авантюристов» — игра о бесстрашных путешественниках, скитающихся между мирами в поисках следов Древних.

"""
