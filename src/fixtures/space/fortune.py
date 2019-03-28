import random
import math
from PIL import Image, ImageDraw
from pyvoronoi import Pyvoronoi


def generate_points(count=5, size=(512, 512)):
    for _ in range(count):
        yield [random.randrange(c) for c in size]


def point2ellipse(point):
    return point[0] - 1, point[1] - 1, point[0] + 1, point[1] + 1


class Parabola:
    def __init__(self, focus, directress):
        self.focus = focus
        self.directress = directress
        self.p = (self.directress - self.focus[0]) / 2
        print("x = 2 * {} * (y ** 2)".format(self.p))

    def x(self, y):
        y0 = y - self.focus[1]
        x0 = self.directress - self.p
        return x0 - (y0 ** 2) / (2 * self.p)


def coastline(parabols):
    def x(y):
        px = list(map(lambda p: p.x(y), parabols))
        return max(px)
    return x


def intersections(parabols, size):
    res = []
    for y in range(size):
        for p1 in parabols:
            x1 = int(p1.x(y))
            for p2 in parabols:
                if p2 == p1:
                    continue

                x2 = int(p2.x(y))
                if x1 == x2:
                    res.append((x1, y))
    return res


def field():
    size = 512, 512
    points = list(generate_points(size=size))
    colors = [
        (255, 0, 0),
        (0, 255, 0),
        (255, 255, 0),
        (0, 0, 255),
        (255, 0, 255),
    ]

    image = Image.new('RGB', size)

    draw = ImageDraw.Draw(image)
    sweep = random.randrange(size[0])
    swept = filter(lambda point: point[0] < sweep, points)
    parabols = [Parabola(point, sweep) for point in swept]
    c = coastline(parabols)
    for p in parabols:
        for y in range(size[1]):
            draw.ellipse(point2ellipse((p.x(y), y)), (0, 255, 0))

    for y in range(size[1]):
        draw.ellipse(point2ellipse((sweep, y)), (255, 0, 0))
        draw.ellipse(point2ellipse((c(y), y)), (0, 0, 255))

    print(intersections(parabols, size[1]))

    diagonal = math.hypot(*size)
    for y in range(size[1]):
        for x in range(size[0]):
            # find the closest cell center
            dmin = diagonal
            j = None
            for point_id, point in enumerate(points):
                d = math.hypot(point[0] - x, point[1] - y)
                if d < dmin:
                    dmin = d
                    j = point_id
            if j is not None:
                image.putpixel((x, y), colors[j])
            pass

    # mark the cell centers
    for p in points:
        image.putpixel(p, (255, 255, 255))

    image.show()

    print(points)


"""
def voronoi1(points, size=(500,500)):
    depthmap = numpy.ones(shape, numpy.float) * 1e308
    colormap = numpy.zeros(shape, numpy.int)

    def hypot(X,Y):
        return math.hypot((X, Y), (x, y))

    for i, (x, y) in enumerate(points):
        paraboloid = numpy.fromfunction(hypot, size)
        colormap = numpy.where(paraboloid < depthmap, i + 1, colormap)
        depthmap = numpy.where(paraboloid < depthmap, paraboloid, depthmap)

    for (x, y) in points:
        colormap[x - 1:x + 2, y - 1:y + 2] = 0

    return colormap


def draw_map(colormap):
    shape = colormap.shape

    palette = numpy.array([
        0x000000FF,
        0xFF0000FF,
        0x00FF00FF,
        0xFFFF00FF,
        0x0000FFFF,
        0xFF00FFFF,
        0x00FFFFFF,
        0xFFFFFFFF,
    ])

    colormap = numpy.transpose(colormap)
    pixels = numpy.empty(colormap.shape + (4, ), numpy.int8)

    pixels[:, :, 3] = palette[colormap] & 0xFF
    pixels[:, :, 2] = (palette[colormap]>>8) & 0xFF
    pixels[:, :, 1] = (palette[colormap]>>16) & 0xFF
    pixels[:, :, 0] = (palette[colormap]>>24) & 0xFF
"""