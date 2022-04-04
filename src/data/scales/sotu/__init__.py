from models.scales import Sized as Scalable, Distance, ScalableSize as Size
from .space.galaxy import ITEMS as GALAXIES
from .space.star_system import ITEMS as STAR_SYSTEM

SOTU = [
    Scalable("Планковская длина", Size(1.6, -35)),
    Scalable("Квантовая пена", Size(1, -35)),
    Scalable("Суперструна", Size(1, -35)),
    Scalable("Нейтрино", Size(1, -24)),

    Scalable("Верхний Кварк", Size(0.1, -21)),

    Scalable("Высокоэнергетическое Нейтрино", Size(15, -21)),
    Scalable("Преон", Size(1, -21)),

    Scalable("Нижний Кварк", Size(30, -21)),

    Scalable("Очарованный Кварк", Size(0.1, -18)),
    Scalable("Странный Кварк", Size(0.4, -18)),
    Scalable("Истинный Кварк", Size(1, -18)),
    Scalable("Прелестный Кварк", Size(1, -18)),
    Scalable("Ядро электрона", Size(1, -18)),

    Scalable("Слабые Силы", Size(10, -18)),

    Scalable("Неподтвержденные размеры", Size(0.1, -15)),
    Scalable("Протон", Size(1, -15)),
    Scalable("Нейтрон", Size(1, -15)),
    Scalable("Ядро Гелия", Size(3, -15)),
    Scalable("Электрон (Классический)", Size(5, -15)),
    Scalable("Ядро Хлора", Size(6, -15)),
    Scalable("Ядро Урана", Size(15, -15)),
    Scalable("Атомное Ядро (Среднее)", Size(10, -15)),

    Scalable("Длина Волны Гамма-излучения", Size(1, -12)),

    Scalable("Electron Compton Wavelength", Size(2, -12)),

    Scalable("Атом Гелия", Size(25, -12)),
    Scalable("Атом Водорода", Size(31, -12)),

    Scalable("Молекула Воды", Size(0.28, -9)),
    Scalable("Атом Углерода", Size(0.34, -9)),
    Scalable("Атом Серы", Size(0.1, -9)),
    Scalable("Атом Цезия", Size(0.23, -9)),

    Scalable("Alpha Helix", Size(0.5, -9)),

    Scalable("Глюкоза", Size(0.8, -9)),
    Scalable("Длина Волны Рентгенновского Излучения", Size(0.5, -9)),
    Scalable("Углеродная Нанотрубка", Size(1, -9)),

    Scalable("Buckyball", Size(1, -9)),

    Scalable("Фосфолипид", Size(2.5, -9)),
    Scalable("ДНК", Size(3, -9)),

    Scalable("Phospholipid Bilayer", Size(5, -9)),

    Scalable("Транзисторный Переход", Size(25, -9)),

    Scalable("Porcine circovirus", Size(17, -9)),

    Scalable("Вирус Гепатита B", Size(42, -9)),
    Scalable("ВИЧ", Size(90, -9)),
    Scalable("Клеточная Мембрана", Size(10, -9)),
    Scalable("Длина Волны Ультрафиолетового Света", Size(60, -9)),

    Scalable("Глубина Пита Комакт-Диска", Size(0.12, -6)),
    Scalable("Наибольшее Разрешение Оптического Микроскопа", Size(0.2, -6)),
    Scalable("Бактериофаг", Size(0.2, -6)),

    Scalable("Mimivirus", Size(0.4, -6)),

    Scalable("Самый Большой Вирус", Size(0.44, -6)),
    Scalable("Длина Волны Фиолетового Света", Size(0.4, -6)),
    Scalable("Наибольшая частица, способная проникнуть сквозь хирургическую маску", Size(1, -6)),

    Scalable("E. coli", Size(2, -6)),

    Scalable("Частица Глины", Size(2, -6)),
    Scalable("X Хромосома", Size(4, -6)),
    Scalable("Y Хромосома", Size(1.5, -6)),
    Scalable("Длина Волны Красного Света", Size(0.75, -6)),
    Scalable("Митохондрия", Size(4, -6)),
    Scalable("Красная Кровяная Клетка", Size(7, -6)),
    Scalable("Хлоропласт", Size(8, -6)),
    Scalable("Клеточное Ядро", Size(7, -6)),
    Scalable("Белая Кровяная Клетка", Size(10, -6)),
    Scalable("Капля Тумана", Size(20, -6)),

    Scalable("Thou", Size(25.4, -6)),
    Scalable("Twip", Size(17.6, -6)),

    Scalable("Толщина Акриловой Нити", Size(12, -6)),
    Scalable("Толщина Шелковой Нити", Size(15, -6)),
    Scalable("Клетка Кожи", Size(35, -6)),
    Scalable("Длина Волны Инфракрасного Света", Size(15, -6)),

    Scalable("Slit Particle", Size(50, -6)),
    Scalable("Pollen Grain", Size(50, -6)),

    Scalable("Разрешение Человеческого Глаза", Size(0.1, -3)),
    Scalable("Человеческая Яйцеклетка", Size(0.12, -3)),
    Scalable("Толщина Человеческого Волоса", Size(0.1, -3)),
    Scalable("Толщина Бумаги", Size(0.15, -3)),

    Scalable("Ciliate Protist", Size(0.2, -3)),
    Scalable("Paramecium", Size(0.2, -3)),

    Scalable("Амеба", Size(0.3, -3)),
    Scalable("Пылевой Клещ", Size(0.3, -3)),
    Scalable("Пиксель ЖКМ", Size(0.3, -3)),
    Scalable("Кристалл Соли", Size(0.5, -3)),
    Scalable("Крупнейшая Бактерия", Size(0.75, -3)),
    Scalable("Песчинка", Size(0.5, -3)),
    Scalable("Толщина Человеческой Кожи", Size(0.5, -3)),
    Scalable("Толщина Кредитной Карты", Size(0.7, -3)),

    Scalable("Duckweed", Size(2, -3)),

    Scalable("Муравей", Size(4, -3)),
    Scalable("Семечка Подсолнечника", Size(7, -3)),
    Scalable("Град", Size(5, -3)),
    Scalable("Рисовое Зерно", Size(5, -3)),
    Scalable("Толщина Грифеля", Size(0.7, -3)),
    Scalable("Толщина Человеческой Кожи (подошвы)", Size(4, -3)),
    Scalable("Зерно Сезама", Size(3, -3)),
    Scalable("Микрочип", Size(4, -3)),

    Scalable("Кофейное Зерно", Size(10, -3)),
    Scalable("Яйцо Колибри", Size(12, -3)),
    Scalable("Стеклянный Шарик", Size(15, -3)),
    Scalable("Длина Волны Микроволновки", Size(10, -3)),
    Scalable("Квадратный Дюйм", Size(25, -3)),
    Scalable("Пенни США", Size(19, -3)),
    Scalable("Снежинка", Size(10, -3)),
    Scalable("Перепелиное Яйцо", Size(30, -3)),
    Scalable("Дождевой Червь", Size(40, -3)),
    Scalable("Спичка", Size(50, -3)),
    Scalable("Куриное Яйцо", Size(55, -3)),
    Scalable("Кубик Рубика", Size(55, -3)),

    Scalable("Стакан", Size(0.12, 0)),
    Scalable("Страусиное Яйцо", Size(0.15, 0)),
    Scalable("Землеройка", Size(0.1, 0)),
    Scalable("Колибри", Size(0.1, 0)),
    Scalable("Это Окно", Size(0.2, 0)),
    Scalable("Чайник Рассела", Size(0.25, 0)),
    Scalable("Крупнейшая Градина", Size(0.2, 0)),
    Scalable("Крупнейшая Снежинка", Size(0.38, 0)),
    Scalable("Баскетбольный Мяч", Size(0.24, 0)),
    Scalable("Дюймовая Линейка", Size(0.3, 0)),
    Scalable("Дронт", Size(1, 0)),
    Scalable("Маленький Пляжный мяч", Size(0.5, 0)),
    Scalable("Большой Пляжный мяч", Size(1, 0)),
    Scalable("Раффлезия", Size(1, 0)),
    Scalable("Человек", Size(1.7, 0)),
    Scalable("Гигантский Дождевой Червь", Size(3, 0)),
    Scalable("Подсолнечник", Size(2.5, 0)),
    Scalable("Странствующий Альбатрос", Size(3, 0)),
    Scalable("FM Волна", Size(1, 0)),
    Scalable("Машина", Size(4, 0)),
    Scalable("Высота дома", Size(2.5, 0)),
    Scalable("Японский Краб", Size(3, 0)),
    Scalable("Автобус", Size(12, 0)),
    Scalable("Слон", Size(5, 0)),
    Scalable("Жираф", Size(6, 0)),
    Scalable("Тирранозавр Рекс", Size(7, 0)),
    Scalable("Анаконда", Size(8, 0)),
    Scalable("Лунный Модуль Аполло", Size(9, 0)),
    Scalable("Сагуаро", Size(14, 0)),
    Scalable("Дом", Size(15, 0)),
    Scalable("Дуб", Size(15, 0)),

    Scalable("Amphilicoelias fragilimus", Size(60, 0)),

    Scalable("Синий Кит", Size(30, 0)),

    Scalable("Redwood Tree", Size(0.1, 3)),

    Scalable("Боинг 747", Size(65, 0)),
    Scalable("Статуя Свободы", Size(93, 0)),
    Scalable("МКС", Size(0.108, 3)),
    Scalable("Сатурн V", Size(0.11, 3)),
    Scalable("Футбольное поле", Size(0.1097, 3)),
    Scalable("Титаник", Size(0.27, 3)),

    Scalable("Gateway Arc", Size(0.192, 3)),

    Scalable("Эйфелева Башня", Size(0.32, 3)),
    Scalable("Пирамиды в Гизе", Size(0.15, 3)),
    Scalable("Монумент Вашингтона", Size(0.169, 3)),
    Scalable("Дамба Гувера", Size(0.22, 3)),

    Scalable("Half Dome", Size(0.41, 3)),
    Scalable("International Commercial Centre", Size(0.484, 3)),
    Scalable("Sears Tower", Size(0.442, 3)),

    Scalable("Ватикан", Size(0.8, 3)),
    # Бурж Халифа
    Scalable("Водопад Анхель", Size(0.979, 3)),

    Scalable("Boeing Everett Factory", Size(1, 3)),
    Scalable("Stanford Linear Accelerator", Size(3, 3)),
    Scalable("Uluru", Size(3, 3)),

    Scalable("Центральный Парк", Size(4, 3)),
    Scalable("AM Волна", Size(1, 3)),

    Scalable("Palm Jebel Ali", Size(8, 3)),

    Scalable("Большой Адронный Коллайдер", Size(8.6, 3)),
    Scalable("Эверест", Size(8.8, 3)),
    Scalable("Марианская Впадина", Size(10.9, 3)),
    Scalable("Марафон", Size(42.2, 3)),
    Scalable("Нейтронная Звезда", Size(24, 3)),
    Scalable("Род Айленд", Size(75, 3)),

    Scalable("Бруней", Size(0.12, 6)),
    Scalable("Западная Вирджиния", Size(0.4, 6)),
    Scalable("Великий Каньон", Size(0.45, 6)),
    Scalable("Руанда", Size(0.24, 6)),
    Scalable("Италия", Size(1.1, 6)),
    Scalable("Калифорния", Size(1.2, 6)),
    Scalable("Техас", Size(1.2, 6)),
    Scalable("Большой Барьерный Риф", Size(2.6, 6)),
    Scalable("Великая Китайская Стена", Size(8.85, 6)),
    Scalable("США", Size(4.2, 6)),
    Scalable("Азия", Size(8, 6)),

    Scalable("Самая длинная радиоволна", Size(.1, 9)),
    Scalable("Суммарная высота человечества", Size(10, 9)),

    Distance("которое прошла Земля относительно Солнца", distance=Size(4.5, 21)),
    Distance("до HDF", distance=Size(0.127, 27)),  # ?
] + GALAXIES + STAR_SYSTEM
