import random
import math
from .locations import Location, Named, Spheric
from pyvoronoi import Pyvoronoi


PARSEC = 3.26


class SpaceStructure(Location):
    # max_size = 500 * 3.26  # Megaparsecs
    min_size = 50
    max_size = 500
    size_scale = .001
    default_color = (255, 255, 255)

    def __init__(self, x=0, y=0, z=0, color=None, size=None):
        super().__init__(x, y, z)
        self.color = color or self.default_color
        self.size = size or random.randrange(self.min_size, self.max_size) * self.size_scale

    def point(self):
        size = self.size / 2
        return self.x - size, self.y - size, self.x + size, self.y + size


class GalaxySupercluster(SpaceStructure):
    default_color = (255, 128, 128)


class Filament(SpaceStructure):
    default_color = (128, 128, 255)
    min_size = 60
    max_size = 5000

    def __init__(self, x=0, y=0, z=0, color=None, size=None):
        size = size or (
            random.randrange(self.min_size, self.max_size) * self.size_scale,
            random.randrange(self.min_size) * self.size_scale,
        )
        super().__init__(x, y, z, color, size)

        self.start = None
        self.end = None
        self.start_point =(0, 0)
        self.end_point =(0, 0)
        self.width = random.randrange(2)
        self.density = random.randrange(255)

    def set_points(self, start=-1, end=-1):
        if start >= 0:
            self.start = start
        else:
            self.start = None

        if end >= 0:
            self.end = end
        else:
            self.end = None

        self.start_point = (0, 0)
        self.end_point = (0, 0)

    def get_dots(self):
        x = self.start_point[0] - self.end_point[0]
        y = self.start_point[1] - self.end_point[1]

        width = int(math.hypot(x, y)) + 10
        height = self.width * 10 + 10
        size = (width, height)

        dots = []
        for _ in range(32):
            point = [random.randrange(c) for c in size]
            color = random.randrange(255)
            alpha = 255
            dots.append((point, (color, color, color, alpha)))
        return size, dots

    def set_start(self, x, y):
        self.start_point = (int(x * 10), int(y * 10))

    def set_end(self, x, y):
        self.end_point = (int(x * 10), int(y * 10))

    def point(self):
        size = (
            self.size[0] / 2,
            self.size[1] / 2,
        )

        return self.x - size[0], self.y - size[1], self.x + size[0], self.y + size[1]

    @property
    def line(self):
        return self.start_point + self.end_point


class Wall(Filament):
    default_color = (128, 255, 255)
    min_size = 100

    def __init__(self, x=0, y=0, z=0, color=None, size=None):
        size = size or (
            random.randrange(self.min_size, self.max_size) * self.size_scale,
            random.randrange(self.min_size, self.max_size) * self.size_scale,
        )
        super().__init__(x, y, z, color, size)


class Void(SpaceStructure):
    default_color = (0, 0, 128)

    def __init__(self, x=0, y=0, z=0, color=None, size=None):
        size = size or .130
        super().__init__(x, y, z, color, size)

    def get_rect(self, scale):
        return [int(x * scale) for x in self.point()]


class SuperVoid(Void):
    default_color = (0, 0, 64)

    def __init__(self, x=0, y=0, z=0, color=None, size=None):
        size = size or 1.304
        print(size, size / PARSEC)
        super().__init__(x, y, z, color, size)


