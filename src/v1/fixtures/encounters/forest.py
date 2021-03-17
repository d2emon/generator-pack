__encounters_1 = map(
    lambda value: {"group_id": 1, **value},
    [
        dict(roll=1, value="Эфирный Демон (например Суккуб) атакует партию из Эфирного Плана"),
        dict(roll=2, value="1d12 высших эльфов атакуют караван"),
        dict(roll=3, value="Охотник выслеживает раненного медведя-альбиноса"),
        dict(roll=4, value="Из кустов выскакивает и убегает Полурослик с хрустальным яйцом, за ним летит гигантский"
                           " орел"),
        dict(roll=5, value="1d4 фирболгов вежливо просят вас покинуть лес"),
        dict(roll=6, value="1d20 проклятых дровосеков постоянно рубят лес и не могут прекратить свою работу"),
        dict(roll=7, value="Магический кристалл, спрятанный в дереве, вынуждает вас ходить кругами"),
        dict(roll=8, value="Невдалеке от дороги вы видите 1d12 фейри"),
        dict(roll=9, value="Охотник просит помощи в выслеживании магического зверя"),
        dict(roll=10, value="В темной чаще леса скрыт глубокий пруд, на дне его лежит сверкающий предмет (Проклят)"),
    ],
)

__encounters_2 = map(
    lambda value: {"group_id": 2, **value},
    [
        dict(roll=1, value="Впереди появляется лохматый отшельник в лохмотьях. Он заявляет что вы вторглись на его"
                           " землю. Отшельник - высокоуровневый маг"),
        dict(roll=2, value="Невдалеке собираются 6 энтов"),
        dict(roll=3, value="Древний храм, посвященный давно забытому богу"),
        dict(roll=4, value="Армия крошечных человечков-брокколи (Ветвистая зараза в виде брокколи) собирается мстить за"
                           " их короля-брокколи"),
        dict(roll=5, value="Дружественный тортл предлагает присоединиться к партии и делиться припасами если партия"
                           " согласна"),
        dict(roll=6, value="Маг сошел с ума и повсюду швыряется фаерболами, сжигая лес и все в нем"),
        dict(roll=7, value="Полупревращенный дроу падает с неба и нападает на партию (Драйдер)"),
        dict(roll=8, value="Яма-ловушка старого охотника заполнена насекомыми и парой скелетов"),
        dict(roll=9, value="Партия приходит во время стычки между кентаврами и лесными эльфами, каждая сторона платит,"
                           " чтобы партия встала на их сторону"),
        dict(roll=10, value="За спинами партии возникает разрыв пространства, он открывает иной план существования. По"
                            " ту сторону разрыва все сильно изменено"),
    ],
)

__encounters_3 = map(
    lambda value: {"group_id": 3, **value},
    [
        dict(roll=1, value="Перед вами стоит дом, сделанный из конфет, из дома доносится безумный хохот карги"),
        dict(roll=2, value="Лагерь орков, похоже что они все умерли во сне (1d8)"),
        dict(roll=3, value="Бездомный с нож вызывает вас на бой посреди дороги (используйте параметры бандита)"),
        dict(roll=4, value="Вы сбились с пути, когда вы оборачиваетесь - дороги больше нет"),
        dict(roll=5, value="На партию нападает гигантский паук, с ним 1d20 пауков"),
        dict(roll=6, value="Вы видите как по лесу бежит гигантский краб"),
        dict(roll=7, value="У подножья дерева вы замечаете маленькую пещерку, которая ведет в подземную сеть туннелей"),
        dict(roll=8, value="Когда вы идет по лесу вас не покидает ощущение будто за вами следят, вы замечаете капли"
                           " крови и остатки снаряжения. 1d6 древесных зараз спрятались здесь чтобы напасть на партию и"
                           " съесть"),
        dict(roll=9, value="Разумный скелет, который верит в то, что он все еще жив, хочет присоединиться к партии"),
        dict(roll=10, value="Партия пересекает территорию агрессивного фейри, который накладывает сон на партию, когда"
                            " партия просыпаются они обнаруживают что у них не осталось блестящих предметов"),
    ],
)

encounters = [
    *__encounters_1,
    *__encounters_2,
    *__encounters_3,
]