class Universe(Named, Spheric):
    resolution = 1  # 10^9 ly (Gigaparsecs)
    items_count = 5000  # 500 * 10^9

    def __init__(self, name="Universe", radius=14 * 3.26):
        radius = int(radius / self.resolution)  # 10^9 ly (Gigaparsecs)

        Named.__init__(self, name)
        Spheric.__init__(self, radius)

        self.structure = []
        self.voids = []

        walls = [
            (10, 7.2),
            (.380, .196),
            (.500, .300),
            (1.380, 1.380),
        ]

        for wall in walls:
            w = Wall(*self.generate_coordinates(), size=wall)
            self.structure.append(w)

        # Voids
        for _ in range(5):
            self.voids.append(Void(*self.generate_coordinates()))

        for _ in range(5):
            self.voids.append(SuperVoid(*self.generate_coordinates()))

        giant_void = SuperVoid(*self.generate_coordinates(), size=.4 * PARSEC)
        self.voids.append(giant_void)

        for _ in range(500):
            self.voids.append(Void(*self.generate_coordinates()))
            self.voids.append(SuperVoid(*self.generate_coordinates()))

        # Structure
        self.structure += self.voids
        for _ in range(500):
            f = Filament(*self.generate_coordinates())
            self.structure.append(f)
            w = Wall(*self.generate_coordinates())
            self.structure.append(w)

        self.structure += [self.generate_location() for _ in range(self.items_count)]

        laniakea = GalaxySupercluster(radius, radius, radius, color=(255, 255, 128), size=.500)
        self.structure.append(laniakea)
        """
        Ланиакея	Размер = 500	
        Ланиакея — сверхскопление галактик, в котором, в частности, содержатся Сверхскопление Девы (составной 
        частью которого является Местная группа, содержащая галактику Млечный Путь с Солнечной системой) и 
        Великий аттрактор. В свою очередь, Ланиакея входит в комплекс сверхскоплений Рыб-Кита.
        """

        superclusters = [
            .110,  # Местное сверхскопление (Сверхскопление Девы)
            .150,  # Сверхскопление Гидры-Центавра
            .100,  # Сверхскопление Рыб-Персея
            .100,  # Сверхскопление Павлина-Индейца
            .290,  # Сверхскопление Волос Вероники
            .150,  # Сверхскопление Феникса
            .100,  # Сверхскопление Геркулеса
            .150,  # Сверхскопление Льва
            .070,  # Сверхскопление Змееносца
            .200,  # Сверхскопление Шепли
            .100,  # Сверхскопление Скульптора
        ]
        """
        Местное сверхскопление (Сверхскопление Девы)	Размер = 110	Сверхскопление содержит Местную 
        группу галактик, включая нашу галактику Млечный Путь. В сверхскопление также входит Скопление Девы — 
        ближайшее к Местной группе скопление галактик.
        Входит в состав анонсированного в 2014 году сверхскопления Ланиакея[3].

        Сверхскопление Гидры-Центавра	Расстояние = 150—200
        Размер = 150

        Сверхскопление состоит из двух частей, иногда упоминаемых в качестве отдельных сверхскоплений:
        Сверхскопление Гидры
        Сверхскопление Центавра
        Это сверхскопление является ближайшим сверхскоплением к Сверхскоплению Девы.

        Сверхскопление Рыб-Персея	Расстояние = 222
        Размер = 100

        Сверхскопление занимает область на небе размером 15 градусов и содержит более тысячи галактик.

        Сверхскопление Павлина-Индейца	Расстояние = 235
        Размер = 100

        Сверхскопление имеет относительно низкую плотность галактик и не содержит богатые скопления галактик.

        Сверхскопление Волос Вероники	Расстояние = 290
        Размер = 100

        Сверхскопление содержит более 3000 галактик и формирует значительную часть структуры CfA Homunculus, 
        которая в свою очередь является центром Великой стены CfA2.

        Сверхскопление Феникса	Расстояние = 372
        Размер = 150

        Сверхскопление Геркулеса	Расстояние = 413
        Размер = 100

        SCl 160

        Сверхскопление Льва	Расстояние = 440
        Размер = 150

        SCl 93

        Сверхскопление Змееносца	
        cz=8500-9000 км/с (центр) 59 x 85

        Сверхскопление Шепли	Расстояние = 654
        Размер = 200

        Второе обнаруженное сверхскопление после Сверхскопления Девы.

        Сверхскопление Скульптора (англ.)	Расстояние = 668
        Размер = 100

        Сверхскопление формирует часть Стены Скульптора (англ.)[4]        
        """

        for supercluster in superclusters:
            l = GalaxySupercluster(*self.generate_coordinates(), size=supercluster)
            self.structure.append(l)

        self.filaments = []

    def generate_location(self):
        return SpaceStructure(*self.generate_coordinates())

    def generate_voids(self):
        return [Void(*self.generate_coordinates()) for _ in range(self.items_count)]

    def generate_map(self):
        pv = Pyvoronoi(1)
        for void in self.voids:
            pv.AddPoint((void.x, void.y))
        pv.Construct()

        self.filaments = []
        for cell in pv.GetCells():
            for edge_id in cell.edges:
                if edge_id < 0:
                    continue

                edge = pv.GetEdge(edge_id)
                filament = Filament()
                filament.set_points(edge.start, edge.end)

                if filament.start:
                    vertex = pv.GetVertex(filament.start)
                    filament.set_start(vertex.X, vertex.Y)
                else:
                    continue

                if filament.end:
                    vertex = pv.GetVertex(filament.end)
                    filament.set_end(vertex.X, vertex.Y)
                else:
                    continue

                self.filaments.append(filament)

    def get_size(self, scale=10):
        return (
            int(self.diameter * scale),
            int(self.diameter * scale),
        )

    def get_rect(self, scale=10):
        return (
            0,
            0,
            self.diameter * scale,
            self.diameter * scale,
        )
